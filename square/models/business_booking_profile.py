from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .business_appointment_settings import BusinessAppointmentSettings, BusinessAppointmentSettingsDict
from .enums.business_booking_profile_booking_policy import BusinessBookingProfileBookingPolicyOrStr
from .enums.business_booking_profile_customer_timezone_choice import BusinessBookingProfileCustomerTimezoneChoiceOrStr


class BusinessBookingProfile(SdkBaseModel):
    """A seller's business booking profile, including booking policy, appointment settings, etc."""

    seller_id: OptionalNullable[str] = UNSET
    """The ID of the seller, obtainable using the Merchants API."""

    created_at: Optional[str] = UNSET
    """The RFC 3339 timestamp specifying the booking's creation time."""

    booking_enabled: OptionalNullable[bool] = UNSET
    """Indicates whether the seller is open for booking."""

    customer_timezone_choice: Optional[BusinessBookingProfileCustomerTimezoneChoiceOrStr] = UNSET
    """Choices of customer-facing time zone used for bookings."""

    booking_policy: Optional[BusinessBookingProfileBookingPolicyOrStr] = UNSET
    """Policies for accepting bookings."""

    allow_user_cancel: OptionalNullable[bool] = UNSET
    """Indicates whether customers can cancel or reschedule their own bookings (``true``) or not (``false``)."""

    business_appointment_settings: Optional[BusinessAppointmentSettings] = UNSET
    """The service appointment settings, including where and how the service is provided."""

    support_seller_level_writes: OptionalNullable[bool] = UNSET
    """Indicates whether the seller's subscription to Square Appointments supports creating, updating or canceling an
    appointment through the API (``true``) or not (``false``) using seller permission."""


class BusinessBookingProfileDict(TypedDict):
    seller_id: NotRequired[str | None]
    created_at: NotRequired[str]
    booking_enabled: NotRequired[bool | None]
    customer_timezone_choice: NotRequired[BusinessBookingProfileCustomerTimezoneChoiceOrStr]
    booking_policy: NotRequired[BusinessBookingProfileBookingPolicyOrStr]
    allow_user_cancel: NotRequired[bool | None]
    business_appointment_settings: NotRequired[BusinessAppointmentSettings | BusinessAppointmentSettingsDict]
    support_seller_level_writes: NotRequired[bool | None]
