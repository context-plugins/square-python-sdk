<!-- Generated file — do not edit; regenerated with the SDK. -->

# Cards — operations

Accessor: `client.cards` · Source: `square/apis/cards.py` · 4 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.cards.create_card

- **Route**: `POST /v2/cards`
- **Signature**: `def create_card(body: CreateCardRequest | CreateCardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateCardResponse`
- **Returns (raw)**: `ApiResult[CreateCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCardRequest` | `square/models/create_card_request.py` |
| `CreateCardRequestDict` | `square/models/create_card_request.py` |
| `CreateCardResponse` | `square/models/create_card_response.py` |

### client.cards.disable_card

- **Route**: `POST /v2/cards/{card_id}/disable`
- **Signature**: `def disable_card(card_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `card_id`
- **Params**: `card_id` — path
- **Returns (parsed)**: `DisableCardResponse`
- **Returns (raw)**: `ApiResult[DisableCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DisableCardResponse` | `square/models/disable_card_response.py` |

### client.cards.list_cards

- **Route**: `GET /v2/cards`
- **Signature**: `def list_cards(*, cursor: str | None = None, customer_id: str | None = None, include_disabled: bool | None = False, reference_id: str | None = None, sort_order: SortOrderOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `customer_id` — query · `include_disabled` — query · `reference_id` — query · `sort_order` — query
- **Returns (parsed)**: `ListCardsResponse`
- **Returns (raw)**: `ApiResult[ListCardsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListCardsResponse` | `square/models/list_cards_response.py` |

### client.cards.retrieve_card

- **Route**: `GET /v2/cards/{card_id}`
- **Signature**: `def retrieve_card(card_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `card_id`
- **Params**: `card_id` — path
- **Returns (parsed)**: `RetrieveCardResponse`
- **Returns (raw)**: `ApiResult[RetrieveCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCardResponse` | `square/models/retrieve_card_response.py` |

