<!-- Generated file — do not edit; regenerated with the SDK. -->

# V1Transactions — operations

Accessor: `client.v1_transactions` · Source: `square/apis/v1_transactions.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.v1_transactions.v1_list_orders

- **Route**: `GET /v1/{location_id}/orders`
- **Signature**: `def v1_list_orders(location_id: str, *, order: SortOrderOrStr | None = None, limit: int | None = None, batch_token: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — path · `order` — query · `limit` — query · `batch_token` — query
- **Returns (parsed)**: `list[V1Order]`
- **Returns (raw)**: `ApiResult[list[V1Order], RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `V1Order` | `square/models/v1_order.py` |

### client.v1_transactions.v1_retrieve_order

- **Route**: `GET /v1/{location_id}/orders/{order_id}`
- **Signature**: `def v1_retrieve_order(location_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `order_id`
- **Params**: `location_id` — path · `order_id` — path
- **Returns (parsed)**: `V1Order`
- **Returns (raw)**: `ApiResult[V1Order, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V1Order` | `square/models/v1_order.py` |

### client.v1_transactions.v1_update_order

- **Route**: `PUT /v1/{location_id}/orders/{order_id}`
- **Signature**: `def v1_update_order(location_id: str, order_id: str, body: V1UpdateOrderRequest | V1UpdateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `order_id`, `body`
- **Params**: `location_id` — path · `order_id` — path · `body` — JSON body
- **Returns (parsed)**: `V1Order`
- **Returns (raw)**: `ApiResult[V1Order, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `V1UpdateOrderRequest` | `square/models/v1_update_order_request.py` |
| `V1UpdateOrderRequestDict` | `square/models/v1_update_order_request.py` |
| `V1Order` | `square/models/v1_order.py` |

