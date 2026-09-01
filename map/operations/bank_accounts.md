<!-- Generated file — do not edit; regenerated with the SDK. -->

# BankAccounts — operations

Accessor: `client.bank_accounts` · Source: `square/apis/bank_accounts.py` · 5 operations

Each `###` block is one operation and assumes `sdk-map.md` is loaded: blocks omit what its invariants table covers and are otherwise self-contained, so chunk at block level. Signatures are the sync parsed spelling; the async and raw spellings take the same parameters (see sdk-map.md). **Type sources** names the module declaring each type an operation mentions, so resolving a body, return or error payload is a lookup rather than a search; the runtime types `RawError` and `ApiResult` are excluded.

### client.bank_accounts.create_bank_account

- **Route**: `POST /v2/bank-accounts`
- **Auth**: `oauth2`
- **Signature**: `def create_bank_account(body: CreateBankAccountRequest | CreateBankAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `body`
- **Params**: `body` — JSON body
- **Returns (parsed)**: `CreateBankAccountResponse`
- **Returns (raw)**: `ApiResult[CreateBankAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `CreateBankAccountRequest` | `square/models/create_bank_account_request.py` |
| `CreateBankAccountRequestDict` | `square/models/create_bank_account_request.py` |
| `CreateBankAccountResponse` | `square/models/create_bank_account_response.py` |

### client.bank_accounts.disable_bank_account

- **Route**: `POST /v2/bank-accounts/{bank_account_id}/disable`
- **Auth**: `oauth2`
- **Signature**: `def disable_bank_account(bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bank_account_id`
- **Params**: `bank_account_id` — path
- **Returns (parsed)**: `DisableBankAccountResponse`
- **Returns (raw)**: `ApiResult[DisableBankAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `DisableBankAccountResponse` | `square/models/disable_bank_account_response.py` |

### client.bank_accounts.get_bank_account

- **Route**: `GET /v2/bank-accounts/{bank_account_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_bank_account(bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `bank_account_id`
- **Params**: `bank_account_id` — path
- **Returns (parsed)**: `GetBankAccountResponse`
- **Returns (raw)**: `ApiResult[GetBankAccountResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetBankAccountResponse` | `square/models/get_bank_account_response.py` |

### client.bank_accounts.get_bank_account_by_v1_id

- **Route**: `GET /v2/bank-accounts/by-v1-id/{v1_bank_account_id}`
- **Auth**: `oauth2`
- **Signature**: `def get_bank_account_by_v1_id(v1_bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None)`
  - required, positional: `v1_bank_account_id`
- **Params**: `v1_bank_account_id` — path
- **Returns (parsed)**: `GetBankAccountByV1IdResponse`
- **Returns (raw)**: `ApiResult[GetBankAccountByV1IdResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `GetBankAccountByV1IdResponse` | `square/models/get_bank_account_by_v1_id_response.py` |

### client.bank_accounts.list_bank_accounts

- **Route**: `GET /v2/bank-accounts`
- **Auth**: `oauth2`
- **Signature**: `def list_bank_accounts(*, cursor: str | None = None, limit: int | None = None, location_id: str | None = None, customer_id: str | None = None, request_options: RequestOptionsOrDict | None = None)`
- **Params**: `cursor` — query · `limit` — query · `location_id` — query · `customer_id` — query
- **Returns (parsed)**: `ListBankAccountsResponse`
- **Returns (raw)**: `ApiResult[ListBankAccountsResponse, RawError]`
- **Error**: `RawError` — **Case B**

| Type | Source |
| --- | --- |
| `ListBankAccountsResponse` | `square/models/list_bank_accounts_response.py` |

