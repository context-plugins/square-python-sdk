from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class SubscriptionSource(SdkBaseModel):
    """The origination details of the subscription."""

    name: OptionalNullable[str] = UNSET
    """The name used to identify the place (physical or digital) that a subscription originates. If unset, the name
    defaults to the name of the application that created the subscription."""


class SubscriptionSourceDict(TypedDict):
    name: NotRequired[str | None]
