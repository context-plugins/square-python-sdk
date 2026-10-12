from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_json_decoder,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.payout_status import PayoutStatusOrStr
from ..models.enums.sort_order import SortOrderOrStr
from ..models.get_payout_response import GetPayoutResponse
from ..models.list_payout_entries_response import ListPayoutEntriesResponse
from ..models.list_payouts_response import ListPayoutsResponse
from ..server.server import Server


class Payouts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PayoutsWithRawResponse(client, server, auth)

    def get_payout(self, payout_id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetPayoutResponse:
        """Retrieves details of a specific payout identified by a payout ID. To call this endpoint, set ``PAYOUTS_READ``
        for the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_payout(payout_id, request_options=request_options))

    def list_payout_entries(
        self,
        payout_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPayoutEntriesResponse:
        """Retrieves a list of all payout entries for a specific payout. To call this endpoint, set ``PAYOUTS_READ`` for
        the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            sort_order: The order in which payout entries are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_payout_entries(
                payout_id, sort_order=sort_order, cursor=cursor, limit=limit, request_options=request_options
            ),
        )

    def list_payouts(
        self,
        *,
        location_id: str | None = None,
        status: PayoutStatusOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPayoutsResponse:
        """Retrieves a list of all payouts for the default location. You can filter payouts by location ID, status, time
        range, and order them in ascending or descending order. To call this endpoint, set ``PAYOUTS_READ`` for the
        OAuth scope.

        Args:
            location_id: The ID of the location for which to list the payouts. By default, payouts are returned for the
                default (main) location associated with the seller.
            status: If provided, only payouts with the given status are returned.
            begin_time: The timestamp for the beginning of the payout creation time, in RFC 3339 format. Inclusive.
                Default: The current time minus one year.
            end_time: The timestamp for the end of the payout creation time, in RFC 3339 format. Default: The current
                time.
            sort_order: The order in which payouts are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_payouts(
                location_id=location_id,
                status=status,
                begin_time=begin_time,
                end_time=end_time,
                sort_order=sort_order,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> PayoutsWithRawResponse:
        return self._with_raw_response


class AsyncPayouts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPayoutsWithRawResponse(client, server, auth)

    async def get_payout(
        self, payout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPayoutResponse:
        """Retrieves details of a specific payout identified by a payout ID. To call this endpoint, set ``PAYOUTS_READ``
        for the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_payout(payout_id, request_options=request_options))

    async def list_payout_entries(
        self,
        payout_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPayoutEntriesResponse:
        """Retrieves a list of all payout entries for a specific payout. To call this endpoint, set ``PAYOUTS_READ`` for
        the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            sort_order: The order in which payout entries are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_payout_entries(
                payout_id, sort_order=sort_order, cursor=cursor, limit=limit, request_options=request_options
            ),
        )

    async def list_payouts(
        self,
        *,
        location_id: str | None = None,
        status: PayoutStatusOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPayoutsResponse:
        """Retrieves a list of all payouts for the default location. You can filter payouts by location ID, status, time
        range, and order them in ascending or descending order. To call this endpoint, set ``PAYOUTS_READ`` for the
        OAuth scope.

        Args:
            location_id: The ID of the location for which to list the payouts. By default, payouts are returned for the
                default (main) location associated with the seller.
            status: If provided, only payouts with the given status are returned.
            begin_time: The timestamp for the beginning of the payout creation time, in RFC 3339 format. Inclusive.
                Default: The current time minus one year.
            end_time: The timestamp for the end of the payout creation time, in RFC 3339 format. Default: The current
                time.
            sort_order: The order in which payouts are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_payouts(
                location_id=location_id,
                status=status,
                begin_time=begin_time,
                end_time=end_time,
                sort_order=sort_order,
                cursor=cursor,
                limit=limit,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncPayoutsWithRawResponse:
        return self._with_raw_response


class PayoutsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_payout(
        self, payout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPayoutResponse, RawError]:
        """Retrieves details of a specific payout identified by a payout ID. To call this endpoint, set ``PAYOUTS_READ``
        for the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payouts/{payout_id}"),
            path_params=[param[str]("payout_id", payout_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetPayoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_payout_entries(
        self,
        payout_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPayoutEntriesResponse, RawError]:
        """Retrieves a list of all payout entries for a specific payout. To call this endpoint, set ``PAYOUTS_READ`` for
        the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            sort_order: The order in which payout entries are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payouts/{payout_id}/payout-entries"),
            path_params=[param[str]("payout_id", payout_id)],
            query_params=[
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListPayoutEntriesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_payouts(
        self,
        *,
        location_id: str | None = None,
        status: PayoutStatusOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPayoutsResponse, RawError]:
        """Retrieves a list of all payouts for the default location. You can filter payouts by location ID, status, time
        range, and order them in ascending or descending order. To call this endpoint, set ``PAYOUTS_READ`` for the
        OAuth scope.

        Args:
            location_id: The ID of the location for which to list the payouts. By default, payouts are returned for the
                default (main) location associated with the seller.
            status: If provided, only payouts with the given status are returned.
            begin_time: The timestamp for the beginning of the payout creation time, in RFC 3339 format. Inclusive.
                Default: The current time minus one year.
            end_time: The timestamp for the end of the payout creation time, in RFC 3339 format. Default: The current
                time.
            sort_order: The order in which payouts are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payouts"),
            query_params=[
                param[str | None]("location_id", location_id),
                param[PayoutStatusOrStr | None]("status", status),
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListPayoutsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPayoutsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_payout(
        self, payout_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPayoutResponse, RawError]:
        """Retrieves details of a specific payout identified by a payout ID. To call this endpoint, set ``PAYOUTS_READ``
        for the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payouts/{payout_id}"),
            path_params=[param[str]("payout_id", payout_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[GetPayoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_payout_entries(
        self,
        payout_id: str,
        *,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPayoutEntriesResponse, RawError]:
        """Retrieves a list of all payout entries for a specific payout. To call this endpoint, set ``PAYOUTS_READ`` for
        the OAuth scope.

        Args:
            payout_id: The ID of the payout to retrieve the information for.
            sort_order: The order in which payout entries are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payouts/{payout_id}/payout-entries"),
            path_params=[param[str]("payout_id", payout_id)],
            query_params=[
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListPayoutEntriesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_payouts(
        self,
        *,
        location_id: str | None = None,
        status: PayoutStatusOrStr | None = None,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPayoutsResponse, RawError]:
        """Retrieves a list of all payouts for the default location. You can filter payouts by location ID, status, time
        range, and order them in ascending or descending order. To call this endpoint, set ``PAYOUTS_READ`` for the
        OAuth scope.

        Args:
            location_id: The ID of the location for which to list the payouts. By default, payouts are returned for the
                default (main) location associated with the seller.
            status: If provided, only payouts with the given status are returned.
            begin_time: The timestamp for the beginning of the payout creation time, in RFC 3339 format. Inclusive.
                Default: The current time minus one year.
            end_time: The timestamp for the end of the payout creation time, in RFC 3339 format. Default: The current
                time.
            sort_order: The order in which payouts are listed.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__. If request
                parameters change between requests, subsequent results may contain duplicates or missing records.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payouts"),
            query_params=[
                param[str | None]("location_id", location_id),
                param[PayoutStatusOrStr | None]("status", status),
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListPayoutsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
