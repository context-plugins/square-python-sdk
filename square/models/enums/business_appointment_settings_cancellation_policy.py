from enum import Enum
from typing import Annotated, TypeAlias

from ...core import open_enum_validator


class BusinessAppointmentSettingsCancellationPolicy(str, Enum):
    """The category of the seller’s cancellation policy."""

    CANCELLATION_TREATED_AS_NO_SHOW = "CANCELLATION_TREATED_AS_NO_SHOW"
    """Cancellations are treated as no shows and may incur a fee as specified by ``cancellation_fee_money``."""

    CUSTOM_POLICY = "CUSTOM_POLICY"
    """Cancellations follow the seller-specified policy that is described in free-form text and not enforced
    automatically by Square."""

    __str__ = str.__str__


BusinessAppointmentSettingsCancellationPolicyOrStr: TypeAlias = Annotated[
    BusinessAppointmentSettingsCancellationPolicy | str,
    open_enum_validator(BusinessAppointmentSettingsCancellationPolicy),
]
