<!-- Generated file — do not edit; regenerated with the SDK. -->

# Refunds — operations

Accessor: `client.refunds` · Source: `square/apis/refunds.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.refunds.get_payment_refund

- **Route**: `GET /v2/refunds/{refund_id}`
- **Signature**: `def get_payment_refund(refund_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `refund_id`
- **Params**: `refund_id` — path
- **Returns (parsed)**: `GetPaymentRefundResponse`
- **Returns (raw)**: `ApiResult[GetPaymentRefundResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetPaymentRefundResponse` | `square/models/get_payment_refund_response.py` |

### client.refunds.list_payment_refunds

- **Route**: `GET /v2/refunds`
- **Signature**: `def list_payment_refunds(*, begin_time: str | None = None, end_time: str | None = None, sort_order: str | None = None, cursor: str | None = None, location_id: str | None = None, status: str | None = None, source_type: str | None = None, limit: int | None = None, updated_at_begin_time: str | None = None, updated_at_end_time: str | None = None, sort_field: ListPaymentRefundsRequestSortFieldOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `begin_time` — query · `end_time` — query · `sort_order` — query · `cursor` — query · `location_id` — query · `status` — query · `source_type` — query · `limit` — query · `updated_at_begin_time` — query · `updated_at_end_time` — query · `sort_field` — query
- **Returns (parsed)**: `ListPaymentRefundsResponse`
- **Returns (raw)**: `ApiResult[ListPaymentRefundsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPaymentRefundsRequestSortFieldOrStr` | `square/models/enums/list_payment_refunds_request_sort_field.py` |
| `ListPaymentRefundsResponse` | `square/models/list_payment_refunds_response.py` |

### client.refunds.refund_payment

- **Route**: `POST /v2/refunds`
- **Signature**: `def refund_payment(body: RefundPaymentRequest | RefundPaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RefundPaymentResponse`
- **Returns (raw)**: `ApiResult[RefundPaymentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RefundPaymentRequest` | `square/models/refund_payment_request.py` |
| `RefundPaymentRequestDict` | `square/models/refund_payment_request.py` |
| `RefundPaymentResponse` | `square/models/refund_payment_response.py` |

