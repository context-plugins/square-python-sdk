<!-- Generated file — do not edit; regenerated with the SDK. -->

# CheckoutApi — operations

Accessor: `client.checkout_api` · Source: `square/apis/checkout_api.py` · 10 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.checkout_api.create_checkout

- **Route**: `POST /v2/locations/{location_id}/checkouts`
- **Auth**: `oauth2`
- **Signature**: `def create_checkout(location_id: str, body: CreateCheckoutRequest | CreateCheckoutRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `body`
- **Params**: `location_id` — path · `body` — JSON body
- **Returns (parsed)**: `CreateCheckoutResponse`
- **Returns (raw)**: `ApiResult[CreateCheckoutResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateCheckoutRequest` | `square/models/create_checkout_request.py` |
| `CreateCheckoutRequestDict` | `square/models/create_checkout_request.py` |
| `CreateCheckoutResponse` | `square/models/create_checkout_response.py` |

### client.checkout_api.create_payment_link

- **Route**: `POST /v2/online-checkout/payment-links`
- **Auth**: `oauth2`
- **Signature**: `def create_payment_link(body: CreatePaymentLinkRequest | CreatePaymentLinkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreatePaymentLinkResponse`
- **Returns (raw)**: `ApiResult[CreatePaymentLinkResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreatePaymentLinkRequest` | `square/models/create_payment_link_request.py` |
| `CreatePaymentLinkRequestDict` | `square/models/create_payment_link_request.py` |
| `CreatePaymentLinkResponse` | `square/models/create_payment_link_response.py` |

### client.checkout_api.delete_payment_link

- **Route**: `DELETE /v2/online-checkout/payment-links/{id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_payment_link(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `DeletePaymentLinkResponse`
- **Returns (raw)**: `ApiResult[DeletePaymentLinkResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeletePaymentLinkResponse` | `square/models/delete_payment_link_response.py` |

### client.checkout_api.list_payment_links

- **Route**: `GET /v2/online-checkout/payment-links`
- **Auth**: `oauth2`
- **Signature**: `def list_payment_links(*, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListPaymentLinksResponse`
- **Returns (raw)**: `ApiResult[ListPaymentLinksResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListPaymentLinksResponse` | `square/models/list_payment_links_response.py` |

### client.checkout_api.retrieve_location_settings

- **Route**: `GET /v2/online-checkout/location-settings/{location_id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_location_settings(location_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`
- **Params**: `location_id` — path
- **Returns (parsed)**: `RetrieveLocationSettingsResponse`
- **Returns (raw)**: `ApiResult[RetrieveLocationSettingsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveLocationSettingsResponse` | `square/models/retrieve_location_settings_response.py` |

### client.checkout_api.retrieve_merchant_settings

- **Route**: `GET /v2/online-checkout/merchant-settings`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_merchant_settings(*, request_options: RequestOptionsOrDict | None = None)`
- **Returns (parsed)**: `RetrieveMerchantSettingsResponse`
- **Returns (raw)**: `ApiResult[RetrieveMerchantSettingsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveMerchantSettingsResponse` | `square/models/retrieve_merchant_settings_response.py` |

### client.checkout_api.retrieve_payment_link

- **Route**: `GET /v2/online-checkout/payment-links/{id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_payment_link(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `RetrievePaymentLinkResponse`
- **Returns (raw)**: `ApiResult[RetrievePaymentLinkResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrievePaymentLinkResponse` | `square/models/retrieve_payment_link_response.py` |

### client.checkout_api.update_location_settings

- **Route**: `PUT /v2/online-checkout/location-settings/{location_id}`
- **Auth**: `oauth2`
- **Signature**: `def update_location_settings(location_id: str, body: UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `location_id`, `body`
- **Params**: `location_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateLocationSettingsResponse`
- **Returns (raw)**: `ApiResult[UpdateLocationSettingsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateLocationSettingsRequest` | `square/models/update_location_settings_request.py` |
| `UpdateLocationSettingsRequestDict` | `square/models/update_location_settings_request.py` |
| `UpdateLocationSettingsResponse` | `square/models/update_location_settings_response.py` |

### client.checkout_api.update_merchant_settings

- **Route**: `PUT /v2/online-checkout/merchant-settings`
- **Auth**: `oauth2`
- **Signature**: `def update_merchant_settings(body: UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `UpdateMerchantSettingsResponse`
- **Returns (raw)**: `ApiResult[UpdateMerchantSettingsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateMerchantSettingsRequest` | `square/models/update_merchant_settings_request.py` |
| `UpdateMerchantSettingsRequestDict` | `square/models/update_merchant_settings_request.py` |
| `UpdateMerchantSettingsResponse` | `square/models/update_merchant_settings_response.py` |

### client.checkout_api.update_payment_link

- **Route**: `PUT /v2/online-checkout/payment-links/{id}`
- **Auth**: `oauth2`
- **Signature**: `def update_payment_link(id: str, body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`, `body`
- **Params**: `id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdatePaymentLinkResponse`
- **Returns (raw)**: `ApiResult[UpdatePaymentLinkResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdatePaymentLinkRequest` | `square/models/update_payment_link_request.py` |
| `UpdatePaymentLinkRequestDict` | `square/models/update_payment_link_request.py` |
| `UpdatePaymentLinkResponse` | `square/models/update_payment_link_response.py` |

