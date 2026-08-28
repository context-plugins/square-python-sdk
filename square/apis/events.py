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
from ..models.disable_events_response import DisableEventsResponse
from ..models.enable_events_response import EnableEventsResponse
from ..models.list_event_types_response import ListEventTypesResponse
from ..models.search_events_request import SearchEventsRequest, SearchEventsRequestDict
from ..models.search_events_response import SearchEventsResponse
from ..server.server import Server


class Events:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = EventsWithRawResponse(client, server, auth)

    def disable_events(self, *, request_options: RequestOptionsOrDict | None = None) -> DisableEventsResponse:
        """Disables events to prevent them from being searchable. All events are disabled by default. You must enable
        events to make them searchable. Disabling events for a specific time period prevents them from being searchable,
        even if you re-enable them later.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.disable_events(request_options=request_options).unwrap()

    def enable_events(self, *, request_options: RequestOptionsOrDict | None = None) -> EnableEventsResponse:
        """Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.enable_events(request_options=request_options).unwrap()

    def list_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListEventTypesResponse:
        """Lists all event types that you can subscribe to as webhooks or query using the Events API.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_event_types(
            api_version=api_version, request_options=request_options
        ).unwrap()

    def search_events(
        self,
        body: SearchEventsRequest | SearchEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchEventsResponse:
        """Search for Square API events that occur within a 28-day timeframe.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_events(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> EventsWithRawResponse:
        return self._with_raw_response


class AsyncEvents:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncEventsWithRawResponse(client, server, auth)

    async def disable_events(self, *, request_options: RequestOptionsOrDict | None = None) -> DisableEventsResponse:
        """Disables events to prevent them from being searchable. All events are disabled by default. You must enable
        events to make them searchable. Disabling events for a specific time period prevents them from being searchable,
        even if you re-enable them later.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.disable_events(request_options=request_options)).unwrap()

    async def enable_events(self, *, request_options: RequestOptionsOrDict | None = None) -> EnableEventsResponse:
        """Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.enable_events(request_options=request_options)).unwrap()

    async def list_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListEventTypesResponse:
        """Lists all event types that you can subscribe to as webhooks or query using the Events API.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_event_types(api_version=api_version, request_options=request_options)
        ).unwrap()

    async def search_events(
        self,
        body: SearchEventsRequest | SearchEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchEventsResponse:
        """Search for Square API events that occur within a 28-day timeframe.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_events(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncEventsWithRawResponse:
        return self._with_raw_response


class EventsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def disable_events(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisableEventsResponse, RawError]:
        """Disables events to prevent them from being searchable. All events are disabled by default. You must enable
        events to make them searchable. Disabling events for a specific time period prevents them from being searchable,
        even if you re-enable them later.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/events/disable"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DisableEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def enable_events(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EnableEventsResponse, RawError]:
        """Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/events/enable"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[EnableEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListEventTypesResponse, RawError]:
        """Lists all event types that you can subscribe to as webhooks or query using the Events API.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/events/types"),
            query_params=[param[str | None]("api_version", api_version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListEventTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_events(
        self,
        body: SearchEventsRequest | SearchEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchEventsResponse, RawError]:
        """Search for Square API events that occur within a 28-day timeframe.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/events"),
            body=json_body[SearchEventsRequest | SearchEventsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncEventsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def disable_events(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisableEventsResponse, RawError]:
        """Disables events to prevent them from being searchable. All events are disabled by default. You must enable
        events to make them searchable. Disabling events for a specific time period prevents them from being searchable,
        even if you re-enable them later.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/events/disable"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DisableEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def enable_events(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[EnableEventsResponse, RawError]:
        """Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/events/enable"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[EnableEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListEventTypesResponse, RawError]:
        """Lists all event types that you can subscribe to as webhooks or query using the Events API.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/events/types"),
            query_params=[param[str | None]("api_version", api_version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListEventTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_events(
        self,
        body: SearchEventsRequest | SearchEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchEventsResponse, RawError]:
        """Search for Square API events that occur within a 28-day timeframe.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/events"),
            body=json_body[SearchEventsRequest | SearchEventsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
