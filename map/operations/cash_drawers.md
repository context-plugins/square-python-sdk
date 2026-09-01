<!-- Generated file — do not edit; regenerated with the SDK. -->

# CashDrawers — operations

Accessor: `client.cash_drawers` · Source: `square/apis/cash_drawers.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cash_drawers.list_cash_drawer_shift_events

- **Route**: `GET /v2/cash-drawers/shifts/{shift_id}/events`
- **Auth**: `oauth2`
- **Signature**: `def list_cash_drawer_shift_events(shift_id: str, location_id: str, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shift_id`, `location_id`
- **Params**: `shift_id` — path · `location_id` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListCashDrawerShiftEventsResponse`
- **Returns (raw)**: `ApiResult[ListCashDrawerShiftEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCashDrawerShiftEventsResponse` | `square/models/list_cash_drawer_shift_events_response.py` |

### client.cash_drawers.list_cash_drawer_shifts

- **Route**: `GET /v2/cash-drawers/shifts`
- **Auth**: `oauth2`
- **Signature**: `def list_cash_drawer_shifts(location_id: str, *, sort_order: SortOrderOrStr | None = None, begin_time: str | None = None, end_time: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — query · `sort_order` — query · `begin_time` — query · `end_time` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListCashDrawerShiftsResponse`
- **Returns (raw)**: `ApiResult[ListCashDrawerShiftsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListCashDrawerShiftsResponse` | `square/models/list_cash_drawer_shifts_response.py` |

### client.cash_drawers.retrieve_cash_drawer_shift

- **Route**: `GET /v2/cash-drawers/shifts/{shift_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_cash_drawer_shift(shift_id: str, location_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `shift_id`, `location_id`
- **Params**: `shift_id` — path · `location_id` — query
- **Returns (parsed)**: `RetrieveCashDrawerShiftResponse`
- **Returns (raw)**: `ApiResult[RetrieveCashDrawerShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCashDrawerShiftResponse` | `square/models/retrieve_cash_drawer_shift_response.py` |

