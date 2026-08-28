from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute_definition import CustomAttributeDefinition, CustomAttributeDefinitionDict
from .error import Error, ErrorDict


class ListBookingCustomAttributeDefinitionsResponse(SdkBaseModel):
    """Represents a `ListBookingCustomAttributeDefinitions
    <api-endpoint:BookingCustomAttributes-ListBookingCustomAttributeDefinitions>`__ response. Either
    ``custom_attribute_definitions``, an empty object, or ``errors`` is present in the response. If additional results
    are available, the ``cursor`` field is also present along with ``custom_attribute_definitions``."""

    custom_attribute_definitions: Optional[list[CustomAttributeDefinition]] = UNSET
    """The retrieved custom attribute definitions. If no custom attribute definitions are found, Square returns an empty
    object (``{}``)."""

    cursor: Optional[str] = UNSET
    """The cursor to provide in your next call to this endpoint to retrieve the next page of results for your original
    request. This field is present only if the request succeeded and additional results are available. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListBookingCustomAttributeDefinitionsResponseDict(TypedDict):
    custom_attribute_definitions: NotRequired[list[CustomAttributeDefinition | CustomAttributeDefinitionDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
