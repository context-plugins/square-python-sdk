<!-- Generated file — do not edit; regenerated with the SDK. -->

# MerchantCustomAttributes — operations

Accessor: `client.merchant_custom_attributes` · Source: `square/apis/merchant_custom_attributes.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.merchant_custom_attributes.bulk_delete_merchant_custom_attributes

- **Route**: `POST /v2/merchants/custom-attributes/bulk-delete`
- **Signature**: `def bulk_delete_merchant_custom_attributes(body: BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkDeleteMerchantCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkDeleteMerchantCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkDeleteMerchantCustomAttributesRequest` | `square/models/bulk_delete_merchant_custom_attributes_request.py` |
| `BulkDeleteMerchantCustomAttributesRequestDict` | `square/models/bulk_delete_merchant_custom_attributes_request.py` |
| `BulkDeleteMerchantCustomAttributesResponse` | `square/models/bulk_delete_merchant_custom_attributes_response.py` |

### client.merchant_custom_attributes.bulk_upsert_merchant_custom_attributes

- **Route**: `POST /v2/merchants/custom-attributes/bulk-upsert`
- **Signature**: `def bulk_upsert_merchant_custom_attributes(body: BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpsertMerchantCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkUpsertMerchantCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpsertMerchantCustomAttributesRequest` | `square/models/bulk_upsert_merchant_custom_attributes_request.py` |
| `BulkUpsertMerchantCustomAttributesRequestDict` | `square/models/bulk_upsert_merchant_custom_attributes_request.py` |
| `BulkUpsertMerchantCustomAttributesResponse` | `square/models/bulk_upsert_merchant_custom_attributes_response.py` |

### client.merchant_custom_attributes.create_merchant_custom_attribute_definition

- **Route**: `POST /v2/merchants/custom-attribute-definitions`
- **Signature**: `def create_merchant_custom_attribute_definition(body: CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateMerchantCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[CreateMerchantCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateMerchantCustomAttributeDefinitionRequest` | `square/models/create_merchant_custom_attribute_definition_request.py` |
| `CreateMerchantCustomAttributeDefinitionRequestDict` | `square/models/create_merchant_custom_attribute_definition_request.py` |
| `CreateMerchantCustomAttributeDefinitionResponse` | `square/models/create_merchant_custom_attribute_definition_response.py` |

### client.merchant_custom_attributes.delete_merchant_custom_attribute

- **Route**: `DELETE /v2/merchants/{merchant_id}/custom-attributes/{key}`
- **Signature**: `def delete_merchant_custom_attribute(merchant_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `key`
- **Params**: `merchant_id` — path · `key` — path
- **Returns (parsed)**: `DeleteMerchantCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[DeleteMerchantCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteMerchantCustomAttributeResponse` | `square/models/delete_merchant_custom_attribute_response.py` |

### client.merchant_custom_attributes.delete_merchant_custom_attribute_definition

- **Route**: `DELETE /v2/merchants/custom-attribute-definitions/{key}`
- **Signature**: `def delete_merchant_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path
- **Returns (parsed)**: `DeleteMerchantCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[DeleteMerchantCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteMerchantCustomAttributeDefinitionResponse` | `square/models/delete_merchant_custom_attribute_definition_response.py` |

### client.merchant_custom_attributes.list_merchant_custom_attribute_definitions

- **Route**: `GET /v2/merchants/custom-attribute-definitions`
- **Signature**: `def list_merchant_custom_attribute_definitions(*, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `visibility_filter` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListMerchantCustomAttributeDefinitionsResponse`
- **Returns (raw)**: `ApiResult[ListMerchantCustomAttributeDefinitionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisibilityFilterOrStr` | `square/models/enums/visibility_filter.py` |
| `ListMerchantCustomAttributeDefinitionsResponse` | `square/models/list_merchant_custom_attribute_definitions_response.py` |

### client.merchant_custom_attributes.list_merchant_custom_attributes

- **Route**: `GET /v2/merchants/{merchant_id}/custom-attributes`
- **Signature**: `def list_merchant_custom_attributes(merchant_id: str, *, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path · `visibility_filter` — query · `limit` — query · `cursor` — query · `with_definitions` — query
- **Returns (parsed)**: `ListMerchantCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[ListMerchantCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisibilityFilterOrStr` | `square/models/enums/visibility_filter.py` |
| `ListMerchantCustomAttributesResponse` | `square/models/list_merchant_custom_attributes_response.py` |

### client.merchant_custom_attributes.retrieve_merchant_custom_attribute

- **Route**: `GET /v2/merchants/{merchant_id}/custom-attributes/{key}`
- **Signature**: `def retrieve_merchant_custom_attribute(merchant_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `key`
- **Params**: `merchant_id` — path · `key` — path · `with_definition` — query · `version` — query
- **Returns (parsed)**: `RetrieveMerchantCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[RetrieveMerchantCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveMerchantCustomAttributeResponse` | `square/models/retrieve_merchant_custom_attribute_response.py` |

### client.merchant_custom_attributes.retrieve_merchant_custom_attribute_definition

- **Route**: `GET /v2/merchants/custom-attribute-definitions/{key}`
- **Signature**: `def retrieve_merchant_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path · `version` — query
- **Returns (parsed)**: `RetrieveMerchantCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[RetrieveMerchantCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveMerchantCustomAttributeDefinitionResponse` | `square/models/retrieve_merchant_custom_attribute_definition_response.py` |

### client.merchant_custom_attributes.update_merchant_custom_attribute_definition

- **Route**: `PUT /v2/merchants/custom-attribute-definitions/{key}`
- **Signature**: `def update_merchant_custom_attribute_definition(key: str, body: UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`, `body`
- **Params**: `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateMerchantCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[UpdateMerchantCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateMerchantCustomAttributeDefinitionRequest` | `square/models/update_merchant_custom_attribute_definition_request.py` |
| `UpdateMerchantCustomAttributeDefinitionRequestDict` | `square/models/update_merchant_custom_attribute_definition_request.py` |
| `UpdateMerchantCustomAttributeDefinitionResponse` | `square/models/update_merchant_custom_attribute_definition_response.py` |

### client.merchant_custom_attributes.upsert_merchant_custom_attribute

- **Route**: `POST /v2/merchants/{merchant_id}/custom-attributes/{key}`
- **Signature**: `def upsert_merchant_custom_attribute(merchant_id: str, key: str, body: UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`, `key`, `body`
- **Params**: `merchant_id` — path · `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpsertMerchantCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[UpsertMerchantCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertMerchantCustomAttributeRequest` | `square/models/upsert_merchant_custom_attribute_request.py` |
| `UpsertMerchantCustomAttributeRequestDict` | `square/models/upsert_merchant_custom_attribute_request.py` |
| `UpsertMerchantCustomAttributeResponse` | `square/models/upsert_merchant_custom_attribute_response.py` |

