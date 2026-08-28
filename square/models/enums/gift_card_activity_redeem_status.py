from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityRedeemStatus(str, Enum):
    """Indicates the status of a `gift card <entity:GiftCard>`__ redemption. This status is relevant only for
    redemptions made from Square products (such as Square Point of Sale) because Square products use a two-state
    process. Gift cards redeemed using the Gift Card Activities API always have a ``COMPLETED`` status."""

    PENDING = "PENDING"
    """The gift card redemption is pending. ``PENDING`` is a temporary status that applies when a gift card is redeemed
    from Square Point of Sale or another Square product. A ``PENDING`` status is updated to ``COMPLETED`` if the payment
    is captured or ``CANCELED`` if the authorization is voided."""

    COMPLETED = "COMPLETED"
    """The gift card redemption is completed."""

    CANCELED = "CANCELED"
    """The gift card redemption is canceled. A redemption is canceled if the authorization on the gift card is
    voided."""

    __str__ = str.__str__


GiftCardActivityRedeemStatusOrStr: TypeAlias = Annotated[
    GiftCardActivityRedeemStatus | str, open_enum_validator(GiftCardActivityRedeemStatus)
]
