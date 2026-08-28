from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class CatalogItemProductType(str, Enum):
    """The type of a CatalogItem. Connect V2 only allows the creation of ``REGULAR`` or ``APPOINTMENTS_SERVICE``
    items."""

    REGULAR = "REGULAR"
    """An ordinary item."""

    GIFT_CARD = "GIFT_CARD"
    """A Square gift card."""

    APPOINTMENTS_SERVICE = "APPOINTMENTS_SERVICE"
    """A service that can be booked using the Square Appointments app."""

    FOOD_AND_BEV = "FOOD_AND_BEV"
    """A food or beverage item that can be sold by restaurants and other food venues."""

    EVENT = "EVENT"
    """An event which tickets can be sold for, including location, address, and times."""

    DIGITAL = "DIGITAL"
    """A digital item like an ebook or song."""

    DONATION = "DONATION"
    """A donation which site visitors can send for any cause."""

    LEGACY_SQUARE_ONLINE_SERVICE = "LEGACY_SQUARE_ONLINE_SERVICE"
    """A legacy Square Online service that is manually fulfilled. This corresponds to the ``Other`` item type displayed
    in the Square Seller Dashboard and Square POS apps."""

    LEGACY_SQUARE_ONLINE_MEMBERSHIP = "LEGACY_SQUARE_ONLINE_MEMBERSHIP"
    """A legacy Square Online membership that is manually fulfilled. This corresponds to the ``Membership`` item type
    displayed in the Square Seller Dashboard and Square POS apps."""

    __str__ = str.__str__


CatalogItemProductTypeOrStr: TypeAlias = Annotated[
    CatalogItemProductType | str, open_enum_validator(CatalogItemProductType)
]
