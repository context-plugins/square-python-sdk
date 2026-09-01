<!-- Generated file — do not edit; regenerated with the SDK. -->

# GiftCardActivities — operations

Accessor: `client.gift_card_activities` · Source: `square/apis/gift_card_activities.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.gift_card_activities.create_gift_card_activity

- **Route**: `POST /v2/gift-cards/activities`
- **Auth**: `oauth2`
- **Signature**: `def create_gift_card_activity(body: CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateGiftCardActivityResponse`
- **Returns (raw)**: `ApiResult[CreateGiftCardActivityResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateGiftCardActivityRequest` | `square/models/create_gift_card_activity_request.py` |
| `CreateGiftCardActivityRequestDict` | `square/models/create_gift_card_activity_request.py` |
| `CreateGiftCardActivityResponse` | `square/models/create_gift_card_activity_response.py` |

### client.gift_card_activities.list_gift_card_activities

- **Route**: `GET /v2/gift-cards/activities`
- **Auth**: `oauth2`
- **Signature**: `def list_gift_card_activities(*, gift_card_id: str | None = None, type_: str | None = None, location_id: str | None = None, begin_time: str | None = None, end_time: str | None = None, limit: int | None = None, cursor: str | None = None, sort_order: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `gift_card_id` — query · `type_` — query `type` · `location_id` — query · `begin_time` — query · `end_time` — query · `limit` — query · `cursor` — query · `sort_order` — query
- **Returns (parsed)**: `ListGiftCardActivitiesResponse`
- **Returns (raw)**: `ApiResult[ListGiftCardActivitiesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListGiftCardActivitiesResponse` | `square/models/list_gift_card_activities_response.py` |

