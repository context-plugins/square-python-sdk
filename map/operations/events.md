<!-- Generated file — do not edit; regenerated with the SDK. -->

# Events — operations

Accessor: `client.events` · Source: `square/apis/events.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.events.disable_events

- **Route**: `PUT /v2/events/disable`
- **Signature**: `def disable_events(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `DisableEventsResponse`
- **Returns (raw)**: `ApiResult[DisableEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DisableEventsResponse` | `square/models/disable_events_response.py` |

### client.events.enable_events

- **Route**: `PUT /v2/events/enable`
- **Signature**: `def enable_events(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `EnableEventsResponse`
- **Returns (raw)**: `ApiResult[EnableEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EnableEventsResponse` | `square/models/enable_events_response.py` |

### client.events.list_event_types

- **Route**: `GET /v2/events/types`
- **Signature**: `def list_event_types(*, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `api_version` — query
- **Returns (parsed)**: `ListEventTypesResponse`
- **Returns (raw)**: `ApiResult[ListEventTypesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEventTypesResponse` | `square/models/list_event_types_response.py` |

### client.events.search_events

- **Route**: `POST /v2/events`
- **Signature**: `def search_events(body: SearchEventsRequest | SearchEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchEventsResponse`
- **Returns (raw)**: `ApiResult[SearchEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchEventsRequest` | `square/models/search_events_request.py` |
| `SearchEventsRequestDict` | `square/models/search_events_request.py` |
| `SearchEventsResponse` | `square/models/search_events_response.py` |

