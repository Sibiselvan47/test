import pytest


@pytest.mark.asyncio
@pytest.mark.with_schema_stack(preset="coercion")
@pytest.mark.parametrize(
    "query,variables,expected",
    [
        (
            """query { booleanField }""",
            None,
            {"data": {"booleanField": "SUCCESS"}},
        ),
        (
            """query { booleanField(param: null) }""",
            None,
            {"data": {"booleanField": "SUCCESS-None"}},
        ),
        (
            """query { booleanField(param: false) }""",
            None,
            {"data": {"booleanField": "SUCCESS-False"}},
        ),
        (
            """query ($param: Boolean) { booleanField(param: $param) }""",
            None,
            {"data": {"booleanField": "SUCCESS"}},
        ),
        (
            """query ($param: Boolean) { booleanField(param: $param) }""",
            {"param": None},
            {"data": {"booleanField": "SUCCESS-None"}},
        ),
        (
            """query ($param: Boolean) { booleanField(param: $param) }""",
            {"param": True},
            {"data": {"booleanField": "SUCCESS-True"}},
        ),
        (
            """query ($param: Boolean = null) { booleanField(param: $param) }""",
            None,
            {"data": {"booleanField": "SUCCESS-None"}},
        ),
        (
            """query ($param: Boolean = null) { booleanField(param: $param) }""",
            {"param": None},
            {"data": {"booleanField": "SUCCESS-None"}},
        ),
        (
            """query ($param: Boolean = null) { booleanField(param: $param) }""",
            {"param": True},
            {"data": {"booleanField": "SUCCESS-True"}},
        ),
        (
            """query ($param: Boolean = false) { booleanField(param: $param) }""",
            None,
            {"data": {"booleanField": "SUCCESS-False"}},
        ),
        (
            """query ($param: Boolean = false) { booleanField(param: $param) }""",
            {"param": None},
            {"data": {"booleanField": "SUCCESS-None"}},
        ),
        (
            """query ($param: Boolean = false) { booleanField(param: $param) }""",
            {"param": True},
            {"data": {"booleanField": "SUCCESS-True"}},
        ),
        (
            """query ($param: Boolean!) { booleanField(param: $param) }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    }
                ],
            },
        ),
        (
            """query ($param: Boolean!) { booleanField(param: $param) }""",
            {"param": None},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    }
                ],
            },
        ),
        (
            """query ($param: Boolean!) { booleanField(param: $param) }""",
            {"param": True},
            {"data": {"booleanField": "SUCCESS-True"}},
        ),
    ],
)
async def test_coercion_boolean_field(
    schema_stack, query, variables, expected
):
    assert await schema_stack.execute(query, variables=variables) == expected
