from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.gift_card_activity_type import GiftCardActivityTypeOrStr
from .gift_card_activity_activate import GiftCardActivityActivate, GiftCardActivityActivateDict
from .gift_card_activity_adjust_decrement import GiftCardActivityAdjustDecrement, GiftCardActivityAdjustDecrementDict
from .gift_card_activity_adjust_increment import GiftCardActivityAdjustIncrement, GiftCardActivityAdjustIncrementDict
from .gift_card_activity_block import GiftCardActivityBlock, GiftCardActivityBlockDict
from .gift_card_activity_clear_balance import GiftCardActivityClearBalance, GiftCardActivityClearBalanceDict
from .gift_card_activity_deactivate import GiftCardActivityDeactivate, GiftCardActivityDeactivateDict
from .gift_card_activity_import import GiftCardActivityImport, GiftCardActivityImportDict
from .gift_card_activity_import_reversal import GiftCardActivityImportReversal, GiftCardActivityImportReversalDict
from .gift_card_activity_load import GiftCardActivityLoad, GiftCardActivityLoadDict
from .gift_card_activity_redeem import GiftCardActivityRedeem, GiftCardActivityRedeemDict
from .gift_card_activity_refund import GiftCardActivityRefund, GiftCardActivityRefundDict
from .gift_card_activity_transfer_balance_from import (
    GiftCardActivityTransferBalanceFrom,
    GiftCardActivityTransferBalanceFromDict,
)
from .gift_card_activity_transfer_balance_to import (
    GiftCardActivityTransferBalanceTo,
    GiftCardActivityTransferBalanceToDict,
)
from .gift_card_activity_unblock import GiftCardActivityUnblock, GiftCardActivityUnblockDict
from .gift_card_activity_unlinked_activity_refund import (
    GiftCardActivityUnlinkedActivityRefund,
    GiftCardActivityUnlinkedActivityRefundDict,
)
from .money import Money, MoneyDict


class GiftCardActivity(SdkBaseModel):
    """Represents an action performed on a `gift card <entity:GiftCard>`__ that affects its state or balance. A gift
    card activity contains information about a specific activity type. For example, a ``REDEEM`` activity includes a
    ``redeem_activity_details`` field that contains information about the redemption."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the gift card activity."""

    type_: GiftCardActivityTypeOrStr = Field(alias="type")
    """Indicates the type of `gift card activity <entity:GiftCardActivity>`__."""

    location_id: str
    """The ID of the `business location <entity:Location>`__ where the activity occurred."""

    created_at: Optional[str] = UNSET
    """The timestamp when the gift card activity was created, in RFC 3339 format."""

    gift_card_id: OptionalNullable[str] = UNSET
    """The gift card ID. When creating a gift card activity, ``gift_card_id`` is not required if ``gift_card_gan`` is
    specified."""

    gift_card_gan: OptionalNullable[str] = UNSET
    """The gift card account number (GAN). When creating a gift card activity, ``gift_card_gan`` is not required if
    ``gift_card_id`` is specified."""

    gift_card_balance_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    load_activity_details: Optional[GiftCardActivityLoad] = UNSET
    """Represents details about a ``LOAD`` `gift card activity type <entity:GiftCardActivityType>`__."""

    activate_activity_details: Optional[GiftCardActivityActivate] = UNSET
    """Represents details about an ``ACTIVATE`` `gift card activity type <entity:GiftCardActivityType>`__."""

    redeem_activity_details: Optional[GiftCardActivityRedeem] = UNSET
    """Represents details about a ``REDEEM`` `gift card activity type <entity:GiftCardActivityType>`__."""

    clear_balance_activity_details: Optional[GiftCardActivityClearBalance] = UNSET
    """Represents details about a ``CLEAR_BALANCE`` `gift card activity type <entity:GiftCardActivityType>`__."""

    deactivate_activity_details: Optional[GiftCardActivityDeactivate] = UNSET
    """Represents details about a ``DEACTIVATE`` `gift card activity type <entity:GiftCardActivityType>`__."""

    adjust_increment_activity_details: Optional[GiftCardActivityAdjustIncrement] = UNSET
    """Represents details about an ``ADJUST_INCREMENT`` `gift card activity type <entity:GiftCardActivityType>`__."""

    adjust_decrement_activity_details: Optional[GiftCardActivityAdjustDecrement] = UNSET
    """Represents details about an ``ADJUST_DECREMENT`` `gift card activity type <entity:GiftCardActivityType>`__."""

    refund_activity_details: Optional[GiftCardActivityRefund] = UNSET
    """Represents details about a ``REFUND`` `gift card activity type <entity:GiftCardActivityType>`__."""

    unlinked_activity_refund_activity_details: Optional[GiftCardActivityUnlinkedActivityRefund] = UNSET
    """Represents details about an ``UNLINKED_ACTIVITY_REFUND`` `gift card activity type
    <entity:GiftCardActivityType>`__."""

    import_activity_details: Optional[GiftCardActivityImport] = UNSET
    """Represents details about an ``IMPORT`` `gift card activity type <entity:GiftCardActivityType>`__. This activity
    type is used when Square imports a third-party gift card, in which case the ``gan_source`` of the gift card is set
    to ``OTHER``."""

    block_activity_details: Optional[GiftCardActivityBlock] = UNSET
    """Represents details about a ``BLOCK`` `gift card activity type <entity:GiftCardActivityType>`__."""

    unblock_activity_details: Optional[GiftCardActivityUnblock] = UNSET
    """Represents details about an ``UNBLOCK`` `gift card activity type <entity:GiftCardActivityType>`__."""

    import_reversal_activity_details: Optional[GiftCardActivityImportReversal] = UNSET
    """Represents details about an ``IMPORT_REVERSAL`` `gift card activity type <entity:GiftCardActivityType>`__."""

    transfer_balance_to_activity_details: Optional[GiftCardActivityTransferBalanceTo] = UNSET
    """Represents details about a ``TRANSFER_BALANCE_TO`` `gift card activity type <entity:GiftCardActivityType>`__."""

    transfer_balance_from_activity_details: Optional[GiftCardActivityTransferBalanceFrom] = UNSET
    """Represents details about a ``TRANSFER_BALANCE_FROM`` `gift card activity type
    <entity:GiftCardActivityType>`__."""


