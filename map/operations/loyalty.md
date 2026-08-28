<!-- Generated file — do not edit; regenerated with the SDK. -->

# Loyalty — operations

Accessor: `client.loyalty` · Source: `square/apis/loyalty.py` · 18 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.loyalty.accumulate_loyalty_points

- **Route**: `POST /v2/loyalty/accounts/{account_id}/accumulate`
- **Signature**: `def accumulate_loyalty_points(account_id: str, body: AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_id`, `body`
- **Params**: `account_id` — path · `body` — JSON body
- **Returns (parsed)**: `AccumulateLoyaltyPointsResponse`
- **Returns (raw)**: `ApiResult[AccumulateLoyaltyPointsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AccumulateLoyaltyPointsRequest` | `square/models/accumulate_loyalty_points_request.py` |
| `AccumulateLoyaltyPointsRequestDict` | `square/models/accumulate_loyalty_points_request.py` |
| `AccumulateLoyaltyPointsResponse` | `square/models/accumulate_loyalty_points_response.py` |

### client.loyalty.adjust_loyalty_points

- **Route**: `POST /v2/loyalty/accounts/{account_id}/adjust`
- **Signature**: `def adjust_loyalty_points(account_id: str, body: AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_id`, `body`
- **Params**: `account_id` — path · `body` — JSON body
- **Returns (parsed)**: `AdjustLoyaltyPointsResponse`
- **Returns (raw)**: `ApiResult[AdjustLoyaltyPointsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AdjustLoyaltyPointsRequest` | `square/models/adjust_loyalty_points_request.py` |
| `AdjustLoyaltyPointsRequestDict` | `square/models/adjust_loyalty_points_request.py` |
| `AdjustLoyaltyPointsResponse` | `square/models/adjust_loyalty_points_response.py` |

### client.loyalty.calculate_loyalty_points

