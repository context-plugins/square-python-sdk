from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class GiftCardActivityType(str, Enum):
    """Indicates the type of `gift card activity <entity:GiftCardActivity>`__."""

    ACTIVATE = "ACTIVATE"
    """Activated a gift card with a balance. When a gift card is activated, Square changes the gift card state from
    ``PENDING`` to ``ACTIVE``. A gift card must be in the ``ACTIVE`` state to be used for other balance-changing
    activities."""

    LOAD = "LOAD"
    """Loaded a gift card with additional funds."""

    REDEEM = "REDEEM"
    """Redeemed a gift card for a purchase."""

    CLEAR_BALANCE = "CLEAR_BALANCE"
    """Set the balance of a gift card to zero."""

    DEACTIVATE = "DEACTIVATE"
    """Permanently blocked a gift card from balance-changing activities."""

    ADJUST_INCREMENT = "ADJUST_INCREMENT"
    """Added money to a gift card outside of a typical ``ACTIVATE``, ``LOAD``, or ``REFUND`` activity flow."""

    ADJUST_DECREMENT = "ADJUST_DECREMENT"
    """Deducted money from a gift card outside of a typical ``REDEEM`` activity flow."""

    REFUND = "REFUND"
    """Added money to a gift card from a refunded transaction. A ``REFUND`` activity might be linked to a Square
    payment, depending on how the payment and refund are processed. For example:
    - A payment processed by Square can be refunded to a ``PENDING`` or ``ACTIVE`` gift card using the Square
    Seller Dashboard, Square Point of Sale, or Refunds API.
    - A payment processed using a custom processing system can be refunded to the same gift card."""

    UNLINKED_ACTIVITY_REFUND = "UNLINKED_ACTIVITY_REFUND"
    """Added money to a gift card from a refunded transaction that was processed using a custom payment processing
    system and not linked to the gift card."""

    IMPORT = "IMPORT"
    """Imported a third-party gift card with a balance. ``IMPORT`` activities are managed by Square and cannot be
    created using the Gift Card Activities API."""

    BLOCK = "BLOCK"
    """Temporarily blocked a gift card from balance-changing activities. ``BLOCK`` activities are managed by Square and
    cannot be created using the Gift Card Activities API."""

    UNBLOCK = "UNBLOCK"
    """Unblocked a gift card, which enables it to resume balance-changing activities. ``UNBLOCK`` activities are managed
    by Square and cannot be created using the Gift Card Activities API."""

    IMPORT_REVERSAL = "IMPORT_REVERSAL"
    """Reversed the import of a third-party gift card, which sets the gift card state to ``PENDING`` and clears the
    balance. ``IMPORT_REVERSAL`` activities are managed by Square and cannot be created using the Gift Card Activities
    API."""

    TRANSFER_BALANCE_FROM = "TRANSFER_BALANCE_FROM"
    """Deducted money from a gift card as the result of a transfer to the balance of another gift card.
    ``TRANSFER_BALANCE_FROM`` activities are managed by Square and cannot be created using the Gift Card Activities
    API."""

    TRANSFER_BALANCE_TO = "TRANSFER_BALANCE_TO"
    """Added money to a gift card as the result of a transfer from the balance of another gift card.
    ``TRANSFER_BALANCE_TO`` activities are managed by Square and cannot be created using the Gift Card Activities
    API."""

    __str__ = str.__str__


GiftCardActivityTypeOrStr: TypeAlias = Annotated[GiftCardActivityType | str, open_enum_validator(GiftCardActivityType)]
