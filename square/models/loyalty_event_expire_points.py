from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyEventExpirePoints(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``EXPIRE_POINTS``."""

    loyalty_program_id: str
    """The Square-assigned ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    points: int
    """The number of points expired."""


class LoyaltyEventExpirePointsDict(TypedDict):
    loyalty_program_id: str
    points: int
