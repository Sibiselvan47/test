OK = None
SKIP = object()
BREAK = object()
REMOVE = object()

QUERY_DOCUMENT_KEYS = {
    "NameNode": (),
    "DocumentNode": ("definitions",),
    "OperationDefinitionNode": (
        "name",
        "variable_definitions",
        "directives",
        "selection_set",
    ),
    "VariableDefinitionNode": ("variable", "type", "default_value"),
    "VariableNode": ("name",),
    "SelectionSetNode": ("selections",),
    "FieldNode": ("alias", "name", "arguments", "directives", "selection_set"),
    "ArgumentNode": ("name", "value"),
    "FragmentSpreadNode": ("name", "directives"),
    "InlineFragmentNode": ("type_condition", "directives", "selection_set"),
    "FragmentDefinitionNode": (
        "name",
        "type_condition",
        "directives",
        "selection_set",
    ),
    "IntValueNode": (),
    "FloatValueNode": (),
    "StringValueNode": (),
    "BooleanValueNode": (),
    "NullValueNode": (),
    "EnumValueNode": (),
    "ListValueNode": ("values",),
    "ObjectValueNode": ("fields",),
    "ObjectFieldNode": ("name", "value"),
    "DirectiveNode": ("name", "arguments"),
    "NamedTypeNode": ("name",),
    "ListTypeNode": ("type",),
    "NonNullTypeNode": ("type",),
    "SchemaDefinitionNode": ("directives", "operation_type_definitions"),
    "OperationTypeDefinitionNode": ("type",),
    "ScalarTypeDefinitionNode": ("description", "name", "directives"),
    "ObjectTypeDefinitionNode": (
        "description",
        "name",
        "interfaces",
        "directives",
        "fields",
    ),
    "FieldDefinitionNode": (
        "description",
        "name",
        "arguments",
        "type",
        "directives",
    ),
    "InputValueDefinitionNode": (
        "description",
        "name",
        "type",
        "default_value",
        "directives",
    ),
    "InterfaceTypeDefinitionNode": (
        "description",
        "name",
        "directives",
        "fields",
    ),
    "UnionTypeDefinitionNode": ("description", "name", "directives", "types"),
    "EnumTypeDefinitionNode": ("description", "name", "directives", "values"),
    "EnumValueDefinitionNode": ("description", "name", "directives"),
    "InputObjectTypeDefinitionNode": (
        "description",
        "name",
        "directives",
        "fields",
    ),
    "DirectiveDefinitionNode": (
        "description",
        "name",
        "arguments",
        "locations",
    ),
    "SchemaExtensionNode": ("directives", "operation_type_definitions"),
    "ScalarTypeExtensionNode": ("name", "directives"),
    "ObjectTypeExtensionNode": ("name", "interfaces", "directives", "fields"),
    "InterfaceTypeExtensionNode": ("name", "directives", "fields"),
    "UnionTypeExtensionNode": ("name", "directives", "types"),
    "EnumTypeExtensionNode": ("name", "directives", "values"),
    "InputObjectTypeExtensionNode": ("name", "directives", "fields"),
}

__all__ = ("OK", "SKIP", "BREAK", "REMOVE", "QUERY_DOCUMENT_KEYS")
