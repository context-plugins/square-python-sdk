from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LoyaltyEventAccumulatePoints(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``ACCUMULATE_POINTS``."""

    loyalty_program_id: Optional[str] = UNSET
    """The ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    points: OptionalNullable[int] = UNSET
    """The number of points accumulated by the event."""

    order_id: OptionalNullable[str] = UNSET
    """The ID of the `order <entity:Order>`__ for which the buyer accumulated the points. This field is returned only if
    the Orders API is used to process orders."""


class LoyaltyEventAccumulatePointsDict(TypedDict):
    loyalty_program_id: NotRequired[str]
    points: NotRequired[int | None]
    order_id: NotRequired[str | None]
