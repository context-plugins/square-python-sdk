<!-- Generated file — do not edit; regenerated with the SDK. -->

# CustomerCustomAttributes — operations

Accessor: `client.customer_custom_attributes` · Source: `square/apis/customer_custom_attributes.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.customer_custom_attributes.bulk_upsert_customer_custom_attributes

- **Route**: `POST /v2/customers/custom-attributes/bulk-upsert`
- **Signature**: `def bulk_upsert_customer_custom_attributes(body: BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpsertCustomerCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[BulkUpsertCustomerCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpsertCustomerCustomAttributesRequest` | `square/models/bulk_upsert_customer_custom_attributes_request.py` |
| `BulkUpsertCustomerCustomAttributesRequestDict` | `square/models/bulk_upsert_customer_custom_attributes_request.py` |
| `BulkUpsertCustomerCustomAttributesResponse` | `square/models/bulk_upsert_customer_custom_attributes_response.py` |

### client.customer_custom_attributes.create_customer_custom_attribute_definition

- **Route**: `POST /v2/customers/custom-attribute-definitions`
- **Signature**: `def create_customer_custom_attribute_definition(body: CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateCustomerCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[CreateCustomerCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCustomerCustomAttributeDefinitionRequest` | `square/models/create_customer_custom_attribute_definition_request.py` |
| `CreateCustomerCustomAttributeDefinitionRequestDict` | `square/models/create_customer_custom_attribute_definition_request.py` |
| `CreateCustomerCustomAttributeDefinitionResponse` | `square/models/create_customer_custom_attribute_definition_response.py` |

### client.customer_custom_attributes.delete_customer_custom_attribute

- **Route**: `DELETE /v2/customers/{customer_id}/custom-attributes/{key}`
- **Signature**: `def delete_customer_custom_attribute(customer_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `key`
- **Params**: `customer_id` — path · `key` — path
- **Returns (parsed)**: `DeleteCustomerCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[DeleteCustomerCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCustomerCustomAttributeResponse` | `square/models/delete_customer_custom_attribute_response.py` |

### client.customer_custom_attributes.delete_customer_custom_attribute_definition

- **Route**: `DELETE /v2/customers/custom-attribute-definitions/{key}`
- **Signature**: `def delete_customer_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path
- **Returns (parsed)**: `DeleteCustomerCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[DeleteCustomerCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCustomerCustomAttributeDefinitionResponse` | `square/models/delete_customer_custom_attribute_definition_response.py` |

### client.customer_custom_attributes.list_customer_custom_attribute_definitions

- **Route**: `GET /v2/customers/custom-attribute-definitions`
- **Signature**: `def list_customer_custom_attribute_definitions(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListCustomerCustomAttributeDefinitionsResponse`
- **Returns (raw)**: `ApiResult[ListCustomerCustomAttributeDefinitionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerCustomAttributeDefinitionsResponse` | `square/models/list_customer_custom_attribute_definitions_response.py` |

### client.customer_custom_attributes.list_customer_custom_attributes

- **Route**: `GET /v2/customers/{customer_id}/custom-attributes`
- **Signature**: `def list_customer_custom_attributes(customer_id: str, *, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`
- **Params**: `customer_id` — path · `limit` — query · `cursor` — query · `with_definitions` — query
- **Returns (parsed)**: `ListCustomerCustomAttributesResponse`
- **Returns (raw)**: `ApiResult[ListCustomerCustomAttributesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerCustomAttributesResponse` | `square/models/list_customer_custom_attributes_response.py` |

### client.customer_custom_attributes.retrieve_customer_custom_attribute

- **Route**: `GET /v2/customers/{customer_id}/custom-attributes/{key}`
- **Signature**: `def retrieve_customer_custom_attribute(customer_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `key`
- **Params**: `customer_id` — path · `key` — path · `with_definition` — query · `version` — query
- **Returns (parsed)**: `RetrieveCustomerCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[RetrieveCustomerCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCustomerCustomAttributeResponse` | `square/models/retrieve_customer_custom_attribute_response.py` |

### client.customer_custom_attributes.retrieve_customer_custom_attribute_definition

- **Route**: `GET /v2/customers/custom-attribute-definitions/{key}`
- **Signature**: `def retrieve_customer_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`
- **Params**: `key` — path · `version` — query
- **Returns (parsed)**: `RetrieveCustomerCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[RetrieveCustomerCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCustomerCustomAttributeDefinitionResponse` | `square/models/retrieve_customer_custom_attribute_definition_response.py` |

### client.customer_custom_attributes.update_customer_custom_attribute_definition

- **Route**: `PUT /v2/customers/custom-attribute-definitions/{key}`
- **Signature**: `def update_customer_custom_attribute_definition(key: str, body: UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `key`, `body`
- **Params**: `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateCustomerCustomAttributeDefinitionResponse`
- **Returns (raw)**: `ApiResult[UpdateCustomerCustomAttributeDefinitionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateCustomerCustomAttributeDefinitionRequest` | `square/models/update_customer_custom_attribute_definition_request.py` |
| `UpdateCustomerCustomAttributeDefinitionRequestDict` | `square/models/update_customer_custom_attribute_definition_request.py` |
| `UpdateCustomerCustomAttributeDefinitionResponse` | `square/models/update_customer_custom_attribute_definition_response.py` |

### client.customer_custom_attributes.upsert_customer_custom_attribute

- **Route**: `POST /v2/customers/{customer_id}/custom-attributes/{key}`
- **Signature**: `def upsert_customer_custom_attribute(customer_id: str, key: str, body: UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `key`, `body`
- **Params**: `customer_id` — path · `key` — path · `body` — JSON body
- **Returns (parsed)**: `UpsertCustomerCustomAttributeResponse`
- **Returns (raw)**: `ApiResult[UpsertCustomerCustomAttributeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertCustomerCustomAttributeRequest` | `square/models/upsert_customer_custom_attribute_request.py` |
| `UpsertCustomerCustomAttributeRequestDict` | `square/models/upsert_customer_custom_attribute_request.py` |
| `UpsertCustomerCustomAttributeResponse` | `square/models/upsert_customer_custom_attribute_response.py` |

