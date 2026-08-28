from __future__ import annotations

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
from ..models.delete_snippet_response import DeleteSnippetResponse
from ..models.retrieve_snippet_response import RetrieveSnippetResponse
from ..models.upsert_snippet_request import UpsertSnippetRequest, UpsertSnippetRequestDict
from ..models.upsert_snippet_response import UpsertSnippetResponse
from ..server.server import Server


class Snippets:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SnippetsWithRawResponse(client, server, auth)

    def delete_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteSnippetResponse:
        """Removes your snippet from a Square Online site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_snippet(site_id, request_options=request_options).unwrap()

    def retrieve_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveSnippetResponse:
        """Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet
        applications, but you can retrieve only the snippet that was added by your application.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_snippet(site_id, request_options=request_options).unwrap()

    def upsert_snippet(
        self,
        site_id: str,
        body: UpsertSnippetRequest | UpsertSnippetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertSnippetResponse:
        """Adds a snippet to a Square Online site or updates the existing snippet on the site. The snippet code is
        appended to the end of the ``head`` element on every page of the site, except checkout pages. A snippet
        application can add one snippet to a given site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site where you want to add or update the snippet.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.upsert_snippet(site_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> SnippetsWithRawResponse:
        return self._with_raw_response


class AsyncSnippets:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSnippetsWithRawResponse(client, server, auth)

    async def delete_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteSnippetResponse:
        """Removes your snippet from a Square Online site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_snippet(site_id, request_options=request_options)).unwrap()

    async def retrieve_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveSnippetResponse:
        """Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet
        applications, but you can retrieve only the snippet that was added by your application.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_snippet(site_id, request_options=request_options)).unwrap()

    async def upsert_snippet(
        self,
        site_id: str,
        body: UpsertSnippetRequest | UpsertSnippetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpsertSnippetResponse:
        """Adds a snippet to a Square Online site or updates the existing snippet on the site. The snippet code is
        appended to the end of the ``head`` element on every page of the site, except checkout pages. A snippet
        application can add one snippet to a given site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site where you want to add or update the snippet.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.upsert_snippet(site_id, body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncSnippetsWithRawResponse:
        return self._with_raw_response


class SnippetsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteSnippetResponse, RawError]:
        """Removes your snippet from a Square Online site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/sites/{site_id}/snippet"),
            path_params=[param[str]("site_id", site_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteSnippetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveSnippetResponse, RawError]:
        """Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet
        applications, but you can retrieve only the snippet that was added by your application.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sites/{site_id}/snippet"),
            path_params=[param[str]("site_id", site_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveSnippetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def upsert_snippet(
        self,
        site_id: str,
        body: UpsertSnippetRequest | UpsertSnippetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertSnippetResponse, RawError]:
        """Adds a snippet to a Square Online site or updates the existing snippet on the site. The snippet code is
        appended to the end of the ``head`` element on every page of the site, except checkout pages. A snippet
        application can add one snippet to a given site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site where you want to add or update the snippet.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/sites/{site_id}/snippet"),
            path_params=[param[str]("site_id", site_id)],
            body=json_body[UpsertSnippetRequest | UpsertSnippetRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertSnippetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSnippetsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteSnippetResponse, RawError]:
        """Removes your snippet from a Square Online site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/sites/{site_id}/snippet"),
            path_params=[param[str]("site_id", site_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteSnippetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_snippet(
        self, site_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveSnippetResponse, RawError]:
        """Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet
        applications, but you can retrieve only the snippet that was added by your application.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site that contains the snippet.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/sites/{site_id}/snippet"),
            path_params=[param[str]("site_id", site_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveSnippetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def upsert_snippet(
        self,
        site_id: str,
        body: UpsertSnippetRequest | UpsertSnippetRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpsertSnippetResponse, RawError]:
        """Adds a snippet to a Square Online site or updates the existing snippet on the site. The snippet code is
        appended to the end of the ``head`` element on every page of the site, except checkout pages. A snippet
        application can add one snippet to a given site.

        You can call `ListSites <api-endpoint:Sites-ListSites>`__ to get the IDs of the sites that belong to a seller.


        __Note:__ Square Online APIs are publicly available as part of an early access program. For more information,
        see `Early access program for Square Online APIs
        <https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis>`__.

        Args:
            site_id: The ID of the site where you want to add or update the snippet.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/sites/{site_id}/snippet"),
            path_params=[param[str]("site_id", site_id)],
            body=json_body[UpsertSnippetRequest | UpsertSnippetRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpsertSnippetResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
