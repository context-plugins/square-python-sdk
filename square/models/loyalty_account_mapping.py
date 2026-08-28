from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class LoyaltyAccountMapping(SdkBaseModel):
    """Represents the mapping that associates a loyalty account with a buyer.

    Currently, a loyalty account can only be mapped to a buyer by phone number. For more information, see `Loyalty
    Overview <https://developer.squareup.com/docs/loyalty/overview>`__."""

    id: Optional[str] = UNSET
    """The Square-assigned ID of the mapping."""

    created_at: Optional[str] = UNSET
    """The timestamp when the mapping was created, in RFC 3339 format."""

    phone_number: OptionalNullable[str] = UNSET
    """The phone number of the buyer, in E.164 format. For example, "+14155551111"."""


class LoyaltyAccountMappingDict(TypedDict):
    id: NotRequired[str]
    created_at: NotRequired[str]
    phone_number: NotRequired[str | None]
