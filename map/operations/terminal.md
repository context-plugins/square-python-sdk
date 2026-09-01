<!-- Generated file — do not edit; regenerated with the SDK. -->

# Terminal — operations

Accessor: `client.terminal` · Source: `square/apis/terminal.py` · 15 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.terminal.cancel_terminal_action

- **Route**: `POST /v2/terminals/actions/{action_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_terminal_action(action_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `action_id`
- **Params**: `action_id` — path
- **Returns (parsed)**: `CancelTerminalActionResponse`
- **Returns (raw)**: `ApiResult[CancelTerminalActionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelTerminalActionResponse` | `square/models/cancel_terminal_action_response.py` |

### client.terminal.cancel_terminal_checkout

- **Route**: `POST /v2/terminals/checkouts/{checkout_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_terminal_checkout(checkout_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `checkout_id`
- **Params**: `checkout_id` — path
- **Returns (parsed)**: `CancelTerminalCheckoutResponse`
- **Returns (raw)**: `ApiResult[CancelTerminalCheckoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelTerminalCheckoutResponse` | `square/models/cancel_terminal_checkout_response.py` |

### client.terminal.cancel_terminal_refund

- **Route**: `POST /v2/terminals/refunds/{terminal_refund_id}/cancel`
- **Auth**: `oauth2`
- **Signature**: `def cancel_terminal_refund(terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_refund_id`
- **Params**: `terminal_refund_id` — path
- **Returns (parsed)**: `CancelTerminalRefundResponse`
- **Returns (raw)**: `ApiResult[CancelTerminalRefundResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelTerminalRefundResponse` | `square/models/cancel_terminal_refund_response.py` |

### client.terminal.create_terminal_action

- **Route**: `POST /v2/terminals/actions`
- **Auth**: `oauth2`
- **Signature**: `def create_terminal_action(body: CreateTerminalActionRequest | CreateTerminalActionRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTerminalActionResponse`
- **Returns (raw)**: `ApiResult[CreateTerminalActionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTerminalActionRequest` | `square/models/create_terminal_action_request.py` |
| `CreateTerminalActionRequestDict` | `square/models/create_terminal_action_request.py` |
| `CreateTerminalActionResponse` | `square/models/create_terminal_action_response.py` |

### client.terminal.create_terminal_checkout

- **Route**: `POST /v2/terminals/checkouts`
- **Auth**: `oauth2`
- **Signature**: `def create_terminal_checkout(body: CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTerminalCheckoutResponse`
- **Returns (raw)**: `ApiResult[CreateTerminalCheckoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTerminalCheckoutRequest` | `square/models/create_terminal_checkout_request.py` |
| `CreateTerminalCheckoutRequestDict` | `square/models/create_terminal_checkout_request.py` |
| `CreateTerminalCheckoutResponse` | `square/models/create_terminal_checkout_response.py` |

### client.terminal.create_terminal_refund

- **Route**: `POST /v2/terminals/refunds`
- **Auth**: `oauth2`
- **Signature**: `def create_terminal_refund(body: CreateTerminalRefundRequest | CreateTerminalRefundRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTerminalRefundResponse`
- **Returns (raw)**: `ApiResult[CreateTerminalRefundResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTerminalRefundRequest` | `square/models/create_terminal_refund_request.py` |
| `CreateTerminalRefundRequestDict` | `square/models/create_terminal_refund_request.py` |
| `CreateTerminalRefundResponse` | `square/models/create_terminal_refund_response.py` |

### client.terminal.dismiss_terminal_action

- **Route**: `POST /v2/terminals/actions/{action_id}/dismiss`
- **Auth**: `oauth2`
- **Signature**: `def dismiss_terminal_action(action_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `action_id`
- **Params**: `action_id` — path
- **Returns (parsed)**: `DismissTerminalActionResponse`
- **Returns (raw)**: `ApiResult[DismissTerminalActionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DismissTerminalActionResponse` | `square/models/dismiss_terminal_action_response.py` |

### client.terminal.dismiss_terminal_checkout

- **Route**: `POST /v2/terminals/checkouts/{checkout_id}/dismiss`
- **Auth**: `oauth2`
- **Signature**: `def dismiss_terminal_checkout(checkout_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `checkout_id`
- **Params**: `checkout_id` — path
- **Returns (parsed)**: `DismissTerminalCheckoutResponse`
- **Returns (raw)**: `ApiResult[DismissTerminalCheckoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DismissTerminalCheckoutResponse` | `square/models/dismiss_terminal_checkout_response.py` |

### client.terminal.dismiss_terminal_refund

- **Route**: `POST /v2/terminals/refunds/{terminal_refund_id}/dismiss`
- **Auth**: `oauth2`
- **Signature**: `def dismiss_terminal_refund(terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_refund_id`
- **Params**: `terminal_refund_id` — path
- **Returns (parsed)**: `DismissTerminalRefundResponse`
- **Returns (raw)**: `ApiResult[DismissTerminalRefundResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DismissTerminalRefundResponse` | `square/models/dismiss_terminal_refund_response.py` |

### client.terminal.get_terminal_action

- **Route**: `GET /v2/terminals/actions/{action_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_terminal_action(action_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `action_id`
- **Params**: `action_id` — path
- **Returns (parsed)**: `GetTerminalActionResponse`
- **Returns (raw)**: `ApiResult[GetTerminalActionResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetTerminalActionResponse` | `square/models/get_terminal_action_response.py` |

### client.terminal.get_terminal_checkout

- **Route**: `GET /v2/terminals/checkouts/{checkout_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_terminal_checkout(checkout_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `checkout_id`
- **Params**: `checkout_id` — path
- **Returns (parsed)**: `GetTerminalCheckoutResponse`
- **Returns (raw)**: `ApiResult[GetTerminalCheckoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetTerminalCheckoutResponse` | `square/models/get_terminal_checkout_response.py` |

### client.terminal.get_terminal_refund

- **Route**: `GET /v2/terminals/refunds/{terminal_refund_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_terminal_refund(terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `terminal_refund_id`
- **Params**: `terminal_refund_id` — path
- **Returns (parsed)**: `GetTerminalRefundResponse`
- **Returns (raw)**: `ApiResult[GetTerminalRefundResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetTerminalRefundResponse` | `square/models/get_terminal_refund_response.py` |

### client.terminal.search_terminal_actions

- **Route**: `POST /v2/terminals/actions/search`
- **Auth**: `oauth2`
- **Signature**: `def search_terminal_actions(body: SearchTerminalActionsRequest | SearchTerminalActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchTerminalActionsResponse`
- **Returns (raw)**: `ApiResult[SearchTerminalActionsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchTerminalActionsRequest` | `square/models/search_terminal_actions_request.py` |
| `SearchTerminalActionsRequestDict` | `square/models/search_terminal_actions_request.py` |
| `SearchTerminalActionsResponse` | `square/models/search_terminal_actions_response.py` |

### client.terminal.search_terminal_checkouts

- **Route**: `POST /v2/terminals/checkouts/search`
- **Auth**: `oauth2`
- **Signature**: `def search_terminal_checkouts(body: SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchTerminalCheckoutsResponse`
- **Returns (raw)**: `ApiResult[SearchTerminalCheckoutsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchTerminalCheckoutsRequest` | `square/models/search_terminal_checkouts_request.py` |
| `SearchTerminalCheckoutsRequestDict` | `square/models/search_terminal_checkouts_request.py` |
| `SearchTerminalCheckoutsResponse` | `square/models/search_terminal_checkouts_response.py` |

### client.terminal.search_terminal_refunds

- **Route**: `POST /v2/terminals/refunds/search`
- **Auth**: `oauth2`
- **Signature**: `def search_terminal_refunds(body: SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchTerminalRefundsResponse`
- **Returns (raw)**: `ApiResult[SearchTerminalRefundsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchTerminalRefundsRequest` | `square/models/search_terminal_refunds_request.py` |
| `SearchTerminalRefundsRequestDict` | `square/models/search_terminal_refunds_request.py` |
| `SearchTerminalRefundsResponse` | `square/models/search_terminal_refunds_response.py` |

