from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .range import Range, RangeDict


class CustomAttributeFilter(SdkBaseModel):
    """Supported custom attribute query expressions for calling the `SearchCatalogItems
    <api-endpoint:Catalog-SearchCatalogItems>`__ endpoint to search for items or item variations."""

    custom_attribute_definition_id: OptionalNullable[str] = UNSET
    """A query expression to filter items or item variations by matching their custom attributes'
    ``custom_attribute_definition_id`` property value against the the specified id. Exactly one of
    ``custom_attribute_definition_id`` or ``key`` must be specified."""

    key: OptionalNullable[str] = UNSET
    """A query expression to filter items or item variations by matching their custom attributes' ``key`` property value
    against the specified key. Exactly one of ``custom_attribute_definition_id`` or ``key`` must be specified."""

    string_filter: OptionalNullable[str] = UNSET
    """A query expression to filter items or item variations by matching their custom attributes' ``string_value``
    property value against the specified text. Exactly one of ``string_filter``, ``number_filter``,
    ``selection_uids_filter``, or ``bool_filter`` must be specified."""

    number_filter: Optional[Range] = UNSET
    """The range of a number value between the specified lower and upper bounds."""

    selection_uids_filter: Optional[list[str | None]] = UNSET
    """A query expression to filter items or item variations by matching their custom attributes'
    ``selection_uid_values`` values against the specified selection uids. Exactly one of ``string_filter``,
    ``number_filter``, ``selection_uids_filter``, or ``bool_filter`` must be specified."""

    bool_filter: OptionalNullable[bool] = UNSET
    """A query expression to filter items or item variations by matching their custom attributes' ``boolean_value``
    property values against the specified Boolean expression. Exactly one of ``string_filter``, ``number_filter``,
    ``selection_uids_filter``, or ``bool_filter`` must be specified."""


class CustomAttributeFilterDict(TypedDict):
    custom_attribute_definition_id: NotRequired[str | None]
    key: NotRequired[str | None]
    string_filter: NotRequired[str | None]
    number_filter: NotRequired[Range | RangeDict]
    selection_uids_filter: NotRequired[list[str | None]]
    bool_filter: NotRequired[bool | None]
