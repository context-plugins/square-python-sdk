<!-- Generated file — do not edit; regenerated with the SDK. -->

# Labor — operations

Accessor: `client.labor` · Source: `square/apis/labor.py` · 27 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.labor.bulk_publish_scheduled_shifts

- **Route**: `POST /v2/labor/scheduled-shifts/bulk-publish`
- **Auth**: `oauth2`
- **Signature**: `def bulk_publish_scheduled_shifts(body: BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkPublishScheduledShiftsResponse`
- **Returns (raw)**: `ApiResult[BulkPublishScheduledShiftsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkPublishScheduledShiftsRequest` | `square/models/bulk_publish_scheduled_shifts_request.py` |
| `BulkPublishScheduledShiftsRequestDict` | `square/models/bulk_publish_scheduled_shifts_request.py` |
| `BulkPublishScheduledShiftsResponse` | `square/models/bulk_publish_scheduled_shifts_response.py` |

### client.labor.create_break_type

- **Route**: `POST /v2/labor/break-types`
- **Auth**: `oauth2`
- **Signature**: `def create_break_type(body: CreateBreakTypeRequest | CreateBreakTypeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateBreakTypeResponse`
- **Returns (raw)**: `ApiResult[CreateBreakTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateBreakTypeRequest` | `square/models/create_break_type_request.py` |
| `CreateBreakTypeRequestDict` | `square/models/create_break_type_request.py` |
| `CreateBreakTypeResponse` | `square/models/create_break_type_response.py` |

### client.labor.create_scheduled_shift

- **Route**: `POST /v2/labor/scheduled-shifts`
- **Auth**: `oauth2`
- **Signature**: `def create_scheduled_shift(body: CreateScheduledShiftRequest | CreateScheduledShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateScheduledShiftResponse`
- **Returns (raw)**: `ApiResult[CreateScheduledShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateScheduledShiftRequest` | `square/models/create_scheduled_shift_request.py` |
| `CreateScheduledShiftRequestDict` | `square/models/create_scheduled_shift_request.py` |
| `CreateScheduledShiftResponse` | `square/models/create_scheduled_shift_response.py` |

### client.labor.create_shift

- **Route**: `POST /v2/labor/shifts`
- **Auth**: `oauth2`
- **Signature**: `def create_shift(body: CreateShiftRequest | CreateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateShiftResponse`
- **Returns (raw)**: `ApiResult[CreateShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateShiftRequest` | `square/models/create_shift_request.py` |
| `CreateShiftRequestDict` | `square/models/create_shift_request.py` |
| `CreateShiftResponse` | `square/models/create_shift_response.py` |

### client.labor.create_timecard

- **Route**: `POST /v2/labor/timecards`
- **Auth**: `oauth2`
- **Signature**: `def create_timecard(body: CreateTimecardRequest | CreateTimecardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTimecardResponse`
- **Returns (raw)**: `ApiResult[CreateTimecardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTimecardRequest` | `square/models/create_timecard_request.py` |
| `CreateTimecardRequestDict` | `square/models/create_timecard_request.py` |
| `CreateTimecardResponse` | `square/models/create_timecard_response.py` |

### client.labor.delete_break_type

