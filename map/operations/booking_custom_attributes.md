<!-- Generated file — do not edit; regenerated with the SDK. -->

# BookingCustomAttributes — operations

Accessor: `client.booking_custom_attributes` · Source: `square/apis/booking_custom_attributes.py` · 11 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.booking_custom_attributes.bulk_delete_booking_custom_attributes

- **Route**: `POST /v2/bookings/custom-attributes/bulk-delete`
- **Auth**: `oauth2`
- **Signature**: `def bulk_delete_booking_custom_attributes(body: BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkDeleteBookingCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkDeleteBookingCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkDeleteBookingCustomAttributesRequest` | `square/models/bulk_delete_booking_custom_attributes_request.py` |
| `BulkDeleteBookingCustomAttributesRequestDict` | `square/models/bulk_delete_booking_custom_attributes_request.py` |
| `BulkDeleteBookingCustomAttributesResponse` | `square/models/bulk_delete_booking_custom_attributes_response.py` |

### client.booking_custom_attributes.bulk_upsert_booking_custom_attributes

- **Route**: `POST /v2/bookings/custom-attributes/bulk-upsert`
- **Auth**: `oauth2`
- **Signature**: `def bulk_upsert_booking_custom_attributes(body: BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpsertBookingCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkUpsertBookingCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpsertBookingCustomAttributesRequest` | `square/models/bulk_upsert_booking_custom_attributes_request.py` |
| `BulkUpsertBookingCustomAttributesRequestDict` | `square/models/bulk_upsert_booking_custom_attributes_request.py` |
| `BulkUpsertBookingCustomAttributesResponse` | `square/models/bulk_upsert_booking_custom_attributes_response.py` |

### client.booking_custom_attributes.create_booking_custom_attribute_definition

- **Route**: `POST /v2/bookings/custom-attribute-definitions`
- **Auth**: `oauth2`
- **Signature**: `def create_booking_custom_attribute_definition(body: CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateBookingCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[CreateBookingCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateBookingCustomAttributeDefinitionRequest` | `square/models/create_booking_custom_attribute_definition_request.py` |
| `CreateBookingCustomAttributeDefinitionRequestDict` | `square/models/create_booking_custom_attribute_definition_request.py` |
| `CreateBookingCustomAttributeDefinitionResponse` | `square/models/create_booking_custom_attribute_definition_response.py` |

### client.booking_custom_attributes.delete_booking_custom_attribute

- **Route**: `DELETE /v2/bookings/{booking_id}/custom-attributes/{key}`
- **Auth**: `oauth2`
- **Signature**: `def delete_booking_custom_attribute(booking_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`, `key`
- **Params**: `booking_id` — path · `key` — path
- **Returns (parsed)**: `DeleteBookingCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[DeleteBookingCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteBookingCustomAttributeResponse` | `square/models/delete_booking_custom_attribute_response.py` |

### client.booking_custom_attributes.delete_booking_custom_attribute_definition

- **Route**: `DELETE /v2/bookings/custom-attribute-definitions/{key}`
- **Auth**: `oauth2`
- **Signature**: `def delete_booking_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path
- **Returns (parsed)**: `DeleteBookingCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[DeleteBookingCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteBookingCustomAttributeDefinitionResponse` | `square/models/delete_booking_custom_attribute_definition_response.py` |

### client.booking_custom_attributes.list_booking_custom_attribute_definitions

- **Route**: `GET /v2/bookings/custom-attribute-definitions`
- **Auth**: `oauth2`
- **Signature**: `def list_booking_custom_attribute_definitions(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListBookingCustomAttributeDefinitionsResponse`
- **Returns (raw)**: `ApiResult[ListBookingCustomAttributeDefinitionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBookingCustomAttributeDefinitionsResponse` | `square/models/list_booking_custom_attribute_definitions_response.py` |

### client.booking_custom_attributes.list_booking_custom_attributes

- **Route**: `GET /v2/bookings/{booking_id}/custom-attributes`
- **Auth**: `oauth2`
- **Signature**: `def list_booking_custom_attributes(booking_id: str, *, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`
- **Params**: `booking_id` — path · `limit` — query · `cursor` — query · `with_definitions` — query
- **Returns (parsed)**: `ListBookingCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[ListBookingCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBookingCustomAttributesResponse` | `square/models/list_booking_custom_attributes_response.py` |

### client.booking_custom_attributes.retrieve_booking_custom_attribute

- **Route**: `GET /v2/bookings/{booking_id}/custom-attributes/{key}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_booking_custom_attribute(booking_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`, `key`
- **Params**: `booking_id` — path · `key` — path · `with_definition` — query · `version` — query
- **Returns (parsed)**: `RetrieveBookingCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[RetrieveBookingCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveBookingCustomAttributeResponse` | `square/models/retrieve_booking_custom_attribute_response.py` |

### client.booking_custom_attributes.retrieve_booking_custom_attribute_definition

- **Route**: `GET /v2/bookings/custom-attribute-definitions/{key}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_booking_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path · `version` — query
- **Returns (parsed)**: `RetrieveBookingCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[RetrieveBookingCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveBookingCustomAttributeDefinitionResponse` | `square/models/retrieve_booking_custom_attribute_definition_response.py` |

### client.booking_custom_attributes.update_booking_custom_attribute_definition

- **Route**: `PUT /v2/bookings/custom-attribute-definitions/{key}`
- **Auth**: `oauth2`
- **Signature**: `def update_booking_custom_attribute_definition(key: str, body: UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`, `body`
- **Params**: `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateBookingCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[UpdateBookingCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateBookingCustomAttributeDefinitionRequest` | `square/models/update_booking_custom_attribute_definition_request.py` |
| `UpdateBookingCustomAttributeDefinitionRequestDict` | `square/models/update_booking_custom_attribute_definition_request.py` |
| `UpdateBookingCustomAttributeDefinitionResponse` | `square/models/update_booking_custom_attribute_definition_response.py` |

### client.booking_custom_attributes.upsert_booking_custom_attribute

- **Route**: `PUT /v2/bookings/{booking_id}/custom-attributes/{key}`
- **Auth**: `oauth2`
- **Signature**: `def upsert_booking_custom_attribute(booking_id: str, key: str, body: UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`, `key`, `body`
- **Params**: `booking_id` — path · `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpsertBookingCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[UpsertBookingCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertBookingCustomAttributeRequest` | `square/models/upsert_booking_custom_attribute_request.py` |
| `UpsertBookingCustomAttributeRequestDict` | `square/models/upsert_booking_custom_attribute_request.py` |
| `UpsertBookingCustomAttributeResponse` | `square/models/upsert_booking_custom_attribute_response.py` |

