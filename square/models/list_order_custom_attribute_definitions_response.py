from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict
from .error import Error, ErrorDict


class ListOrderCustomAttributeDefinitionsResponse(SdkBaseModel):
    """Represents a response from listing order custom attribute definitions."""

    custom_attribute_definitions: list[CustomAttributeDefinition]
    """The retrieved custom attribute definitions. If no custom attribute definitions are found, Square returns an empty
    object (``{}``)."""

    cursor: Optional[str] = UNSET
    """The cursor to provide in your next call to this endpoint to retrieve the next page of results for your original
    request. This field is present only if the request succeeded and additional results are available. For more
    information, see `Pagination <https://developer.squareup.com/docs/working-with-apis/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListOrderCustomAttributeDefinitionsResponseDict(TypedDict):
    custom_attribute_definitions: list[CustomAttributeDefinition | CustomAttributeDefinitionDict]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
