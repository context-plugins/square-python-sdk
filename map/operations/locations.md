<!-- Generated file — do not edit; regenerated with the SDK. -->

# Locations — operations

Accessor: `client.locations` · Source: `square/apis/locations.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.locations.create_location

- **Route**: `POST /v2/locations`
- **Auth**: `oauth2`
- **Signature**: `def create_location(body: CreateLocationRequest | CreateLocationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateLocationResponse`
- **Returns (raw)**: `ApiResult[CreateLocationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateLocationRequest` | `square/models/create_location_request.py` |
| `CreateLocationRequestDict` | `square/models/create_location_request.py` |
| `CreateLocationResponse` | `square/models/create_location_response.py` |

### client.locations.list_locations

- **Route**: `GET /v2/locations`
- **Auth**: `oauth2`
- **Signature**: `def list_locations(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ListLocationsResponse`
- **Returns (raw)**: `ApiResult[ListLocationsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListLocationsResponse` | `square/models/list_locations_response.py` |

### client.locations.retrieve_location

- **Route**: `GET /v2/locations/{location_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_location(location_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — path
- **Returns (parsed)**: `RetrieveLocationResponse`
- **Returns (raw)**: `ApiResult[RetrieveLocationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLocationResponse` | `square/models/retrieve_location_response.py` |

### client.locations.update_location

- **Route**: `PUT /v2/locations/{location_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_location(location_id: str, body: UpdateLocationRequest | UpdateLocationRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `body`
- **Params**: `location_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateLocationResponse`
- **Returns (raw)**: `ApiResult[UpdateLocationResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateLocationRequest` | `square/models/update_location_request.py` |
| `UpdateLocationRequestDict` | `square/models/update_location_request.py` |
| `UpdateLocationResponse` | `square/models/update_location_response.py` |

