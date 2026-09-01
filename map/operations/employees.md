<!-- Generated file — do not edit; regenerated with the SDK. -->

# Employees — operations

Accessor: `client.employees` · Source: `square/apis/employees.py` · 2 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.employees.list_employees

- **Route**: `GET /v2/employees`
- **Auth**: `oauth2`
- **Signature**: `def list_employees(*, location_id: str | None = None, status: EmployeeStatusOrStr | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `location_id` — query · `status` — query · `limit` — query · `cursor` — query
- **Returns (parsed)**: `ListEmployeesResponse`
- **Returns (raw)**: `ApiResult[ListEmployeesResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `EmployeeStatusOrStr` | `square/models/enums/employee_status.py` |
| `ListEmployeesResponse` | `square/models/list_employees_response.py` |

### client.employees.retrieve_employee

- **Route**: `GET /v2/employees/{id}`
- **Auth**: `oauth2`
- **Signature**: `def retrieve_employee(id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `id`
- **Params**: `id` — path
- **Returns (parsed)**: `RetrieveEmployeeResponse`
- **Returns (raw)**: `ApiResult[RetrieveEmployeeResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `RetrieveEmployeeResponse` | `square/models/retrieve_employee_response.py` |

