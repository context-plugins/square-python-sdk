from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.business_appointment_settings_alignment_time import BusinessAppointmentSettingsAlignmentTimeOrStr
from .enums.business_appointment_settings_booking_location_type import (
    BusinessAppointmentSettingsBookingLocationTypeOrStr,
)
from .enums.business_appointment_settings_cancellation_policy import BusinessAppointmentSettingsCancellationPolicyOrStr
from .enums.business_appointment_settings_max_appointments_per_day_limit_type import (
    BusinessAppointmentSettingsMaxAppointmentsPerDayLimitTypeOrStr,
)
from .money import Money, MoneyDict


class BusinessAppointmentSettings(SdkBaseModel):
    """The service appointment settings, including where and how the service is provided."""

    location_types: OptionalNullable[list[BusinessAppointmentSettingsBookingLocationTypeOrStr]] = UNSET
    """Types of the location allowed for bookings. See `BusinessAppointmentSettingsBookingLocationType
    <#type-businessappointmentsettingsbookinglocationtype>`__ for possible values"""

    alignment_time: Optional[BusinessAppointmentSettingsAlignmentTimeOrStr] = UNSET
    """Time units of a service duration for bookings."""

    min_booking_lead_time_seconds: OptionalNullable[int] = UNSET
    """The minimum lead time in seconds before a service can be booked. A booking must be created at least this amount
    of time before its starting time."""

    max_booking_lead_time_seconds: OptionalNullable[int] = UNSET
    """The maximum lead time in seconds before a service can be booked. A booking must be created at most this amount of
    time before its starting time."""

    any_team_member_booking_enabled: OptionalNullable[bool] = UNSET
    """Indicates whether a customer can choose from all available time slots and have a staff member assigned
    automatically (``true``) or not (``false``)."""

    multiple_service_booking_enabled: OptionalNullable[bool] = UNSET
    """Indicates whether a customer can book multiple services in a single online booking."""

    max_appointments_per_day_limit_type: Optional[
        BusinessAppointmentSettingsMaxAppointmentsPerDayLimitTypeOrStr
    ] = UNSET
    """Types of daily appointment limits."""

    max_appointments_per_day_limit: OptionalNullable[int] = UNSET
    """The maximum number of daily appointments per team member or per location."""

    cancellation_window_seconds: OptionalNullable[int] = UNSET
    """The cut-off time in seconds for allowing clients to cancel or reschedule an appointment."""

    cancellation_fee_money: Optional[Money] = UNSET
    """Represents an amount of money. ``Money`` fields can be signed or unsigned. Fields that do not explicitly define
    whether they are signed or unsigned are considered unsigned and can only hold positive amounts. For signed fields,
    the sign of the value indicates the purpose of the money transfer. See `Working with Monetary Amounts
    <https://developer.squareup.com/docs/build-basics/working-with-monetary-amounts>`__ for more information."""

    cancellation_policy: Optional[BusinessAppointmentSettingsCancellationPolicyOrStr] = UNSET
    """The category of the seller’s cancellation policy."""

    cancellation_policy_text: OptionalNullable[str] = UNSET
    """The free-form text of the seller's cancellation policy."""

    skip_booking_flow_staff_selection: OptionalNullable[bool] = UNSET
    """Indicates whether customers has an assigned staff member (``true``) or can select s staff member of their choice
    (``false``)."""


class BusinessAppointmentSettingsDict(TypedDict):
    location_types: NotRequired[list[BusinessAppointmentSettingsBookingLocationTypeOrStr] | None]
    alignment_time: NotRequired[BusinessAppointmentSettingsAlignmentTimeOrStr]
    min_booking_lead_time_seconds: NotRequired[int | None]
    max_booking_lead_time_seconds: NotRequired[int | None]
    any_team_member_booking_enabled: NotRequired[bool | None]
    multiple_service_booking_enabled: NotRequired[bool | None]
    max_appointments_per_day_limit_type: NotRequired[BusinessAppointmentSettingsMaxAppointmentsPerDayLimitTypeOrStr]
    max_appointments_per_day_limit: NotRequired[int | None]
    cancellation_window_seconds: NotRequired[int | None]
    cancellation_fee_money: NotRequired[MoneyDict]
    cancellation_policy: NotRequired[BusinessAppointmentSettingsCancellationPolicyOrStr]
    cancellation_policy_text: NotRequired[str | None]
    skip_booking_flow_staff_selection: NotRequired[bool | None]
