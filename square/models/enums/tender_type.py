from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class TenderType(str, Enum):
    """Indicates a tender's type."""

    CARD = "CARD"
    """A credit card."""

    CASH = "CASH"
    """Cash."""

    THIRD_PARTY_CARD = "THIRD_PARTY_CARD"
    """A credit card processed with a card processor other than Square.

    This value applies only to merchants in countries where Square does not yet provide card processing."""

    SQUARE_GIFT_CARD = "SQUARE_GIFT_CARD"
    """A Square gift card."""

    NO_SALE = "NO_SALE"
    """This tender represents the register being opened for a "no sale" event."""

    BANK_ACCOUNT = "BANK_ACCOUNT"
    """A bank account payment."""

    WALLET = "WALLET"
    """A payment from a digital wallet, e.g. Cash App, Paypay, Rakuten Pay, Au Pay, D Barai, Merpay, Wechat Pay, Alipay.

    Note: Some "digital wallets", including Google Pay and Apple Pay, facilitate card payments. Those payments have the
    ``CARD`` type."""

    BUY_NOW_PAY_LATER = "BUY_NOW_PAY_LATER"
    """A Buy Now Pay Later payment."""

    SQUARE_ACCOUNT = "SQUARE_ACCOUNT"
    """A Square House Account payment."""

    OTHER = "OTHER"
    """A form of tender that does not match any other value."""

    __str__ = str.__str__


TenderTypeOrStr: TypeAlias = Annotated[TenderType | str, open_enum_validator(TenderType)]
