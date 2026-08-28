from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    raw_error_response,
)
from ..models.list_sites_response import ListSitesResponse
from ..server.server import Server


class Sites:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SitesWithRawResponse(client, server, auth)

    def list_sites(self, *, request_options: RequestOptionsOrDict | None = None) -> ListSitesResponse:
        """Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the
        ``created_at`` date.

        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_sites(request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SitesWithRawResponse:
        return self._with_raw_response


class AsyncSites:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSitesWithRawResponse(client, server, auth)

    async def list_sites(self, *, request_options: RequestOptionsOrDict | None = None) -> ListSitesResponse:
        """Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the
        ``created_at`` date.

        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_sites(request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSitesWithRawResponse:
        return self._with_raw_response


class SitesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_sites(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListSitesResponse, RawError]:
        """Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the
        ``created_at`` date.

        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sites"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListSitesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSitesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_sites(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListSitesResponse, RawError]:
        """Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the
        ``created_at`` date.

        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sites"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListSitesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
