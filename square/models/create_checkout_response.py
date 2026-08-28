from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .checkout import Checkout, CheckoutDict
from .error import Error, ErrorDict


class CreateCheckoutResponse(SdkBaseModel):
    """Defines the fields that are included in the response body of a request to the ``CreateCheckout`` endpoint."""

    checkout: Optional[Checkout] = UNSET
    """Square Checkout lets merchants accept online payments for supported payment types using a checkout workflow
    hosted on squareup.com."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""


class CreateCheckoutResponseDict(TypedDict):
    checkout: NotRequired[Checkout | CheckoutDict]
    errors: NotRequired[list[Error | ErrorDict]]
