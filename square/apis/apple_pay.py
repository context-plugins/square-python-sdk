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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.register_domain_request import RegisterDomainRequest, RegisterDomainRequestDict
from ..models.register_domain_response import RegisterDomainResponse
from ..server.server import Server


class ApplePay:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApplePayWithRawResponse(client, server, auth)

    def register_domain(
        self,
        body: RegisterDomainRequest | RegisterDomainRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterDomainResponse:
        """Activates a domain for use with Apple Pay on the Web and Square. A validation is performed on this domain by
        Apple to ensure that it is properly set up as an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate Apple Pay on the Web with Square for
        merchants using their platform.

        Note: You will need to host a valid domain verification file on your domain to support Apple Pay. The current
        version of this file is always available at
        https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association, and should be
        hosted at ``.well_known/apple-developer-merchantid-domain-association`` on your domain. This file is subject to
        change; we strongly recommend checking for updates regularly and avoiding long-lived caches that might not keep
        in sync with the correct file version.

        To learn more about the Web Payments SDK and how to add Apple Pay, see `Take an Apple Pay Payment
        <https://developer.squareup.com/docs/web-payments/apple-pay>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.register_domain(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ApplePayWithRawResponse:
        return self._with_raw_response


class AsyncApplePay:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApplePayWithRawResponse(client, server, auth)

    async def register_domain(
        self,
        body: RegisterDomainRequest | RegisterDomainRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterDomainResponse:
        """Activates a domain for use with Apple Pay on the Web and Square. A validation is performed on this domain by
        Apple to ensure that it is properly set up as an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate Apple Pay on the Web with Square for
        merchants using their platform.

        Note: You will need to host a valid domain verification file on your domain to support Apple Pay. The current
        version of this file is always available at
        https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association, and should be
        hosted at ``.well_known/apple-developer-merchantid-domain-association`` on your domain. This file is subject to
        change; we strongly recommend checking for updates regularly and avoiding long-lived caches that might not keep
        in sync with the correct file version.

        To learn more about the Web Payments SDK and how to add Apple Pay, see `Take an Apple Pay Payment
        <https://developer.squareup.com/docs/web-payments/apple-pay>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.register_domain(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncApplePayWithRawResponse:
        return self._with_raw_response


class ApplePayWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def register_domain(
        self,
        body: RegisterDomainRequest | RegisterDomainRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterDomainResponse, RawError]:
        """Activates a domain for use with Apple Pay on the Web and Square. A validation is performed on this domain by
        Apple to ensure that it is properly set up as an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate Apple Pay on the Web with Square for
        merchants using their platform.

        Note: You will need to host a valid domain verification file on your domain to support Apple Pay. The current
        version of this file is always available at
        https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association, and should be
        hosted at ``.well_known/apple-developer-merchantid-domain-association`` on your domain. This file is subject to
        change; we strongly recommend checking for updates regularly and avoiding long-lived caches that might not keep
        in sync with the correct file version.

        To learn more about the Web Payments SDK and how to add Apple Pay, see `Take an Apple Pay Payment
        <https://developer.squareup.com/docs/web-payments/apple-pay>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/apple-pay/domains"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterDomainRequest | RegisterDomainRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RegisterDomainResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncApplePayWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def register_domain(
        self,
        body: RegisterDomainRequest | RegisterDomainRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterDomainResponse, RawError]:
        """Activates a domain for use with Apple Pay on the Web and Square. A validation is performed on this domain by
        Apple to ensure that it is properly set up as an Apple Pay enabled domain.

        This endpoint provides an easy way for platform developers to bulk activate Apple Pay on the Web with Square for
        merchants using their platform.

        Note: You will need to host a valid domain verification file on your domain to support Apple Pay. The current
        version of this file is always available at
        https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association, and should be
        hosted at ``.well_known/apple-developer-merchantid-domain-association`` on your domain. This file is subject to
        change; we strongly recommend checking for updates regularly and avoiding long-lived caches that might not keep
        in sync with the correct file version.

        To learn more about the Web Payments SDK and how to add Apple Pay, see `Take an Apple Pay Payment
        <https://developer.squareup.com/docs/web-payments/apple-pay>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/apple-pay/domains"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterDomainRequest | RegisterDomainRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RegisterDomainResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
