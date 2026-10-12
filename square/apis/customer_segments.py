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
from ..models.list_customer_segments_response import ListCustomerSegmentsResponse
from ..models.retrieve_customer_segment_response import RetrieveCustomerSegmentResponse
from ..server.server import Server


class CustomerSegments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomerSegmentsWithRawResponse(client, server, auth)

    def list_customer_segments(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerSegmentsResponse:
        """Retrieves the list of customer segments of a business.

        Args:
            cursor: A pagination cursor returned by previous calls to ``ListCustomerSegments``. This cursor is used to
                retrieve the next set of query results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 50, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_customer_segments(cursor=cursor, limit=limit, request_options=request_options)
        )

    def retrieve_customer_segment(
        self, segment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerSegmentResponse:
        """Retrieves a specific customer segment as identified by the ``segment_id`` value.

        Args:
            segment_id: The Square-issued ID of the customer segment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_customer_segment(segment_id, request_options=request_options))

    @property
    def with_raw_response(self) -> CustomerSegmentsWithRawResponse:
        return self._with_raw_response


class AsyncCustomerSegments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomerSegmentsWithRawResponse(client, server, auth)

    async def list_customer_segments(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomerSegmentsResponse:
        """Retrieves the list of customer segments of a business.

        Args:
            cursor: A pagination cursor returned by previous calls to ``ListCustomerSegments``. This cursor is used to
                retrieve the next set of query results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 50, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_customer_segments(
                cursor=cursor, limit=limit, request_options=request_options
            ),
        )

    async def retrieve_customer_segment(
        self, segment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerSegmentResponse:
        """Retrieves a specific customer segment as identified by the ``segment_id`` value.

        Args:
            segment_id: The Square-issued ID of the customer segment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_customer_segment(segment_id, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncCustomerSegmentsWithRawResponse:
        return self._with_raw_response


class CustomerSegmentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def list_customer_segments(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerSegmentsResponse, RawError]:
        """Retrieves the list of customer segments of a business.

        Args:
            cursor: A pagination cursor returned by previous calls to ``ListCustomerSegments``. This cursor is used to
                retrieve the next set of query results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 50, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/segments"),
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomerSegmentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_customer_segment(
        self, segment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerSegmentResponse, RawError]:
        """Retrieves a specific customer segment as identified by the ``segment_id`` value.

        Args:
            segment_id: The Square-issued ID of the customer segment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/segments/{segment_id}"),
            path_params=[param[str]("segment_id", segment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerSegmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCustomerSegmentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def list_customer_segments(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomerSegmentsResponse, RawError]:
        """Retrieves the list of customer segments of a business.

        Args:
            cursor: A pagination cursor returned by previous calls to ``ListCustomerSegments``. This cursor is used to
                retrieve the next set of query results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 50, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 50. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/segments"),
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListCustomerSegmentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_customer_segment(
        self, segment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerSegmentResponse, RawError]:
        """Retrieves a specific customer segment as identified by the ``segment_id`` value.

        Args:
            segment_id: The Square-issued ID of the customer segment.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/segments/{segment_id}"),
            path_params=[param[str]("segment_id", segment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveCustomerSegmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
