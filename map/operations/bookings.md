<!-- Generated file — do not edit; regenerated with the SDK. -->

# Bookings — operations

Accessor: `client.bookings` · Source: `square/apis/bookings.py` · 13 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bookings.bulk_retrieve_bookings

- **Route**: `POST /v2/bookings/bulk-retrieve`
- **Auth**: `oauth2`
- **Signature**: `def bulk_retrieve_bookings(body: BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkRetrieveBookingsResponse`
- **Returns (raw)**: `ApiResult[BulkRetrieveBookingsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkRetrieveBookingsRequest` | `square/models/bulk_retrieve_bookings_request.py` |
| `BulkRetrieveBookingsRequestDict` | `square/models/bulk_retrieve_bookings_request.py` |
| `BulkRetrieveBookingsResponse` | `square/models/bulk_retrieve_bookings_response.py` |

### client.bookings.bulk_retrieve_team_member_booking_profiles

- **Route**: `POST /v2/bookings/team-member-booking-profiles/bulk-retrieve`
- **Auth**: `oauth2`
- **Signature**: `def bulk_retrieve_team_member_booking_profiles(body: BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkRetrieveTeamMemberBookingProfilesResponse`
- **Returns (raw)**: `ApiResult[BulkRetrieveTeamMemberBookingProfilesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkRetrieveTeamMemberBookingProfilesRequest` | `square/models/bulk_retrieve_team_member_booking_profiles_request.py` |
| `BulkRetrieveTeamMemberBookingProfilesRequestDict` | `square/models/bulk_retrieve_team_member_booking_profiles_request.py` |
| `BulkRetrieveTeamMemberBookingProfilesResponse` | `square/models/bulk_retrieve_team_member_booking_profiles_response.py` |

### client.bookings.cancel_booking

- **Route**: `POST /v2/bookings/{booking_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_booking(booking_id: str, body: CancelBookingRequest | CancelBookingRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`, `body`
- **Params**: `booking_id` — path · `body` — JSON body
- **Returns (parsed)**: `CancelBookingResponse`
- **Returns (raw)**: `ApiResult[CancelBookingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelBookingRequest` | `square/models/cancel_booking_request.py` |
| `CancelBookingRequestDict` | `square/models/cancel_booking_request.py` |
| `CancelBookingResponse` | `square/models/cancel_booking_response.py` |

### client.bookings.create_booking

- **Route**: `POST /v2/bookings`
- **Auth**: `oauth2`
- **Signature**: `def create_booking(body: CreateBookingRequest | CreateBookingRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateBookingResponse`
- **Returns (raw)**: `ApiResult[CreateBookingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateBookingRequest` | `square/models/create_booking_request.py` |
| `CreateBookingRequestDict` | `square/models/create_booking_request.py` |
| `CreateBookingResponse` | `square/models/create_booking_response.py` |

### client.bookings.list_bookings

- **Route**: `GET /v2/bookings`
- **Auth**: `oauth2`
- **Signature**: `def list_bookings(*, limit: int | None = None, cursor: str | None = None, customer_id: str | None = None, team_member_id: str | None = None, location_id: str | None = None, start_at_min: str | None = None, start_at_max: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query · `customer_id` — query · `team_member_id` — query · `location_id` — query · `start_at_min` — query · `start_at_max` — query
- **Returns (parsed)**: `ListBookingsResponse`
- **Returns (raw)**: `ApiResult[ListBookingsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBookingsResponse` | `square/models/list_bookings_response.py` |

### client.bookings.list_location_booking_profiles

- **Route**: `GET /v2/bookings/location-booking-profiles`
- **Auth**: `oauth2`
- **Signature**: `def list_location_booking_profiles(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListLocationBookingProfilesResponse`
- **Returns (raw)**: `ApiResult[ListLocationBookingProfilesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListLocationBookingProfilesResponse` | `square/models/list_location_booking_profiles_response.py` |

### client.bookings.list_team_member_booking_profiles

- **Route**: `GET /v2/bookings/team-member-booking-profiles`
- **Auth**: `oauth2`
- **Signature**: `def list_team_member_booking_profiles(*, bookable_only: bool | None = False, limit: int | None = None, cursor: str | None = None, location_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `bookable_only` — query · `limit` — query · `cursor` — query · `location_id` — query
- **Returns (parsed)**: `ListTeamMemberBookingProfilesResponse`
- **Returns (raw)**: `ApiResult[ListTeamMemberBookingProfilesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTeamMemberBookingProfilesResponse` | `square/models/list_team_member_booking_profiles_response.py` |

### client.bookings.retrieve_booking

- **Route**: `GET /v2/bookings/{booking_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_booking(booking_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`
- **Params**: `booking_id` — path
- **Returns (parsed)**: `RetrieveBookingResponse`
- **Returns (raw)**: `ApiResult[RetrieveBookingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveBookingResponse` | `square/models/retrieve_booking_response.py` |

### client.bookings.retrieve_business_booking_profile

- **Route**: `GET /v2/bookings/business-booking-profile`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_business_booking_profile(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `RetrieveBusinessBookingProfileResponse`
- **Returns (raw)**: `ApiResult[RetrieveBusinessBookingProfileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveBusinessBookingProfileResponse` | `square/models/retrieve_business_booking_profile_response.py` |

### client.bookings.retrieve_location_booking_profile

- **Route**: `GET /v2/bookings/location-booking-profiles/{location_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_location_booking_profile(location_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — path
- **Returns (parsed)**: `RetrieveLocationBookingProfileResponse`
- **Returns (raw)**: `ApiResult[RetrieveLocationBookingProfileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLocationBookingProfileResponse` | `square/models/retrieve_location_booking_profile_response.py` |

### client.bookings.retrieve_team_member_booking_profile

- **Route**: `GET /v2/bookings/team-member-booking-profiles/{team_member_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_team_member_booking_profile(team_member_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_member_id`
- **Params**: `team_member_id` — path
- **Returns (parsed)**: `RetrieveTeamMemberBookingProfileResponse`
- **Returns (raw)**: `ApiResult[RetrieveTeamMemberBookingProfileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveTeamMemberBookingProfileResponse` | `square/models/retrieve_team_member_booking_profile_response.py` |

### client.bookings.search_availability

- **Route**: `POST /v2/bookings/availability/search`
- **Auth**: `oauth2`
- **Signature**: `def search_availability(body: SearchAvailabilityRequest | SearchAvailabilityRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchAvailabilityResponse`
- **Returns (raw)**: `ApiResult[SearchAvailabilityResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchAvailabilityRequest` | `square/models/search_availability_request.py` |
| `SearchAvailabilityRequestDict` | `square/models/search_availability_request.py` |
| `SearchAvailabilityResponse` | `square/models/search_availability_response.py` |

### client.bookings.update_booking

- **Route**: `PUT /v2/bookings/{booking_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_booking(booking_id: str, body: UpdateBookingRequest | UpdateBookingRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `booking_id`, `body`
- **Params**: `booking_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateBookingResponse`
- **Returns (raw)**: `ApiResult[UpdateBookingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateBookingRequest` | `square/models/update_booking_request.py` |
| `UpdateBookingRequestDict` | `square/models/update_booking_request.py` |
| `UpdateBookingResponse` | `square/models/update_booking_response.py` |

