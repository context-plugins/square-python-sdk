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
from ..models.batch_retrieve_orders_request import BatchRetrieveOrdersRequest, BatchRetrieveOrdersRequestDict
from ..models.batch_retrieve_orders_response import BatchRetrieveOrdersResponse
from ..models.calculate_order_request import CalculateOrderRequest, CalculateOrderRequestDict
from ..models.calculate_order_response import CalculateOrderResponse
from ..models.clone_order_request import CloneOrderRequest, CloneOrderRequestDict
from ..models.clone_order_response import CloneOrderResponse
from ..models.create_order_request import CreateOrderRequest, CreateOrderRequestDict
from ..models.create_order_response import CreateOrderResponse
from ..models.pay_order_request import PayOrderRequest, PayOrderRequestDict
from ..models.pay_order_response import PayOrderResponse
from ..models.retrieve_order_response import RetrieveOrderResponse
from ..models.search_orders_request import SearchOrdersRequest, SearchOrdersRequestDict
from ..models.search_orders_response import SearchOrdersResponse
from ..models.update_order_request import UpdateOrderRequest, UpdateOrderRequestDict
from ..models.update_order_response import UpdateOrderResponse
from ..server.server import Server


class Orders:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = OrdersWithRawResponse(client, server, auth)

    def batch_retrieve_orders(
        self,
        body: BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveOrdersResponse:
        """Retrieves a set of `orders <entity:Order>`__ by their IDs.

        If a given order ID does not exist, the ID is ignored instead of generating an error.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.batch_retrieve_orders(body, request_options=request_options))

    def calculate_order(
        self,
        body: CalculateOrderRequest | CalculateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculateOrderResponse:
        """Enables applications to preview order pricing without creating an order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.calculate_order(body, request_options=request_options))

    def clone_order(
        self, body: CloneOrderRequest | CloneOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CloneOrderResponse:
        """Creates a new order, in the ``DRAFT`` state, by duplicating an existing order. The newly created order has
        only the core fields (such as line items, taxes, and discounts) copied from the original order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.clone_order(body, request_options=request_options))

    def create_order(
        self, body: CreateOrderRequest | CreateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateOrderResponse:
        """Creates a new `order <entity:Order>`__ that can include information about products for purchase and settings
        to apply to the purchase.

        To pay for a created order, see `Pay for Orders
        <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        You can modify open orders using the `UpdateOrder <api-endpoint:Orders-UpdateOrder>`__ endpoint.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_order(body, request_options=request_options))

    def pay_order(
        self,
        order_id: str,
        body: PayOrderRequest | PayOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayOrderResponse:
        """Pay for an `order <entity:Order>`__ using one or more approved `payments <entity:Payment>`__ or settle an
        order with a total of ``0``.

        The total of the ``payment_ids`` listed in the request must be equal to the order total. Orders with a total
        amount of ``0`` can be marked as paid by specifying an empty array of ``payment_ids`` in the request.

        To be used with ``PayOrder``, a payment must:

        - Reference the order by specifying the ``order_id`` when `creating the payment
            <api-endpoint:Payments-CreatePayment>`__.
        Any approved payments that reference the same ``order_id`` not specified in the ``payment_ids`` is canceled.
        - Be approved with `delayed capture
            <https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture>`__.
        Using a delayed capture payment with ``PayOrder`` completes the approved payment.

        Args:
            order_id: The ID of the order being paid.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.pay_order(order_id, body, request_options=request_options))

    def retrieve_order(
        self, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveOrderResponse:
        """Retrieves an `Order <entity:Order>`__ by ID.

        Args:
            order_id: The ID of the order to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_order(order_id, request_options=request_options))

    def search_orders(
        self,
        body: SearchOrdersRequest | SearchOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchOrdersResponse:
        """Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of
        how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).

        ``SearchOrders`` requests need to specify which locations to search and define a `SearchOrdersQuery
        <entity:SearchOrdersQuery>`__ object that controls how to sort or filter the results. Your ``SearchOrdersQuery``
        can:

          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete ``Order`` objects or as
        `OrderEntry <entity:OrderEntry>`__ objects.

        Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted
        to Square for up to 72 hours. Offline orders have a ``created_at`` value that reflects the time the order was
        created, not the time it was subsequently transmitted to Square.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_orders(body, request_options=request_options))

    def update_order(
        self,
        order_id: str,
        body: UpdateOrderRequest | UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateOrderResponse:
        """Updates an open `order <entity:Order>`__ by adding, replacing, or deleting fields. Orders with a
        ``COMPLETED`` or ``CANCELED`` state cannot be updated.

        An ``UpdateOrder`` request requires the following:

        - The ``order_id`` in the endpoint path, identifying the order to update.
        - The latest ``version`` of the order to update.
        - The `sparse order
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects>`__
        containing only the fields to update and the version to which the update is being applied.
        - If deleting fields, the `dot notation paths
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete>`__
        identifying the fields to clear.

        To pay for an order, see `Pay for Orders <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        Args:
            order_id: The ID of the order to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.update_order(order_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> OrdersWithRawResponse:
        return self._with_raw_response


class AsyncOrders:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncOrdersWithRawResponse(client, server, auth)

    async def batch_retrieve_orders(
        self,
        body: BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveOrdersResponse:
        """Retrieves a set of `orders <entity:Order>`__ by their IDs.

        If a given order ID does not exist, the ID is ignored instead of generating an error.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.batch_retrieve_orders(body, request_options=request_options))

    async def calculate_order(
        self,
        body: CalculateOrderRequest | CalculateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculateOrderResponse:
        """Enables applications to preview order pricing without creating an order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.calculate_order(body, request_options=request_options))

    async def clone_order(
        self, body: CloneOrderRequest | CloneOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CloneOrderResponse:
        """Creates a new order, in the ``DRAFT`` state, by duplicating an existing order. The newly created order has
        only the core fields (such as line items, taxes, and discounts) copied from the original order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.clone_order(body, request_options=request_options))

    async def create_order(
        self, body: CreateOrderRequest | CreateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateOrderResponse:
        """Creates a new `order <entity:Order>`__ that can include information about products for purchase and settings
        to apply to the purchase.

        To pay for a created order, see `Pay for Orders
        <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        You can modify open orders using the `UpdateOrder <api-endpoint:Orders-UpdateOrder>`__ endpoint.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_order(body, request_options=request_options))

    async def pay_order(
        self,
        order_id: str,
        body: PayOrderRequest | PayOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PayOrderResponse:
        """Pay for an `order <entity:Order>`__ using one or more approved `payments <entity:Payment>`__ or settle an
        order with a total of ``0``.

        The total of the ``payment_ids`` listed in the request must be equal to the order total. Orders with a total
        amount of ``0`` can be marked as paid by specifying an empty array of ``payment_ids`` in the request.

        To be used with ``PayOrder``, a payment must:

        - Reference the order by specifying the ``order_id`` when `creating the payment
            <api-endpoint:Payments-CreatePayment>`__.
        Any approved payments that reference the same ``order_id`` not specified in the ``payment_ids`` is canceled.
        - Be approved with `delayed capture
            <https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture>`__.
        Using a delayed capture payment with ``PayOrder`` completes the approved payment.

        Args:
            order_id: The ID of the order being paid.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.pay_order(order_id, body, request_options=request_options))

    async def retrieve_order(
        self, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveOrderResponse:
        """Retrieves an `Order <entity:Order>`__ by ID.

        Args:
            order_id: The ID of the order to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_order(order_id, request_options=request_options))

    async def search_orders(
        self,
        body: SearchOrdersRequest | SearchOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchOrdersResponse:
        """Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of
        how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).

        ``SearchOrders`` requests need to specify which locations to search and define a `SearchOrdersQuery
        <entity:SearchOrdersQuery>`__ object that controls how to sort or filter the results. Your ``SearchOrdersQuery``
        can:

          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete ``Order`` objects or as
        `OrderEntry <entity:OrderEntry>`__ objects.

        Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted
        to Square for up to 72 hours. Offline orders have a ``created_at`` value that reflects the time the order was
        created, not the time it was subsequently transmitted to Square.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_orders(body, request_options=request_options))

    async def update_order(
        self,
        order_id: str,
        body: UpdateOrderRequest | UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateOrderResponse:
        """Updates an open `order <entity:Order>`__ by adding, replacing, or deleting fields. Orders with a
        ``COMPLETED`` or ``CANCELED`` state cannot be updated.

        An ``UpdateOrder`` request requires the following:

        - The ``order_id`` in the endpoint path, identifying the order to update.
        - The latest ``version`` of the order to update.
        - The `sparse order
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects>`__
        containing only the fields to update and the version to which the update is being applied.
        - If deleting fields, the `dot notation paths
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete>`__
        identifying the fields to clear.

        To pay for an order, see `Pay for Orders <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        Args:
            order_id: The ID of the order to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.update_order(order_id, body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncOrdersWithRawResponse:
        return self._with_raw_response


class OrdersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def batch_retrieve_orders(
        self,
        body: BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveOrdersResponse, RawError]:
        """Retrieves a set of `orders <entity:Order>`__ by their IDs.

        If a given order ID does not exist, the ID is ignored instead of generating an error.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/batch-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calculate_order(
        self,
        body: CalculateOrderRequest | CalculateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculateOrderResponse, RawError]:
        """Enables applications to preview order pricing without creating an order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/calculate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateOrderRequest | CalculateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CalculateOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def clone_order(
        self, body: CloneOrderRequest | CloneOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CloneOrderResponse, RawError]:
        """Creates a new order, in the ``DRAFT`` state, by duplicating an existing order. The newly created order has
        only the core fields (such as line items, taxes, and discounts) copied from the original order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/clone"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloneOrderRequest | CloneOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CloneOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_order(
        self, body: CreateOrderRequest | CreateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateOrderResponse, RawError]:
        """Creates a new `order <entity:Order>`__ that can include information about products for purchase and settings
        to apply to the purchase.

        To pay for a created order, see `Pay for Orders
        <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        You can modify open orders using the `UpdateOrder <api-endpoint:Orders-UpdateOrder>`__ endpoint.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrderRequest | CreateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pay_order(
        self,
        order_id: str,
        body: PayOrderRequest | PayOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayOrderResponse, RawError]:
        """Pay for an `order <entity:Order>`__ using one or more approved `payments <entity:Payment>`__ or settle an
        order with a total of ``0``.

        The total of the ``payment_ids`` listed in the request must be equal to the order total. Orders with a total
        amount of ``0`` can be marked as paid by specifying an empty array of ``payment_ids`` in the request.

        To be used with ``PayOrder``, a payment must:

        - Reference the order by specifying the ``order_id`` when `creating the payment
            <api-endpoint:Payments-CreatePayment>`__.
        Any approved payments that reference the same ``order_id`` not specified in the ``payment_ids`` is canceled.
        - Be approved with `delayed capture
            <https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture>`__.
        Using a delayed capture payment with ``PayOrder`` completes the approved payment.

        Args:
            order_id: The ID of the order being paid.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/{order_id}/pay"),
            path_params=[param[str]("order_id", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayOrderRequest | PayOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PayOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_order(
        self, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveOrderResponse, RawError]:
        """Retrieves an `Order <entity:Order>`__ by ID.

        Args:
            order_id: The ID of the order to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[str]("order_id", order_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_orders(
        self,
        body: SearchOrdersRequest | SearchOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchOrdersResponse, RawError]:
        """Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of
        how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).

        ``SearchOrders`` requests need to specify which locations to search and define a `SearchOrdersQuery
        <entity:SearchOrdersQuery>`__ object that controls how to sort or filter the results. Your ``SearchOrdersQuery``
        can:

          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete ``Order`` objects or as
        `OrderEntry <entity:OrderEntry>`__ objects.

        Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted
        to Square for up to 72 hours. Offline orders have a ``created_at`` value that reflects the time the order was
        created, not the time it was subsequently transmitted to Square.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchOrdersRequest | SearchOrdersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_order(
        self,
        order_id: str,
        body: UpdateOrderRequest | UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateOrderResponse, RawError]:
        """Updates an open `order <entity:Order>`__ by adding, replacing, or deleting fields. Orders with a
        ``COMPLETED`` or ``CANCELED`` state cannot be updated.

        An ``UpdateOrder`` request requires the following:

        - The ``order_id`` in the endpoint path, identifying the order to update.
        - The latest ``version`` of the order to update.
        - The `sparse order
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects>`__
        containing only the fields to update and the version to which the update is being applied.
        - If deleting fields, the `dot notation paths
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete>`__
        identifying the fields to clear.

        To pay for an order, see `Pay for Orders <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        Args:
            order_id: The ID of the order to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[str]("order_id", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateOrderRequest | UpdateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncOrdersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def batch_retrieve_orders(
        self,
        body: BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveOrdersResponse, RawError]:
        """Retrieves a set of `orders <entity:Order>`__ by their IDs.

        If a given order ID does not exist, the ID is ignored instead of generating an error.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/batch-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[BatchRetrieveOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calculate_order(
        self,
        body: CalculateOrderRequest | CalculateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculateOrderResponse, RawError]:
        """Enables applications to preview order pricing without creating an order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/calculate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateOrderRequest | CalculateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CalculateOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def clone_order(
        self, body: CloneOrderRequest | CloneOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CloneOrderResponse, RawError]:
        """Creates a new order, in the ``DRAFT`` state, by duplicating an existing order. The newly created order has
        only the core fields (such as line items, taxes, and discounts) copied from the original order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/clone"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CloneOrderRequest | CloneOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CloneOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_order(
        self, body: CreateOrderRequest | CreateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateOrderResponse, RawError]:
        """Creates a new `order <entity:Order>`__ that can include information about products for purchase and settings
        to apply to the purchase.

        To pay for a created order, see `Pay for Orders
        <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        You can modify open orders using the `UpdateOrder <api-endpoint:Orders-UpdateOrder>`__ endpoint.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateOrderRequest | CreateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pay_order(
        self,
        order_id: str,
        body: PayOrderRequest | PayOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PayOrderResponse, RawError]:
        """Pay for an `order <entity:Order>`__ using one or more approved `payments <entity:Payment>`__ or settle an
        order with a total of ``0``.

        The total of the ``payment_ids`` listed in the request must be equal to the order total. Orders with a total
        amount of ``0`` can be marked as paid by specifying an empty array of ``payment_ids`` in the request.

        To be used with ``PayOrder``, a payment must:

        - Reference the order by specifying the ``order_id`` when `creating the payment
            <api-endpoint:Payments-CreatePayment>`__.
        Any approved payments that reference the same ``order_id`` not specified in the ``payment_ids`` is canceled.
        - Be approved with `delayed capture
            <https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture>`__.
        Using a delayed capture payment with ``PayOrder`` completes the approved payment.

        Args:
            order_id: The ID of the order being paid.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/{order_id}/pay"),
            path_params=[param[str]("order_id", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PayOrderRequest | PayOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[PayOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_order(
        self, order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveOrderResponse, RawError]:
        """Retrieves an `Order <entity:Order>`__ by ID.

        Args:
            order_id: The ID of the order to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[str]("order_id", order_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_orders(
        self,
        body: SearchOrdersRequest | SearchOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchOrdersResponse, RawError]:
        """Search all orders for one or more locations. Orders include all sales, returns, and exchanges regardless of
        how or when they entered the Square ecosystem (such as Point of Sale, Invoices, and Connect APIs).

        ``SearchOrders`` requests need to specify which locations to search and define a `SearchOrdersQuery
        <entity:SearchOrdersQuery>`__ object that controls how to sort or filter the results. Your ``SearchOrdersQuery``
        can:

          Set filter criteria.
          Set the sort order.
          Determine whether to return results as complete ``Order`` objects or as
        `OrderEntry <entity:OrderEntry>`__ objects.

        Note that details for orders processed with Square Point of Sale while in offline mode might not be transmitted
        to Square for up to 72 hours. Offline orders have a ``created_at`` value that reflects the time the order was
        created, not the time it was subsequently transmitted to Square.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/orders/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchOrdersRequest | SearchOrdersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[SearchOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_order(
        self,
        order_id: str,
        body: UpdateOrderRequest | UpdateOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateOrderResponse, RawError]:
        """Updates an open `order <entity:Order>`__ by adding, replacing, or deleting fields. Orders with a
        ``COMPLETED`` or ``CANCELED`` state cannot be updated.

        An ``UpdateOrder`` request requires the following:

        - The ``order_id`` in the endpoint path, identifying the order to update.
        - The latest ``version`` of the order to update.
        - The `sparse order
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects>`__
        containing only the fields to update and the version to which the update is being applied.
        - If deleting fields, the `dot notation paths
            <https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete>`__
        identifying the fields to clear.

        To pay for an order, see `Pay for Orders <https://developer.squareup.com/docs/orders-api/pay-for-orders>`__.

        Args:
            order_id: The ID of the order to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/orders/{order_id}"),
            path_params=[param[str]("order_id", order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateOrderRequest | UpdateOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
