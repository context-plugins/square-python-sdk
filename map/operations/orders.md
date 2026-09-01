<!-- Generated file — do not edit; regenerated with the SDK. -->

# Orders — operations

Accessor: `client.orders` · Source: `square/apis/orders.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.orders.batch_retrieve_orders

- **Route**: `POST /v2/orders/batch-retrieve`
- **Auth**: `oauth2`
- **Signature**: `def batch_retrieve_orders(body: BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchRetrieveOrdersResponse`
- **Returns (raw)**: `ApiResult[BatchRetrieveOrdersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchRetrieveOrdersRequest` | `square/models/batch_retrieve_orders_request.py` |
| `BatchRetrieveOrdersRequestDict` | `square/models/batch_retrieve_orders_request.py` |
| `BatchRetrieveOrdersResponse` | `square/models/batch_retrieve_orders_response.py` |

### client.orders.calculate_order

- **Route**: `POST /v2/orders/calculate`
- **Auth**: `oauth2`
- **Signature**: `def calculate_order(body: CalculateOrderRequest | CalculateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CalculateOrderResponse`
- **Returns (raw)**: `ApiResult[CalculateOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CalculateOrderRequest` | `square/models/calculate_order_request.py` |
| `CalculateOrderRequestDict` | `square/models/calculate_order_request.py` |
| `CalculateOrderResponse` | `square/models/calculate_order_response.py` |

### client.orders.clone_order

- **Route**: `POST /v2/orders/clone`
- **Auth**: `oauth2`
- **Signature**: `def clone_order(body: CloneOrderRequest | CloneOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CloneOrderResponse`
- **Returns (raw)**: `ApiResult[CloneOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CloneOrderRequest` | `square/models/clone_order_request.py` |
| `CloneOrderRequestDict` | `square/models/clone_order_request.py` |
| `CloneOrderResponse` | `square/models/clone_order_response.py` |

### client.orders.create_order

- **Route**: `POST /v2/orders`
- **Auth**: `oauth2`
- **Signature**: `def create_order(body: CreateOrderRequest | CreateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateOrderResponse`
- **Returns (raw)**: `ApiResult[CreateOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateOrderRequest` | `square/models/create_order_request.py` |
| `CreateOrderRequestDict` | `square/models/create_order_request.py` |
| `CreateOrderResponse` | `square/models/create_order_response.py` |

### client.orders.pay_order

- **Route**: `POST /v2/orders/{order_id}/pay`
- **Auth**: `oauth2`
- **Signature**: `def pay_order(order_id: str, body: PayOrderRequest | PayOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `body`
- **Params**: `order_id` — path · `body` — JSON body
- **Returns (parsed)**: `PayOrderResponse`
- **Returns (raw)**: `ApiResult[PayOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PayOrderRequest` | `square/models/pay_order_request.py` |
| `PayOrderRequestDict` | `square/models/pay_order_request.py` |
| `PayOrderResponse` | `square/models/pay_order_response.py` |

### client.orders.retrieve_order

- **Route**: `GET /v2/orders/{order_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_order(order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`
- **Params**: `order_id` — path
- **Returns (parsed)**: `RetrieveOrderResponse`
- **Returns (raw)**: `ApiResult[RetrieveOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveOrderResponse` | `square/models/retrieve_order_response.py` |

### client.orders.search_orders

- **Route**: `POST /v2/orders/search`
- **Auth**: `oauth2`
- **Signature**: `def search_orders(body: SearchOrdersRequest | SearchOrdersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchOrdersResponse`
- **Returns (raw)**: `ApiResult[SearchOrdersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchOrdersRequest` | `square/models/search_orders_request.py` |
| `SearchOrdersRequestDict` | `square/models/search_orders_request.py` |
| `SearchOrdersResponse` | `square/models/search_orders_response.py` |

### client.orders.update_order

- **Route**: `PUT /v2/orders/{order_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_order(order_id: str, body: UpdateOrderRequest | UpdateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `order_id`, `body`
- **Params**: `order_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateOrderResponse`
- **Returns (raw)**: `ApiResult[UpdateOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateOrderRequest` | `square/models/update_order_request.py` |
| `UpdateOrderRequestDict` | `square/models/update_order_request.py` |
| `UpdateOrderResponse` | `square/models/update_order_response.py` |

