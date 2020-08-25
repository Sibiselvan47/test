import pytest

from tartiflette import Resolver
from tests.data.modules.pets.storage import PETS, find_object


async def resolve_query_version(parent, args, ctx, info):
    return "v0.1.0"


async def resolve_query_service_status(parent, args, ctx, info):
    return "UP"


async def resolve_query_human(parent, args, ctx, info):
    return find_object("Human", args["id"])


async def resolve_query_pet(parent, args, ctx, info):
    return find_object("Pet", args["id"])


async def resolve_query_pets(parent, args, ctx, info):
    return [find_object("Pet", pet.split(".")[1]) for pet in PETS]


async def resolve_friends(parent, args, ctx, info):
    friend_ids = parent.get("friend_ids")
    if friend_ids is None:
        return None

    friends = []
    for friend_type_id in friend_ids:
        friend_type, friend_id = friend_type_id.split(".")
        friends.append(find_object(friend_type, friend_id))
    return friends


def pets_bakery(schema_name):
    Resolver("MyQuery.version", schema_name=schema_name)(resolve_query_version)
    Resolver("MyQuery.serviceStatus", schema_name=schema_name)(
        resolve_query_service_status
    )
    Resolver("MyQuery.human", schema_name=schema_name)(resolve_query_human)
    Resolver("Human.friends", schema_name=schema_name)(resolve_friends)
    Resolver("MyQuery.pet", schema_name=schema_name)(resolve_query_pet)
    Resolver("Cat.friends", schema_name=schema_name)(resolve_friends)
    Resolver("Dog.friends", schema_name=schema_name)(resolve_friends)


@pytest.mark.asyncio
@pytest.mark.with_schema_stack(preset="pets", bakery=pets_bakery)
@pytest.mark.parametrize(
    "query,variables,expected",
    [
        (
            """
            {
              __typename
              version
            }
            """,
            None,
            {"data": {"__typename": "MyQuery", "version": "v0.1.0"}},
        ),
        (
            """
            {
              __typename
              serviceStatus
            }
            """,
            None,
            {"data": {"__typename": "MyQuery", "serviceStatus": "UP"}},
        ),
        (
            """
            {
              human(id: 1) {
                __typename
                id
                name
              }
            }
            """,
            None,
            {
                "data": {
                    "human": {
                        "__typename": "Human",
                        "id": 1,
                        "name": "Human 1",
                    }
                }
            },
        ),
        (
            """
            {
              human(id: 1) {
                __typename
                id
                name
                friends {
                  __typename
                  ... on Human {
                    id
                  }
                  ... on Cat {
                    id
                  }
                  ... on Dog {
                    id
                  }
                }
              }
            }
            """,
            None,
            {
                "data": {
                    "human": {
                        "__typename": "Human",
                        "id": 1,
                        "name": "Human 1",
                        "friends": [{"__typename": "Human", "id": 2}],
                    }
                }
            },
        ),
        (
            """
            {
              human(id: 999) {
                __typename
                id
                name
                friends {
                  __typename
                  ... on Human {
                    id
                  }
                  ... on Cat {
                    id
                  }
                  ... on Dog {
                    id
                  }
                }
              }
            }
            """,
            None,
            {
                "data": {"human": None},
                "errors": [
                    {
                        "message": "Object < Human.999 > doesn't exists.",
                        "path": ["human"],
                        "locations": [{"line": 3, "column": 15}],
                        "extensions": {"kind": "Human", "id": 999},
                    }
                ],
            },
        ),
        (
            """
            {
              pet(id: 1) {
                __typename
                id
                name
                friends {
                  __typename
                  ... on Human {
                    id
                  }
                  ... on Cat {
                    id
                  }
                  ... on Dog {
                    id
                  }
                }
              }
            }
            """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Cannot query field < id > on type < Pet >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 17}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.3.1",
                            "tag": "field-selections-on-objects-interfaces-and-unions-types",
                            "details": "https://spec.graphql.org/June2018/#sec-Field-Selections-on-Objects-Interfaces-and-Unions-Types",
                        },
                    },
                    {
                        "message": "Cannot query field < name > on type < Pet >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 17}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.3.1",
                            "tag": "field-selections-on-objects-interfaces-and-unions-types",
                            "details": "https://spec.graphql.org/June2018/#sec-Field-Selections-on-Objects-Interfaces-and-Unions-Types",
                        },
                    },
                    {
                        "message": "Cannot query field < friends > on type < Pet >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 17}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.3.1",
                            "tag": "field-selections-on-objects-interfaces-and-unions-types",
                            "details": "https://spec.graphql.org/June2018/#sec-Field-Selections-on-Objects-Interfaces-and-Unions-Types",
                        },
                    },
                ],
            },
        ),
        (
            """
            {
              pet(id: 2) {
                __typename
                ... on Cat {
                  id
                  name
                  friends {
                    __typename
                    ... on Human {
                      id
                    }
                    ... on Cat {
                      id
                    }
                    ... on Dog {
                      id
                    }
                  }
                }
              }
            }
            """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Fragment cannot be spread here as objects of type < Pet > can never be of type < Human >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 21}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.5.2.3",
                            "tag": "fragment-spread-is-possible",
                            "details": "https://spec.graphql.org/June2018/#sec-Fragment-spread-is-possible",
                        },
                    }
                ],
            },
        ),
        (
            """
            {
              pet(id: 2) {
                __typename
                ... on Cat {
                  id
                  name
                  friends {
                    __typename
                    ... on Cat {
                      id
                    }
                    ... on Dog {
                      id
                    }
                  }
                }
              }
            }
            """,
            None,
            {
                "data": {
                    "pet": {
                        "__typename": "Cat",
                        "id": 2,
                        "name": "Cat 2",
                        "friends": [
                            {"__typename": "Dog", "id": 1},
                            {"__typename": "Cat", "id": 3},
                            {"__typename": "Dog", "id": 5},
                        ],
                    }
                }
            },
        ),
        (
            """
            {
              human(id: 999) {
                __typename
                id
                name
                friends {
                  __typename
                  ... on Human {
                    id
                  }
                  ... on Cat {
                    id
                  }
                  ... on Dog {
                    id
                  }
                }
              }
            }
            """,
            None,
            {
                "data": {"human": None},
                "errors": [
                    {
                        "message": "Object < Human.999 > doesn't exists.",
                        "path": ["human"],
                        "locations": [{"line": 3, "column": 15}],
                        "extensions": {"kind": "Human", "id": 999},
                    }
                ],
            },
        ),
    ],
)
async def test_pets(schema_stack, query, variables, expected):
    assert await schema_stack.execute(query, variables=variables) == expected


