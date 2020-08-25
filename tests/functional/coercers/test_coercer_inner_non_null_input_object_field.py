import pytest


@pytest.mark.asyncio
@pytest.mark.with_schema_stack(preset="coercion")
@pytest.mark.parametrize(
    "query,variables,expected",
    [
        (
            """query { innerNonNullInputObjectField }""",
            None,
            {"data": {"innerNonNullInputObjectField": "SUCCESS"}},
        ),
        (
            """query { innerNonNullInputObjectField(param: null) }""",
            None,
            {"data": {"innerNonNullInputObjectField": "SUCCESS-None"}},
        ),
        (
            """query { innerNonNullInputObjectField(param: {}) }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Field < InnerNonNullMyInput.booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Field < InnerNonNullMyInput.enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Field < InnerNonNullMyInput.floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Field < InnerNonNullMyInput.intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Field < InnerNonNullMyInput.stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """
                query {
                  innerNonNullInputObjectField(param: {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  })
                }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """
                query {
                  innerNonNullInputObjectField(param: {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  })
                }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 13, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """
                query {
                  innerNonNullInputObjectField(param: {
                    booleanField: false
                    enumField: ENUM_2
                    floatField: 23456.789e2
                    intField: 10
                    stringField: "paramDefaultValue"
                    listBooleanField: false
                    listEnumField: ENUM_2
                    listFloatField: 23456.789e2
                    listIntField: 10
                    listStringField: "paramDefaultValue"
                  })
                }""",
            None,
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:False]-[enumField:ENUM_2_2-MyEnum-enumField]-[floatField:2345681.9]-[intField:13]-[stringField:paramdefaultvalue-scalar-stringField]-[listBooleanField:False]-[listEnumField:enum_2_2-myenum]-[listFloatField:2345681.9]-[listIntField:13]-[listStringField:paramdefaultvalue-scalar]"
                }
            },
        ),
        (
            """
                query {
                  innerNonNullInputObjectField(param: {
                    booleanField: false
                    enumField: ENUM_2
                    floatField: 23456.789e2
                    intField: 10
                    stringField: "paramDefaultValue"
                    listBooleanField: [false]
                    listEnumField: [ENUM_2]
                    listFloatField: [23456.789e2]
                    listIntField: [10]
                    listStringField: ["paramDefaultValue"]
                  })
                }""",
            None,
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:False]-[enumField:ENUM_2_2-MyEnum-enumField]-[floatField:2345681.9]-[intField:13]-[stringField:paramdefaultvalue-scalar-stringField]-[listBooleanField:False]-[listEnumField:enum_2_2-myenum]-[listFloatField:2345681.9]-[listIntField:13]-[listStringField:paramdefaultvalue-scalar]"
                }
            },
        ),
        (
            """
                query {
                  innerNonNullInputObjectField(param: {
                    booleanField: false
                    enumField: ENUM_2
                    floatField: 23456.789e2
                    intField: 10
                    stringField: "paramDefaultValue"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_2, null]
                    listFloatField: [23456.789e2, null]
                    listIntField: [10, null]
                    listStringField: ["paramDefaultValue", null]
                  })
                }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 51}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 13, "column": 60}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            None,
            {"data": {"innerNonNullInputObjectField": "SUCCESS"}},
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {"param": None},
            {"data": {"innerNonNullInputObjectField": "SUCCESS-None"}},
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query ($param: InnerNonNullMyInput) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            None,
            {"data": {"innerNonNullInputObjectField": "SUCCESS-None"}},
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {"param": None},
            {"data": {"innerNonNullInputObjectField": "SUCCESS-None"}},
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query ($param: InnerNonNullMyInput = null) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": None},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: null
                    listEnumField: null
                    listFloatField: null
                    listIntField: null
                    listStringField: null
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": None},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: null
                    enumField: null
                    floatField: null
                    intField: null
                    stringField: null
                    listBooleanField: [null]
                    listEnumField: [null]
                    listFloatField: [null]
                    listIntField: [null]
                    listStringField: [null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 3, "column": 35}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 4, "column": 32}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 5, "column": 33}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 6, "column": 31}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 7, "column": 34}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 37}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 38}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 36}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 39}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            None,
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:False]-[enumField:ENUM_4_4-MyEnum-enumField]-[floatField:45681.9]-[intField:33]-[stringField:vardefault-scalar-stringField]-[listBooleanField:False]-[listEnumField:enum_4_4-myenum]-[listFloatField:45681.9]-[listIntField:33]-[listStringField:vardefault-scalar]"
                }
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": None},
            {"data": {"innerNonNullInputObjectField": "SUCCESS-None"}},
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: false
                    listEnumField: ENUM_4
                    listFloatField: 456.789e2
                    listIntField: 30
                    listStringField: "varDefault"
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            None,
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:False]-[enumField:ENUM_4_4-MyEnum-enumField]-[floatField:45681.9]-[intField:33]-[stringField:vardefault-scalar-stringField]-[listBooleanField:False]-[listEnumField:enum_4_4-myenum]-[listFloatField:45681.9]-[listIntField:33]-[listStringField:vardefault-scalar]"
                }
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": None},
            {"data": {"innerNonNullInputObjectField": "SUCCESS-None"}},
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[0].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false]
                    listEnumField: [ENUM_4]
                    listFloatField: [456.789e2]
                    listIntField: [30]
                    listStringField: ["varDefault"]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[1].",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": None},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $param: InnerNonNullMyInput = {
                    booleanField: false
                    enumField: ENUM_4
                    floatField: 456.789e2
                    intField: 30
                    stringField: "varDefault"
                    listBooleanField: [false, null]
                    listEnumField: [ENUM_4, null]
                    listFloatField: [456.789e2, null]
                    listIntField: [30, null]
                    listStringField: ["varDefault", null]
                  }
                ) {
                  innerNonNullInputObjectField(param: $param)
                }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Expected value of type < Boolean! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 8, "column": 47}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < MyEnum! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 9, "column": 45}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Float! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 10, "column": 49}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < Int! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 11, "column": 40}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                    {
                        "message": "Expected value of type < String! >, found < null >.",
                        "path": None,
                        "locations": [{"line": 12, "column": 53}],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.6.1",
                            "tag": "values-of-correct-type",
                            "details": "https://spec.graphql.org/June2018/#sec-Values-of-Correct-Type",
                        },
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > of required type < InnerNonNullMyInput! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    }
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {"param": None},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > of non-null type < InnerNonNullMyInput! > must not be null.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    }
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {"param": {}},
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {} >; Field < value.stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": None,
                    "listEnumField": None,
                    "listFloatField": None,
                    "listIntField": None,
                    "listStringField": None,
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': None, 'listEnumField': None, 'listFloatField': None, 'listIntField': None, 'listStringField': None} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": None,
                    "enumField": None,
                    "floatField": None,
                    "intField": None,
                    "stringField": None,
                    "listBooleanField": [None],
                    "listEnumField": [None],
                    "listFloatField": [None],
                    "listIntField": [None],
                    "listStringField": [None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.booleanField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.enumField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.floatField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.intField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.stringField.",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': None, 'enumField': None, 'floatField': None, 'intField': None, 'stringField': None, 'listBooleanField': [None], 'listEnumField': [None], 'listFloatField': [None], 'listIntField': [None], 'listStringField': [None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[0].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": True,
                    "listEnumField": "ENUM_3",
                    "listFloatField": 3456.789e2,
                    "listIntField": 20,
                    "listStringField": "varValue",
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True],
                    "listEnumField": ["ENUM_3"],
                    "listFloatField": [3456.789e2],
                    "listIntField": [20],
                    "listStringField": ["varValue"],
                }
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query ($param: InnerNonNullMyInput!) { innerNonNullInputObjectField(param: $param) }""",
            {
                "param": {
                    "booleanField": True,
                    "enumField": "ENUM_3",
                    "floatField": 3456.789e2,
                    "intField": 20,
                    "stringField": "varValue",
                    "listBooleanField": [True, None],
                    "listEnumField": ["ENUM_3", None],
                    "listFloatField": [3456.789e2, None],
                    "listIntField": [20, None],
                    "listStringField": ["varValue", None],
                }
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Boolean! > not to be null at value.listBooleanField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < MyEnum! > not to be null at value.listEnumField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Float! > not to be null at value.listFloatField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < Int! > not to be null at value.listIntField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                    {
                        "message": "Variable < $param > got invalid value < {'booleanField': True, 'enumField': 'ENUM_3', 'floatField': 345678.9, 'intField': 20, 'stringField': 'varValue', 'listBooleanField': [True, None], 'listEnumField': ['ENUM_3', None], 'listFloatField': [345678.9, None], 'listIntField': [20, None], 'listStringField': ['varValue', None]} >; Expected non-nullable type < String! > not to be null at value.listStringField[1].",
                        "path": None,
                        "locations": [{"line": 1, "column": 8}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $listBooleanField: [Boolean]
                  $listEnumField: [MyEnum]
                  $listFloatField: [Float]
                  $listIntField: [Int]
                  $listStringField: [String]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $listBooleanField: [Boolean]
                  $listEnumField: [MyEnum]
                  $listFloatField: [Float]
                  $listIntField: [Int]
                  $listStringField: [String]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $listBooleanField: [Boolean]
                  $listEnumField: [MyEnum]
                  $listFloatField: [Float]
                  $listIntField: [Int]
                  $listStringField: [String]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $listBooleanField: [Boolean]
                  $listEnumField: [MyEnum]
                  $listFloatField: [Float]
                  $listIntField: [Int]
                  $listStringField: [String]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $listBooleanField: [Boolean]
                  $listEnumField: [MyEnum]
                  $listFloatField: [Float]
                  $listIntField: [Int]
                  $listStringField: [String]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $listBooleanField: [Boolean]
                  $listEnumField: [MyEnum]
                  $listFloatField: [Float]
                  $listIntField: [Int]
                  $listStringField: [String]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = null
                  $listEnumField: [MyEnum] = null
                  $listFloatField: [Float] = null
                  $listIntField: [Int] = null
                  $listStringField: [String] = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = null
                  $listEnumField: [MyEnum] = null
                  $listFloatField: [Float] = null
                  $listIntField: [Int] = null
                  $listStringField: [String] = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = null
                  $listEnumField: [MyEnum] = null
                  $listFloatField: [Float] = null
                  $listIntField: [Int] = null
                  $listStringField: [String] = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = null
                  $listEnumField: [MyEnum] = null
                  $listFloatField: [Float] = null
                  $listIntField: [Int] = null
                  $listStringField: [String] = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = null
                  $listEnumField: [MyEnum] = null
                  $listFloatField: [Float] = null
                  $listIntField: [Int] = null
                  $listStringField: [String] = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = null
                  $listEnumField: [MyEnum] = null
                  $listFloatField: [Float] = null
                  $listIntField: [Int] = null
                  $listStringField: [String] = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = [null]
                  $listEnumField: [MyEnum] = [null]
                  $listFloatField: [Float] = [null]
                  $listIntField: [Int] = [null]
                  $listStringField: [String] = [null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = [null]
                  $listEnumField: [MyEnum] = [null]
                  $listFloatField: [Float] = [null]
                  $listIntField: [Int] = [null]
                  $listStringField: [String] = [null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = [null]
                  $listEnumField: [MyEnum] = [null]
                  $listFloatField: [Float] = [null]
                  $listIntField: [Int] = [null]
                  $listStringField: [String] = [null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = [null]
                  $listEnumField: [MyEnum] = [null]
                  $listFloatField: [Float] = [null]
                  $listIntField: [Int] = [null]
                  $listStringField: [String] = [null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = [null]
                  $listEnumField: [MyEnum] = [null]
                  $listFloatField: [Float] = [null]
                  $listIntField: [Int] = [null]
                  $listStringField: [String] = [null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $listBooleanField: [Boolean] = [null]
                  $listEnumField: [MyEnum] = [null]
                  $listFloatField: [Float] = [null]
                  $listIntField: [Int] = [null]
                  $listStringField: [String] = [null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = false
                  $listEnumField: [MyEnum] = ENUM_4
                  $listFloatField: [Float] = 456.789e2
                  $listIntField: [Int] = 30
                  $listStringField: [String] = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = false
                  $listEnumField: [MyEnum] = ENUM_4
                  $listFloatField: [Float] = 456.789e2
                  $listIntField: [Int] = 30
                  $listStringField: [String] = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = false
                  $listEnumField: [MyEnum] = ENUM_4
                  $listFloatField: [Float] = 456.789e2
                  $listIntField: [Int] = 30
                  $listStringField: [String] = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = false
                  $listEnumField: [MyEnum] = ENUM_4
                  $listFloatField: [Float] = 456.789e2
                  $listIntField: [Int] = 30
                  $listStringField: [String] = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = false
                  $listEnumField: [MyEnum] = ENUM_4
                  $listFloatField: [Float] = 456.789e2
                  $listIntField: [Int] = 30
                  $listStringField: [String] = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = false
                  $listEnumField: [MyEnum] = ENUM_4
                  $listFloatField: [Float] = 456.789e2
                  $listIntField: [Int] = 30
                  $listStringField: [String] = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false]
                  $listEnumField: [MyEnum] = [ENUM_4]
                  $listFloatField: [Float] = [456.789e2]
                  $listIntField: [Int] = [30]
                  $listStringField: [String] = ["varDefault"]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false]
                  $listEnumField: [MyEnum] = [ENUM_4]
                  $listFloatField: [Float] = [456.789e2]
                  $listIntField: [Int] = [30]
                  $listStringField: [String] = ["varDefault"]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false]
                  $listEnumField: [MyEnum] = [ENUM_4]
                  $listFloatField: [Float] = [456.789e2]
                  $listIntField: [Int] = [30]
                  $listStringField: [String] = ["varDefault"]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false]
                  $listEnumField: [MyEnum] = [ENUM_4]
                  $listFloatField: [Float] = [456.789e2]
                  $listIntField: [Int] = [30]
                  $listStringField: [String] = ["varDefault"]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false]
                  $listEnumField: [MyEnum] = [ENUM_4]
                  $listFloatField: [Float] = [456.789e2]
                  $listIntField: [Int] = [30]
                  $listStringField: [String] = ["varDefault"]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false]
                  $listEnumField: [MyEnum] = [ENUM_4]
                  $listFloatField: [Float] = [456.789e2]
                  $listIntField: [Int] = [30]
                  $listStringField: [String] = ["varDefault"]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false, null]
                  $listEnumField: [MyEnum] = [ENUM_4, null]
                  $listFloatField: [Float] = [456.789e2, null]
                  $listIntField: [Int] = [30, null]
                  $listStringField: [String] = ["varDefault", null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false, null]
                  $listEnumField: [MyEnum] = [ENUM_4, null]
                  $listFloatField: [Float] = [456.789e2, null]
                  $listIntField: [Int] = [30, null]
                  $listStringField: [String] = ["varDefault", null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false, null]
                  $listEnumField: [MyEnum] = [ENUM_4, null]
                  $listFloatField: [Float] = [456.789e2, null]
                  $listIntField: [Int] = [30, null]
                  $listStringField: [String] = ["varDefault", null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false, null]
                  $listEnumField: [MyEnum] = [ENUM_4, null]
                  $listFloatField: [Float] = [456.789e2, null]
                  $listIntField: [Int] = [30, null]
                  $listStringField: [String] = ["varDefault", null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false, null]
                  $listEnumField: [MyEnum] = [ENUM_4, null]
                  $listFloatField: [Float] = [456.789e2, null]
                  $listIntField: [Int] = [30, null]
                  $listStringField: [String] = ["varDefault", null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $listBooleanField: [Boolean] = [false, null]
                  $listEnumField: [MyEnum] = [ENUM_4, null]
                  $listFloatField: [Float] = [456.789e2, null]
                  $listIntField: [Int] = [30, null]
                  $listStringField: [String] = ["varDefault", null]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean] > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum] > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float] > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int] > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String] > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean]!
                  $listEnumField: [MyEnum]!
                  $listFloatField: [Float]!
                  $listIntField: [Int]!
                  $listStringField: [String]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean]! > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum]! > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float]! > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int]! > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String]! > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean]!
                  $listEnumField: [MyEnum]!
                  $listFloatField: [Float]!
                  $listIntField: [Int]!
                  $listStringField: [String]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean]! > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum]! > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float]! > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int]! > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String]! > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean]!
                  $listEnumField: [MyEnum]!
                  $listFloatField: [Float]!
                  $listIntField: [Int]!
                  $listStringField: [String]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean]! > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum]! > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float]! > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int]! > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String]! > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean]!
                  $listEnumField: [MyEnum]!
                  $listFloatField: [Float]!
                  $listIntField: [Int]!
                  $listStringField: [String]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean]! > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum]! > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float]! > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int]! > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String]! > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean]!
                  $listEnumField: [MyEnum]!
                  $listFloatField: [Float]!
                  $listIntField: [Int]!
                  $listStringField: [String]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean]! > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum]! > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float]! > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int]! > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String]! > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean]!
                  $listEnumField: [MyEnum]!
                  $listFloatField: [Float]!
                  $listIntField: [Int]!
                  $listStringField: [String]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > of type < [Boolean]! > used in position expecting type < [Boolean!] >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 39},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listEnumField > of type < [MyEnum]! > used in position expecting type < [MyEnum!] >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 36},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listFloatField > of type < [Float]! > used in position expecting type < [Float!] >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 37},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listIntField > of type < [Int]! > used in position expecting type < [Int!] >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $listStringField > of type < [String]! > used in position expecting type < [String!] >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 38},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]
                  $listEnumField: [MyEnum!]
                  $listFloatField: [Float!]
                  $listIntField: [Int!]
                  $listStringField: [String!]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]
                  $listEnumField: [MyEnum!]
                  $listFloatField: [Float!]
                  $listIntField: [Int!]
                  $listStringField: [String!]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of non-null type < MyEnum! > must not be null.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of non-null type < Float! > must not be null.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of non-null type < String! > must not be null.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]
                  $listEnumField: [MyEnum!]
                  $listFloatField: [Float!]
                  $listIntField: [Int!]
                  $listStringField: [String!]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of non-null type < MyEnum! > must not be null.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of non-null type < Float! > must not be null.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of non-null type < String! > must not be null.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                    {
                        "message": "Variable < $listBooleanField > got invalid value < [None] >; Expected non-nullable type < Boolean! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $listEnumField > got invalid value < [None] >; Expected non-nullable type < MyEnum! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $listFloatField > got invalid value < [None] >; Expected non-nullable type < Float! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $listIntField > got invalid value < [None] >; Expected non-nullable type < Int! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $listStringField > got invalid value < [None] >; Expected non-nullable type < String! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]
                  $listEnumField: [MyEnum!]
                  $listFloatField: [Float!]
                  $listIntField: [Int!]
                  $listStringField: [String!]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]
                  $listEnumField: [MyEnum!]
                  $listFloatField: [Float!]
                  $listIntField: [Int!]
                  $listStringField: [String!]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]
                  $listEnumField: [MyEnum!]
                  $listFloatField: [Float!]
                  $listIntField: [Int!]
                  $listStringField: [String!]
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > got invalid value < [True, None] >; Expected non-nullable type < Boolean! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $listEnumField > got invalid value < ['ENUM_3', None] >; Expected non-nullable type < MyEnum! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $listFloatField > got invalid value < [345678.9, None] >; Expected non-nullable type < Float! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $listIntField > got invalid value < [20, None] >; Expected non-nullable type < Int! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $listStringField > got invalid value < ['varValue', None] >; Expected non-nullable type < String! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]!
                  $listEnumField: [MyEnum!]!
                  $listFloatField: [Float!]!
                  $listIntField: [Int!]!
                  $listStringField: [String!]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                    {
                        "message": "Variable < $listBooleanField > of required type < [Boolean!]! > was not provided.",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $listEnumField > of required type < [MyEnum!]! > was not provided.",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $listFloatField > of required type < [Float!]! > was not provided.",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $listIntField > of required type < [Int!]! > was not provided.",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $listStringField > of required type < [String!]! > was not provided.",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]!
                  $listEnumField: [MyEnum!]!
                  $listFloatField: [Float!]!
                  $listIntField: [Int!]!
                  $listStringField: [String!]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": None,
                "listEnumField": None,
                "listFloatField": None,
                "listIntField": None,
                "listStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of non-null type < MyEnum! > must not be null.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of non-null type < Float! > must not be null.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of non-null type < String! > must not be null.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                    {
                        "message": "Variable < $listBooleanField > of non-null type < [Boolean!]! > must not be null.",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $listEnumField > of non-null type < [MyEnum!]! > must not be null.",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $listFloatField > of non-null type < [Float!]! > must not be null.",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $listIntField > of non-null type < [Int!]! > must not be null.",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $listStringField > of non-null type < [String!]! > must not be null.",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]!
                  $listEnumField: [MyEnum!]!
                  $listFloatField: [Float!]!
                  $listIntField: [Int!]!
                  $listStringField: [String!]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "listBooleanField": [None],
                "listEnumField": [None],
                "listFloatField": [None],
                "listIntField": [None],
                "listStringField": [None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of non-null type < MyEnum! > must not be null.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of non-null type < Float! > must not be null.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of non-null type < String! > must not be null.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                    {
                        "message": "Variable < $listBooleanField > got invalid value < [None] >; Expected non-nullable type < Boolean! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $listEnumField > got invalid value < [None] >; Expected non-nullable type < MyEnum! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $listFloatField > got invalid value < [None] >; Expected non-nullable type < Float! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $listIntField > got invalid value < [None] >; Expected non-nullable type < Int! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $listStringField > got invalid value < [None] >; Expected non-nullable type < String! > not to be null at value[0].",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]!
                  $listEnumField: [MyEnum!]!
                  $listFloatField: [Float!]!
                  $listIntField: [Int!]!
                  $listStringField: [String!]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": True,
                "listEnumField": "ENUM_3",
                "listFloatField": 3456.789e2,
                "listIntField": 20,
                "listStringField": "varValue",
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]!
                  $listEnumField: [MyEnum!]!
                  $listFloatField: [Float!]!
                  $listIntField: [Int!]!
                  $listStringField: [String!]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True],
                "listEnumField": ["ENUM_3"],
                "listFloatField": [3456.789e2],
                "listIntField": [20],
                "listStringField": ["varValue"],
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:True]-[listEnumField:enum_3_3-myenum]-[listFloatField:345681.9]-[listIntField:23]-[listStringField:varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $listBooleanField: [Boolean!]!
                  $listEnumField: [MyEnum!]!
                  $listFloatField: [Float!]!
                  $listIntField: [Int!]!
                  $listStringField: [String!]!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: $listBooleanField
                    listEnumField: $listEnumField
                    listFloatField: $listFloatField
                    listIntField: $listIntField
                    listStringField: $listStringField
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "listBooleanField": [True, None],
                "listEnumField": ["ENUM_3", None],
                "listFloatField": [3456.789e2, None],
                "listIntField": [20, None],
                "listStringField": ["varValue", None],
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $listBooleanField > got invalid value < [True, None] >; Expected non-nullable type < Boolean! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $listEnumField > got invalid value < ['ENUM_3', None] >; Expected non-nullable type < MyEnum! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $listFloatField > got invalid value < [345678.9, None] >; Expected non-nullable type < Float! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $listIntField > got invalid value < [20, None] >; Expected non-nullable type < Int! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $listStringField > got invalid value < ['varValue', None] >; Expected non-nullable type < String! > not to be null at value[1].",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $itemBooleanField: Boolean
                  $itemEnumField: MyEnum
                  $itemFloatField: Float
                  $itemIntField: Int
                  $itemStringField: String
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemBooleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 47},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemEnumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 45},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemFloatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 51},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemIntField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 40},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemStringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 60},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $itemBooleanField: Boolean
                  $itemEnumField: MyEnum
                  $itemFloatField: Float
                  $itemIntField: Int
                  $itemStringField: String
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "itemBooleanField": None,
                "itemEnumField": None,
                "itemFloatField": None,
                "itemIntField": None,
                "itemStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemBooleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 47},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemEnumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 45},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemFloatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 51},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemIntField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 40},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemStringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 60},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean
                  $enumField: MyEnum
                  $floatField: Float
                  $intField: Int
                  $stringField: String
                  $itemBooleanField: Boolean
                  $itemEnumField: MyEnum
                  $itemFloatField: Float
                  $itemIntField: Int
                  $itemStringField: String
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "itemBooleanField": True,
                "itemEnumField": "ENUM_3",
                "itemFloatField": 3456.789e2,
                "itemIntField": 20,
                "itemStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemBooleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 47},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemEnumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 45},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemFloatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 51},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemIntField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 40},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemStringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 60},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $itemBooleanField: Boolean = null
                  $itemEnumField: MyEnum = null
                  $itemFloatField: Float = null
                  $itemIntField: Int = null
                  $itemStringField: String = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemBooleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 47},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemEnumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 45},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemFloatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 51},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemIntField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 40},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemStringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 60},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $itemBooleanField: Boolean = null
                  $itemEnumField: MyEnum = null
                  $itemFloatField: Float = null
                  $itemIntField: Int = null
                  $itemStringField: String = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "itemBooleanField": None,
                "itemEnumField": None,
                "itemFloatField": None,
                "itemIntField": None,
                "itemStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemBooleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 47},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemEnumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 45},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemFloatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 51},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemIntField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 40},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemStringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 60},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = null
                  $enumField: MyEnum = null
                  $floatField: Float = null
                  $intField: Int = null
                  $stringField: String = null
                  $itemBooleanField: Boolean = null
                  $itemEnumField: MyEnum = null
                  $itemFloatField: Float = null
                  $itemIntField: Int = null
                  $itemStringField: String = null
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "itemBooleanField": True,
                "itemEnumField": "ENUM_3",
                "itemFloatField": 3456.789e2,
                "itemIntField": 20,
                "itemStringField": "varValue",
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 2, "column": 19},
                            {"line": 14, "column": 35},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $enumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 3, "column": 19},
                            {"line": 15, "column": 32},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $floatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 4, "column": 19},
                            {"line": 16, "column": 33},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $intField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 5, "column": 19},
                            {"line": 17, "column": 31},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $stringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 6, "column": 19},
                            {"line": 18, "column": 34},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemBooleanField > of type < Boolean > used in position expecting type < Boolean! >.",
                        "path": None,
                        "locations": [
                            {"line": 7, "column": 19},
                            {"line": 19, "column": 47},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemEnumField > of type < MyEnum > used in position expecting type < MyEnum! >.",
                        "path": None,
                        "locations": [
                            {"line": 8, "column": 19},
                            {"line": 20, "column": 45},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemFloatField > of type < Float > used in position expecting type < Float! >.",
                        "path": None,
                        "locations": [
                            {"line": 9, "column": 19},
                            {"line": 21, "column": 51},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemIntField > of type < Int > used in position expecting type < Int! >.",
                        "path": None,
                        "locations": [
                            {"line": 10, "column": 19},
                            {"line": 22, "column": 40},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                    {
                        "message": "Variable < $itemStringField > of type < String > used in position expecting type < String! >.",
                        "path": None,
                        "locations": [
                            {"line": 11, "column": 19},
                            {"line": 23, "column": 60},
                        ],
                        "extensions": {
                            "spec": "June 2018",
                            "rule": "5.8.5",
                            "tag": "all-variable-usages-are-allowed",
                            "details": "https://spec.graphql.org/June2018/#sec-All-Variable-Usages-are-Allowed",
                        },
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $itemBooleanField: Boolean = false
                  $itemEnumField: MyEnum = ENUM_4
                  $itemFloatField: Float = 456.789e2
                  $itemIntField: Int = 30
                  $itemStringField: String = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            None,
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:False]-[enumField:ENUM_4_4-MyEnum-enumField]-[floatField:45681.9]-[intField:33]-[stringField:vardefault-scalar-stringField]-[listBooleanField:False-False]-[listEnumField:enum_2_2-myenum-enum_4_4-myenum]-[listFloatField:2345681.9-45681.9]-[listIntField:13-33]-[listStringField:paramdefaultvalue-scalar-vardefault-scalar]"
                }
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $itemBooleanField: Boolean = false
                  $itemEnumField: MyEnum = ENUM_4
                  $itemFloatField: Float = 456.789e2
                  $itemIntField: Int = 30
                  $itemStringField: String = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "itemBooleanField": None,
                "itemEnumField": None,
                "itemFloatField": None,
                "itemIntField": None,
                "itemStringField": None,
            },
            {
                "data": {"innerNonNullInputObjectField": None},
                "errors": [
                    {
                        "message": 'Argument < param > has invalid value < {booleanField: $booleanField, enumField: $enumField, floatField: $floatField, intField: $intField, stringField: $stringField, listBooleanField: [false, $itemBooleanField], listEnumField: [ENUM_2, $itemEnumField], listFloatField: [23456.789e2, $itemFloatField], listIntField: [10, $itemIntField], listStringField: ["paramDefaultValue", $itemStringField]} >.',
                        "path": ["innerNonNullInputObjectField"],
                        "locations": [{"line": 13, "column": 55}],
                    }
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean = false
                  $enumField: MyEnum = ENUM_4
                  $floatField: Float = 456.789e2
                  $intField: Int = 30
                  $stringField: String = "varDefault"
                  $itemBooleanField: Boolean = false
                  $itemEnumField: MyEnum = ENUM_4
                  $itemFloatField: Float = 456.789e2
                  $itemIntField: Int = 30
                  $itemStringField: String = "varDefault"
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "itemBooleanField": True,
                "itemEnumField": "ENUM_3",
                "itemFloatField": 3456.789e2,
                "itemIntField": 20,
                "itemStringField": "varValue",
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:False-True]-[listEnumField:enum_2_2-myenum-enum_3_3-myenum]-[listFloatField:2345681.9-345681.9]-[listIntField:13-23]-[listStringField:paramdefaultvalue-scalar-varvalue-scalar]"
                }
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $itemBooleanField: Boolean!
                  $itemEnumField: MyEnum!
                  $itemFloatField: Float!
                  $itemIntField: Int!
                  $itemStringField: String!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            None,
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemBooleanField > of required type < Boolean! > was not provided.",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemEnumField > of required type < MyEnum! > was not provided.",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemFloatField > of required type < Float! > was not provided.",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemIntField > of required type < Int! > was not provided.",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemStringField > of required type < String! > was not provided.",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $itemBooleanField: Boolean!
                  $itemEnumField: MyEnum!
                  $itemFloatField: Float!
                  $itemIntField: Int!
                  $itemStringField: String!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": None,
                "enumField": None,
                "floatField": None,
                "intField": None,
                "stringField": None,
                "itemBooleanField": None,
                "itemEnumField": None,
                "itemFloatField": None,
                "itemIntField": None,
                "itemStringField": None,
            },
            {
                "data": None,
                "errors": [
                    {
                        "message": "Variable < $booleanField > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 2, "column": 19}],
                    },
                    {
                        "message": "Variable < $enumField > of non-null type < MyEnum! > must not be null.",
                        "path": None,
                        "locations": [{"line": 3, "column": 19}],
                    },
                    {
                        "message": "Variable < $floatField > of non-null type < Float! > must not be null.",
                        "path": None,
                        "locations": [{"line": 4, "column": 19}],
                    },
                    {
                        "message": "Variable < $intField > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 5, "column": 19}],
                    },
                    {
                        "message": "Variable < $stringField > of non-null type < String! > must not be null.",
                        "path": None,
                        "locations": [{"line": 6, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemBooleanField > of non-null type < Boolean! > must not be null.",
                        "path": None,
                        "locations": [{"line": 7, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemEnumField > of non-null type < MyEnum! > must not be null.",
                        "path": None,
                        "locations": [{"line": 8, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemFloatField > of non-null type < Float! > must not be null.",
                        "path": None,
                        "locations": [{"line": 9, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemIntField > of non-null type < Int! > must not be null.",
                        "path": None,
                        "locations": [{"line": 10, "column": 19}],
                    },
                    {
                        "message": "Variable < $itemStringField > of non-null type < String! > must not be null.",
                        "path": None,
                        "locations": [{"line": 11, "column": 19}],
                    },
                ],
            },
        ),
        (
            """query (
                  $booleanField: Boolean!
                  $enumField: MyEnum!
                  $floatField: Float!
                  $intField: Int!
                  $stringField: String!
                  $itemBooleanField: Boolean!
                  $itemEnumField: MyEnum!
                  $itemFloatField: Float!
                  $itemIntField: Int!
                  $itemStringField: String!
                ) {
                  innerNonNullInputObjectField(param: {
                    booleanField: $booleanField
                    enumField: $enumField
                    floatField: $floatField
                    intField: $intField
                    stringField: $stringField
                    listBooleanField: [false, $itemBooleanField]
                    listEnumField: [ENUM_2, $itemEnumField]
                    listFloatField: [23456.789e2, $itemFloatField]
                    listIntField: [10, $itemIntField]
                    listStringField: ["paramDefaultValue", $itemStringField]
                  })
                }
                """,
            {
                "booleanField": True,
                "enumField": "ENUM_3",
                "floatField": 3456.789e2,
                "intField": 20,
                "stringField": "varValue",
                "itemBooleanField": True,
                "itemEnumField": "ENUM_3",
                "itemFloatField": 3456.789e2,
                "itemIntField": 20,
                "itemStringField": "varValue",
            },
            {
                "data": {
                    "innerNonNullInputObjectField": "SUCCESS-[booleanField:True]-[enumField:ENUM_3_3-MyEnum-enumField]-[floatField:345681.9]-[intField:23]-[stringField:varvalue-scalar-stringField]-[listBooleanField:False-True]-[listEnumField:enum_2_2-myenum-enum_3_3-myenum]-[listFloatField:2345681.9-345681.9]-[listIntField:13-23]-[listStringField:paramdefaultvalue-scalar-varvalue-scalar]"
                }
            },
        ),
    ],
)
async def test_coercer_inner_non_null_input_object_field(
    schema_stack, query, variables, expected
):
    assert await schema_stack.execute(query, variables=variables) == expected
