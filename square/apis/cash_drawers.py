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
    param,
    raw_error_response,
)
from ..models.enums.sort_order import SortOrderOrStr
from ..models.list_cash_drawer_shift_events_response import ListCashDrawerShiftEventsResponse
from ..models.list_cash_drawer_shifts_response import ListCashDrawerShiftsResponse
from ..models.retrieve_cash_drawer_shift_response import RetrieveCashDrawerShiftResponse
from ..server.server import Server


class CashDrawers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CashDrawersWithRawResponse(client, server, auth)

    def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        location_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCashDrawerShiftEventsResponse:
        """Provides a paginated list of events for a single cash drawer shift.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to list cash drawer shifts for.
            limit: Number of resources to be returned in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_cash_drawer_shift_events(
            shift_id, location_id, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_cash_drawer_shifts(
        self,
        location_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCashDrawerShiftsResponse:
        """Provides the details for all of the cash drawer shifts for a location in a date range.

        Args:
            location_id: The ID of the location to query for a list of cash drawer shifts.
            sort_order: The order in which cash drawer shifts are listed in the response, based on their opened_at
                field. Default value: ASC
            begin_time: The inclusive start time of the query on opened_at, in ISO 8601 format.
            end_time: The exclusive end date of the query on opened_at, in ISO 8601 format.
            limit: Number of cash drawer shift events in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_cash_drawer_shifts(
            location_id,
            sort_order=sort_order,
            begin_time=begin_time,
            end_time=end_time,
            limit=limit,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def retrieve_cash_drawer_shift(
        self, shift_id: str, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCashDrawerShiftResponse:
        """Provides the summary details for a single cash drawer shift. See `ListCashDrawerShiftEvents
        <api-endpoint:CashDrawers-ListCashDrawerShiftEvents>`__ for a list of cash drawer shift events.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to retrieve cash drawer shifts from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_cash_drawer_shift(
            shift_id, location_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> CashDrawersWithRawResponse:
        return self._with_raw_response


class AsyncCashDrawers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCashDrawersWithRawResponse(client, server, auth)

    async def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        location_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCashDrawerShiftEventsResponse:
        """Provides a paginated list of events for a single cash drawer shift.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to list cash drawer shifts for.
            limit: Number of resources to be returned in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_cash_drawer_shift_events(
                shift_id, location_id, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_cash_drawer_shifts(
        self,
        location_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCashDrawerShiftsResponse:
        """Provides the details for all of the cash drawer shifts for a location in a date range.

        Args:
            location_id: The ID of the location to query for a list of cash drawer shifts.
            sort_order: The order in which cash drawer shifts are listed in the response, based on their opened_at
                field. Default value: ASC
            begin_time: The inclusive start time of the query on opened_at, in ISO 8601 format.
            end_time: The exclusive end date of the query on opened_at, in ISO 8601 format.
            limit: Number of cash drawer shift events in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_cash_drawer_shifts(
                location_id,
                sort_order=sort_order,
                begin_time=begin_time,
                end_time=end_time,
                limit=limit,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_cash_drawer_shift(
        self, shift_id: str, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCashDrawerShiftResponse:
        """Provides the summary details for a single cash drawer shift. See `ListCashDrawerShiftEvents
        <api-endpoint:CashDrawers-ListCashDrawerShiftEvents>`__ for a list of cash drawer shift events.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to retrieve cash drawer shifts from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_cash_drawer_shift(
                shift_id, location_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCashDrawersWithRawResponse:
        return self._with_raw_response


class CashDrawersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        location_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCashDrawerShiftEventsResponse, RawError]:
        """Provides a paginated list of events for a single cash drawer shift.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to list cash drawer shifts for.
            limit: Number of resources to be returned in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cash-drawers/shifts/{shift_id}/events"),
            path_params=[param[str]("shift_id", shift_id)],
            query_params=[
                param[str]("location_id", location_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCashDrawerShiftEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_cash_drawer_shifts(
        self,
        location_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCashDrawerShiftsResponse, RawError]:
        """Provides the details for all of the cash drawer shifts for a location in a date range.

        Args:
            location_id: The ID of the location to query for a list of cash drawer shifts.
            sort_order: The order in which cash drawer shifts are listed in the response, based on their opened_at
                field. Default value: ASC
            begin_time: The inclusive start time of the query on opened_at, in ISO 8601 format.
            end_time: The exclusive end date of the query on opened_at, in ISO 8601 format.
            limit: Number of cash drawer shift events in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cash-drawers/shifts"),
            query_params=[
                param[str]("location_id", location_id),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCashDrawerShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_cash_drawer_shift(
        self, shift_id: str, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCashDrawerShiftResponse, RawError]:
        """Provides the summary details for a single cash drawer shift. See `ListCashDrawerShiftEvents
        <api-endpoint:CashDrawers-ListCashDrawerShiftEvents>`__ for a list of cash drawer shift events.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to retrieve cash drawer shifts from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cash-drawers/shifts/{shift_id}"),
            path_params=[param[str]("shift_id", shift_id)],
            query_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCashDrawerShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCashDrawersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_cash_drawer_shift_events(
        self,
        shift_id: str,
        location_id: str,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCashDrawerShiftEventsResponse, RawError]:
        """Provides a paginated list of events for a single cash drawer shift.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to list cash drawer shifts for.
            limit: Number of resources to be returned in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cash-drawers/shifts/{shift_id}/events"),
            path_params=[param[str]("shift_id", shift_id)],
            query_params=[
                param[str]("location_id", location_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCashDrawerShiftEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_cash_drawer_shifts(
        self,
        location_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCashDrawerShiftsResponse, RawError]:
        """Provides the details for all of the cash drawer shifts for a location in a date range.

        Args:
            location_id: The ID of the location to query for a list of cash drawer shifts.
            sort_order: The order in which cash drawer shifts are listed in the response, based on their opened_at
                field. Default value: ASC
            begin_time: The inclusive start time of the query on opened_at, in ISO 8601 format.
            end_time: The exclusive end date of the query on opened_at, in ISO 8601 format.
            limit: Number of cash drawer shift events in a page of results (200 by default, 1000 max).
            cursor: Opaque cursor for fetching the next page of results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cash-drawers/shifts"),
            query_params=[
                param[str]("location_id", location_id),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCashDrawerShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_cash_drawer_shift(
        self, shift_id: str, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCashDrawerShiftResponse, RawError]:
        """Provides the summary details for a single cash drawer shift. See `ListCashDrawerShiftEvents
        <api-endpoint:CashDrawers-ListCashDrawerShiftEvents>`__ for a list of cash drawer shift events.

        Args:
            shift_id: The shift ID.
            location_id: The ID of the location to retrieve cash drawer shifts from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/cash-drawers/shifts/{shift_id}"),
            path_params=[param[str]("shift_id", shift_id)],
            query_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCashDrawerShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
