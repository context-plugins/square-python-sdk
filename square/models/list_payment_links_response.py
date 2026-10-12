from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict
from .payment_link import PaymentLink, PaymentLinkDict


class ListPaymentLinksResponse(SdkBaseModel):
    errors: Optional[list[Error]] = UNSET
    """Errors that occurred during the request."""

    payment_links: Optional[list[PaymentLink]] = UNSET
    """The list of payment links."""

    cursor: Optional[str] = UNSET
    """When a response is truncated, it includes a cursor that you can use in a subsequent request to retrieve the next
    set of gift cards. If a cursor is not present, this is the final response. For more information, see `Pagination
    <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__."""


class ListPaymentLinksResponseDict(TypedDict):
    errors: NotRequired[list[ErrorDict]]
    payment_links: NotRequired[list[PaymentLinkDict]]
    cursor: NotRequired[str]
