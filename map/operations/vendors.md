<!-- Generated file — do not edit; regenerated with the SDK. -->

# Vendors — operations

Accessor: `client.vendors` · Source: `square/apis/vendors.py` · 7 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.vendors.bulk_create_vendors

- **Route**: `POST /v2/vendors/bulk-create`
- **Auth**: `oauth2`
- **Signature**: `def bulk_create_vendors(body: BulkCreateVendorsRequest | BulkCreateVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkCreateVendorsResponse`
- **Returns (raw)**: `ApiResult[BulkCreateVendorsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkCreateVendorsRequest` | `square/models/bulk_create_vendors_request.py` |
| `BulkCreateVendorsRequestDict` | `square/models/bulk_create_vendors_request.py` |
| `BulkCreateVendorsResponse` | `square/models/bulk_create_vendors_response.py` |

### client.vendors.bulk_retrieve_vendors

- **Route**: `POST /v2/vendors/bulk-retrieve`
- **Auth**: `oauth2`
- **Signature**: `def bulk_retrieve_vendors(body: BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkRetrieveVendorsResponse`
- **Returns (raw)**: `ApiResult[BulkRetrieveVendorsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkRetrieveVendorsRequest` | `square/models/bulk_retrieve_vendors_request.py` |
| `BulkRetrieveVendorsRequestDict` | `square/models/bulk_retrieve_vendors_request.py` |
| `BulkRetrieveVendorsResponse` | `square/models/bulk_retrieve_vendors_response.py` |

### client.vendors.bulk_update_vendors

- **Route**: `PUT /v2/vendors/bulk-update`
- **Auth**: `oauth2`
- **Signature**: `def bulk_update_vendors(body: BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpdateVendorsResponse`
- **Returns (raw)**: `ApiResult[BulkUpdateVendorsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpdateVendorsRequest` | `square/models/bulk_update_vendors_request.py` |
| `BulkUpdateVendorsRequestDict` | `square/models/bulk_update_vendors_request.py` |
| `BulkUpdateVendorsResponse` | `square/models/bulk_update_vendors_response.py` |

### client.vendors.create_vendor

- **Route**: `POST /v2/vendors/create`
- **Auth**: `oauth2`
- **Signature**: `def create_vendor(body: CreateVendorRequest | CreateVendorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateVendorResponse`
- **Returns (raw)**: `ApiResult[CreateVendorResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateVendorRequest` | `square/models/create_vendor_request.py` |
| `CreateVendorRequestDict` | `square/models/create_vendor_request.py` |
| `CreateVendorResponse` | `square/models/create_vendor_response.py` |

### client.vendors.retrieve_vendor

- **Route**: `GET /v2/vendors/{vendor_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_vendor(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`
- **Params**: `vendor_id` — path
- **Returns (parsed)**: `RetrieveVendorResponse`
- **Returns (raw)**: `ApiResult[RetrieveVendorResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveVendorResponse` | `square/models/retrieve_vendor_response.py` |

### client.vendors.search_vendors

- **Route**: `POST /v2/vendors/search`
- **Auth**: `oauth2`
- **Signature**: `def search_vendors(body: SearchVendorsRequest | SearchVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchVendorsResponse`
- **Returns (raw)**: `ApiResult[SearchVendorsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchVendorsRequest` | `square/models/search_vendors_request.py` |
| `SearchVendorsRequestDict` | `square/models/search_vendors_request.py` |
| `SearchVendorsResponse` | `square/models/search_vendors_response.py` |

### client.vendors.update_vendor

- **Route**: `PUT /v2/vendors/{vendor_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_vendor(vendor_id: str, body: UpdateVendorRequest | UpdateVendorRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `vendor_id`, `body`
- **Params**: `vendor_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateVendorResponse`
- **Returns (raw)**: `ApiResult[UpdateVendorResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateVendorRequest` | `square/models/update_vendor_request.py` |
| `UpdateVendorRequestDict` | `square/models/update_vendor_request.py` |
| `UpdateVendorResponse` | `square/models/update_vendor_response.py` |

