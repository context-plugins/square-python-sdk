from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class CustomerPreferences(SdkBaseModel):
    """Represents communication preferences for the customer profile."""

    email_unsubscribed: OptionalNullable[bool] = UNSET
    """Indicates whether the customer has unsubscribed from marketing campaign emails. A value of ``true`` means that
    the customer chose to opt out of email marketing from the current Square seller or from all Square sellers. This
    value is read-only from the Customers API."""


class CustomerPreferencesDict(TypedDict):
    email_unsubscribed: NotRequired[bool | None]
