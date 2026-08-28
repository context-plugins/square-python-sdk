from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CheckoutOptionsPaymentType(str, Enum):
    CARD_PRESENT = "CARD_PRESENT"
    """Accept credit card or debit card payments via tap, dip or swipe."""

    MANUAL_CARD_ENTRY = "MANUAL_CARD_ENTRY"
    """Launches the manual credit or debit card entry screen for the buyer to complete."""

    FELICA_ID = "FELICA_ID"
    """Launches the iD checkout screen for the buyer to complete."""

    FELICA_QUICPAY = "FELICA_QUICPAY"
    """Launches the QUICPay checkout screen for the buyer to complete."""

    FELICA_TRANSPORTATION_GROUP = "FELICA_TRANSPORTATION_GROUP"
    """Launches the Transportation Group checkout screen for the buyer to complete."""

    FELICA_ALL = "FELICA_ALL"
    """Launches a checkout screen for the buyer on the Square Terminal that allows them to select a specific FeliCa
    brand or select the check balance screen."""

    PAYPAY = "PAYPAY"
    """Replaced by ``QR_CODE``."""

    QR_CODE = "QR_CODE"
    """Launches Square's QR Code checkout screen for the buyer to complete. Displays a single code that supports all
    digital wallets connected to the target Seller location (e.g. PayPay)"""

    __str__ = str.__str__


CheckoutOptionsPaymentTypeOrStr: TypeAlias = Annotated[
    CheckoutOptionsPaymentType | str, open_enum_validator(CheckoutOptionsPaymentType)
]