- **Route**: `POST /v2/loyalty/programs/{program_id}/calculate`
- **Signature**: `def calculate_loyalty_points(program_id: str, body: CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `program_id`, `body`
- **Params**: `program_id` — path · `body` — JSON body
- **Returns (parsed)**: `CalculateLoyaltyPointsResponse`
- **Returns (raw)**: `ApiResult[CalculateLoyaltyPointsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CalculateLoyaltyPointsRequest` | `square/models/calculate_loyalty_points_request.py` |
| `CalculateLoyaltyPointsRequestDict` | `square/models/calculate_loyalty_points_request.py` |
| `CalculateLoyaltyPointsResponse` | `square/models/calculate_loyalty_points_response.py` |

### client.loyalty.cancel_loyalty_promotion

- **Route**: `POST /v2/loyalty/programs/{program_id}/promotions/{promotion_id}/cancel`
- **Signature**: `def cancel_loyalty_promotion(promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `promotion_id`, `program_id`
- **Params**: `promotion_id` — path · `program_id` — path
- **Returns (parsed)**: `CancelLoyaltyPromotionResponse`
- **Returns (raw)**: `ApiResult[CancelLoyaltyPromotionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelLoyaltyPromotionResponse` | `square/models/cancel_loyalty_promotion_response.py` |

### client.loyalty.create_loyalty_account

- **Route**: `POST /v2/loyalty/accounts`
- **Signature**: `def create_loyalty_account(body: CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateLoyaltyAccountResponse`
- **Returns (raw)**: `ApiResult[CreateLoyaltyAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateLoyaltyAccountRequest` | `square/models/create_loyalty_account_request.py` |
| `CreateLoyaltyAccountRequestDict` | `square/models/create_loyalty_account_request.py` |
| `CreateLoyaltyAccountResponse` | `square/models/create_loyalty_account_response.py` |

### client.loyalty.create_loyalty_promotion

- **Route**: `POST /v2/loyalty/programs/{program_id}/promotions`
- **Signature**: `def create_loyalty_promotion(program_id: str, body: CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `program_id`, `body`
- **Params**: `program_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateLoyaltyPromotionResponse`
- **Returns (raw)**: `ApiResult[CreateLoyaltyPromotionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateLoyaltyPromotionRequest` | `square/models/create_loyalty_promotion_request.py` |
| `CreateLoyaltyPromotionRequestDict` | `square/models/create_loyalty_promotion_request.py` |
| `CreateLoyaltyPromotionResponse` | `square/models/create_loyalty_promotion_response.py` |

### client.loyalty.create_loyalty_reward

- **Route**: `POST /v2/loyalty/rewards`
- **Signature**: `def create_loyalty_reward(body: CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateLoyaltyRewardResponse`
- **Returns (raw)**: `ApiResult[CreateLoyaltyRewardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateLoyaltyRewardRequest` | `square/models/create_loyalty_reward_request.py` |
| `CreateLoyaltyRewardRequestDict` | `square/models/create_loyalty_reward_request.py` |
| `CreateLoyaltyRewardResponse` | `square/models/create_loyalty_reward_response.py` |

### client.loyalty.delete_loyalty_reward

- **Route**: `DELETE /v2/loyalty/rewards/{reward_id}`
- **Signature**: `def delete_loyalty_reward(reward_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `reward_id`
- **Params**: `reward_id` — path
- **Returns (parsed)**: `DeleteLoyaltyRewardResponse`
- **Returns (raw)**: `ApiResult[DeleteLoyaltyRewardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteLoyaltyRewardResponse` | `square/models/delete_loyalty_reward_response.py` |

### client.loyalty.list_loyalty_programs

- **Route**: `GET /v2/loyalty/programs`
- **Signature**: `def list_loyalty_programs(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ListLoyaltyProgramsResponse`
- **Returns (raw)**: `ApiResult[ListLoyaltyProgramsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListLoyaltyProgramsResponse` | `square/models/list_loyalty_programs_response.py` |

### client.loyalty.list_loyalty_promotions

- **Route**: `GET /v2/loyalty/programs/{program_id}/promotions`
- **Signature**: `def list_loyalty_promotions(program_id: str, *, status: LoyaltyPromotionStatusOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `program_id`
- **Params**: `program_id` — path · `status` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListLoyaltyPromotionsResponse`
- **Returns (raw)**: `ApiResult[ListLoyaltyPromotionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `LoyaltyPromotionStatusOrStr` | `square/models/enums/loyalty_promotion_status.py` |
| `ListLoyaltyPromotionsResponse` | `square/models/list_loyalty_promotions_response.py` |

### client.loyalty.redeem_loyalty_reward

- **Route**: `POST /v2/loyalty/rewards/{reward_id}/redeem`
- **Signature**: `def redeem_loyalty_reward(reward_id: str, body: RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `reward_id`, `body`
- **Params**: `reward_id` — path · `body` — JSON body
- **Returns (parsed)**: `RedeemLoyaltyRewardResponse`
- **Returns (raw)**: `ApiResult[RedeemLoyaltyRewardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RedeemLoyaltyRewardRequest` | `square/models/redeem_loyalty_reward_request.py` |
| `RedeemLoyaltyRewardRequestDict` | `square/models/redeem_loyalty_reward_request.py` |
| `RedeemLoyaltyRewardResponse` | `square/models/redeem_loyalty_reward_response.py` |

### client.loyalty.retrieve_loyalty_account

- **Route**: `GET /v2/loyalty/accounts/{account_id}`
- **Signature**: `def retrieve_loyalty_account(account_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `account_id`
- **Params**: `account_id` — path
- **Returns (parsed)**: `RetrieveLoyaltyAccountResponse`
- **Returns (raw)**: `ApiResult[RetrieveLoyaltyAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLoyaltyAccountResponse` | `square/models/retrieve_loyalty_account_response.py` |

### client.loyalty.retrieve_loyalty_program

- **Route**: `GET /v2/loyalty/programs/{program_id}`
- **Signature**: `def retrieve_loyalty_program(program_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `program_id`
- **Params**: `program_id` — path
- **Returns (parsed)**: `RetrieveLoyaltyProgramResponse`
- **Returns (raw)**: `ApiResult[RetrieveLoyaltyProgramResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLoyaltyProgramResponse` | `square/models/retrieve_loyalty_program_response.py` |

### client.loyalty.retrieve_loyalty_promotion

- **Route**: `GET /v2/loyalty/programs/{program_id}/promotions/{promotion_id}`
- **Signature**: `def retrieve_loyalty_promotion(promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `promotion_id`, `program_id`
- **Params**: `promotion_id` — path · `program_id` — path
- **Returns (parsed)**: `RetrieveLoyaltyPromotionResponse`
- **Returns (raw)**: `ApiResult[RetrieveLoyaltyPromotionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLoyaltyPromotionResponse` | `square/models/retrieve_loyalty_promotion_response.py` |

### client.loyalty.retrieve_loyalty_reward

- **Route**: `GET /v2/loyalty/rewards/{reward_id}`
- **Signature**: `def retrieve_loyalty_reward(reward_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `reward_id`
- **Params**: `reward_id` — path
- **Returns (parsed)**: `RetrieveLoyaltyRewardResponse`
- **Returns (raw)**: `ApiResult[RetrieveLoyaltyRewardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLoyaltyRewardResponse` | `square/models/retrieve_loyalty_reward_response.py` |

### client.loyalty.search_loyalty_accounts

- **Route**: `POST /v2/loyalty/accounts/search`
- **Signature**: `def search_loyalty_accounts(body: SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchLoyaltyAccountsResponse`
- **Returns (raw)**: `ApiResult[SearchLoyaltyAccountsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchLoyaltyAccountsRequest` | `square/models/search_loyalty_accounts_request.py` |
| `SearchLoyaltyAccountsRequestDict` | `square/models/search_loyalty_accounts_request.py` |
| `SearchLoyaltyAccountsResponse` | `square/models/search_loyalty_accounts_response.py` |

### client.loyalty.search_loyalty_events

- **Route**: `POST /v2/loyalty/events/search`
- **Signature**: `def search_loyalty_events(body: SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchLoyaltyEventsResponse`
- **Returns (raw)**: `ApiResult[SearchLoyaltyEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchLoyaltyEventsRequest` | `square/models/search_loyalty_events_request.py` |
| `SearchLoyaltyEventsRequestDict` | `square/models/search_loyalty_events_request.py` |
| `SearchLoyaltyEventsResponse` | `square/models/search_loyalty_events_response.py` |

### client.loyalty.search_loyalty_rewards

- **Route**: `POST /v2/loyalty/rewards/search`
- **Signature**: `def search_loyalty_rewards(body: SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchLoyaltyRewardsResponse`
- **Returns (raw)**: `ApiResult[SearchLoyaltyRewardsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchLoyaltyRewardsRequest` | `square/models/search_loyalty_rewards_request.py` |
| `SearchLoyaltyRewardsRequestDict` | `square/models/search_loyalty_rewards_request.py` |
| `SearchLoyaltyRewardsResponse` | `square/models/search_loyalty_rewards_response.py` |

