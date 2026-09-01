<!-- Generated file — do not edit; regenerated with the SDK. -->

# Snippets — operations

Accessor: `client.snippets` · Source: `square/apis/snippets.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.snippets.delete_snippet

- **Route**: `DELETE /v2/sites/{site_id}/snippet`
- **Auth**: `oauth2`
- **Signature**: `def delete_snippet(site_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `site_id`
- **Params**: `site_id` — path
- **Returns (parsed)**: `DeleteSnippetResponse`
- **Returns (raw)**: `ApiResult[DeleteSnippetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteSnippetResponse` | `square/models/delete_snippet_response.py` |

### client.snippets.retrieve_snippet

- **Route**: `GET /v2/sites/{site_id}/snippet`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_snippet(site_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `site_id`
- **Params**: `site_id` — path
- **Returns (parsed)**: `RetrieveSnippetResponse`
- **Returns (raw)**: `ApiResult[RetrieveSnippetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveSnippetResponse` | `square/models/retrieve_snippet_response.py` |

### client.snippets.upsert_snippet

- **Route**: `POST /v2/sites/{site_id}/snippet`
- **Auth**: `oauth2`
- **Signature**: `def upsert_snippet(site_id: str, body: UpsertSnippetRequest | UpsertSnippetRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `site_id`, `body`
- **Params**: `site_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpsertSnippetResponse`
- **Returns (raw)**: `ApiResult[UpsertSnippetResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertSnippetRequest` | `square/models/upsert_snippet_request.py` |
| `UpsertSnippetRequestDict` | `square/models/upsert_snippet_request.py` |
| `UpsertSnippetResponse` | `square/models/upsert_snippet_response.py` |

