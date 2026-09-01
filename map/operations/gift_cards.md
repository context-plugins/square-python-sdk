<!-- Generated file — do not edit; regenerated with the SDK. -->

# GiftCards — operations

Accessor: `client.gift_cards` · Source: `square/apis/gift_cards.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.gift_cards.create_gift_card

- **Route**: `POST /v2/gift-cards`
- **Auth**: `oauth2`
- **Signature**: `def create_gift_card(body: CreateGiftCardRequest | CreateGiftCardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateGiftCardResponse`
- **Returns (raw)**: `ApiResult[CreateGiftCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateGiftCardRequest` | `square/models/create_gift_card_request.py` |
| `CreateGiftCardRequestDict` | `square/models/create_gift_card_request.py` |
| `CreateGiftCardResponse` | `square/models/create_gift_card_response.py` |

### client.gift_cards.link_customer_to_gift_card

- **Route**: `POST /v2/gift-cards/{gift_card_id}/link-customer`
- **Auth**: `oauth2`
- **Signature**: `def link_customer_to_gift_card(gift_card_id: str, body: LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gift_card_id`, `body`
- **Params**: `gift_card_id` — path · `body` — JSON body
- **Returns (parsed)**: `LinkCustomerToGiftCardResponse`
- **Returns (raw)**: `ApiResult[LinkCustomerToGiftCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LinkCustomerToGiftCardRequest` | `square/models/link_customer_to_gift_card_request.py` |
| `LinkCustomerToGiftCardRequestDict` | `square/models/link_customer_to_gift_card_request.py` |
| `LinkCustomerToGiftCardResponse` | `square/models/link_customer_to_gift_card_response.py` |

### client.gift_cards.list_gift_cards

- **Route**: `GET /v2/gift-cards`
- **Auth**: `oauth2`
- **Signature**: `def list_gift_cards(*, type_: str | None = None, state: str | None = None, limit: int | None = None, cursor: str | None = None, customer_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `type_` — query `type` · `state` — query · `limit` — query · `cursor` — query · `customer_id` — query
- **Returns (parsed)**: `ListGiftCardsResponse`
- **Returns (raw)**: `ApiResult[ListGiftCardsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListGiftCardsResponse` | `square/models/list_gift_cards_response.py` |

### client.gift_cards.retrieve_gift_card

- **Route**: `GET /v2/gift-cards/{id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_gift_card(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `RetrieveGiftCardResponse`
- **Returns (raw)**: `ApiResult[RetrieveGiftCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveGiftCardResponse` | `square/models/retrieve_gift_card_response.py` |

### client.gift_cards.retrieve_gift_card_from_gan

- **Route**: `POST /v2/gift-cards/from-gan`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_gift_card_from_gan(body: RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RetrieveGiftCardFromGanresponse`
- **Returns (raw)**: `ApiResult[RetrieveGiftCardFromGanresponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveGiftCardFromGanrequest` | `square/models/retrieve_gift_card_from_ganrequest.py` |
| `RetrieveGiftCardFromGanrequestDict` | `square/models/retrieve_gift_card_from_ganrequest.py` |
| `RetrieveGiftCardFromGanresponse` | `square/models/retrieve_gift_card_from_ganresponse.py` |

### client.gift_cards.retrieve_gift_card_from_nonce

- **Route**: `POST /v2/gift-cards/from-nonce`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_gift_card_from_nonce(body: RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RetrieveGiftCardFromNonceResponse`
- **Returns (raw)**: `ApiResult[RetrieveGiftCardFromNonceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveGiftCardFromNonceRequest` | `square/models/retrieve_gift_card_from_nonce_request.py` |
| `RetrieveGiftCardFromNonceRequestDict` | `square/models/retrieve_gift_card_from_nonce_request.py` |
| `RetrieveGiftCardFromNonceResponse` | `square/models/retrieve_gift_card_from_nonce_response.py` |

### client.gift_cards.unlink_customer_from_gift_card

- **Route**: `POST /v2/gift-cards/{gift_card_id}/unlink-customer`
- **Auth**: `oauth2`
- **Signature**: `def unlink_customer_from_gift_card(gift_card_id: str, body: UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `gift_card_id`, `body`
- **Params**: `gift_card_id` — path · `body` — JSON body
- **Returns (parsed)**: `UnlinkCustomerFromGiftCardResponse`
- **Returns (raw)**: `ApiResult[UnlinkCustomerFromGiftCardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UnlinkCustomerFromGiftCardRequest` | `square/models/unlink_customer_from_gift_card_request.py` |
| `UnlinkCustomerFromGiftCardRequestDict` | `square/models/unlink_customer_from_gift_card_request.py` |
| `UnlinkCustomerFromGiftCardResponse` | `square/models/unlink_customer_from_gift_card_response.py` |

