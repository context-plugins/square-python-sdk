from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .oauth_authorization_revoked_event_revocation_object import (
    OauthAuthorizationRevokedEventRevocationObject,
    OauthAuthorizationRevokedEventRevocationObjectDict,
)


class OauthAuthorizationRevokedEventObject(SdkBaseModel):
    revocation: Optional[OauthAuthorizationRevokedEventRevocationObject] = UNSET


class OauthAuthorizationRevokedEventObjectDict(TypedDict):
    revocation: NotRequired[OauthAuthorizationRevokedEventRevocationObjectDict]
