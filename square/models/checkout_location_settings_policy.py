from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CheckoutLocationSettingsPolicy(SdkBaseModel):
    uid: OptionalNullable[str] = UNSET
    """A unique ID to identify the policy when making changes. You must set the UID for policy updates, but it’s
    optional when setting new policies."""

    title: OptionalNullable[str] = UNSET
    """The title of the policy. This is required when setting the description, though you can update it in a different
    request."""

    description: OptionalNullable[str] = UNSET
    """The description of the policy."""


class CheckoutLocationSettingsPolicyDict(TypedDict):
    uid: NotRequired[str | None]
    title: NotRequired[str | None]
    description: NotRequired[str | None]
