from __future__ import annotations

from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, OptionalNullable, SdkBaseModel


class ObtainTokenRequest(SdkBaseModel):
    """Represents an `ObtainToken <api-endpoint:OAuth-ObtainToken>`__ request."""

    client_id: str
    """The Square-issued ID of your application, which is available as the **Application ID** on the **OAuth** page in
    the `Developer Console <https://developer.squareup.com/apps>`__.

    Required for the code flow and PKCE flow for any grant type."""

    client_secret: OptionalNullable[str] = UNSET
    """The secret key for your application, which is available as the **Application secret** on the **OAuth** page in
    the `Developer Console <https://developer.squareup.com/apps>`__.

    Required for the code flow for any grant type. Don't confuse your client secret with your personal access token."""

    code: OptionalNullable[str] = UNSET
    """The authorization code to exchange for an OAuth access token. This is the ``code`` value that Square sent to your
    redirect URL in the authorization response.

    Required for the code flow and PKCE flow if ``grant_type`` is ``authorization_code``."""

    redirect_uri: OptionalNullable[str] = UNSET
    """The redirect URL for your application, which you registered as the **Redirect URL** on the **OAuth** page in the
    `Developer Console <https://developer.squareup.com/apps>`__.

    Required for the code flow and PKCE flow if ``grant_type`` is ``authorization_code`` and you provided the
    ``redirect_uri`` parameter in your authorization URL."""

    grant_type: str
    """The method used to obtain an OAuth access token. The request must include the credential that corresponds to the
    specified grant type. Valid values are:
    - ``authorization_code`` - Requires the ``code`` field.
    - ``refresh_token`` - Requires the ``refresh_token`` field.
    - ``migration_token`` - LEGACY for access tokens obtained using a Square API version prior
    to 2019-03-13. Requires the ``migration_token`` field."""

    refresh_token: OptionalNullable[str] = UNSET
    """A valid refresh token used to generate a new OAuth access token. This is a refresh token that was returned in a
    previous ``ObtainToken`` response.

    Required for the code flow and PKCE flow if ``grant_type`` is ``refresh_token``."""

    migration_token: OptionalNullable[str] = UNSET
    """__LEGACY__ A valid access token (obtained using a Square API version prior to 2019-03-13) used to generate a new
    OAuth access token.

    Required if ``grant_type`` is ``migration_token``. For more information, see `Migrate to Using Refresh Tokens
    <https://developer.squareup.com/docs/oauth-api/migrate-to-refresh-tokens>`__."""

    scopes: Optional[list[str | None]] = UNSET
    """The list of permissions that are explicitly requested for the access token. For example,
    ["MERCHANT_PROFILE_READ","PAYMENTS_READ","BANK_ACCOUNTS_READ"].

    The returned access token is limited to the permissions that are the intersection of these requested permissions and
    those authorized by the provided ``refresh_token``.

    Optional for the code flow and PKCE flow if ``grant_type`` is ``refresh_token``."""

    short_lived: OptionalNullable[bool] = UNSET
    """Indicates whether the returned access token should expire in 24 hours.

    Optional for the code flow and PKCE flow for any grant type. The default value is ``false``."""

    code_verifier: OptionalNullable[str] = UNSET
    """The secret your application generated for the authorization request used to obtain the authorization code. This
    is the source of the ``code_challenge`` hash you provided in your authorization URL.

    Required for the PKCE flow if ``grant_type`` is ``authorization_code``."""

    use_jwt: OptionalNullable[bool] = UNSET
    """Indicates whether to use a JWT (JSON Web Token) as the OAuth access token. When set to ``true``, the OAuth flow
    returns a JWT to your application, used in the same way as a regular token. The default value is ``false``."""


class ObtainTokenRequestDict(TypedDict):
    client_id: str
    client_secret: NotRequired[str | None]
    code: NotRequired[str | None]
    redirect_uri: NotRequired[str | None]
    grant_type: str
    refresh_token: NotRequired[str | None]
    migration_token: NotRequired[str | None]
    scopes: NotRequired[list[str | None]]
    short_lived: NotRequired[bool | None]
    code_verifier: NotRequired[str | None]
    use_jwt: NotRequired[bool | None]
