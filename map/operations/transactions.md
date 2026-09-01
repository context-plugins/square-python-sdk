<!-- Generated file — do not edit; regenerated with the SDK. -->

# Transactions — operations

Accessor: `client.transactions` · Source: `square/apis/transactions.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.transactions.capture_transaction

- **Route**: `POST /v2/locations/{location_id}/transactions/{transaction_id}/capture`
- **Auth**: `oauth2`
- **Signature**: `def capture_transaction(location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `transaction_id`
- **Params**: `location_id` — path · `transaction_id` — path
- **Returns (parsed)**: `CaptureTransactionResponse`
- **Returns (raw)**: `ApiResult[CaptureTransactionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CaptureTransactionResponse` | `square/models/capture_transaction_response.py` |

### client.transactions.list_transactions

- **Route**: `GET /v2/locations/{location_id}/transactions`
- **Auth**: `oauth2`
- **Signature**: `def list_transactions(location_id: str, *, begin_time: str | None = None, end_time: str | None = None, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — path · `begin_time` — query · `end_time` — query · `sort_order` — query · `cursor` — query
- **Returns (parsed)**: `ListTransactionsResponse`
- **Returns (raw)**: `ApiResult[ListTransactionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListTransactionsResponse` | `square/models/list_transactions_response.py` |

### client.transactions.retrieve_transaction

- **Route**: `GET /v2/locations/{location_id}/transactions/{transaction_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_transaction(location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `transaction_id`
- **Params**: `location_id` — path · `transaction_id` — path
- **Returns (parsed)**: `RetrieveTransactionResponse`
- **Returns (raw)**: `ApiResult[RetrieveTransactionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveTransactionResponse` | `square/models/retrieve_transaction_response.py` |

### client.transactions.void_transaction

- **Route**: `POST /v2/locations/{location_id}/transactions/{transaction_id}/void`
- **Auth**: `oauth2`
- **Signature**: `def void_transaction(location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `transaction_id`
- **Params**: `location_id` — path · `transaction_id` — path
- **Returns (parsed)**: `VoidTransactionResponse`
- **Returns (raw)**: `ApiResult[VoidTransactionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `VoidTransactionResponse` | `square/models/void_transaction_response.py` |

