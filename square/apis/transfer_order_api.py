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
from ..models.cancel_transfer_order_request import CancelTransferOrderRequest, CancelTransferOrderRequestDict
from ..models.cancel_transfer_order_response import CancelTransferOrderResponse
from ..models.create_transfer_order_request import CreateTransferOrderRequest, CreateTransferOrderRequestDict
from ..models.create_transfer_order_response import CreateTransferOrderResponse
from ..models.delete_transfer_order_response import DeleteTransferOrderResponse
from ..models.receive_transfer_order_request import ReceiveTransferOrderRequest, ReceiveTransferOrderRequestDict
from ..models.receive_transfer_order_response import ReceiveTransferOrderResponse
from ..models.retrieve_transfer_order_response import RetrieveTransferOrderResponse
from ..models.search_transfer_orders_request import SearchTransferOrdersRequest, SearchTransferOrdersRequestDict
from ..models.search_transfer_orders_response import SearchTransferOrdersResponse
from ..models.start_transfer_order_request import StartTransferOrderRequest, StartTransferOrderRequestDict
from ..models.start_transfer_order_response import StartTransferOrderResponse
from ..models.update_transfer_order_request import UpdateTransferOrderRequest, UpdateTransferOrderRequestDict
from ..models.update_transfer_order_response import UpdateTransferOrderResponse
from ..server.server import Server


class TransferOrderApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransferOrderApiWithRawResponse(client, server, auth)

    def cancel_transfer_order(
        self,
        transfer_order_id: str,
        body: CancelTransferOrderRequest | CancelTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelTransferOrderResponse:
        """Cancels a transfer order in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Any unreceived quantities will no longer be receivable and will be
        immediately returned to the source `Location <entity:Location>`__'s inventory.

        Common reasons for cancellation:
        - Items no longer needed at destination
        - Source location needs the inventory
        - Order created in error

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to cancel. Must be in STARTED or PARTIALLY_RECEIVED status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_transfer_order(
            transfer_order_id, body, request_options=request_options
        ).unwrap()

    def create_transfer_order(
        self,
        body: CreateTransferOrderRequest | CreateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTransferOrderResponse:
        """Creates a new transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. A transfer order represents
        the intent to move `CatalogItemVariation <entity:CatalogItemVariation>`__s from one `Location
        <entity:Location>`__ to another. The source and destination locations must be different and must belong to your
        Square account.

        In `DRAFT <entity:TransferOrderStatus>`__ status, you can:
        - Add or remove items
        - Modify quantities
        - Update shipping information
        - Delete the entire order via `DeleteTransferOrder <api-endpoint:TransferOrders-DeleteTransferOrder>`__

        The request requires source_location_id and destination_location_id. Inventory levels are not affected until the
        order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__.

        Common integration points:
        - Sync with warehouse management systems
        - Automate regular stock transfers
        - Initialize transfers from inventory optimization systems

        Creates a `transfer_order.created <webhook:transfer_order.created>`__ webhook event.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_transfer_order(body, request_options=request_options).unwrap()

    def delete_transfer_order(
        self, transfer_order_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteTransferOrderResponse:
        """Deletes a transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. Only draft orders can be deleted.
        Once an order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__, it can no
        longer be deleted.

        Creates a `transfer_order.deleted <webhook:transfer_order.deleted>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to delete
            version: Version for optimistic concurrency
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_transfer_order(
            transfer_order_id, version=version, request_options=request_options
        ).unwrap()

    def receive_transfer_order(
        self,
        transfer_order_id: str,
        body: ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReceiveTransferOrderResponse:
        """Records receipt of `CatalogItemVariation <entity:CatalogItemVariation>`__s for a transfer order. This
        endpoint supports partial receiving - you can receive items in multiple batches.

        For each line item, you can specify:
        - Quantity received in good condition (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of IN_STOCK)
        - Quantity damaged during transit/handling (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of WASTE)
        - Quantity canceled (returned to source location's inventory)

        The order must be in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Received quantities are added to the destination `Location
        <entity:Location>`__'s inventory according to their condition. Canceled quantities are immediately returned to
        the source `Location <entity:Location>`__'s inventory.

        When all items are either received, damaged, or canceled, the order moves to `COMPLETED
        <entity:TransferOrderStatus>`__ status.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to receive items for
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.receive_transfer_order(
            transfer_order_id, body, request_options=request_options
        ).unwrap()

    def retrieve_transfer_order(
        self, transfer_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTransferOrderResponse:
        """Retrieves a specific `TransferOrder <entity:TransferOrder>`__ by ID. Returns the complete order details
        including:

        - Basic information (status, dates, notes)
        - Line items with ordered and received quantities
        - Source and destination `Location <entity:Location>`__s
        - Tracking information (if available)

        Args:
            transfer_order_id: The ID of the transfer order to retrieve
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_transfer_order(
            transfer_order_id, request_options=request_options
        ).unwrap()

    def search_transfer_orders(
        self,
        body: SearchTransferOrdersRequest | SearchTransferOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTransferOrdersResponse:
        """Searches for transfer orders using filters. Returns a paginated list of matching `TransferOrder
        <entity:TransferOrder>`__s sorted by creation date.

        Common search scenarios:
        - Find orders for a source `Location <entity:Location>`__
        - Find orders for a destination `Location <entity:Location>`__
        - Find orders in a particular `TransferOrderStatus <entity:TransferOrderStatus>`__

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_transfer_orders(body, request_options=request_options).unwrap()

    def start_transfer_order(
        self,
        transfer_order_id: str,
        body: StartTransferOrderRequest | StartTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartTransferOrderResponse:
        """Changes a `DRAFT <entity:TransferOrderStatus>`__ transfer order to `STARTED <entity:TransferOrderStatus>`__
        status. This decrements inventory at the source `Location <entity:Location>`__ and marks it as in-transit.

        The order must be in `DRAFT <entity:TransferOrderStatus>`__ status and have all required fields populated. Once
        started, the order can no longer be deleted, but it can be canceled via `CancelTransferOrder
        <api-endpoint:TransferOrders-CancelTransferOrder>`__.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to start. Must be in DRAFT status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.start_transfer_order(
            transfer_order_id, body, request_options=request_options
        ).unwrap()

    def update_transfer_order(
        self,
        transfer_order_id: str,
        body: UpdateTransferOrderRequest | UpdateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateTransferOrderResponse:
        """Updates an existing transfer order. This endpoint supports sparse updates, allowing you to modify specific
        fields without affecting others.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to update
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_transfer_order(
            transfer_order_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TransferOrderApiWithRawResponse:
        return self._with_raw_response


class AsyncTransferOrderApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransferOrderApiWithRawResponse(client, server, auth)

    async def cancel_transfer_order(
        self,
        transfer_order_id: str,
        body: CancelTransferOrderRequest | CancelTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelTransferOrderResponse:
        """Cancels a transfer order in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Any unreceived quantities will no longer be receivable and will be
        immediately returned to the source `Location <entity:Location>`__'s inventory.

        Common reasons for cancellation:
        - Items no longer needed at destination
        - Source location needs the inventory
        - Order created in error

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to cancel. Must be in STARTED or PARTIALLY_RECEIVED status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_transfer_order(
                transfer_order_id, body, request_options=request_options
            )
        ).unwrap()

    async def create_transfer_order(
        self,
        body: CreateTransferOrderRequest | CreateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTransferOrderResponse:
        """Creates a new transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. A transfer order represents
        the intent to move `CatalogItemVariation <entity:CatalogItemVariation>`__s from one `Location
        <entity:Location>`__ to another. The source and destination locations must be different and must belong to your
        Square account.

        In `DRAFT <entity:TransferOrderStatus>`__ status, you can:
        - Add or remove items
        - Modify quantities
        - Update shipping information
        - Delete the entire order via `DeleteTransferOrder <api-endpoint:TransferOrders-DeleteTransferOrder>`__

        The request requires source_location_id and destination_location_id. Inventory levels are not affected until the
        order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__.

        Common integration points:
        - Sync with warehouse management systems
        - Automate regular stock transfers
        - Initialize transfers from inventory optimization systems

        Creates a `transfer_order.created <webhook:transfer_order.created>`__ webhook event.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_transfer_order(body, request_options=request_options)).unwrap()

    async def delete_transfer_order(
        self, transfer_order_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteTransferOrderResponse:
        """Deletes a transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. Only draft orders can be deleted.
        Once an order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__, it can no
        longer be deleted.

        Creates a `transfer_order.deleted <webhook:transfer_order.deleted>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to delete
            version: Version for optimistic concurrency
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_transfer_order(
                transfer_order_id, version=version, request_options=request_options
            )
        ).unwrap()

    async def receive_transfer_order(
        self,
        transfer_order_id: str,
        body: ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ReceiveTransferOrderResponse:
        """Records receipt of `CatalogItemVariation <entity:CatalogItemVariation>`__s for a transfer order. This
        endpoint supports partial receiving - you can receive items in multiple batches.

        For each line item, you can specify:
        - Quantity received in good condition (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of IN_STOCK)
        - Quantity damaged during transit/handling (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of WASTE)
        - Quantity canceled (returned to source location's inventory)

        The order must be in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Received quantities are added to the destination `Location
        <entity:Location>`__'s inventory according to their condition. Canceled quantities are immediately returned to
        the source `Location <entity:Location>`__'s inventory.

        When all items are either received, damaged, or canceled, the order moves to `COMPLETED
        <entity:TransferOrderStatus>`__ status.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to receive items for
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.receive_transfer_order(
                transfer_order_id, body, request_options=request_options
            )
        ).unwrap()

    async def retrieve_transfer_order(
        self, transfer_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTransferOrderResponse:
        """Retrieves a specific `TransferOrder <entity:TransferOrder>`__ by ID. Returns the complete order details
        including:

        - Basic information (status, dates, notes)
        - Line items with ordered and received quantities
        - Source and destination `Location <entity:Location>`__s
        - Tracking information (if available)

        Args:
            transfer_order_id: The ID of the transfer order to retrieve
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_transfer_order(transfer_order_id, request_options=request_options)
        ).unwrap()

    async def search_transfer_orders(
        self,
        body: SearchTransferOrdersRequest | SearchTransferOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTransferOrdersResponse:
        """Searches for transfer orders using filters. Returns a paginated list of matching `TransferOrder
        <entity:TransferOrder>`__s sorted by creation date.

        Common search scenarios:
        - Find orders for a source `Location <entity:Location>`__
        - Find orders for a destination `Location <entity:Location>`__
        - Find orders in a particular `TransferOrderStatus <entity:TransferOrderStatus>`__

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_transfer_orders(body, request_options=request_options)).unwrap()

    async def start_transfer_order(
        self,
        transfer_order_id: str,
        body: StartTransferOrderRequest | StartTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StartTransferOrderResponse:
        """Changes a `DRAFT <entity:TransferOrderStatus>`__ transfer order to `STARTED <entity:TransferOrderStatus>`__
        status. This decrements inventory at the source `Location <entity:Location>`__ and marks it as in-transit.

        The order must be in `DRAFT <entity:TransferOrderStatus>`__ status and have all required fields populated. Once
        started, the order can no longer be deleted, but it can be canceled via `CancelTransferOrder
        <api-endpoint:TransferOrders-CancelTransferOrder>`__.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to start. Must be in DRAFT status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.start_transfer_order(transfer_order_id, body, request_options=request_options)
        ).unwrap()

    async def update_transfer_order(
        self,
        transfer_order_id: str,
        body: UpdateTransferOrderRequest | UpdateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateTransferOrderResponse:
        """Updates an existing transfer order. This endpoint supports sparse updates, allowing you to modify specific
        fields without affecting others.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to update
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_transfer_order(
                transfer_order_id, body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransferOrderApiWithRawResponse:
        return self._with_raw_response


class TransferOrderApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_transfer_order(
        self,
        transfer_order_id: str,
        body: CancelTransferOrderRequest | CancelTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelTransferOrderResponse, RawError]:
        """Cancels a transfer order in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Any unreceived quantities will no longer be receivable and will be
        immediately returned to the source `Location <entity:Location>`__'s inventory.

        Common reasons for cancellation:
        - Items no longer needed at destination
        - Source location needs the inventory
        - Order created in error

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to cancel. Must be in STARTED or PARTIALLY_RECEIVED status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}/cancel"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelTransferOrderRequest | CancelTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_transfer_order(
        self,
        body: CreateTransferOrderRequest | CreateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTransferOrderResponse, RawError]:
        """Creates a new transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. A transfer order represents
        the intent to move `CatalogItemVariation <entity:CatalogItemVariation>`__s from one `Location
        <entity:Location>`__ to another. The source and destination locations must be different and must belong to your
        Square account.

        In `DRAFT <entity:TransferOrderStatus>`__ status, you can:
        - Add or remove items
        - Modify quantities
        - Update shipping information
        - Delete the entire order via `DeleteTransferOrder <api-endpoint:TransferOrders-DeleteTransferOrder>`__

        The request requires source_location_id and destination_location_id. Inventory levels are not affected until the
        order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__.

        Common integration points:
        - Sync with warehouse management systems
        - Automate regular stock transfers
        - Initialize transfers from inventory optimization systems

        Creates a `transfer_order.created <webhook:transfer_order.created>`__ webhook event.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTransferOrderRequest | CreateTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_transfer_order(
        self, transfer_order_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteTransferOrderResponse, RawError]:
        """Deletes a transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. Only draft orders can be deleted.
        Once an order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__, it can no
        longer be deleted.

        Creates a `transfer_order.deleted <webhook:transfer_order.deleted>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to delete
            version: Version for optimistic concurrency
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            query_params=[param[int | None]("version", version)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def receive_transfer_order(
        self,
        transfer_order_id: str,
        body: ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReceiveTransferOrderResponse, RawError]:
        """Records receipt of `CatalogItemVariation <entity:CatalogItemVariation>`__s for a transfer order. This
        endpoint supports partial receiving - you can receive items in multiple batches.

        For each line item, you can specify:
        - Quantity received in good condition (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of IN_STOCK)
        - Quantity damaged during transit/handling (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of WASTE)
        - Quantity canceled (returned to source location's inventory)

        The order must be in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Received quantities are added to the destination `Location
        <entity:Location>`__'s inventory according to their condition. Canceled quantities are immediately returned to
        the source `Location <entity:Location>`__'s inventory.

        When all items are either received, damaged, or canceled, the order moves to `COMPLETED
        <entity:TransferOrderStatus>`__ status.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to receive items for
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}/receive"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ReceiveTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_transfer_order(
        self, transfer_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTransferOrderResponse, RawError]:
        """Retrieves a specific `TransferOrder <entity:TransferOrder>`__ by ID. Returns the complete order details
        including:

        - Basic information (status, dates, notes)
        - Line items with ordered and received quantities
        - Source and destination `Location <entity:Location>`__s
        - Tracking information (if available)

        Args:
            transfer_order_id: The ID of the transfer order to retrieve
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_transfer_orders(
        self,
        body: SearchTransferOrdersRequest | SearchTransferOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTransferOrdersResponse, RawError]:
        """Searches for transfer orders using filters. Returns a paginated list of matching `TransferOrder
        <entity:TransferOrder>`__s sorted by creation date.

        Common search scenarios:
        - Find orders for a source `Location <entity:Location>`__
        - Find orders for a destination `Location <entity:Location>`__
        - Find orders in a particular `TransferOrderStatus <entity:TransferOrderStatus>`__

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTransferOrdersRequest | SearchTransferOrdersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTransferOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def start_transfer_order(
        self,
        transfer_order_id: str,
        body: StartTransferOrderRequest | StartTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartTransferOrderResponse, RawError]:
        """Changes a `DRAFT <entity:TransferOrderStatus>`__ transfer order to `STARTED <entity:TransferOrderStatus>`__
        status. This decrements inventory at the source `Location <entity:Location>`__ and marks it as in-transit.

        The order must be in `DRAFT <entity:TransferOrderStatus>`__ status and have all required fields populated. Once
        started, the order can no longer be deleted, but it can be canceled via `CancelTransferOrder
        <api-endpoint:TransferOrders-CancelTransferOrder>`__.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to start. Must be in DRAFT status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}/start"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StartTransferOrderRequest | StartTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[StartTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_transfer_order(
        self,
        transfer_order_id: str,
        body: UpdateTransferOrderRequest | UpdateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateTransferOrderResponse, RawError]:
        """Updates an existing transfer order. This endpoint supports sparse updates, allowing you to modify specific
        fields without affecting others.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to update
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateTransferOrderRequest | UpdateTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTransferOrderApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_transfer_order(
        self,
        transfer_order_id: str,
        body: CancelTransferOrderRequest | CancelTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelTransferOrderResponse, RawError]:
        """Cancels a transfer order in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Any unreceived quantities will no longer be receivable and will be
        immediately returned to the source `Location <entity:Location>`__'s inventory.

        Common reasons for cancellation:
        - Items no longer needed at destination
        - Source location needs the inventory
        - Order created in error

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to cancel. Must be in STARTED or PARTIALLY_RECEIVED status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}/cancel"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelTransferOrderRequest | CancelTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_transfer_order(
        self,
        body: CreateTransferOrderRequest | CreateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTransferOrderResponse, RawError]:
        """Creates a new transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. A transfer order represents
        the intent to move `CatalogItemVariation <entity:CatalogItemVariation>`__s from one `Location
        <entity:Location>`__ to another. The source and destination locations must be different and must belong to your
        Square account.

        In `DRAFT <entity:TransferOrderStatus>`__ status, you can:
        - Add or remove items
        - Modify quantities
        - Update shipping information
        - Delete the entire order via `DeleteTransferOrder <api-endpoint:TransferOrders-DeleteTransferOrder>`__

        The request requires source_location_id and destination_location_id. Inventory levels are not affected until the
        order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__.

        Common integration points:
        - Sync with warehouse management systems
        - Automate regular stock transfers
        - Initialize transfers from inventory optimization systems

        Creates a `transfer_order.created <webhook:transfer_order.created>`__ webhook event.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateTransferOrderRequest | CreateTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_transfer_order(
        self, transfer_order_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteTransferOrderResponse, RawError]:
        """Deletes a transfer order in `DRAFT <entity:TransferOrderStatus>`__ status. Only draft orders can be deleted.
        Once an order is started via `StartTransferOrder <api-endpoint:TransferOrders-StartTransferOrder>`__, it can no
        longer be deleted.

        Creates a `transfer_order.deleted <webhook:transfer_order.deleted>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to delete
            version: Version for optimistic concurrency
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            query_params=[param[int | None]("version", version)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def receive_transfer_order(
        self,
        transfer_order_id: str,
        body: ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ReceiveTransferOrderResponse, RawError]:
        """Records receipt of `CatalogItemVariation <entity:CatalogItemVariation>`__s for a transfer order. This
        endpoint supports partial receiving - you can receive items in multiple batches.

        For each line item, you can specify:
        - Quantity received in good condition (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of IN_STOCK)
        - Quantity damaged during transit/handling (added to destination inventory with `InventoryState
            <entity:InventoryState>`__ of WASTE)
        - Quantity canceled (returned to source location's inventory)

        The order must be in `STARTED <entity:TransferOrderStatus>`__ or `PARTIALLY_RECEIVED
        <entity:TransferOrderStatus>`__ status. Received quantities are added to the destination `Location
        <entity:Location>`__'s inventory according to their condition. Canceled quantities are immediately returned to
        the source `Location <entity:Location>`__'s inventory.

        When all items are either received, damaged, or canceled, the order moves to `COMPLETED
        <entity:TransferOrderStatus>`__ status.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to receive items for
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}/receive"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ReceiveTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_transfer_order(
        self, transfer_order_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTransferOrderResponse, RawError]:
        """Retrieves a specific `TransferOrder <entity:TransferOrder>`__ by ID. Returns the complete order details
        including:

        - Basic information (status, dates, notes)
        - Line items with ordered and received quantities
        - Source and destination `Location <entity:Location>`__s
        - Tracking information (if available)

        Args:
            transfer_order_id: The ID of the transfer order to retrieve
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_transfer_orders(
        self,
        body: SearchTransferOrdersRequest | SearchTransferOrdersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTransferOrdersResponse, RawError]:
        """Searches for transfer orders using filters. Returns a paginated list of matching `TransferOrder
        <entity:TransferOrder>`__s sorted by creation date.

        Common search scenarios:
        - Find orders for a source `Location <entity:Location>`__
        - Find orders for a destination `Location <entity:Location>`__
        - Find orders in a particular `TransferOrderStatus <entity:TransferOrderStatus>`__

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchTransferOrdersRequest | SearchTransferOrdersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTransferOrdersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def start_transfer_order(
        self,
        transfer_order_id: str,
        body: StartTransferOrderRequest | StartTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StartTransferOrderResponse, RawError]:
        """Changes a `DRAFT <entity:TransferOrderStatus>`__ transfer order to `STARTED <entity:TransferOrderStatus>`__
        status. This decrements inventory at the source `Location <entity:Location>`__ and marks it as in-transit.

        The order must be in `DRAFT <entity:TransferOrderStatus>`__ status and have all required fields populated. Once
        started, the order can no longer be deleted, but it can be canceled via `CancelTransferOrder
        <api-endpoint:TransferOrders-CancelTransferOrder>`__.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to start. Must be in DRAFT status.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}/start"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[StartTransferOrderRequest | StartTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[StartTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_transfer_order(
        self,
        transfer_order_id: str,
        body: UpdateTransferOrderRequest | UpdateTransferOrderRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateTransferOrderResponse, RawError]:
        """Updates an existing transfer order. This endpoint supports sparse updates, allowing you to modify specific
        fields without affecting others.

        Creates a `transfer_order.updated <webhook:transfer_order.updated>`__ webhook event.

        Args:
            transfer_order_id: The ID of the transfer order to update
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/transfer-orders/{transfer_order_id}"),
            path_params=[param[str]("transfer_order_id", transfer_order_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateTransferOrderRequest | UpdateTransferOrderRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateTransferOrderResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