def pets_errors_bakery(schema_name):
    Resolver("MyQuery.pets", schema_name=schema_name)(resolve_query_pets)


@pytest.mark.asyncio
@pytest.mark.with_schema_stack(preset="pets", bakery=pets_errors_bakery)
@pytest.mark.parametrize(
    "query,variables,expected",
    [
        (
            """
            query ($petFilters: PetFilters) {
              pets(filters: $petFilters) { ... on Dog { name } }
            }
            """,
            {"petFilters": {"kind": "DG"}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $petFilters > got invalid value < {'kind': 'DG'} >; Expected type < PetKind > at value.kind; Did you mean DOG?",
                        "path": None,
                        "locations": [{"line": 2, "column": 20}],
                    }
                ],
            },
        ),
        (
            """
            query ($petFilters: PetFilters) {
              pets(filters: $petFilters) { ... on Dog { name } }
            }
            """,
            {"petFilters": {"kind": "CA"}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $petFilters > got invalid value < {'kind': 'CA'} >; Expected type < PetKind > at value.kind; Did you mean CAT?",
                        "path": None,
                        "locations": [{"line": 2, "column": 20}],
                    }
                ],
            },
        ),
        (
            """
            query ($petFilters: PetFilters) {
              pets(filters: $petFilters) { ... on Dog { name } }
            }
            """,
            {"petFilters": {"na": "C"}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $petFilters > got invalid value < {'na': 'C'} >; Field < na > is not defined by type < PetFilters >; Did you mean name?",
                        "path": None,
                        "locations": [{"line": 2, "column": 20}],
                    }
                ],
            },
        ),
        (
            """
            query ($petFilters: PetFilters) {
              pets(filters: $petFilters) { ... on Dog { name } }
            }
            """,
            {"petFilters": {"hasien": True}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $petFilters > got invalid value < {'hasien': True} >; Field < hasien > is not defined by type < PetFilters >; Did you mean hasFriends or hasChildren?",
                        "path": None,
                        "locations": [{"line": 2, "column": 20}],
                    }
                ],
            },
        ),
    ],
)
async def test_pets_errors(schema_stack, query, variables, expected):
    assert await schema_stack.execute(query, variables=variables) == expected
