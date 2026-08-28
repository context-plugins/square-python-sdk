<!-- Generated file — do not edit; regenerated with the SDK. -->

# Catalog — operations

Accessor: `client.catalog` · Source: `square/apis/catalog.py` · 14 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.catalog.batch_delete_catalog_objects

- **Route**: `POST /v2/catalog/batch-delete`
- **Signature**: `def batch_delete_catalog_objects(body: BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchDeleteCatalogObjectsResponse`
- **Returns (raw)**: `ApiResult[BatchDeleteCatalogObjectsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchDeleteCatalogObjectsRequest` | `square/models/batch_delete_catalog_objects_request.py` |
| `BatchDeleteCatalogObjectsRequestDict` | `square/models/batch_delete_catalog_objects_request.py` |
| `BatchDeleteCatalogObjectsResponse` | `square/models/batch_delete_catalog_objects_response.py` |

### client.catalog.batch_retrieve_catalog_objects

- **Route**: `POST /v2/catalog/batch-retrieve`
- **Signature**: `def batch_retrieve_catalog_objects(body: BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchRetrieveCatalogObjectsResponse`
- **Returns (raw)**: `ApiResult[BatchRetrieveCatalogObjectsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchRetrieveCatalogObjectsRequest` | `square/models/batch_retrieve_catalog_objects_request.py` |
| `BatchRetrieveCatalogObjectsRequestDict` | `square/models/batch_retrieve_catalog_objects_request.py` |
| `BatchRetrieveCatalogObjectsResponse` | `square/models/batch_retrieve_catalog_objects_response.py` |

### client.catalog.batch_upsert_catalog_objects

- **Route**: `POST /v2/catalog/batch-upsert`
- **Signature**: `def batch_upsert_catalog_objects(body: BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BatchUpsertCatalogObjectsResponse`
- **Returns (raw)**: `ApiResult[BatchUpsertCatalogObjectsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BatchUpsertCatalogObjectsRequest` | `square/models/batch_upsert_catalog_objects_request.py` |
| `BatchUpsertCatalogObjectsRequestDict` | `square/models/batch_upsert_catalog_objects_request.py` |
| `BatchUpsertCatalogObjectsResponse` | `square/models/batch_upsert_catalog_objects_response.py` |

### client.catalog.catalog_info

