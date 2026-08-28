from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel


class LoyaltyEventOther(SdkBaseModel):
    """Provides metadata when the event ``type`` is ``OTHER``."""

    loyalty_program_id: str
    """The Square-assigned ID of the `loyalty program <entity:LoyaltyProgram>`__."""

    points: int
    """The number of points added or removed."""


class LoyaltyEventOtherDict(TypedDict):
    loyalty_program_id: str
    points: int
