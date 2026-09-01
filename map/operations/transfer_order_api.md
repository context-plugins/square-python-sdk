<!-- Generated file — do not edit; regenerated with the SDK. -->

# TransferOrderApi — operations

Accessor: `client.transfer_order_api` · Source: `square/apis/transfer_order_api.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transfer_order_api.cancel_transfer_order

- **Route**: `POST /v2/transfer-orders/{transfer_order_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_transfer_order(transfer_order_id: str, body: CancelTransferOrderRequest | CancelTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_order_id`, `body`
- **Params**: `transfer_order_id` — path · `body` — JSON body
- **Returns (parsed)**: `CancelTransferOrderResponse`
- **Returns (raw)**: `ApiResult[CancelTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelTransferOrderRequest` | `square/models/cancel_transfer_order_request.py` |
| `CancelTransferOrderRequestDict` | `square/models/cancel_transfer_order_request.py` |
| `CancelTransferOrderResponse` | `square/models/cancel_transfer_order_response.py` |

### client.transfer_order_api.create_transfer_order

- **Route**: `POST /v2/transfer-orders`
- **Auth**: `oauth2`
- **Signature**: `def create_transfer_order(body: CreateTransferOrderRequest | CreateTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTransferOrderResponse`
- **Returns (raw)**: `ApiResult[CreateTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTransferOrderRequest` | `square/models/create_transfer_order_request.py` |
| `CreateTransferOrderRequestDict` | `square/models/create_transfer_order_request.py` |
| `CreateTransferOrderResponse` | `square/models/create_transfer_order_response.py` |

### client.transfer_order_api.delete_transfer_order

- **Route**: `DELETE /v2/transfer-orders/{transfer_order_id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_transfer_order(transfer_order_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_order_id`
- **Params**: `transfer_order_id` — path · `version` — query
- **Returns (parsed)**: `DeleteTransferOrderResponse`
- **Returns (raw)**: `ApiResult[DeleteTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteTransferOrderResponse` | `square/models/delete_transfer_order_response.py` |

### client.transfer_order_api.receive_transfer_order

- **Route**: `POST /v2/transfer-orders/{transfer_order_id}/receive`
- **Auth**: `oauth2`
- **Signature**: `def receive_transfer_order(transfer_order_id: str, body: ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_order_id`, `body`
- **Params**: `transfer_order_id` — path · `body` — JSON body
- **Returns (parsed)**: `ReceiveTransferOrderResponse`
- **Returns (raw)**: `ApiResult[ReceiveTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReceiveTransferOrderRequest` | `square/models/receive_transfer_order_request.py` |
| `ReceiveTransferOrderRequestDict` | `square/models/receive_transfer_order_request.py` |
| `ReceiveTransferOrderResponse` | `square/models/receive_transfer_order_response.py` |

### client.transfer_order_api.retrieve_transfer_order

- **Route**: `GET /v2/transfer-orders/{transfer_order_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_transfer_order(transfer_order_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_order_id`
- **Params**: `transfer_order_id` — path
- **Returns (parsed)**: `RetrieveTransferOrderResponse`
- **Returns (raw)**: `ApiResult[RetrieveTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveTransferOrderResponse` | `square/models/retrieve_transfer_order_response.py` |

### client.transfer_order_api.search_transfer_orders

- **Route**: `POST /v2/transfer-orders/search`
- **Auth**: `oauth2`
- **Signature**: `def search_transfer_orders(body: SearchTransferOrdersRequest | SearchTransferOrdersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchTransferOrdersResponse`
- **Returns (raw)**: `ApiResult[SearchTransferOrdersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchTransferOrdersRequest` | `square/models/search_transfer_orders_request.py` |
| `SearchTransferOrdersRequestDict` | `square/models/search_transfer_orders_request.py` |
| `SearchTransferOrdersResponse` | `square/models/search_transfer_orders_response.py` |

### client.transfer_order_api.start_transfer_order

- **Route**: `POST /v2/transfer-orders/{transfer_order_id}/start`
- **Auth**: `oauth2`
- **Signature**: `def start_transfer_order(transfer_order_id: str, body: StartTransferOrderRequest | StartTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_order_id`, `body`
- **Params**: `transfer_order_id` — path · `body` — JSON body
- **Returns (parsed)**: `StartTransferOrderResponse`
- **Returns (raw)**: `ApiResult[StartTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `StartTransferOrderRequest` | `square/models/start_transfer_order_request.py` |
| `StartTransferOrderRequestDict` | `square/models/start_transfer_order_request.py` |
| `StartTransferOrderResponse` | `square/models/start_transfer_order_response.py` |

### client.transfer_order_api.update_transfer_order

- **Route**: `PUT /v2/transfer-orders/{transfer_order_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_transfer_order(transfer_order_id: str, body: UpdateTransferOrderRequest | UpdateTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `transfer_order_id`, `body`
- **Params**: `transfer_order_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateTransferOrderResponse`
- **Returns (raw)**: `ApiResult[UpdateTransferOrderResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateTransferOrderRequest` | `square/models/update_transfer_order_request.py` |
| `UpdateTransferOrderRequestDict` | `square/models/update_transfer_order_request.py` |
| `UpdateTransferOrderResponse` | `square/models/update_transfer_order_response.py` |

