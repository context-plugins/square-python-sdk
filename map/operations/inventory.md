<!-- Generated file — do not edit; regenerated with the SDK. -->

# Inventory — operations

Accessor: `client.inventory` · Source: `square/apis/inventory.py` · 19 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.inventory.batch_change_inventory

- **Route**: `POST /v2/inventory/changes/batch-create`
- **Signature**: `def batch_change_inventory(body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchChangeInventoryResponse`
- **Returns (raw)**: `ApiResult[BatchChangeInventoryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchChangeInventoryRequest` | `square/models/batch_change_inventory_request.py` |
| `BatchChangeInventoryRequestDict` | `square/models/batch_change_inventory_request.py` |
| `BatchChangeInventoryResponse` | `square/models/batch_change_inventory_response.py` |

### client.inventory.batch_retrieve_inventory_changes

- **Route**: `POST /v2/inventory/changes/batch-retrieve`
- **Signature**: `def batch_retrieve_inventory_changes(body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchRetrieveInventoryChangesResponse`
- **Returns (raw)**: `ApiResult[BatchRetrieveInventoryChangesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchRetrieveInventoryChangesRequest` | `square/models/batch_retrieve_inventory_changes_request.py` |
| `BatchRetrieveInventoryChangesRequestDict` | `square/models/batch_retrieve_inventory_changes_request.py` |
| `BatchRetrieveInventoryChangesResponse` | `square/models/batch_retrieve_inventory_changes_response.py` |

### client.inventory.batch_retrieve_inventory_counts

- **Route**: `POST /v2/inventory/counts/batch-retrieve`
- **Signature**: `def batch_retrieve_inventory_counts(body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchRetrieveInventoryCountsResponse`
- **Returns (raw)**: `ApiResult[BatchRetrieveInventoryCountsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchRetrieveInventoryCountsRequest` | `square/models/batch_retrieve_inventory_counts_request.py` |
| `BatchRetrieveInventoryCountsRequestDict` | `square/models/batch_retrieve_inventory_counts_request.py` |
| `BatchRetrieveInventoryCountsResponse` | `square/models/batch_retrieve_inventory_counts_response.py` |

### client.inventory.create_inventory_adjustment_reason

- **Route**: `POST /v2/inventory/adjustment-reasons/create`
- **Signature**: `def create_inventory_adjustment_reason(body: CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateInventoryAdjustmentReasonResponse`
- **Returns (raw)**: `ApiResult[CreateInventoryAdjustmentReasonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateInventoryAdjustmentReasonRequest` | `square/models/create_inventory_adjustment_reason_request.py` |
| `CreateInventoryAdjustmentReasonRequestDict` | `square/models/create_inventory_adjustment_reason_request.py` |
| `CreateInventoryAdjustmentReasonResponse` | `square/models/create_inventory_adjustment_reason_response.py` |

### client.inventory.delete_inventory_adjustment_reason

