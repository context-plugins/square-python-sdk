<!-- Generated file — do not edit; regenerated with the SDK. -->

# Subscriptions — operations

Accessor: `client.subscriptions` · Source: `square/apis/subscriptions.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.subscriptions.bulk_swap_plan

- **Route**: `POST /v2/subscriptions/bulk-swap-plan`
- **Auth**: `oauth2`
- **Signature**: `def bulk_swap_plan(body: BulkSwapPlanRequest | BulkSwapPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkSwapPlanResponse`
- **Returns (raw)**: `ApiResult[BulkSwapPlanResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkSwapPlanRequest` | `square/models/bulk_swap_plan_request.py` |
| `BulkSwapPlanRequestDict` | `square/models/bulk_swap_plan_request.py` |
| `BulkSwapPlanResponse` | `square/models/bulk_swap_plan_response.py` |

### client.subscriptions.cancel_subscription

- **Route**: `POST /v2/subscriptions/{subscription_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_subscription(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path
- **Returns (parsed)**: `CancelSubscriptionResponse`
- **Returns (raw)**: `ApiResult[CancelSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelSubscriptionResponse` | `square/models/cancel_subscription_response.py` |

### client.subscriptions.change_billing_anchor_date

- **Route**: `POST /v2/subscriptions/{subscription_id}/billing-anchor`
- **Auth**: `oauth2`
- **Signature**: `def change_billing_anchor_date(subscription_id: str, body: ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `ChangeBillingAnchorDateResponse`
- **Returns (raw)**: `ApiResult[ChangeBillingAnchorDateResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ChangeBillingAnchorDateRequest` | `square/models/change_billing_anchor_date_request.py` |
| `ChangeBillingAnchorDateRequestDict` | `square/models/change_billing_anchor_date_request.py` |
| `ChangeBillingAnchorDateResponse` | `square/models/change_billing_anchor_date_response.py` |

### client.subscriptions.create_subscription

- **Route**: `POST /v2/subscriptions`
- **Auth**: `oauth2`
- **Signature**: `def create_subscription(body: CreateSubscriptionRequest | CreateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateSubscriptionResponse`
- **Returns (raw)**: `ApiResult[CreateSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateSubscriptionRequest` | `square/models/create_subscription_request.py` |
| `CreateSubscriptionRequestDict` | `square/models/create_subscription_request.py` |
| `CreateSubscriptionResponse` | `square/models/create_subscription_response.py` |

### client.subscriptions.delete_subscription_action

- **Route**: `DELETE /v2/subscriptions/{subscription_id}/actions/{action_id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_subscription_action(subscription_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `action_id`
- **Params**: `subscription_id` — path · `action_id` — path
- **Returns (parsed)**: `DeleteSubscriptionActionResponse`
- **Returns (raw)**: `ApiResult[DeleteSubscriptionActionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteSubscriptionActionResponse` | `square/models/delete_subscription_action_response.py` |

### client.subscriptions.list_subscription_events

- **Route**: `GET /v2/subscriptions/{subscription_id}/events`
- **Auth**: `oauth2`
- **Signature**: `def list_subscription_events(subscription_id: str, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListSubscriptionEventsResponse`
- **Returns (raw)**: `ApiResult[ListSubscriptionEventsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSubscriptionEventsResponse` | `square/models/list_subscription_events_response.py` |

### client.subscriptions.pause_subscription

- **Route**: `POST /v2/subscriptions/{subscription_id}/pause`
- **Auth**: `oauth2`
- **Signature**: `def pause_subscription(subscription_id: str, body: PauseSubscriptionRequest | PauseSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `PauseSubscriptionResponse`
- **Returns (raw)**: `ApiResult[PauseSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PauseSubscriptionRequest` | `square/models/pause_subscription_request.py` |
| `PauseSubscriptionRequestDict` | `square/models/pause_subscription_request.py` |
| `PauseSubscriptionResponse` | `square/models/pause_subscription_response.py` |

### client.subscriptions.resume_subscription

- **Route**: `POST /v2/subscriptions/{subscription_id}/resume`
- **Auth**: `oauth2`
- **Signature**: `def resume_subscription(subscription_id: str, body: ResumeSubscriptionRequest | ResumeSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `ResumeSubscriptionResponse`
- **Returns (raw)**: `ApiResult[ResumeSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ResumeSubscriptionRequest` | `square/models/resume_subscription_request.py` |
| `ResumeSubscriptionRequestDict` | `square/models/resume_subscription_request.py` |
| `ResumeSubscriptionResponse` | `square/models/resume_subscription_response.py` |

### client.subscriptions.retrieve_subscription

- **Route**: `GET /v2/subscriptions/{subscription_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_subscription(subscription_id: str, *, include: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path · `include` — query
- **Returns (parsed)**: `RetrieveSubscriptionResponse`
- **Returns (raw)**: `ApiResult[RetrieveSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveSubscriptionResponse` | `square/models/retrieve_subscription_response.py` |

### client.subscriptions.search_subscriptions

- **Route**: `POST /v2/subscriptions/search`
- **Auth**: `oauth2`
- **Signature**: `def search_subscriptions(body: SearchSubscriptionsRequest | SearchSubscriptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchSubscriptionsResponse`
- **Returns (raw)**: `ApiResult[SearchSubscriptionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchSubscriptionsRequest` | `square/models/search_subscriptions_request.py` |
| `SearchSubscriptionsRequestDict` | `square/models/search_subscriptions_request.py` |
| `SearchSubscriptionsResponse` | `square/models/search_subscriptions_response.py` |

### client.subscriptions.swap_plan

- **Route**: `POST /v2/subscriptions/{subscription_id}/swap-plan`
- **Auth**: `oauth2`
- **Signature**: `def swap_plan(subscription_id: str, body: SwapPlanRequest | SwapPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `SwapPlanResponse`
- **Returns (raw)**: `ApiResult[SwapPlanResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SwapPlanRequest` | `square/models/swap_plan_request.py` |
| `SwapPlanRequestDict` | `square/models/swap_plan_request.py` |
| `SwapPlanResponse` | `square/models/swap_plan_response.py` |

### client.subscriptions.update_subscription

- **Route**: `PUT /v2/subscriptions/{subscription_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_subscription(subscription_id: str, body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateSubscriptionResponse`
- **Returns (raw)**: `ApiResult[UpdateSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateSubscriptionRequest` | `square/models/update_subscription_request.py` |
| `UpdateSubscriptionRequestDict` | `square/models/update_subscription_request.py` |
| `UpdateSubscriptionResponse` | `square/models/update_subscription_response.py` |

