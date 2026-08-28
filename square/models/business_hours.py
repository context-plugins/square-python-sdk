from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .business_hours_period import BusinessHoursPeriod, BusinessHoursPeriodDict


class BusinessHours(SdkBaseModel):
    """The hours of operation for a location."""

    periods: Optional[list[BusinessHoursPeriod | None]] = UNSET
    """The list of time periods during which the business is open. There can be at most 10 periods per day."""


class BusinessHoursDict(TypedDict):
    periods: NotRequired[list[BusinessHoursPeriod | BusinessHoursPeriodDict | None]]
