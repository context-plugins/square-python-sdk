<!-- Generated file — do not edit; regenerated with the SDK. -->

# CustomerSegments — operations

Accessor: `client.customer_segments` · Source: `square/apis/customer_segments.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.customer_segments.list_customer_segments

- **Route**: `GET /v2/customers/segments`
- **Auth**: `oauth2`
- **Signature**: `def list_customer_segments(*, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListCustomerSegmentsResponse`
- **Returns (raw)**: `ApiResult[ListCustomerSegmentsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCustomerSegmentsResponse` | `square/models/list_customer_segments_response.py` |

### client.customer_segments.retrieve_customer_segment

- **Route**: `GET /v2/customers/segments/{segment_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_customer_segment(segment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `segment_id`
- **Params**: `segment_id` — path
- **Returns (parsed)**: `RetrieveCustomerSegmentResponse`
- **Returns (raw)**: `ApiResult[RetrieveCustomerSegmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCustomerSegmentResponse` | `square/models/retrieve_customer_segment_response.py` |

