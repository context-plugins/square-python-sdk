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
from ..models.bulk_retrieve_channels_request import BulkRetrieveChannelsRequest, BulkRetrieveChannelsRequestDict
from ..models.bulk_retrieve_channels_response import BulkRetrieveChannelsResponse
from ..models.enums.channel_status import ChannelStatusOrStr
from ..models.enums.reference_type import ReferenceTypeOrStr
from ..models.list_channels_response import ListChannelsResponse
from ..models.retrieve_channel_response import RetrieveChannelResponse
from ..server.server import Server


class Channels:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ChannelsWithRawResponse(client, server, auth)

    def bulk_retrieve_channels(
        self,
        body: BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveChannelsResponse:
        """Send a ``POST`` request.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.bulk_retrieve_channels(body, request_options=request_options))

    def list_channels(
        self,
        *,
        reference_type: ReferenceTypeOrStr | None = None,
        reference_id: str | None = None,
        status: ChannelStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelsResponse:
        """Send a ``GET`` request.

        Args:
            reference_type: Type of reference associated to channel
            reference_id: id of reference associated to channel
            status: Status of channel
            cursor: Cursor to fetch the next result
            limit: Maximum number of results to return. When not provided the returned results will be cap at 100
                channels.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_channels(
                reference_type=reference_type,
                reference_id=reference_id,
                status=status,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            ),
        )

    def retrieve_channel(
        self, channel_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveChannelResponse:
        """Send a ``GET`` request.

        Args:
            channel_id: A channel id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_channel(channel_id, request_options=request_options))

    @property
    def with_raw_response(self) -> ChannelsWithRawResponse:
        return self._with_raw_response


class AsyncChannels:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncChannelsWithRawResponse(client, server, auth)

    async def bulk_retrieve_channels(
        self,
        body: BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveChannelsResponse:
        """Send a ``POST`` request.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.bulk_retrieve_channels(body, request_options=request_options))

    async def list_channels(
        self,
        *,
        reference_type: ReferenceTypeOrStr | None = None,
        reference_id: str | None = None,
        status: ChannelStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListChannelsResponse:
        """Send a ``GET`` request.

        Args:
            reference_type: Type of reference associated to channel
            reference_id: id of reference associated to channel
            status: Status of channel
            cursor: Cursor to fetch the next result
            limit: Maximum number of results to return. When not provided the returned results will be cap at 100
                channels.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_channels(
                reference_type=reference_type,
                reference_id=reference_id,
                status=status,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            ),
        )

    async def retrieve_channel(
        self, channel_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveChannelResponse:
        """Send a ``GET`` request.

        Args:
            channel_id: A channel id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_channel(channel_id, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncChannelsWithRawResponse:
        return self._with_raw_response


class ChannelsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_retrieve_channels(
        self,
        body: BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveChannelsResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/channels/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveChannelsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_channels(
        self,
        *,
        reference_type: ReferenceTypeOrStr | None = None,
        reference_id: str | None = None,
        status: ChannelStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            reference_type: Type of reference associated to channel
            reference_id: id of reference associated to channel
            status: Status of channel
            cursor: Cursor to fetch the next result
            limit: Maximum number of results to return. When not provided the returned results will be cap at 100
                channels.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/channels"),
            query_params=[
                param[ReferenceTypeOrStr | None]("reference_type", reference_type),
                param[str | None]("reference_id", reference_id),
                param[ChannelStatusOrStr | None]("status", status),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListChannelsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_channel(
        self, channel_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveChannelResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            channel_id: A channel id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/channels/{channel_id}"),
            path_params=[param[str]("channel_id", channel_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncChannelsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_retrieve_channels(
        self,
        body: BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveChannelsResponse, RawError]:
        """Send a ``POST`` request.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/channels/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BulkRetrieveChannelsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_channels(
        self,
        *,
        reference_type: ReferenceTypeOrStr | None = None,
        reference_id: str | None = None,
        status: ChannelStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListChannelsResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            reference_type: Type of reference associated to channel
            reference_id: id of reference associated to channel
            status: Status of channel
            cursor: Cursor to fetch the next result
            limit: Maximum number of results to return. When not provided the returned results will be cap at 100
                channels.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/channels"),
            query_params=[
                param[ReferenceTypeOrStr | None]("reference_type", reference_type),
                param[str | None]("reference_id", reference_id),
                param[ChannelStatusOrStr | None]("status", status),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListChannelsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_channel(
        self, channel_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveChannelResponse, RawError]:
        """Send a ``GET`` request.

        Args:
            channel_id: A channel id
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/channels/{channel_id}"),
            path_params=[param[str]("channel_id", channel_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveChannelResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
