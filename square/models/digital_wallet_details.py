from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .cash_app_details import CashAppDetails, CashAppDetailsDict
from .error import Error, ErrorDict
from .lightning_details import LightningDetails, LightningDetailsDict


class DigitalWalletDetails(SdkBaseModel):
    """Additional details about ``WALLET`` type payments. Contains only non-confidential information."""

    status: OptionalNullable[str] = UNSET
    """The status of the ``WALLET`` payment. The status can be ``AUTHORIZED``, ``CAPTURED``, ``VOIDED``, or
    ``FAILED``."""

    brand: OptionalNullable[str] = UNSET
    """The brand used for the ``WALLET`` payment. The brand can be ``CASH_APP``, ``PAYPAY``, ``ALIPAY``,
    ``RAKUTEN_PAY``, ``AU_PAY``, ``D_BARAI``, ``MERPAY``, ``WECHAT_PAY``, ``LIGHTNING`` or ``UNKNOWN``."""

    cash_app_details: Optional[CashAppDetails] = UNSET
    """Additional details about ``WALLET`` type payments with the ``brand`` of ``CASH_APP``."""

    lightning_details: Optional[LightningDetails] = UNSET
    """Additional details about ``WALLET`` type payments with the ``brand`` of ``LIGHTNING``."""

    errors: Optional[list[Error]] = UNSET
    """Information about errors encountered during the payment."""


class DigitalWalletDetailsDict(TypedDict):
    status: NotRequired[str | None]
    brand: NotRequired[str | None]
    cash_app_details: NotRequired[CashAppDetailsDict]
    lightning_details: NotRequired[LightningDetailsDict]
    errors: NotRequired[list[ErrorDict]]
