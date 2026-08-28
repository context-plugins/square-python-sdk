from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class Phase(SdkBaseModel):
    """Represents a phase, which can override subscription phases as defined by plan_id"""

    uid: OptionalNullable[str] = UNSET
    """id of subscription phase"""

    ordinal: OptionalNullable[int] = UNSET
    """index of phase in total subscription plan"""

    order_template_id: OptionalNullable[str] = UNSET
    """id of order to be used in billing"""

    plan_phase_uid: OptionalNullable[str] = UNSET
    """the uid from the plan's phase in catalog"""


class PhaseDict(TypedDict):
    uid: NotRequired[str | None]
    ordinal: NotRequired[int | None]
    order_template_id: NotRequired[str | None]
    plan_phase_uid: NotRequired[str | None]
