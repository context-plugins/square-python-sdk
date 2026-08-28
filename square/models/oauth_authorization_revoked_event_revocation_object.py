from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .enums.oauth_authorization_revoked_event_revoker_type import OauthAuthorizationRevokedEventRevokerTypeOrStr


class OauthAuthorizationRevokedEventRevocationObject(SdkBaseModel):
    revoked_at: OptionalNullable[str] = UNSET
    """Timestamp of when the revocation event occurred, in RFC 3339 format."""

    revoker_type: Optional[OauthAuthorizationRevokedEventRevokerTypeOrStr] = UNSET
    """Defines the possible types for the revoking client."""


class OauthAuthorizationRevokedEventRevocationObjectDict(TypedDict):
    revoked_at: NotRequired[str | None]
    revoker_type: NotRequired[OauthAuthorizationRevokedEventRevokerTypeOrStr]
