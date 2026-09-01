<!-- Generated file — do not edit; regenerated with the SDK. -->

# ApplePay — operations

Accessor: `client.apple_pay` · Source: `square/apis/apple_pay.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.apple_pay.register_domain

- **Route**: `POST /v2/apple-pay/domains`
- **Auth**: `oauth2`
- **Signature**: `def register_domain(body: RegisterDomainRequest | RegisterDomainRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `RegisterDomainResponse`
- **Returns (raw)**: `ApiResult[RegisterDomainResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RegisterDomainRequest` | `square/models/register_domain_request.py` |
| `RegisterDomainRequestDict` | `square/models/register_domain_request.py` |
| `RegisterDomainResponse` | `square/models/register_domain_response.py` |

