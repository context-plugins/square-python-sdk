<!-- Generated file — do not edit; regenerated with the SDK. -->

# OrderCustomAttributes — operations

Accessor: `client.order_custom_attributes` · Source: `square/apis/order_custom_attributes.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.order_custom_attributes.bulk_delete_order_custom_attributes

- **Route**: `POST /v2/orders/custom-attributes/bulk-delete`
- **Signature**: `def bulk_delete_order_custom_attributes(body: BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkDeleteOrderCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkDeleteOrderCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkDeleteOrderCustomAttributesRequest` | `square/models/bulk_delete_order_custom_attributes_request.py` |
| `BulkDeleteOrderCustomAttributesRequestDict` | `square/models/bulk_delete_order_custom_attributes_request.py` |
| `BulkDeleteOrderCustomAttributesResponse` | `square/models/bulk_delete_order_custom_attributes_response.py` |

### client.order_custom_attributes.bulk_upsert_order_custom_attributes

- **Route**: `POST /v2/orders/custom-attributes/bulk-upsert`
- **Signature**: `def bulk_upsert_order_custom_attributes(body: BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpsertOrderCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkUpsertOrderCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpsertOrderCustomAttributesRequest` | `square/models/bulk_upsert_order_custom_attributes_request.py` |
| `BulkUpsertOrderCustomAttributesRequestDict` | `square/models/bulk_upsert_order_custom_attributes_request.py` |
| `BulkUpsertOrderCustomAttributesResponse` | `square/models/bulk_upsert_order_custom_attributes_response.py` |

### client.order_custom_attributes.create_order_custom_attribute_definition

- **Route**: `POST /v2/orders/custom-attribute-definitions`
- **Signature**: `def create_order_custom_attribute_definition(body: CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateOrderCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[CreateOrderCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateOrderCustomAttributeDefinitionRequest` | `square/models/create_order_custom_attribute_definition_request.py` |
| `CreateOrderCustomAttributeDefinitionRequestDict` | `square/models/create_order_custom_attribute_definition_request.py` |
| `CreateOrderCustomAttributeDefinitionResponse` | `square/models/create_order_custom_attribute_definition_response.py` |

### client.order_custom_attributes.delete_order_custom_attribute

- **Route**: `DELETE /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}`
- **Signature**: `def delete_order_custom_attribute(order_id: str, custom_attribute_key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `custom_attribute_key`
- **Params**: `order_id` — path · `custom_attribute_key` — path
- **Returns (parsed)**: `DeleteOrderCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[DeleteOrderCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteOrderCustomAttributeResponse` | `square/models/delete_order_custom_attribute_response.py` |

### client.order_custom_attributes.delete_order_custom_attribute_definition

- **Route**: `DELETE /v2/orders/custom-attribute-definitions/{key}`
- **Signature**: `def delete_order_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path
- **Returns (parsed)**: `DeleteOrderCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[DeleteOrderCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteOrderCustomAttributeDefinitionResponse` | `square/models/delete_order_custom_attribute_definition_response.py` |

### client.order_custom_attributes.list_order_custom_attribute_definitions

- **Route**: `GET /v2/orders/custom-attribute-definitions`
- **Signature**: `def list_order_custom_attribute_definitions(*, visibility_filter: VisibilityFilterOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `visibility_filter` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListOrderCustomAttributeDefinitionsResponse`
- **Returns (raw)**: `ApiResult[ListOrderCustomAttributeDefinitionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisibilityFilterOrStr` | `square/models/enums/visibility_filter.py` |
| `ListOrderCustomAttributeDefinitionsResponse` | `square/models/list_order_custom_attribute_definitions_response.py` |

### client.order_custom_attributes.list_order_custom_attributes

- **Route**: `GET /v2/orders/{order_id}/custom-attributes`
- **Signature**: `def list_order_custom_attributes(order_id: str, *, visibility_filter: VisibilityFilterOrStr | None = None, cursor: str | None = None, limit: int | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path · `visibility_filter` — query · `cursor` — query · `limit` — query · `with_definitions` — query
- **Returns (parsed)**: `ListOrderCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[ListOrderCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisibilityFilterOrStr` | `square/models/enums/visibility_filter.py` |
| `ListOrderCustomAttributesResponse` | `square/models/list_order_custom_attributes_response.py` |

### client.order_custom_attributes.retrieve_order_custom_attribute

- **Route**: `GET /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}`
- **Signature**: `def retrieve_order_custom_attribute(order_id: str, custom_attribute_key: str, *, version: int | None = None, with_definition: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `custom_attribute_key`
- **Params**: `order_id` — path · `custom_attribute_key` — path · `version` — query · `with_definition` — query
- **Returns (parsed)**: `RetrieveOrderCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[RetrieveOrderCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveOrderCustomAttributeResponse` | `square/models/retrieve_order_custom_attribute_response.py` |

### client.order_custom_attributes.retrieve_order_custom_attribute_definition

- **Route**: `GET /v2/orders/custom-attribute-definitions/{key}`
- **Signature**: `def retrieve_order_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path · `version` — query
- **Returns (parsed)**: `RetrieveOrderCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[RetrieveOrderCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveOrderCustomAttributeDefinitionResponse` | `square/models/retrieve_order_custom_attribute_definition_response.py` |

### client.order_custom_attributes.update_order_custom_attribute_definition

- **Route**: `PUT /v2/orders/custom-attribute-definitions/{key}`
- **Signature**: `def update_order_custom_attribute_definition(key: str, body: UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`, `body`
- **Params**: `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateOrderCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[UpdateOrderCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateOrderCustomAttributeDefinitionRequest` | `square/models/update_order_custom_attribute_definition_request.py` |
| `UpdateOrderCustomAttributeDefinitionRequestDict` | `square/models/update_order_custom_attribute_definition_request.py` |
| `UpdateOrderCustomAttributeDefinitionResponse` | `square/models/update_order_custom_attribute_definition_response.py` |

### client.order_custom_attributes.upsert_order_custom_attribute

- **Route**: `POST /v2/orders/{order_id}/custom-attributes/{custom_attribute_key}`
- **Signature**: `def upsert_order_custom_attribute(order_id: str, custom_attribute_key: str, body: UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `custom_attribute_key`, `body`
- **Params**: `order_id` — path · `custom_attribute_key` — path · `body` — JSON body
- **Returns (parsed)**: `UpsertOrderCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[UpsertOrderCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertOrderCustomAttributeRequest` | `square/models/upsert_order_custom_attribute_request.py` |
| `UpsertOrderCustomAttributeRequestDict` | `square/models/upsert_order_custom_attribute_request.py` |
| `UpsertOrderCustomAttributeResponse` | `square/models/upsert_order_custom_attribute_response.py` |

