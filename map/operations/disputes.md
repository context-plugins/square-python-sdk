<!-- Generated file — do not edit; regenerated with the SDK. -->

# Disputes — operations

Accessor: `client.disputes` · Source: `square/apis/disputes.py` · 9 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.disputes.accept_dispute

- **Route**: `POST /v2/disputes/{dispute_id}/accept`
- **Auth**: `oauth2`
- **Signature**: `def accept_dispute(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`
- **Params**: `dispute_id` — path
- **Returns (parsed)**: `AcceptDisputeResponse`
- **Returns (raw)**: `ApiResult[AcceptDisputeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `AcceptDisputeResponse` | `square/models/accept_dispute_response.py` |

### client.disputes.create_dispute_evidence_file

- **Route**: `POST /v2/disputes/{dispute_id}/evidence-files`
- **Auth**: `oauth2`
- **Signature**: `def create_dispute_evidence_file(dispute_id: str, *, request: CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`
- **Params**: `dispute_id` — path · `request` — multipart field · `image_file` — multipart file
- **Returns (parsed)**: `CreateDisputeEvidenceFileResponse`
- **Returns (raw)**: `ApiResult[CreateDisputeEvidenceFileResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateDisputeEvidenceFileRequest` | `square/models/create_dispute_evidence_file_request.py` |
| `CreateDisputeEvidenceFileRequestDict` | `square/models/create_dispute_evidence_file_request.py` |
| `CreateDisputeEvidenceFileResponse` | `square/models/create_dispute_evidence_file_response.py` |

### client.disputes.create_dispute_evidence_text

- **Route**: `POST /v2/disputes/{dispute_id}/evidence-text`
- **Auth**: `oauth2`
- **Signature**: `def create_dispute_evidence_text(dispute_id: str, body: CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`, `body`
- **Params**: `dispute_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateDisputeEvidenceTextResponse`
- **Returns (raw)**: `ApiResult[CreateDisputeEvidenceTextResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateDisputeEvidenceTextRequest` | `square/models/create_dispute_evidence_text_request.py` |
| `CreateDisputeEvidenceTextRequestDict` | `square/models/create_dispute_evidence_text_request.py` |
| `CreateDisputeEvidenceTextResponse` | `square/models/create_dispute_evidence_text_response.py` |

### client.disputes.delete_dispute_evidence

- **Route**: `DELETE /v2/disputes/{dispute_id}/evidence/{evidence_id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_dispute_evidence(dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`, `evidence_id`
- **Params**: `dispute_id` — path · `evidence_id` — path
- **Returns (parsed)**: `DeleteDisputeEvidenceResponse`
- **Returns (raw)**: `ApiResult[DeleteDisputeEvidenceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteDisputeEvidenceResponse` | `square/models/delete_dispute_evidence_response.py` |

### client.disputes.list_dispute_evidence

- **Route**: `GET /v2/disputes/{dispute_id}/evidence`
- **Auth**: `oauth2`
- **Signature**: `def list_dispute_evidence(dispute_id: str, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`
- **Params**: `dispute_id` — path · `cursor` — query
- **Returns (parsed)**: `ListDisputeEvidenceResponse`
- **Returns (raw)**: `ApiResult[ListDisputeEvidenceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListDisputeEvidenceResponse` | `square/models/list_dispute_evidence_response.py` |

### client.disputes.list_disputes

- **Route**: `GET /v2/disputes`
- **Auth**: `oauth2`
- **Signature**: `def list_disputes(*, cursor: str | None = None, states: DisputeStateOrStr | None = None, location_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `states` — query · `location_id` — query
- **Returns (parsed)**: `ListDisputesResponse`
- **Returns (raw)**: `ApiResult[ListDisputesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DisputeStateOrStr` | `square/models/enums/dispute_state.py` |
| `ListDisputesResponse` | `square/models/list_disputes_response.py` |

### client.disputes.retrieve_dispute

- **Route**: `GET /v2/disputes/{dispute_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_dispute(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`
- **Params**: `dispute_id` — path
- **Returns (parsed)**: `RetrieveDisputeResponse`
- **Returns (raw)**: `ApiResult[RetrieveDisputeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveDisputeResponse` | `square/models/retrieve_dispute_response.py` |

### client.disputes.retrieve_dispute_evidence

- **Route**: `GET /v2/disputes/{dispute_id}/evidence/{evidence_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_dispute_evidence(dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`, `evidence_id`
- **Params**: `dispute_id` — path · `evidence_id` — path
- **Returns (parsed)**: `RetrieveDisputeEvidenceResponse`
- **Returns (raw)**: `ApiResult[RetrieveDisputeEvidenceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveDisputeEvidenceResponse` | `square/models/retrieve_dispute_evidence_response.py` |

### client.disputes.submit_evidence

- **Route**: `POST /v2/disputes/{dispute_id}/submit-evidence`
- **Auth**: `oauth2`
- **Signature**: `def submit_evidence(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `dispute_id`
- **Params**: `dispute_id` — path
- **Returns (parsed)**: `SubmitEvidenceResponse`
- **Returns (raw)**: `ApiResult[SubmitEvidenceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SubmitEvidenceResponse` | `square/models/submit_evidence_response.py` |

