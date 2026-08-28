from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class OrderSource(SdkBaseModel):
    """Represents the origination details of an order."""

    name: OptionalNullable[str] = UNSET
    """The name used to identify the place (physical or digital) that an order originates. If unset, the name defaults
    to the name of the application that created the order."""


class OrderSourceDict(TypedDict):
    name: NotRequired[str | None]
