from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel
from .oauth_authorization_revoked_event_object import (
    OauthAuthorizationRevokedEventObject,
    OauthAuthorizationRevokedEventObjectDict,
)


class OauthAuthorizationRevokedEventData(SdkBaseModel):
    type_: OptionalNullable[str] = Field(default=UNSET, alias="type")
    """Name of the affected object’s type, ``"revocation"``."""

    id: Optional[str] = UNSET
    """Not applicable, revocation is not an object"""

    object_: Optional[OauthAuthorizationRevokedEventObject] = Field(default=UNSET, alias="object")


class OauthAuthorizationRevokedEventDataDict(TypedDict):
    type_: NotRequired[str | None]
    id: NotRequired[str]
    object_: NotRequired[OauthAuthorizationRevokedEventObjectDict]
