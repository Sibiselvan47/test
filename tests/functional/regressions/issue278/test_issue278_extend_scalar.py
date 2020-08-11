from typing import Any, Callable, Dict, Optional

import pytest

from tartiflette import Directive, Resolver, create_engine
from tartiflette.types.exceptions.tartiflette import GraphQLSchemaError
from tests.functional.utils import match_schema_errors


@pytest.fixture(scope="module")
async def ttftt_engine():
    schema_sdl = """
        type Query {
            test1: Int
        }

        directive @addValue(value: Int) on SCALAR

        extend scalar Int @addValue(value: 5)
    """

    @Directive(name="addValue", schema_name="test_issue_278_scalar_extend")
    class AddValue:
        @staticmethod
        async def on_pre_output_coercion(
            directive_args: Dict[str, Any],
            next_directive: Callable,
            value: Any,
            ctx: Optional[Any],
            info: "ResolveInfo",
        ):
            return (
                await next_directive(value, ctx, info)
                + directive_args["value"]
            )

    @Resolver("Query.test1", schema_name="test_issue_278_scalar_extend")
    async def resolver_test_1(*_args, **_kwargs):
        return 7

    return await create_engine(
        schema_sdl, schema_name="test_issue_278_scalar_extend"
    )


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "query,expected",
    [
        (
            """
            query {
                test1
            }
            """,
            {"data": {"test1": 12}},
        )
    ],
)
async def test_issue_278_scalar_extend(query, expected, ttftt_engine):
    assert await ttftt_engine.execute(query) == expected


@pytest.mark.asyncio
async def test_issue_278_scalar_extend_invalid_sdl():
    with pytest.raises(GraphQLSchemaError) as excinfo:
        await create_engine(
            sdl="""
                directive @C on OBJECT | SCALAR

                scalar bob @C

                extend scalar bob @C

                type Query {
                    a: bob
                }

                extend scalar dontexists @C

                extend scalar Query @C
            """,
            schema_name="test_issue_278_scalar_extend_invalid_sdl",
        )

    match_schema_errors(
        excinfo.value,
        [
            "The directive < @C > can only be used once at this location.",
            "Cannot extend type < dontexists > because it is not defined.",
            "Cannot extend non-object type < Query >.",
        ],
    )
