<!-- Generated file — do not edit; regenerated with the SDK. -->

# Merchants — operations

Accessor: `client.merchants` · Source: `square/apis/merchants.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.merchants.list_merchants

- **Route**: `GET /v2/merchants`
- **Auth**: `oauth2`
- **Signature**: `def list_merchants(*, cursor: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query
- **Returns (parsed)**: `ListMerchantsResponse`
- **Returns (raw)**: `ApiResult[ListMerchantsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListMerchantsResponse` | `square/models/list_merchants_response.py` |

### client.merchants.retrieve_merchant

- **Route**: `GET /v2/merchants/{merchant_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_merchant(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `merchant_id`
- **Params**: `merchant_id` — path
- **Returns (parsed)**: `RetrieveMerchantResponse`
- **Returns (raw)**: `ApiResult[RetrieveMerchantResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveMerchantResponse` | `square/models/retrieve_merchant_response.py` |

