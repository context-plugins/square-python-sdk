from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, OptionalNullable, SdkBaseModel


class RevokeTokenRequest(SdkBaseModel):
    client_id: OptionalNullable[str] = UNSET
    """The Square-issued ID for your application, which is available on the **OAuth** page in the `Developer Dashboard
    <https://developer.squareup.com/apps>`__."""

    access_token: OptionalNullable[str] = UNSET
    """The access token of the merchant whose token you want to revoke. Do not provide a value for ``merchant_id`` if
    you provide this parameter."""

    merchant_id: OptionalNullable[str] = UNSET
    """The ID of the merchant whose token you want to revoke. Do not provide a value for ``access_token`` if you provide
    this parameter."""

    revoke_only_access_token: OptionalNullable[bool] = UNSET
    """If ``true``, terminate the given single access token, but do not terminate the entire authorization. Default:
    ``false``"""


class RevokeTokenRequestDict(TypedDict):
    client_id: NotRequired[str | None]
    access_token: NotRequired[str | None]
    merchant_id: NotRequired[str | None]
    revoke_only_access_token: NotRequired[bool | None]
