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
from ..models.enums.sort_order import SortOrderOrStr
from ..models.v1_order import V1Order
from ..models.v1_update_order_request import V1UpdateOrderRequest, V1UpdateOrderRequestDict
from ..server.server import Server


class V1Transactions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = V1TransactionsWithRawResponse(client, server, auth)

    def v1_list_orders(
        self,
        location_id: str,
        *,
        order: SortOrderOrStr | None = None,
        limit: int | None = None,
        batch_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V1Order]:
        """Provides summary information for a merchant's online store orders.

        Args:
            location_id: The ID of the location to list online store orders for.
            order: The order in which payments are listed in the response.
            limit: The maximum number of payments to return in a single response. This value cannot exceed 200.
            batch_token: A pagination cursor to retrieve the next set of results for your original query to the
                endpoint.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.v1_list_orders(
                location_id, order=order, limit=limit, batch_token=batch_token, request_options=request_options
            ),
        )

    def v1_retrieve_order(
        self, location_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1Order:
        """Provides comprehensive information for a single online store order, including the order's history.

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.v1_retrieve_order(location_id, order_id, request_options=request_options))

    def v1_update_order(
        self,
        location_id: str,
        order_id: str,
        body: V1UpdateOrderRequest | V1UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1Order:
        """Updates the details of an online store order. Every update you perform on an order corresponds to one of
        three actions:

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.v1_update_order(location_id, order_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> V1TransactionsWithRawResponse:
        return self._with_raw_response


class AsyncV1Transactions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncV1TransactionsWithRawResponse(client, server, auth)

    async def v1_list_orders(
        self,
        location_id: str,
        *,
        order: SortOrderOrStr | None = None,
        limit: int | None = None,
        batch_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> list[V1Order]:
        """Provides summary information for a merchant's online store orders.

        Args:
            location_id: The ID of the location to list online store orders for.
            order: The order in which payments are listed in the response.
            limit: The maximum number of payments to return in a single response. This value cannot exceed 200.
            batch_token: A pagination cursor to retrieve the next set of results for your original query to the
                endpoint.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.v1_list_orders(
                location_id, order=order, limit=limit, batch_token=batch_token, request_options=request_options
            ),
        )

    async def v1_retrieve_order(
        self, location_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> V1Order:
        """Provides comprehensive information for a single online store order, including the order's history.

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.v1_retrieve_order(location_id, order_id, request_options=request_options)
        )

    async def v1_update_order(
        self,
        location_id: str,
        order_id: str,
        body: V1UpdateOrderRequest | V1UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> V1Order:
        """Updates the details of an online store order. Every update you perform on an order corresponds to one of
        three actions:

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.v1_update_order(location_id, order_id, body, request_options=request_options)
        )

    @property
    def with_raw_response(self) -> AsyncV1TransactionsWithRawResponse:
        return self._with_raw_response


class V1TransactionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def v1_list_orders(
        self,
        location_id: str,
        *,
        order: SortOrderOrStr | None = None,
        limit: int | None = None,
        batch_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V1Order], RawError]:
        """Provides summary information for a merchant's online store orders.

        Args:
            location_id: The ID of the location to list online store orders for.
            order: The order in which payments are listed in the response.
            limit: The maximum number of payments to return in a single response. This value cannot exceed 200.
            batch_token: A pagination cursor to retrieve the next set of results for your original query to the
                endpoint.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/{location_id}/orders"),
            path_params=[param[str]("location_id", location_id)],
            query_params=[
                param[SortOrderOrStr | None]("order", order),
                param[int | None]("limit", limit),
                param[str | None]("batch_token", batch_token),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[list[V1Order]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def v1_retrieve_order(
        self, location_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1Order, RawError]:
        """Provides comprehensive information for a single online store order, including the order's history.

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/{location_id}/orders/{order_id}"),
            path_params=[param[str]("location_id", location_id), param[str]("order_id", order_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[V1Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def v1_update_order(
        self,
        location_id: str,
        order_id: str,
        body: V1UpdateOrderRequest | V1UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1Order, RawError]:
        """Updates the details of an online store order. Every update you perform on an order corresponds to one of
        three actions:

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/{location_id}/orders/{order_id}"),
            path_params=[param[str]("location_id", location_id), param[str]("order_id", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1UpdateOrderRequest | V1UpdateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[V1Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncV1TransactionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def v1_list_orders(
        self,
        location_id: str,
        *,
        order: SortOrderOrStr | None = None,
        limit: int | None = None,
        batch_token: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[list[V1Order], RawError]:
        """Provides summary information for a merchant's online store orders.

        Args:
            location_id: The ID of the location to list online store orders for.
            order: The order in which payments are listed in the response.
            limit: The maximum number of payments to return in a single response. This value cannot exceed 200.
            batch_token: A pagination cursor to retrieve the next set of results for your original query to the
                endpoint.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/{location_id}/orders"),
            path_params=[param[str]("location_id", location_id)],
            query_params=[
                param[SortOrderOrStr | None]("order", order),
                param[int | None]("limit", limit),
                param[str | None]("batch_token", batch_token),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[list[V1Order]],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def v1_retrieve_order(
        self, location_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[V1Order, RawError]:
        """Provides comprehensive information for a single online store order, including the order's history.

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v1/{location_id}/orders/{order_id}"),
            path_params=[param[str]("location_id", location_id), param[str]("order_id", order_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[V1Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def v1_update_order(
        self,
        location_id: str,
        order_id: str,
        body: V1UpdateOrderRequest | V1UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[V1Order, RawError]:
        """Updates the details of an online store order. Every update you perform on an order corresponds to one of
        three actions:

        Args:
            location_id: The ID of the order's associated location.
            order_id: The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders
                endpoint
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v1/{location_id}/orders/{order_id}"),
            path_params=[param[str]("location_id", location_id), param[str]("order_id", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[V1UpdateOrderRequest | V1UpdateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[V1Order],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
