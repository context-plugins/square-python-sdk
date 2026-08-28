from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class ReferenceType(str, Enum):
    """The type of platform concept a channel can represent."""

    UNKNOWN_TYPE = "UNKNOWN_TYPE"
    LOCATION = "LOCATION"
    FIRST_PARTY_INTEGRATION = "FIRST_PARTY_INTEGRATION"
    OAUTH_APPLICATION = "OAUTH_APPLICATION"
    ONLINE_SITE = "ONLINE_SITE"
    ONLINE_CHECKOUT = "ONLINE_CHECKOUT"
    INVOICE = "INVOICE"
    GIFT_CARD = "GIFT_CARD"
    GIFT_CARD_MARKETPLACE = "GIFT_CARD_MARKETPLACE"
    RECURRING_SUBSCRIPTION = "RECURRING_SUBSCRIPTION"
    ONLINE_BOOKING_FLOW = "ONLINE_BOOKING_FLOW"
    SQUARE_ASSISTANT = "SQUARE_ASSISTANT"
    CASH_LOCAL = "CASH_LOCAL"
    POINT_OF_SALE = "POINT_OF_SALE"
    KIOSK = "KIOSK"

    __str__ = str.__str__


ReferenceTypeOrStr: TypeAlias = Annotated[ReferenceType | str, open_enum_validator(ReferenceType)]