- **Route**: `DELETE /v2/labor/break-types/{id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_break_type(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `DeleteBreakTypeResponse`
- **Returns (raw)**: `ApiResult[DeleteBreakTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteBreakTypeResponse` | `square/models/delete_break_type_response.py` |

### client.labor.delete_shift

- **Route**: `DELETE /v2/labor/shifts/{id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_shift(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `DeleteShiftResponse`
- **Returns (raw)**: `ApiResult[DeleteShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteShiftResponse` | `square/models/delete_shift_response.py` |

### client.labor.delete_timecard

- **Route**: `DELETE /v2/labor/timecards/{id}`
- **Auth**: `oauth2`
- **Signature**: `def delete_timecard(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `DeleteTimecardResponse`
- **Returns (raw)**: `ApiResult[DeleteTimecardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DeleteTimecardResponse` | `square/models/delete_timecard_response.py` |

### client.labor.get_break_type

- **Route**: `GET /v2/labor/break-types/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_break_type(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GetBreakTypeResponse`
- **Returns (raw)**: `ApiResult[GetBreakTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetBreakTypeResponse` | `square/models/get_break_type_response.py` |

### client.labor.get_employee_wage

- **Route**: `GET /v2/labor/employee-wages/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_employee_wage(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GetEmployeeWageResponse`
- **Returns (raw)**: `ApiResult[GetEmployeeWageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetEmployeeWageResponse` | `square/models/get_employee_wage_response.py` |

### client.labor.get_shift

- **Route**: `GET /v2/labor/shifts/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_shift(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GetShiftResponse`
- **Returns (raw)**: `ApiResult[GetShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetShiftResponse` | `square/models/get_shift_response.py` |

### client.labor.get_team_member_wage

- **Route**: `GET /v2/labor/team-member-wages/{id}`
- **Auth**: `oauth2`
- **Signature**: `def get_team_member_wage(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `GetTeamMemberWageResponse`
- **Returns (raw)**: `ApiResult[GetTeamMemberWageResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetTeamMemberWageResponse` | `square/models/get_team_member_wage_response.py` |

### client.labor.list_break_types

- **Route**: `GET /v2/labor/break-types`
- **Auth**: `oauth2`
- **Signature**: `def list_break_types(*, location_id: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `location_id` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListBreakTypesResponse`
- **Returns (raw)**: `ApiResult[ListBreakTypesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBreakTypesResponse` | `square/models/list_break_types_response.py` |

### client.labor.list_employee_wages

- **Route**: `GET /v2/labor/employee-wages`
- **Auth**: `oauth2`
- **Signature**: `def list_employee_wages(*, employee_id: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `employee_id` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListEmployeeWagesResponse`
- **Returns (raw)**: `ApiResult[ListEmployeeWagesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListEmployeeWagesResponse` | `square/models/list_employee_wages_response.py` |

### client.labor.list_team_member_wages

- **Route**: `GET /v2/labor/team-member-wages`
- **Auth**: `oauth2`
- **Signature**: `def list_team_member_wages(*, team_member_id: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `team_member_id` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListTeamMemberWagesResponse`
- **Returns (raw)**: `ApiResult[ListTeamMemberWagesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListTeamMemberWagesResponse` | `square/models/list_team_member_wages_response.py` |

### client.labor.list_workweek_configs

- **Route**: `GET /v2/labor/workweek-configs`
- **Auth**: `oauth2`
- **Signature**: `def list_workweek_configs(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListWorkweekConfigsResponse`
- **Returns (raw)**: `ApiResult[ListWorkweekConfigsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListWorkweekConfigsResponse` | `square/models/list_workweek_configs_response.py` |

### client.labor.publish_scheduled_shift

- **Route**: `POST /v2/labor/scheduled-shifts/{id}/publish`
- **Auth**: `oauth2`
- **Signature**: `def publish_scheduled_shift(id_: str, body: PublishScheduledShiftRequest | PublishScheduledShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `PublishScheduledShiftResponse`
- **Returns (raw)**: `ApiResult[PublishScheduledShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `PublishScheduledShiftRequest` | `square/models/publish_scheduled_shift_request.py` |
| `PublishScheduledShiftRequestDict` | `square/models/publish_scheduled_shift_request.py` |
| `PublishScheduledShiftResponse` | `square/models/publish_scheduled_shift_response.py` |

### client.labor.retrieve_scheduled_shift

- **Route**: `GET /v2/labor/scheduled-shifts/{id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_scheduled_shift(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `RetrieveScheduledShiftResponse`
- **Returns (raw)**: `ApiResult[RetrieveScheduledShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveScheduledShiftResponse` | `square/models/retrieve_scheduled_shift_response.py` |

### client.labor.retrieve_timecard

- **Route**: `GET /v2/labor/timecards/{id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_timecard(id_: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`
- **Params**: `id_` — path `id`
- **Returns (parsed)**: `RetrieveTimecardResponse`
- **Returns (raw)**: `ApiResult[RetrieveTimecardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveTimecardResponse` | `square/models/retrieve_timecard_response.py` |

### client.labor.search_scheduled_shifts

- **Route**: `POST /v2/labor/scheduled-shifts/search`
- **Auth**: `oauth2`
- **Signature**: `def search_scheduled_shifts(body: SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchScheduledShiftsResponse`
- **Returns (raw)**: `ApiResult[SearchScheduledShiftsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchScheduledShiftsRequest` | `square/models/search_scheduled_shifts_request.py` |
| `SearchScheduledShiftsRequestDict` | `square/models/search_scheduled_shifts_request.py` |
| `SearchScheduledShiftsResponse` | `square/models/search_scheduled_shifts_response.py` |

### client.labor.search_shifts

- **Route**: `POST /v2/labor/shifts/search`
- **Auth**: `oauth2`
- **Signature**: `def search_shifts(body: SearchShiftsRequest | SearchShiftsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchShiftsResponse`
- **Returns (raw)**: `ApiResult[SearchShiftsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchShiftsRequest` | `square/models/search_shifts_request.py` |
| `SearchShiftsRequestDict` | `square/models/search_shifts_request.py` |
| `SearchShiftsResponse` | `square/models/search_shifts_response.py` |

### client.labor.search_timecards

- **Route**: `POST /v2/labor/timecards/search`
- **Auth**: `oauth2`
- **Signature**: `def search_timecards(body: SearchTimecardsRequest | SearchTimecardsRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchTimecardsResponse`
- **Returns (raw)**: `ApiResult[SearchTimecardsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchTimecardsRequest` | `square/models/search_timecards_request.py` |
| `SearchTimecardsRequestDict` | `square/models/search_timecards_request.py` |
| `SearchTimecardsResponse` | `square/models/search_timecards_response.py` |

### client.labor.update_break_type

- **Route**: `PUT /v2/labor/break-types/{id}`
- **Auth**: `oauth2`
- **Signature**: `def update_break_type(id_: str, body: UpdateBreakTypeRequest | UpdateBreakTypeRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `UpdateBreakTypeResponse`
- **Returns (raw)**: `ApiResult[UpdateBreakTypeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateBreakTypeRequest` | `square/models/update_break_type_request.py` |
| `UpdateBreakTypeRequestDict` | `square/models/update_break_type_request.py` |
| `UpdateBreakTypeResponse` | `square/models/update_break_type_response.py` |

### client.labor.update_scheduled_shift

- **Route**: `PUT /v2/labor/scheduled-shifts/{id}`
- **Auth**: `oauth2`
- **Signature**: `def update_scheduled_shift(id_: str, body: UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `UpdateScheduledShiftResponse`
- **Returns (raw)**: `ApiResult[UpdateScheduledShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateScheduledShiftRequest` | `square/models/update_scheduled_shift_request.py` |
| `UpdateScheduledShiftRequestDict` | `square/models/update_scheduled_shift_request.py` |
| `UpdateScheduledShiftResponse` | `square/models/update_scheduled_shift_response.py` |

### client.labor.update_shift

- **Route**: `PUT /v2/labor/shifts/{id}`
- **Auth**: `oauth2`
- **Signature**: `def update_shift(id_: str, body: UpdateShiftRequest | UpdateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `UpdateShiftResponse`
- **Returns (raw)**: `ApiResult[UpdateShiftResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateShiftRequest` | `square/models/update_shift_request.py` |
| `UpdateShiftRequestDict` | `square/models/update_shift_request.py` |
| `UpdateShiftResponse` | `square/models/update_shift_response.py` |

### client.labor.update_timecard

- **Route**: `PUT /v2/labor/timecards/{id}`
- **Auth**: `oauth2`
- **Signature**: `def update_timecard(id_: str, body: UpdateTimecardRequest | UpdateTimecardRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `UpdateTimecardResponse`
- **Returns (raw)**: `ApiResult[UpdateTimecardResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateTimecardRequest` | `square/models/update_timecard_request.py` |
| `UpdateTimecardRequestDict` | `square/models/update_timecard_request.py` |
| `UpdateTimecardResponse` | `square/models/update_timecard_response.py` |

### client.labor.update_workweek_config

- **Route**: `PUT /v2/labor/workweek-configs/{id}`
- **Auth**: `oauth2`
- **Signature**: `def update_workweek_config(id_: str, body: UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id_`, `body`
- **Params**: `id_` — path `id` · `body` — JSON body
- **Returns (parsed)**: `UpdateWorkweekConfigResponse`
- **Returns (raw)**: `ApiResult[UpdateWorkweekConfigResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateWorkweekConfigRequest` | `square/models/update_workweek_config_request.py` |
| `UpdateWorkweekConfigRequestDict` | `square/models/update_workweek_config_request.py` |
| `UpdateWorkweekConfigResponse` | `square/models/update_workweek_config_response.py` |

