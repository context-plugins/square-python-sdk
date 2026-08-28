from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .afterpay_details import AfterpayDetails, AfterpayDetailsDict
from .clearpay_details import ClearpayDetails, ClearpayDetailsDict
from .error import Error, ErrorDict


class BuyNowPayLaterDetails(SdkBaseModel):
    """Additional details about a Buy Now Pay Later payment type."""

    brand: OptionalNullable[str] = UNSET
    """The brand used for the Buy Now Pay Later payment. The brand can be ``AFTERPAY``, ``CLEARPAY`` or ``UNKNOWN``."""

    afterpay_details: Optional[AfterpayDetails] = UNSET
    """Additional details about Afterpay payments."""

    clearpay_details: Optional[ClearpayDetails] = UNSET
    """Additional details about Clearpay payments."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the payment."""


class BuyNowPayLaterDetailsDict(TypedDict):
    brand: NotRequired[str | None]
    afterpay_details: NotRequired[AfterpayDetails | AfterpayDetailsDict]
    clearpay_details: NotRequired[ClearpayDetails | ClearpayDetailsDict]
    errors: NotRequired[list[Error | ErrorDict]]
