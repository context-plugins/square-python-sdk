from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .loyalty_account_expiring_point_deadline import (
    LoyaltyAccountExpiringPointDeadline,
    LoyaltyAccountExpiringPointDeadlineDict,
)
from .loyalty_account_mapping import LoyaltyAccountMapping, LoyaltyAccountMappingDict


class LoyaltyAccount(SdkBaseModel):
    """Describes a loyalty account in a `loyalty program <entity:LoyaltyProgram>`__. For more information, see `Create
    and Retrieve Loyalty Accounts <https://developer.squareup.com/docs/loyalty-api/loyalty-accounts>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the loyalty account."""

    program_id: str
    """The Square-assigned ID of the `loyalty program <entity:LoyaltyProgram>`__ to which the account belongs."""

    balance: Optional[int] = UNSET
    """The available point balance in the loyalty account. If points are scheduled to expire, they are listed in the
    ``expiring_point_deadlines`` field.

    Your application should be able to handle loyalty accounts that have a negative point balance (``balance`` is less
    than 0). This might occur if a seller makes a manual adjustment or as a result of a refund or exchange."""

    lifetime_points: Optional[int] = UNSET
    """The total points accrued during the lifetime of the account."""

    customer_id: OptionalNullable[str] = UNSET
    """The Square-assigned ID of the `customer <entity:Customer>`__ that is associated with the account."""

    enrolled_at: OptionalNullable[str] = UNSET
    """The timestamp when the buyer joined the loyalty program, in RFC 3339 format. This field is used to display the
    **Enrolled On** or **Member Since** date in first-party Square products.

    If this field is not set in a ``CreateLoyaltyAccount`` request, Square populates it after the buyer's first action
    on their account (when ``AccumulateLoyaltyPoints`` or ``CreateLoyaltyReward`` is called). In first-party flows,
    Square populates the field when the buyer agrees to the terms of service on Square Point of Sale.

    If this field is set in a ``CreateLoyaltyAccount`` request, it is meant to be used when there is a loyalty migration
    from another system and into Square. In that case, the timestamp can reflect when the buyer originally enrolled in
    the previous system. It may represent a current or past date, but cannot be set in the future. Note: Setting this
    field in this scenario does not, by itself, impact the first-party enrollment flow on Square Point of Sale."""

    created_at: Optional[str] = UNSET
    """The timestamp when the loyalty account was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the loyalty account was last updated, in RFC 3339 format."""

    mapping: Optional[LoyaltyAccountMapping] = UNSET
    """Represents the mapping that associates a loyalty account with a buyer.

    Currently, a loyalty account can only be mapped to a buyer by phone number. For more information, see `Loyalty
    Overview <https://developer.squareup.com/docs/loyalty/overview>`__."""

    expiring_point_deadlines: OptionalNullable[list[LoyaltyAccountExpiringPointDeadline]] = UNSET
    """The schedule for when points expire in the loyalty account balance. This field is present only if the account has
    points that are scheduled to expire.

    The total number of points in this field equals the number of points in the ``balance`` field."""


class LoyaltyAccountDict(TypedDict):
    id: NotRequired[str]
    program_id: str
    balance: NotRequired[int]
    lifetime_points: NotRequired[int]
    customer_id: NotRequired[str | None]
    enrolled_at: NotRequired[str | None]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
    mapping: NotRequired[LoyaltyAccountMappingDict]
    expiring_point_deadlines: NotRequired[list[LoyaltyAccountExpiringPointDeadlineDict] | None]
