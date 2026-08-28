from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel
from .loyalty_event_adjust_points import LoyaltyEventAdjustPoints, LoyaltyEventAdjustPointsDict


class AdjustLoyaltyPointsRequest(SdkBaseModel):
    """Represents an `AdjustLoyaltyPoints <api-endpoint:Loyalty-AdjustLoyaltyPoints>`__ request."""

    idempotency_key: str
    """A unique string that identifies this ``AdjustLoyaltyPoints`` request. Keys can be any valid string, but must be
    unique for every request."""

    adjust_points: LoyaltyEventAdjustPoints
    """Provides metadata when the event ``type`` is ``ADJUST_POINTS``."""

    allow_negative_balance: OptionalNullable[bool] = UNSET
    """Indicates whether to allow a negative adjustment to result in a negative balance. If ``true``, a negative balance
    is allowed when subtracting points. If ``false``, Square returns a ``BAD_REQUEST`` error when subtracting the
    specified number of points would result in a negative balance. The default value is ``false``."""


class AdjustLoyaltyPointsRequestDict(TypedDict):
    idempotency_key: str
    adjust_points: LoyaltyEventAdjustPoints | LoyaltyEventAdjustPointsDict
    allow_negative_balance: NotRequired[bool | None]
