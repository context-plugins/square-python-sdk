<!-- Generated file — do not edit; regenerated with the SDK. -->

# Sites — operations

Accessor: `client.sites` · Source: `square/apis/sites.py` · 1 operation

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.sites.list_sites

- **Route**: `GET /v2/sites`
- **Auth**: `oauth2`
- **Signature**: `def list_sites(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `ListSitesResponse`
- **Returns (raw)**: `ApiResult[ListSitesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListSitesResponse` | `square/models/list_sites_response.py` |

