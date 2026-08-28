from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .oauth_authorization_revoked_event_data import (
    OauthAuthorizationRevokedEventData,
    OauthAuthorizationRevokedEventDataDict,
)


class OauthAuthorizationRevokedEvent(SdkBaseModel):
    """Published when a merchant/application revokes all access tokens and refresh tokens granted to an application."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the target merchant associated with the event."""

    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """The type of event this represents, ``"oauth.authorization.revoked"``."""

    event_id: OptionalNullable[str] = UNSET
    """A unique ID for the event."""

    created_at: Optional[str] = UNSET
    """Timestamp of when the event was created, in RFC 3339 format."""

    data: Optional[OauthAuthorizationRevokedEventData] = UNSET


class OauthAuthorizationRevokedEventDict(TypedDict):
    merchant_id: NotRequired[str | None]
    type_: NotRequired[str | None]
    event_id: NotRequired[str | None]
    created_at: NotRequired[str]
    data: NotRequired[OauthAuthorizationRevokedEventData | OauthAuthorizationRevokedEventDataDict]
