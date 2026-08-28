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
from ..models.batch_change_inventory_request import BatchChangeInventoryRequest, BatchChangeInventoryRequestDict
from ..models.batch_change_inventory_response import BatchChangeInventoryResponse
from ..models.batch_retrieve_inventory_changes_request import (
    BatchRetrieveInventoryChangesRequest,
    BatchRetrieveInventoryChangesRequestDict,
)
from ..models.batch_retrieve_inventory_changes_response import BatchRetrieveInventoryChangesResponse
from ..models.batch_retrieve_inventory_counts_request import (
    BatchRetrieveInventoryCountsRequest,
    BatchRetrieveInventoryCountsRequestDict,
)
from ..models.batch_retrieve_inventory_counts_response import BatchRetrieveInventoryCountsResponse
from ..models.create_inventory_adjustment_reason_request import (
    CreateInventoryAdjustmentReasonRequest,
    CreateInventoryAdjustmentReasonRequestDict,
)
from ..models.create_inventory_adjustment_reason_response import CreateInventoryAdjustmentReasonResponse
from ..models.delete_inventory_adjustment_reason_request import (
    DeleteInventoryAdjustmentReasonRequest,
    DeleteInventoryAdjustmentReasonRequestDict,
)
from ..models.delete_inventory_adjustment_reason_response import DeleteInventoryAdjustmentReasonResponse
from ..models.list_inventory_adjustment_reasons_response import ListInventoryAdjustmentReasonsResponse
from ..models.restore_inventory_adjustment_reason_request import (
    RestoreInventoryAdjustmentReasonRequest,
    RestoreInventoryAdjustmentReasonRequestDict,
)
from ..models.restore_inventory_adjustment_reason_response import RestoreInventoryAdjustmentReasonResponse
from ..models.retrieve_inventory_adjustment_reason_request import (
    RetrieveInventoryAdjustmentReasonRequest,
    RetrieveInventoryAdjustmentReasonRequestDict,
)
from ..models.retrieve_inventory_adjustment_reason_response import RetrieveInventoryAdjustmentReasonResponse
from ..models.retrieve_inventory_adjustment_response import RetrieveInventoryAdjustmentResponse
from ..models.retrieve_inventory_changes_response import RetrieveInventoryChangesResponse
from ..models.retrieve_inventory_count_response import RetrieveInventoryCountResponse
from ..models.retrieve_inventory_physical_count_response import RetrieveInventoryPhysicalCountResponse
from ..models.update_inventory_adjustment_reason_request import (
    UpdateInventoryAdjustmentReasonRequest,
    UpdateInventoryAdjustmentReasonRequestDict,
)
from ..models.update_inventory_adjustment_reason_response import UpdateInventoryAdjustmentReasonResponse
from ..models.update_inventory_adjustment_request import (
    UpdateInventoryAdjustmentRequest,
    UpdateInventoryAdjustmentRequestDict,
)
from ..models.update_inventory_adjustment_response import UpdateInventoryAdjustmentResponse
from ..server.server import Server


