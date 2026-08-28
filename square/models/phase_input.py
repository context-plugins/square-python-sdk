from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class PhaseInput(SdkBaseModel):
    """Represents the arguments used to construct a new phase."""

    ordinal: int
    """index of phase in total subscription plan"""

    order_template_id: OptionalNullable[str] = UNSET
    """id of order to be used in billing"""


class PhaseInputDict(TypedDict):
    ordinal: int
    order_template_id: NotRequired[str | None]
