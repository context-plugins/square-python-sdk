<!-- Generated file — do not edit; regenerated with the SDK. -->

# Oauth — operations

Accessor: `client.oauth` · Source: `square/apis/oauth.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.oauth.obtain_token

- **Route**: `POST /oauth2/token`
- **Signature**: `def obtain_token(body: ObtainTokenRequest | ObtainTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `ObtainTokenResponse`
- **Returns (raw)**: `ApiResult[ObtainTokenResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ObtainTokenRequest` | `square/models/obtain_token_request.py` |
| `ObtainTokenRequestDict` | `square/models/obtain_token_request.py` |
| `ObtainTokenResponse` | `square/models/obtain_token_response.py` |

### client.oauth.retrieve_token_status

- **Route**: `POST /oauth2/token/status`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_token_status(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `RetrieveTokenStatusResponse`
- **Returns (raw)**: `ApiResult[RetrieveTokenStatusResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveTokenStatusResponse` | `square/models/retrieve_token_status_response.py` |

### client.oauth.revoke_token

- **Route**: `POST /oauth2/revoke`
- **Signature**: `def revoke_token(body: RevokeTokenRequest | RevokeTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RevokeTokenResponse`
- **Returns (raw)**: `ApiResult[RevokeTokenResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RevokeTokenRequest` | `square/models/revoke_token_request.py` |
| `RevokeTokenRequestDict` | `square/models/revoke_token_request.py` |
| `RevokeTokenResponse` | `square/models/revoke_token_response.py` |

