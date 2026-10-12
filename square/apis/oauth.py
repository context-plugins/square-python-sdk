from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.obtain_token_request import ObtainTokenRequest, ObtainTokenRequestDict
from ..models.obtain_token_response import ObtainTokenResponse
from ..models.retrieve_token_status_response import RetrieveTokenStatusResponse
from ..models.revoke_token_request import RevokeTokenRequest, RevokeTokenRequestDict
from ..models.revoke_token_response import RevokeTokenResponse
from ..server.server import Server


class Oauth:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OauthWithRawResponse(client, server, auth)

    def obtain_token(
        self, body: ObtainTokenRequest | ObtainTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ObtainTokenResponse:
        """Returns an OAuth access token and refresh token using the ``authorization_code`` or ``refresh_token`` grant
        type.

        When ``grant_type`` is ``authorization_code``:
        - With the `code flow <https://developer.squareup.com/docs/oauth-api/overview#code-flow>`__,
        provide ``code``, ``client_id``, and ``client_secret``.
        - With the `PKCE flow <https://developer.squareup.com/docs/oauth-api/overview#pkce-flow>`__,
        provide ``code``, ``client_id``, and ``code_verifier``.

        When ``grant_type`` is ``refresh_token``:
        - With the code flow, provide ``refresh_token``, ``client_id``, and ``client_secret``.
        The response returns the same refresh token provided in the request.
        - With the PKCE flow, provide ``refresh_token`` and ``client_id``. The response returns
        a new refresh token.

        You can use the ``scopes`` parameter to limit the set of permissions authorized by the access token. You can use
        the ``short_lived`` parameter to create an access token that expires in 24 hours.

        __Important:__ OAuth tokens should be encrypted and stored on a secure server. Application clients should never
        interact directly with OAuth tokens.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.obtain_token(body, request_options=request_options))

    def retrieve_token_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTokenStatusResponse:
        """Returns information about an `OAuth access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token>`__ or an
        application’s `personal access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token>`__.

        Add the access token to the Authorization header of the request.

        __Important:__ The ``Authorization`` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        where ``ACCESS_TOKEN`` is a `valid production authorization credential
        <https://developer.squareup.com/docs/build-basics/access-tokens>`__.

        If the access token is expired or not a valid access token, the endpoint returns an ``UNAUTHORIZED`` error.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_token_status(request_options=request_options))

    def revoke_token(
        self, body: RevokeTokenRequest | RevokeTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RevokeTokenResponse:
        """Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this endpoint revokes all of them,
        regardless of which token you specify.

        __Important:__ The ``Authorization`` header for this endpoint must have the following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace ``APPLICATION_SECRET`` with the application secret on the **OAuth** page for your application in the
        Developer Dashboard.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.revoke_token(body, request_options=request_options))

    @property
    def with_raw_response(self) -> OauthWithRawResponse:
        return self._with_raw_response


class AsyncOauth:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOauthWithRawResponse(client, server, auth)

    async def obtain_token(
        self, body: ObtainTokenRequest | ObtainTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ObtainTokenResponse:
        """Returns an OAuth access token and refresh token using the ``authorization_code`` or ``refresh_token`` grant
        type.

        When ``grant_type`` is ``authorization_code``:
        - With the `code flow <https://developer.squareup.com/docs/oauth-api/overview#code-flow>`__,
        provide ``code``, ``client_id``, and ``client_secret``.
        - With the `PKCE flow <https://developer.squareup.com/docs/oauth-api/overview#pkce-flow>`__,
        provide ``code``, ``client_id``, and ``code_verifier``.

        When ``grant_type`` is ``refresh_token``:
        - With the code flow, provide ``refresh_token``, ``client_id``, and ``client_secret``.
        The response returns the same refresh token provided in the request.
        - With the PKCE flow, provide ``refresh_token`` and ``client_id``. The response returns
        a new refresh token.

        You can use the ``scopes`` parameter to limit the set of permissions authorized by the access token. You can use
        the ``short_lived`` parameter to create an access token that expires in 24 hours.

        __Important:__ OAuth tokens should be encrypted and stored on a secure server. Application clients should never
        interact directly with OAuth tokens.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.obtain_token(body, request_options=request_options))

    async def retrieve_token_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTokenStatusResponse:
        """Returns information about an `OAuth access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token>`__ or an
        application’s `personal access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token>`__.

        Add the access token to the Authorization header of the request.

        __Important:__ The ``Authorization`` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        where ``ACCESS_TOKEN`` is a `valid production authorization credential
        <https://developer.squareup.com/docs/build-basics/access-tokens>`__.

        If the access token is expired or not a valid access token, the endpoint returns an ``UNAUTHORIZED`` error.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_token_status(request_options=request_options))

    async def revoke_token(
        self, body: RevokeTokenRequest | RevokeTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> RevokeTokenResponse:
        """Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this endpoint revokes all of them,
        regardless of which token you specify.

        __Important:__ The ``Authorization`` header for this endpoint must have the following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace ``APPLICATION_SECRET`` with the application secret on the **OAuth** page for your application in the
        Developer Dashboard.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.revoke_token(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncOauthWithRawResponse:
        return self._with_raw_response


class OauthWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def obtain_token(
        self, body: ObtainTokenRequest | ObtainTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ObtainTokenResponse, RawError]:
        """Returns an OAuth access token and refresh token using the ``authorization_code`` or ``refresh_token`` grant
        type.

        When ``grant_type`` is ``authorization_code``:
        - With the `code flow <https://developer.squareup.com/docs/oauth-api/overview#code-flow>`__,
        provide ``code``, ``client_id``, and ``client_secret``.
        - With the `PKCE flow <https://developer.squareup.com/docs/oauth-api/overview#pkce-flow>`__,
        provide ``code``, ``client_id``, and ``code_verifier``.

        When ``grant_type`` is ``refresh_token``:
        - With the code flow, provide ``refresh_token``, ``client_id``, and ``client_secret``.
        The response returns the same refresh token provided in the request.
        - With the PKCE flow, provide ``refresh_token`` and ``client_id``. The response returns
        a new refresh token.

        You can use the ``scopes`` parameter to limit the set of permissions authorized by the access token. You can use
        the ``short_lived`` parameter to create an access token that expires in 24 hours.

        __Important:__ OAuth tokens should be encrypted and stored on a secure server. Application clients should never
        interact directly with OAuth tokens.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth2/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ObtainTokenRequest | ObtainTokenRequestDict](body),
            decoder=json_decoder[ObtainTokenResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_token_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTokenStatusResponse, RawError]:
        """Returns information about an `OAuth access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token>`__ or an
        application’s `personal access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token>`__.

        Add the access token to the Authorization header of the request.

        __Important:__ The ``Authorization`` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        where ``ACCESS_TOKEN`` is a `valid production authorization credential
        <https://developer.squareup.com/docs/build-basics/access-tokens>`__.

        If the access token is expired or not a valid access token, the endpoint returns an ``UNAUTHORIZED`` error.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth2/token/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTokenStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def revoke_token(
        self, body: RevokeTokenRequest | RevokeTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevokeTokenResponse, RawError]:
        """Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this endpoint revokes all of them,
        regardless of which token you specify.

        __Important:__ The ``Authorization`` header for this endpoint must have the following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace ``APPLICATION_SECRET`` with the application secret on the **OAuth** page for your application in the
        Developer Dashboard.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth2/revoke"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RevokeTokenRequest | RevokeTokenRequestDict](body),
            decoder=json_decoder[RevokeTokenResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOauthWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def obtain_token(
        self, body: ObtainTokenRequest | ObtainTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ObtainTokenResponse, RawError]:
        """Returns an OAuth access token and refresh token using the ``authorization_code`` or ``refresh_token`` grant
        type.

        When ``grant_type`` is ``authorization_code``:
        - With the `code flow <https://developer.squareup.com/docs/oauth-api/overview#code-flow>`__,
        provide ``code``, ``client_id``, and ``client_secret``.
        - With the `PKCE flow <https://developer.squareup.com/docs/oauth-api/overview#pkce-flow>`__,
        provide ``code``, ``client_id``, and ``code_verifier``.

        When ``grant_type`` is ``refresh_token``:
        - With the code flow, provide ``refresh_token``, ``client_id``, and ``client_secret``.
        The response returns the same refresh token provided in the request.
        - With the PKCE flow, provide ``refresh_token`` and ``client_id``. The response returns
        a new refresh token.

        You can use the ``scopes`` parameter to limit the set of permissions authorized by the access token. You can use
        the ``short_lived`` parameter to create an access token that expires in 24 hours.

        __Important:__ OAuth tokens should be encrypted and stored on a secure server. Application clients should never
        interact directly with OAuth tokens.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth2/token"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ObtainTokenRequest | ObtainTokenRequestDict](body),
            decoder=async_json_decoder[ObtainTokenResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_token_status(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTokenStatusResponse, RawError]:
        """Returns information about an `OAuth access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token>`__ or an
        application’s `personal access token
        <https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token>`__.

        Add the access token to the Authorization header of the request.

        __Important:__ The ``Authorization`` header you provide to this endpoint must have the following format:

        ```
        Authorization: Bearer ACCESS_TOKEN
        ```

        where ``ACCESS_TOKEN`` is a `valid production authorization credential
        <https://developer.squareup.com/docs/build-basics/access-tokens>`__.

        If the access token is expired or not a valid access token, the endpoint returns an ``UNAUTHORIZED`` error.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth2/token/status"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveTokenStatusResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def revoke_token(
        self, body: RevokeTokenRequest | RevokeTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RevokeTokenResponse, RawError]:
        """Revokes an access token generated with the OAuth flow.

        If an account has more than one OAuth access token for your application, this endpoint revokes all of them,
        regardless of which token you specify.

        __Important:__ The ``Authorization`` header for this endpoint must have the following format:

        ```
        Authorization: Client APPLICATION_SECRET
        ```

        Replace ``APPLICATION_SECRET`` with the application secret on the **OAuth** page for your application in the
        Developer Dashboard.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/oauth2/revoke"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RevokeTokenRequest | RevokeTokenRequestDict](body),
            decoder=async_json_decoder[RevokeTokenResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