class GiftCardActivityDict(TypedDict):
    id: NotRequired[str]
    type_: GiftCardActivityTypeOrStr
    location_id: str
    created_at: NotRequired[str]
    gift_card_id: NotRequired[str | None]
    gift_card_gan: NotRequired[str | None]
    gift_card_balance_money: NotRequired[Money | MoneyDict]
    load_activity_details: NotRequired[GiftCardActivityLoad | GiftCardActivityLoadDict]
    activate_activity_details: NotRequired[GiftCardActivityActivate | GiftCardActivityActivateDict]
    redeem_activity_details: NotRequired[GiftCardActivityRedeem | GiftCardActivityRedeemDict]
    clear_balance_activity_details: NotRequired[GiftCardActivityClearBalance | GiftCardActivityClearBalanceDict]
    deactivate_activity_details: NotRequired[GiftCardActivityDeactivate | GiftCardActivityDeactivateDict]
    adjust_increment_activity_details: NotRequired[
        GiftCardActivityAdjustIncrement | GiftCardActivityAdjustIncrementDict
    ]
    adjust_decrement_activity_details: NotRequired[
        GiftCardActivityAdjustDecrement | GiftCardActivityAdjustDecrementDict
    ]
    refund_activity_details: NotRequired[GiftCardActivityRefund | GiftCardActivityRefundDict]
    unlinked_activity_refund_activity_details: NotRequired[
        GiftCardActivityUnlinkedActivityRefund | GiftCardActivityUnlinkedActivityRefundDict
    ]
    import_activity_details: NotRequired[GiftCardActivityImport | GiftCardActivityImportDict]
    block_activity_details: NotRequired[GiftCardActivityBlock | GiftCardActivityBlockDict]
    unblock_activity_details: NotRequired[GiftCardActivityUnblock | GiftCardActivityUnblockDict]
    import_reversal_activity_details: NotRequired[GiftCardActivityImportReversal | GiftCardActivityImportReversalDict]
    transfer_balance_to_activity_details: NotRequired[
        GiftCardActivityTransferBalanceTo | GiftCardActivityTransferBalanceToDict
    ]
    transfer_balance_from_activity_details: NotRequired[
        GiftCardActivityTransferBalanceFrom | GiftCardActivityTransferBalanceFromDict
    ]
