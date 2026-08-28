<!-- Generated file — do not edit; regenerated with the SDK. -->

# Invoices — operations

Accessor: `client.invoices` · Source: `square/apis/invoices.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.invoices.cancel_invoice

- **Route**: `POST /v2/invoices/{invoice_id}/cancel`
- **Signature**: `def cancel_invoice(invoice_id: str, body: CancelInvoiceRequest | CancelInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`, `body`
- **Params**: `invoice_id` — path · `body` — JSON body
- **Returns (parsed)**: `CancelInvoiceResponse`
- **Returns (raw)**: `ApiResult[CancelInvoiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CancelInvoiceRequest` | `square/models/cancel_invoice_request.py` |
| `CancelInvoiceRequestDict` | `square/models/cancel_invoice_request.py` |
| `CancelInvoiceResponse` | `square/models/cancel_invoice_response.py` |

### client.invoices.create_invoice

- **Route**: `POST /v2/invoices`
- **Signature**: `def create_invoice(body: CreateInvoiceRequest | CreateInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateInvoiceResponse`
- **Returns (raw)**: `ApiResult[CreateInvoiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateInvoiceRequest` | `square/models/create_invoice_request.py` |
| `CreateInvoiceRequestDict` | `square/models/create_invoice_request.py` |
| `CreateInvoiceResponse` | `square/models/create_invoice_response.py` |

### client.invoices.create_invoice_attachment

- **Route**: `POST /v2/invoices/{invoice_id}/attachments`
- **Signature**: `def create_invoice_attachment(invoice_id: str, *, request: CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`
- **Params**: `invoice_id` — path · `request` — multipart field · `image_file` — multipart file
- **Returns (parsed)**: `CreateInvoiceAttachmentResponse`
- **Returns (raw)**: `ApiResult[CreateInvoiceAttachmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateInvoiceAttachmentRequest` | `square/models/create_invoice_attachment_request.py` |
| `CreateInvoiceAttachmentRequestDict` | `square/models/create_invoice_attachment_request.py` |
| `CreateInvoiceAttachmentResponse` | `square/models/create_invoice_attachment_response.py` |

### client.invoices.delete_invoice

- **Route**: `DELETE /v2/invoices/{invoice_id}`
- **Signature**: `def delete_invoice(invoice_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`
- **Params**: `invoice_id` — path · `version` — query
- **Returns (parsed)**: `DeleteInvoiceResponse`
- **Returns (raw)**: `ApiResult[DeleteInvoiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteInvoiceResponse` | `square/models/delete_invoice_response.py` |

### client.invoices.delete_invoice_attachment

- **Route**: `DELETE /v2/invoices/{invoice_id}/attachments/{attachment_id}`
- **Signature**: `def delete_invoice_attachment(invoice_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`, `attachment_id`
- **Params**: `invoice_id` — path · `attachment_id` — path
- **Returns (parsed)**: `DeleteInvoiceAttachmentResponse`
- **Returns (raw)**: `ApiResult[DeleteInvoiceAttachmentResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteInvoiceAttachmentResponse` | `square/models/delete_invoice_attachment_response.py` |

### client.invoices.get_invoice

- **Route**: `GET /v2/invoices/{invoice_id}`
- **Signature**: `def get_invoice(invoice_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`
- **Params**: `invoice_id` — path
- **Returns (parsed)**: `GetInvoiceResponse`
- **Returns (raw)**: `ApiResult[GetInvoiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetInvoiceResponse` | `square/models/get_invoice_response.py` |

### client.invoices.list_invoices

- **Route**: `GET /v2/invoices`
- **Signature**: `def list_invoices(location_id: str, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListInvoicesResponse`
- **Returns (raw)**: `ApiResult[ListInvoicesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListInvoicesResponse` | `square/models/list_invoices_response.py` |

### client.invoices.publish_invoice

- **Route**: `POST /v2/invoices/{invoice_id}/publish`
- **Signature**: `def publish_invoice(invoice_id: str, body: PublishInvoiceRequest | PublishInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`, `body`
- **Params**: `invoice_id` — path · `body` — JSON body
- **Returns (parsed)**: `PublishInvoiceResponse`
- **Returns (raw)**: `ApiResult[PublishInvoiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublishInvoiceRequest` | `square/models/publish_invoice_request.py` |
| `PublishInvoiceRequestDict` | `square/models/publish_invoice_request.py` |
| `PublishInvoiceResponse` | `square/models/publish_invoice_response.py` |

### client.invoices.search_invoices

- **Route**: `POST /v2/invoices/search`
- **Signature**: `def search_invoices(body: SearchInvoicesRequest | SearchInvoicesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchInvoicesResponse`
- **Returns (raw)**: `ApiResult[SearchInvoicesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchInvoicesRequest` | `square/models/search_invoices_request.py` |
| `SearchInvoicesRequestDict` | `square/models/search_invoices_request.py` |
| `SearchInvoicesResponse` | `square/models/search_invoices_response.py` |

### client.invoices.update_invoice

- **Route**: `PUT /v2/invoices/{invoice_id}`
- **Signature**: `def update_invoice(invoice_id: str, body: UpdateInvoiceRequest | UpdateInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `invoice_id`, `body`
- **Params**: `invoice_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateInvoiceResponse`
- **Returns (raw)**: `ApiResult[UpdateInvoiceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateInvoiceRequest` | `square/models/update_invoice_request.py` |
| `UpdateInvoiceRequestDict` | `square/models/update_invoice_request.py` |
| `UpdateInvoiceResponse` | `square/models/update_invoice_response.py` |

