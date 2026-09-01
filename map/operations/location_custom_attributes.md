<!-- Generated file — do not edit; regenerated with the SDK. -->

# LocationCustomAttributes — operations

Accessor: `client.location_custom_attributes` · Source: `square/apis/location_custom_attributes.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.location_custom_attributes.bulk_delete_location_custom_attributes

- **Route**: `POST /v2/locations/custom-attributes/bulk-delete`
- **Auth**: `oauth2`
- **Signature**: `def bulk_delete_location_custom_attributes(body: BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkDeleteLocationCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkDeleteLocationCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkDeleteLocationCustomAttributesRequest` | `square/models/bulk_delete_location_custom_attributes_request.py` |
| `BulkDeleteLocationCustomAttributesRequestDict` | `square/models/bulk_delete_location_custom_attributes_request.py` |
| `BulkDeleteLocationCustomAttributesResponse` | `square/models/bulk_delete_location_custom_attributes_response.py` |

### client.location_custom_attributes.bulk_upsert_location_custom_attributes

- **Route**: `POST /v2/locations/custom-attributes/bulk-upsert`
- **Auth**: `oauth2`
- **Signature**: `def bulk_upsert_location_custom_attributes(body: BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpsertLocationCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkUpsertLocationCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpsertLocationCustomAttributesRequest` | `square/models/bulk_upsert_location_custom_attributes_request.py` |
| `BulkUpsertLocationCustomAttributesRequestDict` | `square/models/bulk_upsert_location_custom_attributes_request.py` |
| `BulkUpsertLocationCustomAttributesResponse` | `square/models/bulk_upsert_location_custom_attributes_response.py` |

### client.location_custom_attributes.create_location_custom_attribute_definition

- **Route**: `POST /v2/locations/custom-attribute-definitions`
- **Auth**: `oauth2`
- **Signature**: `def create_location_custom_attribute_definition(body: CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateLocationCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[CreateLocationCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateLocationCustomAttributeDefinitionRequest` | `square/models/create_location_custom_attribute_definition_request.py` |
| `CreateLocationCustomAttributeDefinitionRequestDict` | `square/models/create_location_custom_attribute_definition_request.py` |
| `CreateLocationCustomAttributeDefinitionResponse` | `square/models/create_location_custom_attribute_definition_response.py` |

### client.location_custom_attributes.delete_location_custom_attribute

- **Route**: `DELETE /v2/locations/{location_id}/custom-attributes/{key}`
- **Auth**: `oauth2`
- **Signature**: `def delete_location_custom_attribute(location_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `key`
- **Params**: `location_id` — path · `key` — path
- **Returns (parsed)**: `DeleteLocationCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[DeleteLocationCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteLocationCustomAttributeResponse` | `square/models/delete_location_custom_attribute_response.py` |

### client.location_custom_attributes.delete_location_custom_attribute_definition

- **Route**: `DELETE /v2/locations/custom-attribute-definitions/{key}`
- **Auth**: `oauth2`
- **Signature**: `def delete_location_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path
- **Returns (parsed)**: `DeleteLocationCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[DeleteLocationCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteLocationCustomAttributeDefinitionResponse` | `square/models/delete_location_custom_attribute_definition_response.py` |

### client.location_custom_attributes.list_location_custom_attribute_definitions

- **Route**: `GET /v2/locations/custom-attribute-definitions`
- **Auth**: `oauth2`
- **Signature**: `def list_location_custom_attribute_definitions(*, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `visibility_filter` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListLocationCustomAttributeDefinitionsResponse`
- **Returns (raw)**: `ApiResult[ListLocationCustomAttributeDefinitionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisibilityFilterOrStr` | `square/models/enums/visibility_filter.py` |
| `ListLocationCustomAttributeDefinitionsResponse` | `square/models/list_location_custom_attribute_definitions_response.py` |

### client.location_custom_attributes.list_location_custom_attributes

- **Route**: `GET /v2/locations/{location_id}/custom-attributes`
- **Auth**: `oauth2`
- **Signature**: `def list_location_custom_attributes(location_id: str, *, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — path · `visibility_filter` — query · `limit` — query · `cursor` — query · `with_definitions` — query
- **Returns (parsed)**: `ListLocationCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[ListLocationCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VisibilityFilterOrStr` | `square/models/enums/visibility_filter.py` |
| `ListLocationCustomAttributesResponse` | `square/models/list_location_custom_attributes_response.py` |

### client.location_custom_attributes.retrieve_location_custom_attribute

- **Route**: `GET /v2/locations/{location_id}/custom-attributes/{key}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_location_custom_attribute(location_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `key`
- **Params**: `location_id` — path · `key` — path · `with_definition` — query · `version` — query
- **Returns (parsed)**: `RetrieveLocationCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[RetrieveLocationCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLocationCustomAttributeResponse` | `square/models/retrieve_location_custom_attribute_response.py` |

### client.location_custom_attributes.retrieve_location_custom_attribute_definition

- **Route**: `GET /v2/locations/custom-attribute-definitions/{key}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_location_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path · `version` — query
- **Returns (parsed)**: `RetrieveLocationCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[RetrieveLocationCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLocationCustomAttributeDefinitionResponse` | `square/models/retrieve_location_custom_attribute_definition_response.py` |

### client.location_custom_attributes.update_location_custom_attribute_definition

- **Route**: `PUT /v2/locations/custom-attribute-definitions/{key}`
- **Auth**: `oauth2`
- **Signature**: `def update_location_custom_attribute_definition(key: str, body: UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`, `body`
- **Params**: `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateLocationCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[UpdateLocationCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateLocationCustomAttributeDefinitionRequest` | `square/models/update_location_custom_attribute_definition_request.py` |
| `UpdateLocationCustomAttributeDefinitionRequestDict` | `square/models/update_location_custom_attribute_definition_request.py` |
| `UpdateLocationCustomAttributeDefinitionResponse` | `square/models/update_location_custom_attribute_definition_response.py` |

### client.location_custom_attributes.upsert_location_custom_attribute

- **Route**: `POST /v2/locations/{location_id}/custom-attributes/{key}`
- **Auth**: `oauth2`
- **Signature**: `def upsert_location_custom_attribute(location_id: str, key: str, body: UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `key`, `body`
- **Params**: `location_id` — path · `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpsertLocationCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[UpsertLocationCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertLocationCustomAttributeRequest` | `square/models/upsert_location_custom_attribute_request.py` |
| `UpsertLocationCustomAttributeRequestDict` | `square/models/upsert_location_custom_attribute_request.py` |
| `UpsertLocationCustomAttributeResponse` | `square/models/upsert_location_custom_attribute_response.py` |

