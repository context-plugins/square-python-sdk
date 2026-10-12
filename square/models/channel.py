from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.channel_status import ChannelStatusOrStr
from .reference import Reference, ReferenceDict


class Channel(SdkBaseModel):
    id: Optional[str] = UNSET
    """The channel's unique ID."""

    merchant_id: Optional[str] = UNSET
    """The unique ID of the merchant this channel belongs to."""

    name: OptionalNullable[str] = UNSET
    """The name of the channel."""

    version: Optional[int] = UNSET
    """The version number which is incremented each time an update is made to the channel."""

    reference: Optional[Reference] = UNSET
    status: Optional[ChannelStatusOrStr] = UNSET
    created_at: Optional[str] = UNSET
    """The timestamp for when the channel was created, in RFC 3339 format (for example, "2016-09-04T23:59:33.123Z"). For
    more information, see `Working with Dates
    <https://developer.squareup.com/docs/build-basics/working-with-dates>`__."""

    updated_at: Optional[str] = UNSET
    """The timestamp for when the channel was last updated, in RFC 3339 format (for example,
    "2016-09-04T23:59:33.123Z"). For more information, see `Working with Dates
    <https://developer.squareup.com/docs/build-basics/working-with-dates>`__."""


class ChannelDict(TypedDict):
    id: NotRequired[str]
    merchant_id: NotRequired[str]
    name: NotRequired[str | None]
    version: NotRequired[int]
    reference: NotRequired[ReferenceDict]
    status: NotRequired[ChannelStatusOrStr]
    created_at: NotRequired[str]
    updated_at: NotRequired[str]
