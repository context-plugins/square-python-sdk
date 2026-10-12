<!-- Generated file — do not edit; regenerated with the SDK. -->

# Devices — operations

Accessor: `client.devices` · Source: `square/apis/devices.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.devices.create_device_code

- **Route**: `POST /v2/devices/codes`
- **Auth**: `oauth2`
- **Signature**: `def create_device_code(body: CreateDeviceCodeRequest | CreateDeviceCodeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateDeviceCodeResponse`
- **Returns (raw)**: `ApiResult[CreateDeviceCodeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateDeviceCodeRequest` | `square/models/create_device_code_request.py` |
| `CreateDeviceCodeRequestDict` | `square/models/create_device_code_request.py` |
| `CreateDeviceCodeResponse` | `square/models/create_device_code_response.py` |

### client.devices.get_device

- **Route**: `GET /v2/devices/{device_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_device(device_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `device_id`
- **Params**: `device_id` — path
- **Returns (parsed)**: `GetDeviceResponse`
- **Returns (raw)**: `ApiResult[GetDeviceResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetDeviceResponse` | `square/models/get_device_response.py` |

### client.devices.get_device_code

- **Route**: `GET /v2/devices/codes/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_device_code(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GetDeviceCodeResponse`
- **Returns (raw)**: `ApiResult[GetDeviceCodeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetDeviceCodeResponse` | `square/models/get_device_code_response.py` |

### client.devices.list_device_codes

- **Route**: `GET /v2/devices/codes`
- **Auth**: `oauth2`
- **Signature**: `def list_device_codes(*, cursor: str | None = None, location_id: str | None = None, product_type: ProductTypeOrStr | None = None, status: DeviceCodeStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `location_id` — query · `product_type` — query · `status` — query
- **Returns (parsed)**: `ListDeviceCodesResponse`
- **Returns (raw)**: `ApiResult[ListDeviceCodesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ProductTypeOrStr` | `square/models/enums/product_type.py` |
| `DeviceCodeStatusOrStr` | `square/models/enums/device_code_status.py` |
| `ListDeviceCodesResponse` | `square/models/list_device_codes_response.py` |

### client.devices.list_devices

- **Route**: `GET /v2/devices`
- **Auth**: `oauth2`
- **Signature**: `def list_devices(*, cursor: str | None = None, sort_order: SortOrderOrStr | None = None, limit: int | None = None, location_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `sort_order` — query · `limit` — query · `location_id` — query
- **Returns (parsed)**: `ListDevicesResponse`
- **Returns (raw)**: `ApiResult[ListDevicesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SortOrderOrStr` | `square/models/enums/sort_order.py` |
| `ListDevicesResponse` | `square/models/list_devices_response.py` |

