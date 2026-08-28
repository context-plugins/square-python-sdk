<!-- Generated file — do not edit; regenerated with the SDK. -->

# Team — operations

Accessor: `client.team` · Source: `square/apis/team.py` · 12 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.team.bulk_create_team_members

- **Route**: `POST /v2/team-members/bulk-create`
- **Signature**: `def bulk_create_team_members(body: BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkCreateTeamMembersResponse`
- **Returns (raw)**: `ApiResult[BulkCreateTeamMembersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkCreateTeamMembersRequest` | `square/models/bulk_create_team_members_request.py` |
| `BulkCreateTeamMembersRequestDict` | `square/models/bulk_create_team_members_request.py` |
| `BulkCreateTeamMembersResponse` | `square/models/bulk_create_team_members_response.py` |

### client.team.bulk_update_team_members

- **Route**: `POST /v2/team-members/bulk-update`
- **Signature**: `def bulk_update_team_members(body: BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `BulkUpdateTeamMembersResponse`
- **Returns (raw)**: `ApiResult[BulkUpdateTeamMembersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `BulkUpdateTeamMembersRequest` | `square/models/bulk_update_team_members_request.py` |
| `BulkUpdateTeamMembersRequestDict` | `square/models/bulk_update_team_members_request.py` |
| `BulkUpdateTeamMembersResponse` | `square/models/bulk_update_team_members_response.py` |

### client.team.create_job

- **Route**: `POST /v2/team-members/jobs`
- **Signature**: `def create_job(body: CreateJobRequest | CreateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateJobResponse`
- **Returns (raw)**: `ApiResult[CreateJobResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateJobRequest` | `square/models/create_job_request.py` |
| `CreateJobRequestDict` | `square/models/create_job_request.py` |
| `CreateJobResponse` | `square/models/create_job_response.py` |

### client.team.create_team_member

- **Route**: `POST /v2/team-members`
- **Signature**: `def create_team_member(body: CreateTeamMemberRequest | CreateTeamMemberRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateTeamMemberResponse`
- **Returns (raw)**: `ApiResult[CreateTeamMemberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateTeamMemberRequest` | `square/models/create_team_member_request.py` |
| `CreateTeamMemberRequestDict` | `square/models/create_team_member_request.py` |
| `CreateTeamMemberResponse` | `square/models/create_team_member_response.py` |

### client.team.list_jobs

- **Route**: `GET /v2/team-members/jobs`
- **Signature**: `def list_jobs(*, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query
- **Returns (parsed)**: `ListJobsResponse`
- **Returns (raw)**: `ApiResult[ListJobsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListJobsResponse` | `square/models/list_jobs_response.py` |

### client.team.retrieve_job

- **Route**: `GET /v2/team-members/jobs/{job_id}`
- **Signature**: `def retrieve_job(job_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`
- **Params**: `job_id` — path
- **Returns (parsed)**: `RetrieveJobResponse`
- **Returns (raw)**: `ApiResult[RetrieveJobResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveJobResponse` | `square/models/retrieve_job_response.py` |

### client.team.retrieve_team_member

- **Route**: `GET /v2/team-members/{team_member_id}`
- **Signature**: `def retrieve_team_member(team_member_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_member_id`
- **Params**: `team_member_id` — path
- **Returns (parsed)**: `RetrieveTeamMemberResponse`
- **Returns (raw)**: `ApiResult[RetrieveTeamMemberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveTeamMemberResponse` | `square/models/retrieve_team_member_response.py` |

### client.team.retrieve_wage_setting

- **Route**: `GET /v2/team-members/{team_member_id}/wage-setting`
- **Signature**: `def retrieve_wage_setting(team_member_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_member_id`
- **Params**: `team_member_id` — path
- **Returns (parsed)**: `RetrieveWageSettingResponse`
- **Returns (raw)**: `ApiResult[RetrieveWageSettingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveWageSettingResponse` | `square/models/retrieve_wage_setting_response.py` |

### client.team.search_team_members

- **Route**: `POST /v2/team-members/search`
- **Signature**: `def search_team_members(body: SearchTeamMembersRequest | SearchTeamMembersRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `SearchTeamMembersResponse`
- **Returns (raw)**: `ApiResult[SearchTeamMembersResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `SearchTeamMembersRequest` | `square/models/search_team_members_request.py` |
| `SearchTeamMembersRequestDict` | `square/models/search_team_members_request.py` |
| `SearchTeamMembersResponse` | `square/models/search_team_members_response.py` |

### client.team.update_job

- **Route**: `PUT /v2/team-members/jobs/{job_id}`
- **Signature**: `def update_job(job_id: str, body: UpdateJobRequest | UpdateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `job_id`, `body`
- **Params**: `job_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateJobResponse`
- **Returns (raw)**: `ApiResult[UpdateJobResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateJobRequest` | `square/models/update_job_request.py` |
| `UpdateJobRequestDict` | `square/models/update_job_request.py` |
| `UpdateJobResponse` | `square/models/update_job_response.py` |

### client.team.update_team_member

- **Route**: `PUT /v2/team-members/{team_member_id}`
- **Signature**: `def update_team_member(team_member_id: str, body: UpdateTeamMemberRequest | UpdateTeamMemberRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_member_id`, `body`
- **Params**: `team_member_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateTeamMemberResponse`
- **Returns (raw)**: `ApiResult[UpdateTeamMemberResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateTeamMemberRequest` | `square/models/update_team_member_request.py` |
| `UpdateTeamMemberRequestDict` | `square/models/update_team_member_request.py` |
| `UpdateTeamMemberResponse` | `square/models/update_team_member_response.py` |

### client.team.update_wage_setting

- **Route**: `PUT /v2/team-members/{team_member_id}/wage-setting`
- **Signature**: `def update_wage_setting(team_member_id: str, body: UpdateWageSettingRequest | UpdateWageSettingRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `team_member_id`, `body`
- **Params**: `team_member_id` — path · `body` — JSON body
- **Returns (parsed)**: `UpdateWageSettingResponse`
- **Returns (raw)**: `ApiResult[UpdateWageSettingResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `UpdateWageSettingRequest` | `square/models/update_wage_setting_request.py` |
| `UpdateWageSettingRequestDict` | `square/models/update_wage_setting_request.py` |
| `UpdateWageSettingResponse` | `square/models/update_wage_setting_response.py` |

