<!-- Generated file — do not edit; regenerated with the SDK. -->

# Payouts — operations

Accessor: `client.payouts` · Source: `square/apis/payouts.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.payouts.get_payout

- **Route**: `GET /v2/payouts/{payout_id}`
- **Signature**: `def get_payout(payout_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payout_id`
- **Params**: `payout_id` — path
- **Returns (parsed)**: `GetPayoutResponse`
- **Returns (raw)**: `ApiResult[GetPayoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetPayoutResponse` | `square/models/get_payout_response.py` |

### client.payouts.list_payout_entries

- **Route**: `GET /v2/payouts/{payout_id}/payout-entries`
- **Signature**: `def list_payout_entries(payout_id: str, *, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `payout_id`
- **Params**: `payout_id` — path · `sort_order` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListPayoutEntriesResponse`
- **Returns (raw)**: `ApiResult[ListPayoutEntriesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListPayoutEntriesResponse` | `square/models/list_payout_entries_response.py` |

### client.payouts.list_payouts

- **Route**: `GET /v2/payouts`
- **Signature**: `def list_payouts(*, location_id: str | None = None, status: PayoutStatusOrStr | None = None, begin_time: str | None = None, end_time: str | None = None, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `location_id` — query · `status` — query · `begin_time` — query · `end_time` — query · `sort_order` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListPayoutsResponse`
- **Returns (raw)**: `ApiResult[ListPayoutsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PayoutStatusOrStr` | `square/models/enums/payout_status.py` |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListPayoutsResponse` | `square/models/list_payouts_response.py` |

