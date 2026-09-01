<!-- Generated file — do not edit; regenerated with the SDK. -->

# Payments — operations

Accessor: `client.payments` · Source: `square/apis/payments.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payments.cancel_payment

- **Route**: `POST /v2/payments/{payment_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_payment(payment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_id`
- **Params**: `payment_id` — path
- **Returns (parsed)**: `CancelPaymentResponse`
- **Returns (raw)**: `ApiResult[CancelPaymentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelPaymentResponse` | `square/models/cancel_payment_response.py` |

### client.payments.cancel_payment_by_idempotency_key

- **Route**: `POST /v2/payments/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_payment_by_idempotency_key(body: CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CancelPaymentByIdempotencyKeyResponse`
- **Returns (raw)**: `ApiResult[CancelPaymentByIdempotencyKeyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelPaymentByIdempotencyKeyRequest` | `square/models/cancel_payment_by_idempotency_key_request.py` |
| `CancelPaymentByIdempotencyKeyRequestDict` | `square/models/cancel_payment_by_idempotency_key_request.py` |
| `CancelPaymentByIdempotencyKeyResponse` | `square/models/cancel_payment_by_idempotency_key_response.py` |

### client.payments.complete_payment

- **Route**: `POST /v2/payments/{payment_id}/complete`
- **Auth**: `oauth2`
- **Signature**: `def complete_payment(payment_id: str, body: CompletePaymentRequest | CompletePaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_id`, `body`
- **Params**: `payment_id` — path · `body` — JSON body
- **Returns (parsed)**: `CompletePaymentResponse`
- **Returns (raw)**: `ApiResult[CompletePaymentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CompletePaymentRequest` | `square/models/complete_payment_request.py` |
| `CompletePaymentRequestDict` | `square/models/complete_payment_request.py` |
| `CompletePaymentResponse` | `square/models/complete_payment_response.py` |

### client.payments.create_payment

- **Route**: `POST /v2/payments`
- **Auth**: `oauth2`
- **Signature**: `def create_payment(body: CreatePaymentRequest | CreatePaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreatePaymentResponse`
- **Returns (raw)**: `ApiResult[CreatePaymentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreatePaymentRequest` | `square/models/create_payment_request.py` |
| `CreatePaymentRequestDict` | `square/models/create_payment_request.py` |
| `CreatePaymentResponse` | `square/models/create_payment_response.py` |

### client.payments.get_payment

- **Route**: `GET /v2/payments/{payment_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_payment(payment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_id`
- **Params**: `payment_id` — path
- **Returns (parsed)**: `GetPaymentResponse`
- **Returns (raw)**: `ApiResult[GetPaymentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetPaymentResponse` | `square/models/get_payment_response.py` |

### client.payments.list_payments

- **Route**: `GET /v2/payments`
- **Auth**: `oauth2`
- **Signature**: `def list_payments(*, begin_time: str | None = None, end_time: str | None = None, sort_order: str | None = None, cursor: str | None = None, location_id: str | None = None, total: int | None = None, last_4: str | None = None, card_brand: str | None = None, limit: int | None = None, is_offline_payment: bool | None = False, offline_begin_time: str | None = None, offline_end_time: str | None = None, updated_at_begin_time: str | None = None, updated_at_end_time: str | None = None, sort_field: ListPaymentsRequestSortFieldOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `begin_time` — query · `end_time` — query · `sort_order` — query · `cursor` — query · `location_id` — query · `total` — query · `last_4` — query · `card_brand` — query · `limit` — query · `is_offline_payment` — query · `offline_begin_time` — query · `offline_end_time` — query · `updated_at_begin_time` — query · `updated_at_end_time` — query · `sort_field` — query
- **Returns (parsed)**: `ListPaymentsResponse`
- **Returns (raw)**: `ApiResult[ListPaymentsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPaymentsRequestSortFieldOrStr` | `square/models/enums/list_payments_request_sort_field.py` |
| `ListPaymentsResponse` | `square/models/list_payments_response.py` |

### client.payments.update_payment

- **Route**: `PUT /v2/payments/{payment_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_payment(payment_id: str, body: UpdatePaymentRequest | UpdatePaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payment_id`, `body`
- **Params**: `payment_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdatePaymentResponse`
- **Returns (raw)**: `ApiResult[UpdatePaymentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdatePaymentRequest` | `square/models/update_payment_request.py` |
| `UpdatePaymentRequestDict` | `square/models/update_payment_request.py` |
| `UpdatePaymentResponse` | `square/models/update_payment_response.py` |