- **Route**: `GET /v2/catalog/info`
- **Signature**: `def catalog_info(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `CatalogInfoResponse`
- **Returns (raw)**: `ApiResult[CatalogInfoResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CatalogInfoResponse` | `square/models/catalog_info_response.py` |

### client.catalog.create_catalog_image

- **Route**: `POST /v2/catalog/images`
- **Signature**: `def create_catalog_image(*, request: CreateCatalogImageRequest | CreateCatalogImageRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `request` — multipart field · `image_file` — multipart file
- **Returns (parsed)**: `CreateCatalogImageResponse`
- **Returns (raw)**: `ApiResult[CreateCatalogImageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCatalogImageRequest` | `square/models/create_catalog_image_request.py` |
| `CreateCatalogImageRequestDict` | `square/models/create_catalog_image_request.py` |
| `CreateCatalogImageResponse` | `square/models/create_catalog_image_response.py` |

### client.catalog.delete_catalog_object

- **Route**: `DELETE /v2/catalog/object/{object_id}`
- **Signature**: `def delete_catalog_object(object_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `object_id`
- **Params**: `object_id` — path
- **Returns (parsed)**: `DeleteCatalogObjectResponse`
- **Returns (raw)**: `ApiResult[DeleteCatalogObjectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteCatalogObjectResponse` | `square/models/delete_catalog_object_response.py` |

### client.catalog.list_catalog

- **Route**: `GET /v2/catalog/list`
- **Signature**: `def list_catalog(*, cursor: str | None = None, types: str | None = None, catalog_version: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `types` — query · `catalog_version` — query
- **Returns (parsed)**: `ListCatalogResponse`
- **Returns (raw)**: `ApiResult[ListCatalogResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListCatalogResponse` | `square/models/list_catalog_response.py` |

### client.catalog.retrieve_catalog_object

- **Route**: `GET /v2/catalog/object/{object_id}`
- **Signature**: `def retrieve_catalog_object(object_id: str, *, include_related_objects: bool | None = False, catalog_version: int | None = None, include_category_path_to_root: bool | None = False, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `object_id`
- **Params**: `object_id` — path · `include_related_objects` — query · `catalog_version` — query · `include_category_path_to_root` — query
- **Returns (parsed)**: `RetrieveCatalogObjectResponse`
- **Returns (raw)**: `ApiResult[RetrieveCatalogObjectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveCatalogObjectResponse` | `square/models/retrieve_catalog_object_response.py` |

### client.catalog.search_catalog_items

- **Route**: `POST /v2/catalog/search-catalog-items`
- **Signature**: `def search_catalog_items(body: SearchCatalogItemsRequest | SearchCatalogItemsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchCatalogItemsResponse`
- **Returns (raw)**: `ApiResult[SearchCatalogItemsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchCatalogItemsRequest` | `square/models/search_catalog_items_request.py` |
| `SearchCatalogItemsRequestDict` | `square/models/search_catalog_items_request.py` |
| `SearchCatalogItemsResponse` | `square/models/search_catalog_items_response.py` |

### client.catalog.search_catalog_objects

- **Route**: `POST /v2/catalog/search`
- **Signature**: `def search_catalog_objects(body: SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchCatalogObjectsResponse`
- **Returns (raw)**: `ApiResult[SearchCatalogObjectsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchCatalogObjectsRequest` | `square/models/search_catalog_objects_request.py` |
| `SearchCatalogObjectsRequestDict` | `square/models/search_catalog_objects_request.py` |
| `SearchCatalogObjectsResponse` | `square/models/search_catalog_objects_response.py` |

### client.catalog.update_catalog_image

- **Route**: `PUT /v2/catalog/images/{image_id}`
- **Signature**: `def update_catalog_image(image_id: str, *, request: UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `image_id`
- **Params**: `image_id` — path · `request` — multipart field · `image_file` — multipart file
- **Returns (parsed)**: `UpdateCatalogImageResponse`
- **Returns (raw)**: `ApiResult[UpdateCatalogImageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateCatalogImageRequest` | `square/models/update_catalog_image_request.py` |
| `UpdateCatalogImageRequestDict` | `square/models/update_catalog_image_request.py` |
| `UpdateCatalogImageResponse` | `square/models/update_catalog_image_response.py` |

### client.catalog.update_item_modifier_lists

- **Route**: `POST /v2/catalog/update-item-modifier-lists`
- **Signature**: `def update_item_modifier_lists(body: UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateItemModifierListsResponse`
- **Returns (raw)**: `ApiResult[UpdateItemModifierListsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateItemModifierListsRequest` | `square/models/update_item_modifier_lists_request.py` |
| `UpdateItemModifierListsRequestDict` | `square/models/update_item_modifier_lists_request.py` |
| `UpdateItemModifierListsResponse` | `square/models/update_item_modifier_lists_response.py` |

### client.catalog.update_item_taxes

- **Route**: `POST /v2/catalog/update-item-taxes`
- **Signature**: `def update_item_taxes(body: UpdateItemTaxesRequest | UpdateItemTaxesRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateItemTaxesResponse`
- **Returns (raw)**: `ApiResult[UpdateItemTaxesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateItemTaxesRequest` | `square/models/update_item_taxes_request.py` |
| `UpdateItemTaxesRequestDict` | `square/models/update_item_taxes_request.py` |
| `UpdateItemTaxesResponse` | `square/models/update_item_taxes_response.py` |

### client.catalog.upsert_catalog_object

- **Route**: `POST /v2/catalog/object`
- **Signature**: `def upsert_catalog_object(body: UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpsertCatalogObjectResponse`
- **Returns (raw)**: `ApiResult[UpsertCatalogObjectResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpsertCatalogObjectRequest` | `square/models/upsert_catalog_object_request.py` |
| `UpsertCatalogObjectRequestDict` | `square/models/upsert_catalog_object_request.py` |
| `UpsertCatalogObjectResponse` | `square/models/upsert_catalog_object_response.py` |

