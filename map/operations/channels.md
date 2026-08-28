<!-- Generated file — do not edit; regenerated with the SDK. -->

# Channels — operations

Accessor: `client.channels` · Source: `square/apis/channels.py` · 3 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.channels.bulk_retrieve_channels

- **Route**: `POST /v2/channels/bulk-retrieve`
- **Signature**: `def bulk_retrieve_channels(body: BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkRetrieveChannelsResponse`
- **Returns (raw)**: `ApiResult[BulkRetrieveChannelsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkRetrieveChannelsRequest` | `square/models/bulk_retrieve_channels_request.py` |
| `BulkRetrieveChannelsRequestDict` | `square/models/bulk_retrieve_channels_request.py` |
| `BulkRetrieveChannelsResponse` | `square/models/bulk_retrieve_channels_response.py` |

### client.channels.list_channels

- **Route**: `GET /v2/channels`
- **Signature**: `def list_channels(*, reference_type: ReferenceTypeOrStr | None = None, reference_id: str | None = None, status: ChannelStatusOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `reference_type` — query · `reference_id` — query · `status` — query · `cursor` — query · `limit` — query
- **Returns (parsed)**: `ListChannelsResponse`
- **Returns (raw)**: `ApiResult[ListChannelsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ReferenceTypeOrStr` | `square/models/enums/reference_type.py` |
| `ChannelStatusOrStr` | `square/models/enums/channel_status.py` |
| `ListChannelsResponse` | `square/models/list_channels_response.py` |

### client.channels.retrieve_channel

- **Route**: `GET /v2/channels/{channel_id}`
- **Signature**: `def retrieve_channel(channel_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `channel_id`
- **Params**: `channel_id` — path
- **Returns (parsed)**: `RetrieveChannelResponse`
- **Returns (raw)**: `ApiResult[RetrieveChannelResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveChannelResponse` | `square/models/retrieve_channel_response.py` |

