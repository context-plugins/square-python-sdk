<!-- Generated file — do not edit; regenerated with the SDK. -->

# Customers — operations

Accessor: `client.customers` · Source: `square/apis/customers.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.customers.add_group_to_customer

- **Route**: `PUT /v2/customers/{customer_id}/groups/{group_id}`
- **Auth**: `oauth2`
- **Signature**: `def add_group_to_customer(customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `group_id`
- **Params**: `customer_id` — path · `group_id` — path
- **Returns (parsed)**: `AddGroupToCustomerResponse`
- **Returns (raw)**: `ApiResult[AddGroupToCustomerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AddGroupToCustomerResponse` | `square/models/add_group_to_customer_response.py` |

### client.customers.bulk_create_customers

- **Route**: `POST /v2/customers/bulk-create`
- **Auth**: `oauth2`
- **Signature**: `def bulk_create_customers(body: BulkCreateCustomersRequest | BulkCreateCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkCreateCustomersResponse`
- **Returns (raw)**: `ApiResult[BulkCreateCustomersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkCreateCustomersRequest` | `square/models/bulk_create_customers_request.py` |
| `BulkCreateCustomersRequestDict` | `square/models/bulk_create_customers_request.py` |
| `BulkCreateCustomersResponse` | `square/models/bulk_create_customers_response.py` |

### client.customers.bulk_delete_customers

- **Route**: `POST /v2/customers/bulk-delete`
- **Auth**: `oauth2`
- **Signature**: `def bulk_delete_customers(body: BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkDeleteCustomersResponse`
- **Returns (raw)**: `ApiResult[BulkDeleteCustomersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkDeleteCustomersRequest` | `square/models/bulk_delete_customers_request.py` |
| `BulkDeleteCustomersRequestDict` | `square/models/bulk_delete_customers_request.py` |
| `BulkDeleteCustomersResponse` | `square/models/bulk_delete_customers_response.py` |

### client.customers.bulk_retrieve_customers

- **Route**: `POST /v2/customers/bulk-retrieve`
- **Auth**: `oauth2`
- **Signature**: `def bulk_retrieve_customers(body: BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkRetrieveCustomersResponse`
- **Returns (raw)**: `ApiResult[BulkRetrieveCustomersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkRetrieveCustomersRequest` | `square/models/bulk_retrieve_customers_request.py` |
| `BulkRetrieveCustomersRequestDict` | `square/models/bulk_retrieve_customers_request.py` |
| `BulkRetrieveCustomersResponse` | `square/models/bulk_retrieve_customers_response.py` |

### client.customers.bulk_update_customers

- **Route**: `POST /v2/customers/bulk-update`
- **Auth**: `oauth2`
- **Signature**: `def bulk_update_customers(body: BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpdateCustomersResponse`
- **Returns (raw)**: `ApiResult[BulkUpdateCustomersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpdateCustomersRequest` | `square/models/bulk_update_customers_request.py` |
| `BulkUpdateCustomersRequestDict` | `square/models/bulk_update_customers_request.py` |
| `BulkUpdateCustomersResponse` | `square/models/bulk_update_customers_response.py` |

### client.customers.create_customer

- **Route**: `POST /v2/customers`
- **Auth**: `oauth2`
- **Signature**: `def create_customer(body: CreateCustomerRequest | CreateCustomerRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateCustomerResponse`
- **Returns (raw)**: `ApiResult[CreateCustomerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCustomerRequest` | `square/models/create_customer_request.py` |
| `CreateCustomerRequestDict` | `square/models/create_customer_request.py` |
| `CreateCustomerResponse` | `square/models/create_customer_response.py` |

### client.customers.create_customer_card

- **Route**: `POST /v2/customers/{customer_id}/cards`
- **Auth**: `oauth2`
- **Signature**: `def create_customer_card(customer_id: str, body: CreateCustomerCardRequest | CreateCustomerCardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `body`
- **Params**: `customer_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateCustomerCardResponse`
- **Returns (raw)**: `ApiResult[CreateCustomerCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCustomerCardRequest` | `square/models/create_customer_card_request.py` |
| `CreateCustomerCardRequestDict` | `square/models/create_customer_card_request.py` |
| `CreateCustomerCardResponse` | `square/models/create_customer_card_response.py` |

### client.customers.delete_customer

- **Route**: `DELETE /v2/customers/{customer_id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_customer(customer_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`
- **Params**: `customer_id` — path · `version` — query
- **Returns (parsed)**: `DeleteCustomerResponse`
- **Returns (raw)**: `ApiResult[DeleteCustomerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCustomerResponse` | `square/models/delete_customer_response.py` |

### client.customers.delete_customer_card

- **Route**: `DELETE /v2/customers/{customer_id}/cards/{card_id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_customer_card(customer_id: str, card_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `card_id`
- **Params**: `customer_id` — path · `card_id` — path
- **Returns (parsed)**: `DeleteCustomerCardResponse`
- **Returns (raw)**: `ApiResult[DeleteCustomerCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCustomerCardResponse` | `square/models/delete_customer_card_response.py` |

### client.customers.list_customers

- **Route**: `GET /v2/customers`
- **Auth**: `oauth2`
- **Signature**: `def list_customers(*, cursor: str | None = None, limit: int | None = None, sort_field: CustomerSortFieldOrStr | None = None, sort_order: SortOrderOrStr | None = None, count: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `limit` — query · `sort_field` — query · `sort_order` — query · `count` — query
- **Returns (parsed)**: `ListCustomersResponse`
- **Returns (raw)**: `ApiResult[ListCustomersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CustomerSortFieldOrStr` | `square/models/enums/customer_sort_field.py` |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListCustomersResponse` | `square/models/list_customers_response.py` |

### client.customers.remove_group_from_customer

- **Route**: `DELETE /v2/customers/{customer_id}/groups/{group_id}`
- **Auth**: `oauth2`
- **Signature**: `def remove_group_from_customer(customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `group_id`
- **Params**: `customer_id` — path · `group_id` — path
- **Returns (parsed)**: `RemoveGroupFromCustomerResponse`
- **Returns (raw)**: `ApiResult[RemoveGroupFromCustomerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RemoveGroupFromCustomerResponse` | `square/models/remove_group_from_customer_response.py` |

### client.customers.retrieve_customer

- **Route**: `GET /v2/customers/{customer_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_customer(customer_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`
- **Params**: `customer_id` — path
- **Returns (parsed)**: `RetrieveCustomerResponse`
- **Returns (raw)**: `ApiResult[RetrieveCustomerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCustomerResponse` | `square/models/retrieve_customer_response.py` |

### client.customers.search_customers

- **Route**: `POST /v2/customers/search`
- **Auth**: `oauth2`
- **Signature**: `def search_customers(body: SearchCustomersRequest | SearchCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchCustomersResponse`
- **Returns (raw)**: `ApiResult[SearchCustomersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchCustomersRequest` | `square/models/search_customers_request.py` |
| `SearchCustomersRequestDict` | `square/models/search_customers_request.py` |
| `SearchCustomersResponse` | `square/models/search_customers_response.py` |

### client.customers.update_customer

- **Route**: `PUT /v2/customers/{customer_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_customer(customer_id: str, body: UpdateCustomerRequest | UpdateCustomerRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `customer_id`, `body`
- **Params**: `customer_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateCustomerResponse`
- **Returns (raw)**: `ApiResult[UpdateCustomerResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateCustomerRequest` | `square/models/update_customer_request.py` |
| `UpdateCustomerRequestDict` | `square/models/update_customer_request.py` |
| `UpdateCustomerResponse` | `square/models/update_customer_response.py` |

