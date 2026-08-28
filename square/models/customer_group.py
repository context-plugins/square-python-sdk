from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel


class CustomerGroup(SdkBaseModel):
    """Represents a group of customer profiles.

    Customer groups can be created, be modified, and have their membership defined using the Customers API or within the
    Customer Directory in the Square Seller Dashboard or Point of Sale."""

    id: Optional[str] = UNSET
    """A unique Square-generated ID for the customer group."""

    name: str
    """The name of the customer group."""

    created_at: Optional[str] = UNSET
    """The timestamp when the customer group was created, in RFC 3339 format."""

    updated_at: Optional[str] = UNSET
    """The timestamp when the customer group was last updated, in RFC 3339 format."""


class CustomerGroupDict(TypedDict):
    id: NotRequired[str]
    name: str
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
