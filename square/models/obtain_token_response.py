from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .error import Error, ErrorDict


class ObtainTokenResponse(SdkBaseModel):
    """Represents an `ObtainToken <api-endpoint:OAuth-ObtainToken>`__ response."""

    access_token: Optional[str] = UNSET
    """An OAuth access token used to authorize Square API requests on behalf of the seller. Include this token as a
    bearer token in the ``Authorization`` header of your API requests.

    OAuth access tokens expire in 30 days (except ``short_lived`` access tokens). You should call ``ObtainToken`` and
    provide the returned ``refresh_token`` to get a new access token well before the current one expires. For more
    information, see `OAuth API: Walkthrough <https://developer.squareup.com/docs/oauth-api/walkthrough>`__."""

    token_type: Optional[str] = UNSET
    """The type of access token. This value is always ``bearer``."""

    expires_at: Optional[str] = UNSET
    """The timestamp of when the ``access_token`` expires, in `ISO 8601
    <http://www.iso.org/iso/home/standards/iso8601.htm>`__ format."""

    merchant_id: Optional[str] = UNSET
    """The ID of the authorizing `merchant <entity:Merchant>`__ (seller), which represents a business."""

    subscription_id: Optional[str] = UNSET
    """__LEGACY__ The ID of merchant's subscription. The ID is only present if the merchant signed up for a subscription
    plan during authorization."""

    plan_id: Optional[str] = UNSET
    """__LEGACY__ The ID of the subscription plan the merchant signed up for. The ID is only present if the merchant
    signed up for a subscription plan during authorization."""

    id_token: Optional[str] = UNSET
    """The OpenID token that belongs to this person. This token is only present if the ``OPENID`` scope is included in
    the authorization request.

    Deprecated at version 2021-09-15. Square doesn't support OpenID or other single sign-on (SSO) protocols on top of
    OAuth."""

    refresh_token: Optional[str] = UNSET
    """A refresh token that can be used in an ``ObtainToken`` request to generate a new access token.

    With the code flow:
    - For the ``authorization_code`` grant type, the refresh token is multi-use and never expires.
    - For the ``refresh_token`` grant type, the response returns the same refresh token.

    With the PKCE flow:
    - For the ``authorization_code`` grant type, the refresh token is single-use and expires in 90 days.
    - For the ``refresh_token`` grant type, the refresh token is a new single-use refresh token that expires in 90 days.

    For more information, see `Refresh, Revoke, and Limit the Scope of OAuth Tokens
    <https://developer.squareup.com/docs/oauth-api/refresh-revoke-limit-scope>`__."""

    short_lived: Optional[bool] = UNSET
    """Indicates whether the access_token is short lived. If ``true``, the access token expires in 24 hours. If
    ``false``, the access token expires in 30 days."""

    errors: Optional[list[Error]] = UNSET
    """Any errors that occurred during the request."""

    refresh_token_expires_at: Optional[str] = UNSET
    """The timestamp of when the ``refresh_token`` expires, in `ISO 8601
    <http://www.iso.org/iso/home/standards/iso8601.htm>`__ format.

    This field is only returned for the PKCE flow."""


class ObtainTokenResponseDict(TypedDict):
    access_token: NotRequired[str]
    token_type: NotRequired[str]
    expires_at: NotRequired[str]
    merchant_id: NotRequired[str]
    subscription_id: NotRequired[str]
    plan_id: NotRequired[str]
    id_token: NotRequired[str]
    refresh_token: NotRequired[str]
    short_lived: NotRequired[bool]
    errors: NotRequired[list[ErrorDict]]
    refresh_token_expires_at: NotRequired[str]
