<!-- Generated file — do not edit; regenerated with the SDK. -->

# CustomerGroups — operations

Accessor: `client.customer_groups` · Source: `square/apis/customer_groups.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.customer_groups.create_customer_group

- **Route**: `POST /v2/customers/groups`
- **Signature**: `def create_customer_group(body: CreateCustomerGroupRequest | CreateCustomerGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateCustomerGroupResponse`
- **Returns (raw)**: `ApiResult[CreateCustomerGroupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCustomerGroupRequest` | `square/models/create_customer_group_request.py` |
| `CreateCustomerGroupRequestDict` | `square/models/create_customer_group_request.py` |
| `CreateCustomerGroupResponse` | `square/models/create_customer_group_response.py` |

### client.customer_groups.delete_customer_group

- **Route**: `DELETE /v2/customers/groups/{group_id}`
- **Signature**: `def delete_customer_group(group_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `DeleteCustomerGroupResponse`
- **Returns (raw)**: `ApiResult[DeleteCustomerGroupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCustomerGroupResponse` | `square/models/delete_customer_group_response.py` |

### client.customer_groups.list_customer_groups

- **Route**: `GET /v2/customers/groups`
- **Signature**: `def list_customer_groups(*, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListCustomerGroupsResponse`
- **Returns (raw)**: `ApiResult[ListCustomerGroupsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerGroupsResponse` | `square/models/list_customer_groups_response.py` |

### client.customer_groups.retrieve_customer_group

- **Route**: `GET /v2/customers/groups/{group_id}`
- **Signature**: `def retrieve_customer_group(group_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`
- **Params**: `group_id` — path
- **Returns (parsed)**: `RetrieveCustomerGroupResponse`
- **Returns (raw)**: `ApiResult[RetrieveCustomerGroupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCustomerGroupResponse` | `square/models/retrieve_customer_group_response.py` |

### client.customer_groups.update_customer_group

- **Route**: `PUT /v2/customers/groups/{group_id}`
- **Signature**: `def update_customer_group(group_id: str, body: UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `group_id`, `body`
- **Params**: `group_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateCustomerGroupResponse`
- **Returns (raw)**: `ApiResult[UpdateCustomerGroupResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateCustomerGroupRequest` | `square/models/update_customer_group_request.py` |
| `UpdateCustomerGroupRequestDict` | `square/models/update_customer_group_request.py` |
| `UpdateCustomerGroupResponse` | `square/models/update_customer_group_response.py` |

