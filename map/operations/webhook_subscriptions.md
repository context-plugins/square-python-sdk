<!-- Generated file — do not edit; regenerated with the SDK. -->

# WebhookSubscriptions — operations

Accessor: `client.webhook_subscriptions` · Source: `square/apis/webhook_subscriptions.py` · 8 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.webhook_subscriptions.create_webhook_subscription

- **Route**: `POST /v2/webhooks/subscriptions`
- **Auth**: `oauth2`
- **Signature**: `def create_webhook_subscription(body: CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateWebhookSubscriptionResponse`
- **Returns (raw)**: `ApiResult[CreateWebhookSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateWebhookSubscriptionRequest` | `square/models/create_webhook_subscription_request.py` |
| `CreateWebhookSubscriptionRequestDict` | `square/models/create_webhook_subscription_request.py` |
| `CreateWebhookSubscriptionResponse` | `square/models/create_webhook_subscription_response.py` |

### client.webhook_subscriptions.delete_webhook_subscription

- **Route**: `DELETE /v2/webhooks/subscriptions/{subscription_id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_webhook_subscription(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path
- **Returns (parsed)**: `DeleteWebhookSubscriptionResponse`
- **Returns (raw)**: `ApiResult[DeleteWebhookSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteWebhookSubscriptionResponse` | `square/models/delete_webhook_subscription_response.py` |

### client.webhook_subscriptions.list_webhook_event_types

- **Route**: `GET /v2/webhooks/event-types`
- **Auth**: `oauth2`
- **Signature**: `def list_webhook_event_types(*, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `api_version` — query
- **Returns (parsed)**: `ListWebhookEventTypesResponse`
- **Returns (raw)**: `ApiResult[ListWebhookEventTypesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWebhookEventTypesResponse` | `square/models/list_webhook_event_types_response.py` |

### client.webhook_subscriptions.list_webhook_subscriptions

- **Route**: `GET /v2/webhooks/subscriptions`
- **Auth**: `oauth2`
- **Signature**: `def list_webhook_subscriptions(*, cursor: str | None = None, include_disabled: bool | None = False, sort_order: SortOrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `include_disabled` — query · `sort_order` — query · `limit` — query
- **Returns (parsed)**: `ListWebhookSubscriptionsResponse`
- **Returns (raw)**: `ApiResult[ListWebhookSubscriptionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListWebhookSubscriptionsResponse` | `square/models/list_webhook_subscriptions_response.py` |

### client.webhook_subscriptions.retrieve_webhook_subscription

- **Route**: `GET /v2/webhooks/subscriptions/{subscription_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_webhook_subscription(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`
- **Params**: `subscription_id` — path
- **Returns (parsed)**: `RetrieveWebhookSubscriptionResponse`
- **Returns (raw)**: `ApiResult[RetrieveWebhookSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveWebhookSubscriptionResponse` | `square/models/retrieve_webhook_subscription_response.py` |

### client.webhook_subscriptions.test_webhook_subscription

- **Route**: `POST /v2/webhooks/subscriptions/{subscription_id}/test`
- **Auth**: `oauth2`
- **Signature**: `def test_webhook_subscription(subscription_id: str, body: TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `TestWebhookSubscriptionResponse`
- **Returns (raw)**: `ApiResult[TestWebhookSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `TestWebhookSubscriptionRequest` | `square/models/test_webhook_subscription_request.py` |
| `TestWebhookSubscriptionRequestDict` | `square/models/test_webhook_subscription_request.py` |
| `TestWebhookSubscriptionResponse` | `square/models/test_webhook_subscription_response.py` |

### client.webhook_subscriptions.update_webhook_subscription

- **Route**: `PUT /v2/webhooks/subscriptions/{subscription_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_webhook_subscription(subscription_id: str, body: UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateWebhookSubscriptionResponse`
- **Returns (raw)**: `ApiResult[UpdateWebhookSubscriptionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateWebhookSubscriptionRequest` | `square/models/update_webhook_subscription_request.py` |
| `UpdateWebhookSubscriptionRequestDict` | `square/models/update_webhook_subscription_request.py` |
| `UpdateWebhookSubscriptionResponse` | `square/models/update_webhook_subscription_response.py` |

### client.webhook_subscriptions.update_webhook_subscription_signature_key

- **Route**: `POST /v2/webhooks/subscriptions/{subscription_id}/signature-key`
- **Auth**: `oauth2`
- **Signature**: `def update_webhook_subscription_signature_key(subscription_id: str, body: UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `subscription_id`, `body`
- **Params**: `subscription_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateWebhookSubscriptionSignatureKeyResponse`
- **Returns (raw)**: `ApiResult[UpdateWebhookSubscriptionSignatureKeyResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateWebhookSubscriptionSignatureKeyRequest` | `square/models/update_webhook_subscription_signature_key_request.py` |
| `UpdateWebhookSubscriptionSignatureKeyRequestDict` | `square/models/update_webhook_subscription_signature_key_request.py` |
| `UpdateWebhookSubscriptionSignatureKeyResponse` | `square/models/update_webhook_subscription_signature_key_response.py` |