- **Route**: `POST /v2/inventory/adjustment-reasons/delete`
- **Signature**: `def delete_inventory_adjustment_reason(body: DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `DeleteInventoryAdjustmentReasonResponse`
- **Returns (raw)**: `ApiResult[DeleteInventoryAdjustmentReasonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteInventoryAdjustmentReasonRequest` | `square/models/delete_inventory_adjustment_reason_request.py` |
| `DeleteInventoryAdjustmentReasonRequestDict` | `square/models/delete_inventory_adjustment_reason_request.py` |
| `DeleteInventoryAdjustmentReasonResponse` | `square/models/delete_inventory_adjustment_reason_response.py` |

### client.inventory.deprecated_batch_change_inventory

- **Route**: `POST /v2/inventory/batch-change`
- **Signature**: `def deprecated_batch_change_inventory(body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchChangeInventoryResponse`
- **Returns (raw)**: `ApiResult[BatchChangeInventoryResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchChangeInventoryRequest` | `square/models/batch_change_inventory_request.py` |
| `BatchChangeInventoryRequestDict` | `square/models/batch_change_inventory_request.py` |
| `BatchChangeInventoryResponse` | `square/models/batch_change_inventory_response.py` |

### client.inventory.deprecated_batch_retrieve_inventory_changes

- **Route**: `POST /v2/inventory/batch-retrieve-changes`
- **Signature**: `def deprecated_batch_retrieve_inventory_changes(body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchRetrieveInventoryChangesResponse`
- **Returns (raw)**: `ApiResult[BatchRetrieveInventoryChangesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchRetrieveInventoryChangesRequest` | `square/models/batch_retrieve_inventory_changes_request.py` |
| `BatchRetrieveInventoryChangesRequestDict` | `square/models/batch_retrieve_inventory_changes_request.py` |
| `BatchRetrieveInventoryChangesResponse` | `square/models/batch_retrieve_inventory_changes_response.py` |

### client.inventory.deprecated_batch_retrieve_inventory_counts

- **Route**: `POST /v2/inventory/batch-retrieve-counts`
- **Signature**: `def deprecated_batch_retrieve_inventory_counts(body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchRetrieveInventoryCountsResponse`
- **Returns (raw)**: `ApiResult[BatchRetrieveInventoryCountsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchRetrieveInventoryCountsRequest` | `square/models/batch_retrieve_inventory_counts_request.py` |
| `BatchRetrieveInventoryCountsRequestDict` | `square/models/batch_retrieve_inventory_counts_request.py` |
| `BatchRetrieveInventoryCountsResponse` | `square/models/batch_retrieve_inventory_counts_response.py` |

### client.inventory.deprecated_retrieve_inventory_adjustment

- **Route**: `GET /v2/inventory/adjustment/{adjustment_id}`
- **Signature**: `def deprecated_retrieve_inventory_adjustment(adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `adjustment_id`
- **Params**: `adjustment_id` — path
- **Returns (parsed)**: `RetrieveInventoryAdjustmentResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryAdjustmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryAdjustmentResponse` | `square/models/retrieve_inventory_adjustment_response.py` |

### client.inventory.deprecated_retrieve_inventory_physical_count

- **Route**: `GET /v2/inventory/physical-count/{physical_count_id}`
- **Signature**: `def deprecated_retrieve_inventory_physical_count(physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `physical_count_id`
- **Params**: `physical_count_id` — path
- **Returns (parsed)**: `RetrieveInventoryPhysicalCountResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryPhysicalCountResponse` | `square/models/retrieve_inventory_physical_count_response.py` |

### client.inventory.list_inventory_adjustment_reasons

- **Route**: `GET /v2/inventory/adjustment-reasons`
- **Signature**: `def list_inventory_adjustment_reasons(*, include_deleted: bool | None = False, include_system_codes: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `include_deleted` — query · `include_system_codes` — query
- **Returns (parsed)**: `ListInventoryAdjustmentReasonsResponse`
- **Returns (raw)**: `ApiResult[ListInventoryAdjustmentReasonsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInventoryAdjustmentReasonsResponse` | `square/models/list_inventory_adjustment_reasons_response.py` |

### client.inventory.restore_inventory_adjustment_reason

- **Route**: `POST /v2/inventory/adjustment-reasons/restore`
- **Signature**: `def restore_inventory_adjustment_reason(body: RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RestoreInventoryAdjustmentReasonResponse`
- **Returns (raw)**: `ApiResult[RestoreInventoryAdjustmentReasonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RestoreInventoryAdjustmentReasonRequest` | `square/models/restore_inventory_adjustment_reason_request.py` |
| `RestoreInventoryAdjustmentReasonRequestDict` | `square/models/restore_inventory_adjustment_reason_request.py` |
| `RestoreInventoryAdjustmentReasonResponse` | `square/models/restore_inventory_adjustment_reason_response.py` |

### client.inventory.retrieve_inventory_adjustment

- **Route**: `GET /v2/inventory/adjustments/{adjustment_id}`
- **Signature**: `def retrieve_inventory_adjustment(adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `adjustment_id`
- **Params**: `adjustment_id` — path
- **Returns (parsed)**: `RetrieveInventoryAdjustmentResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryAdjustmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryAdjustmentResponse` | `square/models/retrieve_inventory_adjustment_response.py` |

### client.inventory.retrieve_inventory_adjustment_reason

- **Route**: `POST /v2/inventory/adjustment-reasons/retrieve`
- **Signature**: `def retrieve_inventory_adjustment_reason(body: RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RetrieveInventoryAdjustmentReasonResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryAdjustmentReasonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryAdjustmentReasonRequest` | `square/models/retrieve_inventory_adjustment_reason_request.py` |
| `RetrieveInventoryAdjustmentReasonRequestDict` | `square/models/retrieve_inventory_adjustment_reason_request.py` |
| `RetrieveInventoryAdjustmentReasonResponse` | `square/models/retrieve_inventory_adjustment_reason_response.py` |

### client.inventory.retrieve_inventory_changes

- **Route**: `GET /v2/inventory/{catalog_object_id}/changes`
- **Signature**: `def retrieve_inventory_changes(catalog_object_id: str, *, location_ids: str | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `catalog_object_id`
- **Params**: `catalog_object_id` — path · `location_ids` — query · `cursor` — query
- **Returns (parsed)**: `RetrieveInventoryChangesResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryChangesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryChangesResponse` | `square/models/retrieve_inventory_changes_response.py` |

### client.inventory.retrieve_inventory_count

- **Route**: `GET /v2/inventory/{catalog_object_id}`
- **Signature**: `def retrieve_inventory_count(catalog_object_id: str, *, location_ids: str | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `catalog_object_id`
- **Params**: `catalog_object_id` — path · `location_ids` — query · `cursor` — query
- **Returns (parsed)**: `RetrieveInventoryCountResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryCountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryCountResponse` | `square/models/retrieve_inventory_count_response.py` |

### client.inventory.retrieve_inventory_physical_count

- **Route**: `GET /v2/inventory/physical-counts/{physical_count_id}`
- **Signature**: `def retrieve_inventory_physical_count(physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `physical_count_id`
- **Params**: `physical_count_id` — path
- **Returns (parsed)**: `RetrieveInventoryPhysicalCountResponse`
- **Returns (raw)**: `ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveInventoryPhysicalCountResponse` | `square/models/retrieve_inventory_physical_count_response.py` |

### client.inventory.update_inventory_adjustment

- **Route**: `PUT /v2/inventory/adjustments/update`
- **Signature**: `def update_inventory_adjustment(body: UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateInventoryAdjustmentResponse`
- **Returns (raw)**: `ApiResult[UpdateInventoryAdjustmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateInventoryAdjustmentRequest` | `square/models/update_inventory_adjustment_request.py` |
| `UpdateInventoryAdjustmentRequestDict` | `square/models/update_inventory_adjustment_request.py` |
| `UpdateInventoryAdjustmentResponse` | `square/models/update_inventory_adjustment_response.py` |

### client.inventory.update_inventory_adjustment_reason

- **Route**: `PUT /v2/inventory/adjustment-reasons/update`
- **Signature**: `def update_inventory_adjustment_reason(body: UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateInventoryAdjustmentReasonResponse`
- **Returns (raw)**: `ApiResult[UpdateInventoryAdjustmentReasonResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateInventoryAdjustmentReasonRequest` | `square/models/update_inventory_adjustment_reason_request.py` |
| `UpdateInventoryAdjustmentReasonRequestDict` | `square/models/update_inventory_adjustment_reason_request.py` |
| `UpdateInventoryAdjustmentReasonResponse` | `square/models/update_inventory_adjustment_reason_response.py` |

