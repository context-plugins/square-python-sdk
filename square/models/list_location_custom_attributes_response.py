from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .custom_attribute import CustomAttribute, CustomAttributeDict
from .error import Error, ErrorDict


class ListLocationCustomAttributesResponse(SdkBaseModel):
    """Represents a `ListLocationCustomAttributes
    <api-endpoint:LocationCustomAttributes-ListLocationCustomAttributes>`__ response. Either ``custom_attributes``, an
    empty object, or ``errors`` is present in the response. If additional results are available, the ``cursor`` field is
    also present along with ``custom_attributes``."""

    custom_attributes: Optional[list[CustomAttribute]] = UNSET
    """The retrieved custom attributes. If ``with_definitions`` was set to ``true`` in the request, the custom attribute
    definition is returned in the ``definition`` field of each custom attribute. If no custom attributes are found,
    Square returns an empty object (``{}``)."""

    cursor: Optional[str] = UNSET
    """The cursor to use in your next call to this endpoint to retrieve the next page of results for your original
    request. This field is present only if the request succeeded and additional results are available. For more
    information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class ListLocationCustomAttributesResponseDict(TypedDict):
    custom_attributes: NotRequired[list[CustomAttribute | CustomAttributeDict]]
    cursor: NotRequired[str]
    errors: NotRequired[list[Error | ErrorDict]]