class Inventory:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InventoryWithRawResponse(client, server, auth)

    def batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchChangeInventoryResponse:
        """Applies adjustments and counts to the provided item quantities.

        On success: returns the current calculated counts for all objects referenced in the request. On failure: returns
        a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_change_inventory(body, request_options=request_options).unwrap()

    def batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryChangesResponse:
        """Returns historical physical counts and adjustments based on the provided filter criteria.

        Results are paginated and sorted in ascending order according their ``occurred_at`` timestamp (oldest first).

        BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler
        endpoints.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_retrieve_inventory_changes(body, request_options=request_options).unwrap()

    def batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryCountsResponse:
        """Returns current counts for the provided `CatalogObject <entity:CatalogObject>`__s at the requested `Location
        <entity:Location>`__s.

        Results are paginated and sorted in descending order according to their ``calculated_at`` timestamp (newest
        first).

        When ``updated_after`` is specified, only counts that have changed since that time (based on the server
        timestamp for the most recent change) are returned. This allows clients to perform a "sync" operation, for
        example in response to receiving a Webhook notification.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.batch_retrieve_inventory_counts(body, request_options=request_options).unwrap()

    def create_inventory_adjustment_reason(
        self,
        body: CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInventoryAdjustmentReasonResponse:
        """Creates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_inventory_adjustment_reason(
            body, request_options=request_options
        ).unwrap()

    def delete_inventory_adjustment_reason(
        self,
        body: DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeleteInventoryAdjustmentReasonResponse:
        """Soft deletes a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_inventory_adjustment_reason(
            body, request_options=request_options
        ).unwrap()

    def deprecated_batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchChangeInventoryResponse:
        """Deprecated version of `BatchChangeInventory <api-endpoint:Inventory-BatchChangeInventory>`__ after the
        endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deprecated_batch_change_inventory(body, request_options=request_options).unwrap()

    def deprecated_batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryChangesResponse:
        """Deprecated version of `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deprecated_batch_retrieve_inventory_changes(
            body, request_options=request_options
        ).unwrap()

    def deprecated_batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryCountsResponse:
        """Deprecated version of `BatchRetrieveInventoryCounts <api-endpoint:Inventory-BatchRetrieveInventoryCounts>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deprecated_batch_retrieve_inventory_counts(
            body, request_options=request_options
        ).unwrap()

    def deprecated_retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryAdjustmentResponse:
        """Deprecated version of `RetrieveInventoryAdjustment <api-endpoint:Inventory-RetrieveInventoryAdjustment>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deprecated_retrieve_inventory_adjustment(
            adjustment_id, request_options=request_options
        ).unwrap()

    def deprecated_retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryPhysicalCountResponse:
        """Deprecated version of `RetrieveInventoryPhysicalCount
        <api-endpoint:Inventory-RetrieveInventoryPhysicalCount>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.deprecated_retrieve_inventory_physical_count(
            physical_count_id, request_options=request_options
        ).unwrap()

    def list_inventory_adjustment_reasons(
        self,
        *,
        include_deleted: bool | None = False,
        include_system_codes: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInventoryAdjustmentReasonsResponse:
        """Returns the standard and custom inventory adjustment reasons available to the seller.

        Args:
            include_deleted: Indicates whether the response should include deleted custom inventory adjustment reasons.
                The default value is ``false``.
            include_system_codes: Indicates whether the response should include Square-generated system inventory
                adjustment reason codes that cannot be used to write adjustments from the Connect API, such as ``SALE``,
                ``RECOUNT``, ``TRANSFER``, ``IN_TRANSIT``, and ``CANCELED_SALE``. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_inventory_adjustment_reasons(
            include_deleted=include_deleted, include_system_codes=include_system_codes, request_options=request_options
        ).unwrap()

    def restore_inventory_adjustment_reason(
        self,
        body: RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RestoreInventoryAdjustmentReasonResponse:
        """Restores a soft-deleted custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.restore_inventory_adjustment_reason(
            body, request_options=request_options
        ).unwrap()

    def retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryAdjustmentResponse:
        """Returns the `InventoryAdjustment <entity:InventoryAdjustment>`__ object with the provided ``adjustment_id``.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_inventory_adjustment(
            adjustment_id, request_options=request_options
        ).unwrap()

    def retrieve_inventory_adjustment_reason(
        self,
        body: RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveInventoryAdjustmentReasonResponse:
        """Returns the inventory adjustment reason identified by the provided ``reason_id``. Deleted custom reasons can
        be retrieved by ID.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_inventory_adjustment_reason(
            body, request_options=request_options
        ).unwrap()

    def retrieve_inventory_changes(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveInventoryChangesResponse:
        """Returns a set of physical counts and inventory adjustments for the provided `CatalogObject
        <entity:CatalogObject>`__ at the requested `Location <entity:Location>`__s.

        You can achieve the same result by calling `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ and having the ``catalog_object_ids`` list contain a
        single element of the ``CatalogObject`` ID.

        Results are paginated and sorted in descending order according to their ``occurred_at`` timestamp (newest
        first).

        There are no limits on how far back the caller can page. This endpoint can be used to display recent changes for
        a specific item. For more sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_inventory_changes(
            catalog_object_id, location_ids=location_ids, cursor=cursor, request_options=request_options
        ).unwrap()

    def retrieve_inventory_count(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveInventoryCountResponse:
        """Retrieves the current calculated stock count for a given `CatalogObject <entity:CatalogObject>`__ at a given
        set of `Location <entity:Location>`__s. Responses are paginated and unsorted. For more sophisticated queries,
        use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_inventory_count(
            catalog_object_id, location_ids=location_ids, cursor=cursor, request_options=request_options
        ).unwrap()

    def retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryPhysicalCountResponse:
        """Returns the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ object with the provided
        ``physical_count_id``.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_inventory_physical_count(
            physical_count_id, request_options=request_options
        ).unwrap()

    def update_inventory_adjustment(
        self,
        body: UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInventoryAdjustmentResponse:
        """Applies an update to the provided adjustment.

        On success: returns the newly updated adjustment. On failure: returns a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_inventory_adjustment(body, request_options=request_options).unwrap()

    def update_inventory_adjustment_reason(
        self,
        body: UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInventoryAdjustmentReasonResponse:
        """Updates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_inventory_adjustment_reason(
            body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> InventoryWithRawResponse:
        return self._with_raw_response


class AsyncInventory:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInventoryWithRawResponse(client, server, auth)

    async def batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchChangeInventoryResponse:
        """Applies adjustments and counts to the provided item quantities.

        On success: returns the current calculated counts for all objects referenced in the request. On failure: returns
        a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.batch_change_inventory(body, request_options=request_options)).unwrap()

    async def batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryChangesResponse:
        """Returns historical physical counts and adjustments based on the provided filter criteria.

        Results are paginated and sorted in ascending order according their ``occurred_at`` timestamp (oldest first).

        BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler
        endpoints.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.batch_retrieve_inventory_changes(body, request_options=request_options)
        ).unwrap()

    async def batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryCountsResponse:
        """Returns current counts for the provided `CatalogObject <entity:CatalogObject>`__s at the requested `Location
        <entity:Location>`__s.

        Results are paginated and sorted in descending order according to their ``calculated_at`` timestamp (newest
        first).

        When ``updated_after`` is specified, only counts that have changed since that time (based on the server
        timestamp for the most recent change) are returned. This allows clients to perform a "sync" operation, for
        example in response to receiving a Webhook notification.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.batch_retrieve_inventory_counts(body, request_options=request_options)
        ).unwrap()

    async def create_inventory_adjustment_reason(
        self,
        body: CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInventoryAdjustmentReasonResponse:
        """Creates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_inventory_adjustment_reason(body, request_options=request_options)
        ).unwrap()

    async def delete_inventory_adjustment_reason(
        self,
        body: DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DeleteInventoryAdjustmentReasonResponse:
        """Soft deletes a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_inventory_adjustment_reason(body, request_options=request_options)
        ).unwrap()

    async def deprecated_batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchChangeInventoryResponse:
        """Deprecated version of `BatchChangeInventory <api-endpoint:Inventory-BatchChangeInventory>`__ after the
        endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deprecated_batch_change_inventory(body, request_options=request_options)
        ).unwrap()

    async def deprecated_batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryChangesResponse:
        """Deprecated version of `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deprecated_batch_retrieve_inventory_changes(
                body, request_options=request_options
            )
        ).unwrap()

    async def deprecated_batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BatchRetrieveInventoryCountsResponse:
        """Deprecated version of `BatchRetrieveInventoryCounts <api-endpoint:Inventory-BatchRetrieveInventoryCounts>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deprecated_batch_retrieve_inventory_counts(
                body, request_options=request_options
            )
        ).unwrap()

    async def deprecated_retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryAdjustmentResponse:
        """Deprecated version of `RetrieveInventoryAdjustment <api-endpoint:Inventory-RetrieveInventoryAdjustment>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deprecated_retrieve_inventory_adjustment(
                adjustment_id, request_options=request_options
            )
        ).unwrap()

    async def deprecated_retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryPhysicalCountResponse:
        """Deprecated version of `RetrieveInventoryPhysicalCount
        <api-endpoint:Inventory-RetrieveInventoryPhysicalCount>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.deprecated_retrieve_inventory_physical_count(
                physical_count_id, request_options=request_options
            )
        ).unwrap()

    async def list_inventory_adjustment_reasons(
        self,
        *,
        include_deleted: bool | None = False,
        include_system_codes: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInventoryAdjustmentReasonsResponse:
        """Returns the standard and custom inventory adjustment reasons available to the seller.

        Args:
            include_deleted: Indicates whether the response should include deleted custom inventory adjustment reasons.
                The default value is ``false``.
            include_system_codes: Indicates whether the response should include Square-generated system inventory
                adjustment reason codes that cannot be used to write adjustments from the Connect API, such as ``SALE``,
                ``RECOUNT``, ``TRANSFER``, ``IN_TRANSIT``, and ``CANCELED_SALE``. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_inventory_adjustment_reasons(
                include_deleted=include_deleted,
                include_system_codes=include_system_codes,
                request_options=request_options,
            )
        ).unwrap()

    async def restore_inventory_adjustment_reason(
        self,
        body: RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RestoreInventoryAdjustmentReasonResponse:
        """Restores a soft-deleted custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.restore_inventory_adjustment_reason(body, request_options=request_options)
        ).unwrap()

    async def retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryAdjustmentResponse:
        """Returns the `InventoryAdjustment <entity:InventoryAdjustment>`__ object with the provided ``adjustment_id``.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_inventory_adjustment(adjustment_id, request_options=request_options)
        ).unwrap()

    async def retrieve_inventory_adjustment_reason(
        self,
        body: RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveInventoryAdjustmentReasonResponse:
        """Returns the inventory adjustment reason identified by the provided ``reason_id``. Deleted custom reasons can
        be retrieved by ID.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_inventory_adjustment_reason(body, request_options=request_options)
        ).unwrap()

    async def retrieve_inventory_changes(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveInventoryChangesResponse:
        """Returns a set of physical counts and inventory adjustments for the provided `CatalogObject
        <entity:CatalogObject>`__ at the requested `Location <entity:Location>`__s.

        You can achieve the same result by calling `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ and having the ``catalog_object_ids`` list contain a
        single element of the ``CatalogObject`` ID.

        Results are paginated and sorted in descending order according to their ``occurred_at`` timestamp (newest
        first).

        There are no limits on how far back the caller can page. This endpoint can be used to display recent changes for
        a specific item. For more sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_inventory_changes(
                catalog_object_id, location_ids=location_ids, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def retrieve_inventory_count(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RetrieveInventoryCountResponse:
        """Retrieves the current calculated stock count for a given `CatalogObject <entity:CatalogObject>`__ at a given
        set of `Location <entity:Location>`__s. Responses are paginated and unsorted. For more sophisticated queries,
        use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_inventory_count(
                catalog_object_id, location_ids=location_ids, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveInventoryPhysicalCountResponse:
        """Returns the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ object with the provided
        ``physical_count_id``.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_inventory_physical_count(
                physical_count_id, request_options=request_options
            )
        ).unwrap()

    async def update_inventory_adjustment(
        self,
        body: UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInventoryAdjustmentResponse:
        """Applies an update to the provided adjustment.

        On success: returns the newly updated adjustment. On failure: returns a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_inventory_adjustment(body, request_options=request_options)
        ).unwrap()

    async def update_inventory_adjustment_reason(
        self,
        body: UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInventoryAdjustmentReasonResponse:
        """Updates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_inventory_adjustment_reason(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInventoryWithRawResponse:
        return self._with_raw_response


class InventoryWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchChangeInventoryResponse, RawError]:
        """Applies adjustments and counts to the provided item quantities.

        On success: returns the current calculated counts for all objects referenced in the request. On failure: returns
        a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/changes/batch-create"),
            body=json_body[BatchChangeInventoryRequest | BatchChangeInventoryRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchChangeInventoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryChangesResponse, RawError]:
        """Returns historical physical counts and adjustments based on the provided filter criteria.

        Results are paginated and sorted in ascending order according their ``occurred_at`` timestamp (oldest first).

        BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler
        endpoints.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/changes/batch-retrieve"),
            body=json_body[BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryChangesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryCountsResponse, RawError]:
        """Returns current counts for the provided `CatalogObject <entity:CatalogObject>`__s at the requested `Location
        <entity:Location>`__s.

        Results are paginated and sorted in descending order according to their ``calculated_at`` timestamp (newest
        first).

        When ``updated_after`` is specified, only counts that have changed since that time (based on the server
        timestamp for the most recent change) are returned. This allows clients to perform a "sync" operation, for
        example in response to receiving a Webhook notification.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/counts/batch-retrieve"),
            body=json_body[BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryCountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_inventory_adjustment_reason(
        self,
        body: CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInventoryAdjustmentReasonResponse, RawError]:
        """Creates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/create"),
            body=json_body[CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_inventory_adjustment_reason(
        self,
        body: DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeleteInventoryAdjustmentReasonResponse, RawError]:
        """Soft deletes a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/delete"),
            body=json_body[DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deprecated_batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchChangeInventoryResponse, RawError]:
        """Deprecated version of `BatchChangeInventory <api-endpoint:Inventory-BatchChangeInventory>`__ after the
        endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/batch-change"),
            body=json_body[BatchChangeInventoryRequest | BatchChangeInventoryRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchChangeInventoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deprecated_batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryChangesResponse, RawError]:
        """Deprecated version of `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/batch-retrieve-changes"),
            body=json_body[BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryChangesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deprecated_batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryCountsResponse, RawError]:
        """Deprecated version of `BatchRetrieveInventoryCounts <api-endpoint:Inventory-BatchRetrieveInventoryCounts>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/batch-retrieve-counts"),
            body=json_body[BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryCountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deprecated_retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryAdjustmentResponse, RawError]:
        """Deprecated version of `RetrieveInventoryAdjustment <api-endpoint:Inventory-RetrieveInventoryAdjustment>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/adjustment/{adjustment_id}"),
            path_params=[param[str]("adjustment_id", adjustment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryAdjustmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def deprecated_retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]:
        """Deprecated version of `RetrieveInventoryPhysicalCount
        <api-endpoint:Inventory-RetrieveInventoryPhysicalCount>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/physical-count/{physical_count_id}"),
            path_params=[param[str]("physical_count_id", physical_count_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryPhysicalCountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_inventory_adjustment_reasons(
        self,
        *,
        include_deleted: bool | None = False,
        include_system_codes: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInventoryAdjustmentReasonsResponse, RawError]:
        """Returns the standard and custom inventory adjustment reasons available to the seller.

        Args:
            include_deleted: Indicates whether the response should include deleted custom inventory adjustment reasons.
                The default value is ``false``.
            include_system_codes: Indicates whether the response should include Square-generated system inventory
                adjustment reason codes that cannot be used to write adjustments from the Connect API, such as ``SALE``,
                ``RECOUNT``, ``TRANSFER``, ``IN_TRANSIT``, and ``CANCELED_SALE``. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/adjustment-reasons"),
            query_params=[
                param[bool | None]("include_deleted", include_deleted),
                param[bool | None]("include_system_codes", include_system_codes),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListInventoryAdjustmentReasonsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def restore_inventory_adjustment_reason(
        self,
        body: RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RestoreInventoryAdjustmentReasonResponse, RawError]:
        """Restores a soft-deleted custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/restore"),
            body=json_body[RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RestoreInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryAdjustmentResponse, RawError]:
        """Returns the `InventoryAdjustment <entity:InventoryAdjustment>`__ object with the provided ``adjustment_id``.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/adjustments/{adjustment_id}"),
            path_params=[param[str]("adjustment_id", adjustment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryAdjustmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_inventory_adjustment_reason(
        self,
        body: RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveInventoryAdjustmentReasonResponse, RawError]:
        """Returns the inventory adjustment reason identified by the provided ``reason_id``. Deleted custom reasons can
        be retrieved by ID.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/retrieve"),
            body=json_body[RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_inventory_changes(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveInventoryChangesResponse, RawError]:
        """Returns a set of physical counts and inventory adjustments for the provided `CatalogObject
        <entity:CatalogObject>`__ at the requested `Location <entity:Location>`__s.

        You can achieve the same result by calling `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ and having the ``catalog_object_ids`` list contain a
        single element of the ``CatalogObject`` ID.

        Results are paginated and sorted in descending order according to their ``occurred_at`` timestamp (newest
        first).

        There are no limits on how far back the caller can page. This endpoint can be used to display recent changes for
        a specific item. For more sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/{catalog_object_id}/changes"),
            path_params=[param[str]("catalog_object_id", catalog_object_id)],
            query_params=[param[str | None]("location_ids", location_ids), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryChangesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_inventory_count(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveInventoryCountResponse, RawError]:
        """Retrieves the current calculated stock count for a given `CatalogObject <entity:CatalogObject>`__ at a given
        set of `Location <entity:Location>`__s. Responses are paginated and unsorted. For more sophisticated queries,
        use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/{catalog_object_id}"),
            path_params=[param[str]("catalog_object_id", catalog_object_id)],
            query_params=[param[str | None]("location_ids", location_ids), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryCountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]:
        """Returns the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ object with the provided
        ``physical_count_id``.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/physical-counts/{physical_count_id}"),
            path_params=[param[str]("physical_count_id", physical_count_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryPhysicalCountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_inventory_adjustment(
        self,
        body: UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInventoryAdjustmentResponse, RawError]:
        """Applies an update to the provided adjustment.

        On success: returns the newly updated adjustment. On failure: returns a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/inventory/adjustments/update"),
            body=json_body[UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateInventoryAdjustmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_inventory_adjustment_reason(
        self,
        body: UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInventoryAdjustmentReasonResponse, RawError]:
        """Updates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/update"),
            body=json_body[UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInventoryWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchChangeInventoryResponse, RawError]:
        """Applies adjustments and counts to the provided item quantities.

        On success: returns the current calculated counts for all objects referenced in the request. On failure: returns
        a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/changes/batch-create"),
            body=json_body[BatchChangeInventoryRequest | BatchChangeInventoryRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchChangeInventoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryChangesResponse, RawError]:
        """Returns historical physical counts and adjustments based on the provided filter criteria.

        Results are paginated and sorted in ascending order according their ``occurred_at`` timestamp (oldest first).

        BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler
        endpoints.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/changes/batch-retrieve"),
            body=json_body[BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryChangesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryCountsResponse, RawError]:
        """Returns current counts for the provided `CatalogObject <entity:CatalogObject>`__s at the requested `Location
        <entity:Location>`__s.

        Results are paginated and sorted in descending order according to their ``calculated_at`` timestamp (newest
        first).

        When ``updated_after`` is specified, only counts that have changed since that time (based on the server
        timestamp for the most recent change) are returned. This allows clients to perform a "sync" operation, for
        example in response to receiving a Webhook notification.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/counts/batch-retrieve"),
            body=json_body[BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryCountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_inventory_adjustment_reason(
        self,
        body: CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInventoryAdjustmentReasonResponse, RawError]:
        """Creates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/create"),
            body=json_body[CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_inventory_adjustment_reason(
        self,
        body: DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DeleteInventoryAdjustmentReasonResponse, RawError]:
        """Soft deletes a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/delete"),
            body=json_body[DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deprecated_batch_change_inventory(
        self,
        body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchChangeInventoryResponse, RawError]:
        """Deprecated version of `BatchChangeInventory <api-endpoint:Inventory-BatchChangeInventory>`__ after the
        endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/batch-change"),
            body=json_body[BatchChangeInventoryRequest | BatchChangeInventoryRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchChangeInventoryResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deprecated_batch_retrieve_inventory_changes(
        self,
        body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryChangesResponse, RawError]:
        """Deprecated version of `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/batch-retrieve-changes"),
            body=json_body[BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryChangesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deprecated_batch_retrieve_inventory_counts(
        self,
        body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BatchRetrieveInventoryCountsResponse, RawError]:
        """Deprecated version of `BatchRetrieveInventoryCounts <api-endpoint:Inventory-BatchRetrieveInventoryCounts>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/batch-retrieve-counts"),
            body=json_body[BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BatchRetrieveInventoryCountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deprecated_retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryAdjustmentResponse, RawError]:
        """Deprecated version of `RetrieveInventoryAdjustment <api-endpoint:Inventory-RetrieveInventoryAdjustment>`__
        after the endpoint URL is updated to conform to the standard convention.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/adjustment/{adjustment_id}"),
            path_params=[param[str]("adjustment_id", adjustment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryAdjustmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def deprecated_retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]:
        """Deprecated version of `RetrieveInventoryPhysicalCount
        <api-endpoint:Inventory-RetrieveInventoryPhysicalCount>`__ after the endpoint URL is updated to conform to the
        standard convention.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/physical-count/{physical_count_id}"),
            path_params=[param[str]("physical_count_id", physical_count_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryPhysicalCountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_inventory_adjustment_reasons(
        self,
        *,
        include_deleted: bool | None = False,
        include_system_codes: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInventoryAdjustmentReasonsResponse, RawError]:
        """Returns the standard and custom inventory adjustment reasons available to the seller.

        Args:
            include_deleted: Indicates whether the response should include deleted custom inventory adjustment reasons.
                The default value is ``false``.
            include_system_codes: Indicates whether the response should include Square-generated system inventory
                adjustment reason codes that cannot be used to write adjustments from the Connect API, such as ``SALE``,
                ``RECOUNT``, ``TRANSFER``, ``IN_TRANSIT``, and ``CANCELED_SALE``. The default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/adjustment-reasons"),
            query_params=[
                param[bool | None]("include_deleted", include_deleted),
                param[bool | None]("include_system_codes", include_system_codes),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListInventoryAdjustmentReasonsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def restore_inventory_adjustment_reason(
        self,
        body: RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RestoreInventoryAdjustmentReasonResponse, RawError]:
        """Restores a soft-deleted custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/restore"),
            body=json_body[RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RestoreInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_inventory_adjustment(
        self, adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryAdjustmentResponse, RawError]:
        """Returns the `InventoryAdjustment <entity:InventoryAdjustment>`__ object with the provided ``adjustment_id``.

        Args:
            adjustment_id: ID of the `InventoryAdjustment <entity:InventoryAdjustment>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/adjustments/{adjustment_id}"),
            path_params=[param[str]("adjustment_id", adjustment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryAdjustmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_inventory_adjustment_reason(
        self,
        body: RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveInventoryAdjustmentReasonResponse, RawError]:
        """Returns the inventory adjustment reason identified by the provided ``reason_id``. Deleted custom reasons can
        be retrieved by ID.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/retrieve"),
            body=json_body[RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict](
                body
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_inventory_changes(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveInventoryChangesResponse, RawError]:
        """Returns a set of physical counts and inventory adjustments for the provided `CatalogObject
        <entity:CatalogObject>`__ at the requested `Location <entity:Location>`__s.

        You can achieve the same result by calling `BatchRetrieveInventoryChanges
        <api-endpoint:Inventory-BatchRetrieveInventoryChanges>`__ and having the ``catalog_object_ids`` list contain a
        single element of the ``CatalogObject`` ID.

        Results are paginated and sorted in descending order according to their ``occurred_at`` timestamp (newest
        first).

        There are no limits on how far back the caller can page. This endpoint can be used to display recent changes for
        a specific item. For more sophisticated queries, use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/{catalog_object_id}/changes"),
            path_params=[param[str]("catalog_object_id", catalog_object_id)],
            query_params=[param[str | None]("location_ids", location_ids), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryChangesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_inventory_count(
        self,
        catalog_object_id: str,
        *,
        location_ids: str | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RetrieveInventoryCountResponse, RawError]:
        """Retrieves the current calculated stock count for a given `CatalogObject <entity:CatalogObject>`__ at a given
        set of `Location <entity:Location>`__s. Responses are paginated and unsorted. For more sophisticated queries,
        use a batch endpoint.

        Args:
            catalog_object_id: ID of the `CatalogObject <entity:CatalogObject>`__ to retrieve.
            location_ids: The `Location <entity:Location>`__ IDs to look up as a comma-separated list. An empty list
                queries all locations.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for the original query. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/{catalog_object_id}"),
            path_params=[param[str]("catalog_object_id", catalog_object_id)],
            query_params=[param[str | None]("location_ids", location_ids), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryCountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_inventory_physical_count(
        self, physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]:
        """Returns the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ object with the provided
        ``physical_count_id``.

        Args:
            physical_count_id: ID of the `InventoryPhysicalCount <entity:InventoryPhysicalCount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/inventory/physical-counts/{physical_count_id}"),
            path_params=[param[str]("physical_count_id", physical_count_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveInventoryPhysicalCountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_inventory_adjustment(
        self,
        body: UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInventoryAdjustmentResponse, RawError]:
        """Applies an update to the provided adjustment.

        On success: returns the newly updated adjustment. On failure: returns a list of related errors.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/inventory/adjustments/update"),
            body=json_body[UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateInventoryAdjustmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_inventory_adjustment_reason(
        self,
        body: UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInventoryAdjustmentReasonResponse, RawError]:
        """Updates a custom inventory adjustment reason.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/inventory/adjustment-reasons/update"),
            body=json_body[UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateInventoryAdjustmentReasonResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
