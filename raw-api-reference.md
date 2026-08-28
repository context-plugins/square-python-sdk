# Raw Reference

**Raw** endpoints, reached through `with_raw_response`, return `ApiResult[T, E]` and never raise for an API error. For the parsed endpoints, see [API Reference](api-reference.md).

> Source: [SquareClient](square/client.py)

## ApplePay

> Source: [ApplePay](square/apis/apple_pay.py)

<details>
<summary><code>def register_domain(body: RegisterDomainRequest | RegisterDomainRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RegisterDomainResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Activates a domain for use with Apple Pay on the Web and Square. A validation
is performed on this domain by Apple to ensure that it is properly set up as
an Apple Pay enabled domain.

This endpoint provides an easy way for platform developers to bulk activate
Apple Pay on the Web with Square for merchants using their platform.

Note: You will need to host a valid domain verification file on your domain to support Apple Pay.  The
current version of this file is always available at https://app.squareup.com/digital-wallets/apple-pay/apple-developer-merchantid-domain-association,
and should be hosted at `.well_known/apple-developer-merchantid-domain-association` on your
domain.  This file is subject to change; we strongly recommend checking for updates regularly and avoiding
long-lived caches that might not keep in sync with the correct file version.

To learn more about the Web Payments SDK and how to add Apple Pay, see [Take an Apple Pay Payment](https://developer.squareup.com/docs/web-payments/apple-pay).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.apple_pay.with_raw_response.register_domain(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RegisterDomainResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.apple_pay.with_raw_response.register_domain(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RegisterDomainResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RegisterDomainRequest](square/models/register_domain_request.py) \| [RegisterDomainRequestDict](square/models/register_domain_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RegisterDomainResponse](square/models/register_domain_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RegisterDomainResponse](square/models/register_domain_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## BankAccounts

> Source: [BankAccounts](square/apis/bank_accounts.py)

<details>
<summary><code>def create_bank_account(body: CreateBankAccountRequest | CreateBankAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateBankAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Store a bank account on file for a square account

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bank_accounts.with_raw_response.create_bank_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBankAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bank_accounts.with_raw_response.create_bank_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBankAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateBankAccountRequest](square/models/create_bank_account_request.py) \| [CreateBankAccountRequestDict](square/models/create_bank_account_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateBankAccountResponse](square/models/create_bank_account_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateBankAccountResponse](square/models/create_bank_account_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_bank_account(bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DisableBankAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disable a bank account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bank_accounts.with_raw_response.disable_bank_account(bank_account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisableBankAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bank_accounts.with_raw_response.disable_bank_account(bank_account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisableBankAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>bank_account_id</code> | <code>str</code> | The ID of the bank account to disable. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DisableBankAccountResponse](square/models/disable_bank_account_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DisableBankAccountResponse](square/models/disable_bank_account_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_bank_account(bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetBankAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve details of a [BankAccount](entity:BankAccount) bank account linked to a Square account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bank_accounts.with_raw_response.get_bank_account(bank_account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBankAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bank_accounts.with_raw_response.get_bank_account(bank_account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBankAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>bank_account_id</code> | <code>str</code> | Square-issued ID of the desired `BankAccount`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetBankAccountResponse](square/models/get_bank_account_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetBankAccountResponse](square/models/get_bank_account_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_bank_account_by_v1_id(v1_bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetBankAccountByV1IdResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details of a [BankAccount](entity:BankAccount) identified by V1 bank account ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bank_accounts.with_raw_response.get_bank_account_by_v1_id(v1_bank_account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBankAccountByV1IdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bank_accounts.with_raw_response.get_bank_account_by_v1_id(v1_bank_account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBankAccountByV1IdResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>v1_bank_account_id</code> | <code>str</code> | Connect V1 ID of the desired `BankAccount`. For more information, see <br>[Retrieve a bank account by using an ID issued by V1 Bank Accounts API](https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetBankAccountByV1IdResponse](square/models/get_bank_account_by_v1_id_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetBankAccountByV1IdResponse](square/models/get_bank_account_by_v1_id_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_bank_accounts(*, cursor: str | None = None, limit: int | None = None, location_id: str | None = None, customer_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListBankAccountsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of [BankAccount](entity:BankAccount) objects linked to a Square account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bank_accounts.with_raw_response.list_bank_accounts()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBankAccountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bank_accounts.with_raw_response.list_bank_accounts()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBankAccountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | The pagination cursor returned by a previous call to this endpoint.<br>Use it in the next `ListBankAccounts` request to retrieve the next set<br>of results.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Upper limit on the number of bank accounts to return in the response.<br>Currently, 1000 is the largest supported limit. You can specify a limit<br>of up to 1000 bank accounts. This is also the default limit.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | Location ID. You can specify this optional filter<br>to retrieve only the linked bank accounts belonging to a specific location.<br>**Default**: <code>None</code> |
| <code>customer_id</code> | <code>str \| None</code> | Customer ID. You can specify this optional filter<br>to retrieve only the linked bank accounts belonging to a specific customer.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListBankAccountsResponse](square/models/list_bank_accounts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListBankAccountsResponse](square/models/list_bank_accounts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## BookingCustomAttributes

> Source: [BookingCustomAttributes](square/apis/booking_custom_attributes.py)

<details>
<summary><code>def bulk_delete_booking_custom_attributes(body: BulkDeleteBookingCustomAttributesRequest | BulkDeleteBookingCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkDeleteBookingCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Bulk deletes bookings custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.bulk_delete_booking_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteBookingCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.bulk_delete_booking_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteBookingCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkDeleteBookingCustomAttributesRequest](square/models/bulk_delete_booking_custom_attributes_request.py) \| [BulkDeleteBookingCustomAttributesRequestDict](square/models/bulk_delete_booking_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkDeleteBookingCustomAttributesResponse](square/models/bulk_delete_booking_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkDeleteBookingCustomAttributesResponse](square/models/bulk_delete_booking_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_upsert_booking_custom_attributes(body: BulkUpsertBookingCustomAttributesRequest | BulkUpsertBookingCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpsertBookingCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Bulk upserts bookings custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.bulk_upsert_booking_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertBookingCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.bulk_upsert_booking_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertBookingCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpsertBookingCustomAttributesRequest](square/models/bulk_upsert_booking_custom_attributes_request.py) \| [BulkUpsertBookingCustomAttributesRequestDict](square/models/bulk_upsert_booking_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpsertBookingCustomAttributesResponse](square/models/bulk_upsert_booking_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpsertBookingCustomAttributesResponse](square/models/bulk_upsert_booking_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_booking_custom_attribute_definition(body: CreateBookingCustomAttributeDefinitionRequest | CreateBookingCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateBookingCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.create_booking_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.create_booking_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateBookingCustomAttributeDefinitionRequest](square/models/create_booking_custom_attribute_definition_request.py) \| [CreateBookingCustomAttributeDefinitionRequestDict](square/models/create_booking_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateBookingCustomAttributeDefinitionResponse](square/models/create_booking_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateBookingCustomAttributeDefinitionResponse](square/models/create_booking_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_booking_custom_attribute(booking_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteBookingCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.delete_booking_custom_attribute(booking_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteBookingCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.delete_booking_custom_attribute(booking_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteBookingCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the target [booking](entity:Booking). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteBookingCustomAttributeResponse](square/models/delete_booking_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteBookingCustomAttributeResponse](square/models/delete_booking_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_booking_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteBookingCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.delete_booking_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.delete_booking_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteBookingCustomAttributeDefinitionResponse](square/models/delete_booking_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteBookingCustomAttributeDefinitionResponse](square/models/delete_booking_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_booking_custom_attribute_definitions(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListBookingCustomAttributeDefinitionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Get all bookings custom attribute definitions.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.list_booking_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBookingCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.list_booking_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBookingCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListBookingCustomAttributeDefinitionsResponse](square/models/list_booking_custom_attribute_definitions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListBookingCustomAttributeDefinitionsResponse](square/models/list_booking_custom_attribute_definitions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_booking_custom_attributes(booking_id: str, *, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListBookingCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists a booking's custom attributes.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.list_booking_custom_attributes(booking_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBookingCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.list_booking_custom_attributes(booking_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBookingCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the target [booking](entity:Booking). |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>with_definitions</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListBookingCustomAttributesResponse](square/models/list_booking_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListBookingCustomAttributesResponse](square/models/list_booking_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_booking_custom_attribute(booking_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveBookingCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.retrieve_booking_custom_attribute(booking_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBookingCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.retrieve_booking_custom_attribute(
    booking_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBookingCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the target [booking](entity:Booking). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>with_definition</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveBookingCustomAttributeResponse](square/models/retrieve_booking_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveBookingCustomAttributeResponse](square/models/retrieve_booking_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_booking_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveBookingCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.retrieve_booking_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.retrieve_booking_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveBookingCustomAttributeDefinitionResponse](square/models/retrieve_booking_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveBookingCustomAttributeDefinitionResponse](square/models/retrieve_booking_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_booking_custom_attribute_definition(key: str, body: UpdateBookingCustomAttributeDefinitionRequest | UpdateBookingCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateBookingCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a bookings custom attribute definition.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.update_booking_custom_attribute_definition(key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.update_booking_custom_attribute_definition(
    key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateBookingCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to update. |
| <code>body</code> | <code>[UpdateBookingCustomAttributeDefinitionRequest](square/models/update_booking_custom_attribute_definition_request.py) \| [UpdateBookingCustomAttributeDefinitionRequestDict](square/models/update_booking_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateBookingCustomAttributeDefinitionResponse](square/models/update_booking_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateBookingCustomAttributeDefinitionResponse](square/models/update_booking_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_booking_custom_attribute(booking_id: str, key: str, body: UpsertBookingCustomAttributeRequest | UpsertBookingCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertBookingCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Upserts a bookings custom attribute.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.booking_custom_attributes.with_raw_response.upsert_booking_custom_attribute(booking_id, key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertBookingCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.booking_custom_attributes.with_raw_response.upsert_booking_custom_attribute(
    booking_id, key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertBookingCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the target [booking](entity:Booking). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| <code>body</code> | <code>[UpsertBookingCustomAttributeRequest](square/models/upsert_booking_custom_attribute_request.py) \| [UpsertBookingCustomAttributeRequestDict](square/models/upsert_booking_custom_attribute_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertBookingCustomAttributeResponse](square/models/upsert_booking_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertBookingCustomAttributeResponse](square/models/upsert_booking_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Bookings

> Source: [Bookings](square/apis/bookings.py)

<details>
<summary><code>def bulk_retrieve_bookings(body: BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkRetrieveBookingsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Bulk-Retrieves a list of bookings by booking IDs.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.bulk_retrieve_bookings(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveBookingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.bulk_retrieve_bookings(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveBookingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkRetrieveBookingsRequest](square/models/bulk_retrieve_bookings_request.py) \| [BulkRetrieveBookingsRequestDict](square/models/bulk_retrieve_bookings_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkRetrieveBookingsResponse](square/models/bulk_retrieve_bookings_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkRetrieveBookingsResponse](square/models/bulk_retrieve_bookings_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_retrieve_team_member_booking_profiles(body: BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkRetrieveTeamMemberBookingProfilesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves one or more team members' booking profiles.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.bulk_retrieve_team_member_booking_profiles(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveTeamMemberBookingProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.bulk_retrieve_team_member_booking_profiles(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveTeamMemberBookingProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkRetrieveTeamMemberBookingProfilesRequest](square/models/bulk_retrieve_team_member_booking_profiles_request.py) \| [BulkRetrieveTeamMemberBookingProfilesRequestDict](square/models/bulk_retrieve_team_member_booking_profiles_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkRetrieveTeamMemberBookingProfilesResponse](square/models/bulk_retrieve_team_member_booking_profiles_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkRetrieveTeamMemberBookingProfilesResponse](square/models/bulk_retrieve_team_member_booking_profiles_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_booking(booking_id: str, body: CancelBookingRequest | CancelBookingRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelBookingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels an existing booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.cancel_booking(booking_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.cancel_booking(booking_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the [Booking](entity:Booking) object representing the to-be-cancelled booking. |
| <code>body</code> | <code>[CancelBookingRequest](square/models/cancel_booking_request.py) \| [CancelBookingRequestDict](square/models/cancel_booking_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelBookingResponse](square/models/cancel_booking_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelBookingResponse](square/models/cancel_booking_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_booking(body: CreateBookingRequest | CreateBookingRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateBookingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a booking.

The required input must include the following:
- `Booking.location_id`
- `Booking.start_at`
- `Booking.AppointmentSegment.team_member_id`
- `Booking.AppointmentSegment.service_variation_id`
- `Booking.AppointmentSegment.service_variation_version`

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.create_booking(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.create_booking(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateBookingRequest](square/models/create_booking_request.py) \| [CreateBookingRequestDict](square/models/create_booking_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateBookingResponse](square/models/create_booking_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateBookingResponse](square/models/create_booking_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_bookings(*, limit: int | None = None, cursor: str | None = None, customer_id: str | None = None, team_member_id: str | None = None, location_id: str | None = None, start_at_min: str | None = None, start_at_max: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListBookingsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieve a collection of bookings.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.list_bookings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBookingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.list_bookings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBookingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results per page to return in a paged response.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results.<br>**Default**: <code>None</code> |
| <code>customer_id</code> | <code>str \| None</code> | The [customer](entity:Customer) for whom to retrieve bookings. If this is not set, bookings for all customers are retrieved.<br>**Default**: <code>None</code> |
| <code>team_member_id</code> | <code>str \| None</code> | The team member for whom to retrieve bookings. If this is not set, bookings of all members are retrieved.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | The location for which to retrieve bookings. If this is not set, all locations' bookings are retrieved.<br>**Default**: <code>None</code> |
| <code>start_at_min</code> | <code>str \| None</code> | The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the current time is used.<br>**Default**: <code>None</code> |
| <code>start_at_max</code> | <code>str \| None</code> | The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time of 31 days after `start_at_min` is used.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListBookingsResponse](square/models/list_bookings_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListBookingsResponse](square/models/list_bookings_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_location_booking_profiles(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListLocationBookingProfilesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists location booking profiles of a seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.list_location_booking_profiles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationBookingProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.list_location_booking_profiles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationBookingProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a paged response.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListLocationBookingProfilesResponse](square/models/list_location_booking_profiles_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListLocationBookingProfilesResponse](square/models/list_location_booking_profiles_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_team_member_booking_profiles(*, bookable_only: bool | None = False, limit: int | None = None, cursor: str | None = None, location_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListTeamMemberBookingProfilesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists booking profiles for team members.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.list_team_member_booking_profiles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTeamMemberBookingProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.list_team_member_booking_profiles()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTeamMemberBookingProfilesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>bookable_only</code> | <code>bool \| None</code> | Indicates whether to include only bookable team members in the returned result (`true`) or not (`false`).<br>**Default**: <code>False</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a paged response.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The pagination cursor from the preceding response to return the next page of the results. Do not set this when retrieving the first page of the results.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | Indicates whether to include only team members enabled at the given location in the returned result.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListTeamMemberBookingProfilesResponse](square/models/list_team_member_booking_profiles_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListTeamMemberBookingProfilesResponse](square/models/list_team_member_booking_profiles_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_booking(booking_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveBookingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.retrieve_booking(booking_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.retrieve_booking(booking_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the [Booking](entity:Booking) object representing the to-be-retrieved booking. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveBookingResponse](square/models/retrieve_booking_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveBookingResponse](square/models/retrieve_booking_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_business_booking_profile(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveBusinessBookingProfileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a seller's booking profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.retrieve_business_booking_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBusinessBookingProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.retrieve_business_booking_profile()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveBusinessBookingProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveBusinessBookingProfileResponse](square/models/retrieve_business_booking_profile_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveBusinessBookingProfileResponse](square/models/retrieve_business_booking_profile_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location_booking_profile(location_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLocationBookingProfileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a seller's location booking profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.retrieve_location_booking_profile(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationBookingProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.retrieve_location_booking_profile(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationBookingProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location to retrieve the booking profile. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLocationBookingProfileResponse](square/models/retrieve_location_booking_profile_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLocationBookingProfileResponse](square/models/retrieve_location_booking_profile_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_team_member_booking_profile(team_member_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveTeamMemberBookingProfileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a team member's booking profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.retrieve_team_member_booking_profile(team_member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTeamMemberBookingProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.retrieve_team_member_booking_profile(team_member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTeamMemberBookingProfileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_member_id</code> | <code>str</code> | The ID of the team member to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveTeamMemberBookingProfileResponse](square/models/retrieve_team_member_booking_profile_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveTeamMemberBookingProfileResponse](square/models/retrieve_team_member_booking_profile_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_availability(body: SearchAvailabilityRequest | SearchAvailabilityRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchAvailabilityResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for availabilities for booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_READ` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_READ` and `APPOINTMENTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.search_availability(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchAvailabilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.search_availability(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchAvailabilityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchAvailabilityRequest](square/models/search_availability_request.py) \| [SearchAvailabilityRequestDict](square/models/search_availability_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchAvailabilityResponse](square/models/search_availability_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchAvailabilityResponse](square/models/search_availability_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_booking(booking_id: str, body: UpdateBookingRequest | UpdateBookingRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateBookingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a booking.

To call this endpoint with buyer-level permissions, set `APPOINTMENTS_WRITE` for the OAuth scope.
To call this endpoint with seller-level permissions, set `APPOINTMENTS_ALL_WRITE` and `APPOINTMENTS_WRITE` for the OAuth scope.

For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to *Appointments Plus*
or *Appointments Premium*.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.bookings.with_raw_response.update_booking(booking_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.bookings.with_raw_response.update_booking(booking_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateBookingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>booking_id</code> | <code>str</code> | The ID of the [Booking](entity:Booking) object representing the to-be-updated booking. |
| <code>body</code> | <code>[UpdateBookingRequest](square/models/update_booking_request.py) \| [UpdateBookingRequestDict](square/models/update_booking_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateBookingResponse](square/models/update_booking_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateBookingResponse](square/models/update_booking_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Cards

> Source: [Cards](square/apis/cards.py)

<details>
<summary><code>def create_card(body: CreateCardRequest | CreateCardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a card on file to an existing merchant.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cards.with_raw_response.create_card(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cards.with_raw_response.create_card(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCardRequest](square/models/create_card_request.py) \| [CreateCardRequestDict](square/models/create_card_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCardResponse](square/models/create_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCardResponse](square/models/create_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def disable_card(card_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DisableCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disables the card, preventing any further updates or charges.
Disabling an already disabled card is allowed but has no effect.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cards.with_raw_response.disable_card(card_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisableCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cards.with_raw_response.disable_card(card_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisableCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>card_id</code> | <code>str</code> | Unique ID for the desired Card. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DisableCardResponse](square/models/disable_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DisableCardResponse](square/models/disable_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_cards(*, cursor: str | None = None, customer_id: str | None = None, include_disabled: bool | None = False, reference_id: str | None = None, sort_order: SortOrderOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCardsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of cards owned by the account making the request.
A max of 25 cards will be returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cards.with_raw_response.list_cards()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cards.with_raw_response.list_cards()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.<br>**Default**: <code>None</code> |
| <code>customer_id</code> | <code>str \| None</code> | Limit results to cards associated with the customer supplied.<br>By default, all cards owned by the merchant are returned.<br>**Default**: <code>None</code> |
| <code>include_disabled</code> | <code>bool \| None</code> | Includes disabled cards.<br>By default, all enabled cards owned by the merchant are returned.<br>**Default**: <code>False</code> |
| <code>reference_id</code> | <code>str \| None</code> | Limit results to cards associated with the reference_id supplied.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | Sorts the returned list by when the card was created with the specified order.<br>This field defaults to ASC.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCardsResponse](square/models/list_cards_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCardsResponse](square/models/list_cards_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_card(card_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves details for a specific Card.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cards.with_raw_response.retrieve_card(card_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cards.with_raw_response.retrieve_card(card_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>card_id</code> | <code>str</code> | Unique ID for the desired Card. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCardResponse](square/models/retrieve_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCardResponse](square/models/retrieve_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CashDrawers

> Source: [CashDrawers](square/apis/cash_drawers.py)

<details>
<summary><code>def list_cash_drawer_shift_events(shift_id: str, location_id: str, *, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCashDrawerShiftEventsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides a paginated list of events for a single cash drawer shift.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cash_drawers.with_raw_response.list_cash_drawer_shift_events(shift_id, location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCashDrawerShiftEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cash_drawers.with_raw_response.list_cash_drawer_shift_events(shift_id, location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCashDrawerShiftEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shift_id</code> | <code>str</code> | The shift ID. |
| <code>location_id</code> | <code>str</code> | The ID of the location to list cash drawer shifts for. |
| <code>limit</code> | <code>int \| None</code> | Number of resources to be returned in a page of results (200 by<br>default, 1000 max).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque cursor for fetching the next page of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCashDrawerShiftEventsResponse](square/models/list_cash_drawer_shift_events_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCashDrawerShiftEventsResponse](square/models/list_cash_drawer_shift_events_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_cash_drawer_shifts(location_id: str, *, sort_order: SortOrderOrStr | None = None, begin_time: str | None = None, end_time: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCashDrawerShiftsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides the details for all of the cash drawer shifts for a location
in a date range.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cash_drawers.with_raw_response.list_cash_drawer_shifts(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCashDrawerShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cash_drawers.with_raw_response.list_cash_drawer_shifts(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCashDrawerShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location to query for a list of cash drawer shifts. |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | The order in which cash drawer shifts are listed in the response,<br>based on their opened_at field. Default value: ASC<br>**Default**: <code>None</code> |
| <code>begin_time</code> | <code>str \| None</code> | The inclusive start time of the query on opened_at, in ISO 8601 format.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>str \| None</code> | The exclusive end date of the query on opened_at, in ISO 8601 format.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Number of cash drawer shift events in a page of results (200 by<br>default, 1000 max).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Opaque cursor for fetching the next page of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCashDrawerShiftsResponse](square/models/list_cash_drawer_shifts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCashDrawerShiftsResponse](square/models/list_cash_drawer_shifts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_cash_drawer_shift(shift_id: str, location_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCashDrawerShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides the summary details for a single cash drawer shift. See
[ListCashDrawerShiftEvents](api-endpoint:CashDrawers-ListCashDrawerShiftEvents) for a list of cash drawer shift events.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.cash_drawers.with_raw_response.retrieve_cash_drawer_shift(shift_id, location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCashDrawerShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.cash_drawers.with_raw_response.retrieve_cash_drawer_shift(shift_id, location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCashDrawerShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>shift_id</code> | <code>str</code> | The shift ID. |
| <code>location_id</code> | <code>str</code> | The ID of the location to retrieve cash drawer shifts from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCashDrawerShiftResponse](square/models/retrieve_cash_drawer_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCashDrawerShiftResponse](square/models/retrieve_cash_drawer_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Catalog

> Source: [Catalog](square/apis/catalog.py)

<details>
<summary><code>def batch_delete_catalog_objects(body: BatchDeleteCatalogObjectsRequest | BatchDeleteCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchDeleteCatalogObjectsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a set of [CatalogItem](entity:CatalogItem)s based on the
provided list of target IDs and returns a set of successfully deleted IDs in
the response. Deletion is a cascading event such that all children of the
targeted object are also deleted. For example, deleting a CatalogItem will
also delete all of its [CatalogItemVariation](entity:CatalogItemVariation)
children.

`BatchDeleteCatalogObjects` succeeds even if only a portion of the targeted
IDs can be deleted. The response will only include IDs that were
actually deleted.

To ensure consistency, only one delete request is processed at a time per seller account.
While one (batch or non-batch) delete request is being processed, other (batched and non-batched)
delete requests are rejected with the `429` error code.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.batch_delete_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchDeleteCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.batch_delete_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchDeleteCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchDeleteCatalogObjectsRequest](square/models/batch_delete_catalog_objects_request.py) \| [BatchDeleteCatalogObjectsRequestDict](square/models/batch_delete_catalog_objects_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchDeleteCatalogObjectsResponse](square/models/batch_delete_catalog_objects_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchDeleteCatalogObjectsResponse](square/models/batch_delete_catalog_objects_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def batch_retrieve_catalog_objects(body: BatchRetrieveCatalogObjectsRequest | BatchRetrieveCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchRetrieveCatalogObjectsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a set of objects based on the provided ID.
Each [CatalogItem](entity:CatalogItem) returned in the set includes all of its
child information including: all of its
[CatalogItemVariation](entity:CatalogItemVariation) objects, references to
its [CatalogModifierList](entity:CatalogModifierList) objects, and the ids of
any [CatalogTax](entity:CatalogTax) objects that apply to it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.batch_retrieve_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.batch_retrieve_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchRetrieveCatalogObjectsRequest](square/models/batch_retrieve_catalog_objects_request.py) \| [BatchRetrieveCatalogObjectsRequestDict](square/models/batch_retrieve_catalog_objects_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchRetrieveCatalogObjectsResponse](square/models/batch_retrieve_catalog_objects_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchRetrieveCatalogObjectsResponse](square/models/batch_retrieve_catalog_objects_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def batch_upsert_catalog_objects(body: BatchUpsertCatalogObjectsRequest | BatchUpsertCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchUpsertCatalogObjectsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates up to 10,000 target objects based on the provided
list of objects. The target objects are grouped into batches and each batch is
inserted/updated in an all-or-nothing manner. If an object within a batch is
malformed in some way, or violates a database constraint, the entire batch
containing that item will be disregarded. However, other batches in the same
request may still succeed. Each batch may contain up to 1,000 objects, and
batches will be processed in order as long as the total object count for the
request (items, variations, modifier lists, discounts, and taxes) is no more
than 10,000.

This endpoint uses full-replacement semantics. The client must send the complete object, and any
field absent from the request is interpreted as an intentional clear. This logic applies to
nested objects as well. For example, omitting inlined children like variations will delete them.

To ensure consistency, only one update request is processed at a time per seller account.
While one (batch or non-batch) update request is being processed, other (batched and non-batched)
update requests are rejected with the `429` error code. Prefer batching related changes into a
single call rather than issuing many small writes, since each write acquires the lock separately
and parallel writes to the same seller will contend with each other, producing `429` errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.batch_upsert_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchUpsertCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.batch_upsert_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchUpsertCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchUpsertCatalogObjectsRequest](square/models/batch_upsert_catalog_objects_request.py) \| [BatchUpsertCatalogObjectsRequestDict](square/models/batch_upsert_catalog_objects_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchUpsertCatalogObjectsResponse](square/models/batch_upsert_catalog_objects_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchUpsertCatalogObjectsResponse](square/models/batch_upsert_catalog_objects_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def catalog_info(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CatalogInfoResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves information about the Square Catalog API, such as batch size
limits that can be used by the `BatchUpsertCatalogObjects` endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.catalog_info()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.catalog_info()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CatalogInfoResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CatalogInfoResponse](square/models/catalog_info_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CatalogInfoResponse](square/models/catalog_info_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_catalog_image(*, request: CreateCatalogImageRequest | CreateCatalogImageRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCatalogImageResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads an image file to be represented by a [CatalogImage](entity:CatalogImage) object that can be linked to an existing
[CatalogObject](entity:CatalogObject) instance. The resulting `CatalogImage` is unattached to any `CatalogObject` if the `object_id`
is not specified.

This `CreateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.create_catalog_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCatalogImageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.create_catalog_image()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCatalogImageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request</code> | <code>[CreateCatalogImageRequest](square/models/create_catalog_image_request.py) \| [CreateCatalogImageRequestDict](square/models/create_catalog_image_request.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>image_file</code> | <code>bytes \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCatalogImageResponse](square/models/create_catalog_image_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCatalogImageResponse](square/models/create_catalog_image_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_catalog_object(object_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteCatalogObjectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a single [CatalogObject](entity:CatalogObject) based on the
provided ID and returns the set of successfully deleted IDs in the response.
Deletion is a cascading event such that all children of the targeted object
are also deleted. For example, deleting a [CatalogItem](entity:CatalogItem)
will also delete all of its
[CatalogItemVariation](entity:CatalogItemVariation) children.

To ensure consistency, only one delete request is processed at a time per seller account.
While one (batch or non-batch) delete request is being processed, other (batched and non-batched)
delete requests are rejected with the `429` error code.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.delete_catalog_object(object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCatalogObjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.delete_catalog_object(object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCatalogObjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>object_id</code> | <code>str</code> | The ID of the catalog object to be deleted. When an object is deleted, other<br>objects in the graph that depend on that object will be deleted as well (for example, deleting a<br>catalog item will delete its catalog item variations). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteCatalogObjectResponse](square/models/delete_catalog_object_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteCatalogObjectResponse](square/models/delete_catalog_object_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_catalog(*, cursor: str | None = None, types: str | None = None, catalog_version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCatalogResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of all [CatalogObject](entity:CatalogObject)s of the specified types in the catalog.

The `types` parameter is specified as a comma-separated list of the [CatalogObjectType](entity:CatalogObjectType) values,
for example, "`ITEM`, `ITEM_VARIATION`, `MODIFIER`, `MODIFIER_LIST`, `CATEGORY`, `DISCOUNT`, `TAX`, `IMAGE`".
Always specify `types` explicitly. When upgrading to a newer API version, omitting `types` may
cause new object types to appear in results that were not returned under the previous version.

__Important:__ ListCatalog does not return deleted catalog items. To retrieve
deleted catalog items, use [SearchCatalogObjects](api-endpoint:Catalog-SearchCatalogObjects)
and set the `include_deleted_objects` attribute value to `true`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.list_catalog()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCatalogResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.list_catalog()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCatalogResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | The pagination cursor returned in the previous response. Leave unset for an initial request.<br>The page size is currently set to be 100.<br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.<br>**Default**: <code>None</code> |
| <code>types</code> | <code>str \| None</code> | An optional case-insensitive, comma-separated list of object types to retrieve.<br><br>The valid values are defined in the [CatalogObjectType](entity:CatalogObjectType) enum, for example,<br>`ITEM`, `ITEM_VARIATION`, `CATEGORY`, `DISCOUNT`, `TAX`,<br>`MODIFIER`, `MODIFIER_LIST`, `IMAGE`, etc.<br><br>If this is unspecified, the operation returns objects of all the top level types at the version<br>of the Square API used to make the request. Object types that are nested onto other object types<br>are not included in the defaults.<br><br>At the current API version the default object types are:<br>ITEM, CATEGORY, TAX, DISCOUNT, MODIFIER_LIST, <br>PRICING_RULE, PRODUCT_SET, TIME_PERIOD, MEASUREMENT_UNIT,<br>SUBSCRIPTION_PLAN, ITEM_OPTION, CUSTOM_ATTRIBUTE_DEFINITION, QUICK_AMOUNT_SETTINGS.<br>**Default**: <code>None</code> |
| <code>catalog_version</code> | <code>int \| None</code> | The specific version of the catalog objects to be included in the response.<br>This allows you to retrieve historical versions of objects. The specified version value is matched against<br>the [CatalogObject](entity:CatalogObject)s' `version` attribute.  If not included, results will be from the<br>current version of the catalog.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCatalogResponse](square/models/list_catalog_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCatalogResponse](square/models/list_catalog_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_catalog_object(object_id: str, *, include_related_objects: bool | None = False, catalog_version: int | None = None, include_category_path_to_root: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCatalogObjectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single [CatalogItem](entity:CatalogItem) as a
[CatalogObject](entity:CatalogObject) based on the provided ID. The returned
object includes all of the relevant [CatalogItem](entity:CatalogItem)
information including: [CatalogItemVariation](entity:CatalogItemVariation)
children, references to its
[CatalogModifierList](entity:CatalogModifierList) objects, and the ids of
any [CatalogTax](entity:CatalogTax) objects that apply to it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.retrieve_catalog_object(object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCatalogObjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.retrieve_catalog_object(object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCatalogObjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>object_id</code> | <code>str</code> | The object ID of any type of catalog objects to be retrieved. |
| <code>include_related_objects</code> | <code>bool \| None</code> | If `true`, the response will include additional objects that are related to the<br>requested objects. Related objects are defined as any objects referenced by ID by the results in the `objects` field<br>of the response. These objects are put in the `related_objects` field. Setting this to `true` is<br>helpful when the objects are needed for immediate display to a user.<br>This process only goes one level deep. Objects referenced by the related objects will not be included. For example,<br><br>if the `objects` field of the response contains a CatalogItem, its associated<br>CatalogCategory objects, CatalogTax objects, CatalogImage objects and<br>CatalogModifierLists will be returned in the `related_objects` field of the<br>response. If the `objects` field of the response contains a CatalogItemVariation,<br>its parent CatalogItem will be returned in the `related_objects` field of<br>the response.<br><br>Default value: `false`<br>**Default**: <code>False</code> |
| <code>catalog_version</code> | <code>int \| None</code> | Requests objects as of a specific version of the catalog. This allows you to retrieve historical<br>versions of objects. The value to retrieve a specific version of an object can be found<br>in the version field of [CatalogObject](entity:CatalogObject)s. If not included, results will<br>be from the current version of the catalog.<br>**Default**: <code>None</code> |
| <code>include_category_path_to_root</code> | <code>bool \| None</code> | Specifies whether or not to include the `path_to_root` list for each returned category instance. The `path_to_root` list consists<br>of `CategoryPathToRootNode` objects and specifies the path that starts with the immediate parent category of the returned category<br>and ends with its root category. If the returned category is a top-level category, the `path_to_root` list is empty and is not returned<br>in the response payload.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCatalogObjectResponse](square/models/retrieve_catalog_object_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCatalogObjectResponse](square/models/retrieve_catalog_object_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_catalog_items(body: SearchCatalogItemsRequest | SearchCatalogItemsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchCatalogItemsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for catalog items or item variations by matching supported search attribute values, including
custom attribute values, against one or more of the specified query filters.

This (`SearchCatalogItems`) endpoint differs from the [SearchCatalogObjects](api-endpoint:Catalog-SearchCatalogObjects)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints use different call conventions, including the query filter formats.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.search_catalog_items(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchCatalogItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.search_catalog_items(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchCatalogItemsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchCatalogItemsRequest](square/models/search_catalog_items_request.py) \| [SearchCatalogItemsRequestDict](square/models/search_catalog_items_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchCatalogItemsResponse](square/models/search_catalog_items_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchCatalogItemsResponse](square/models/search_catalog_items_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_catalog_objects(body: SearchCatalogObjectsRequest | SearchCatalogObjectsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchCatalogObjectsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for [CatalogObject](entity:CatalogObject) of any type by matching supported search attribute values,
excluding custom attribute values on items or item variations, against one or more of the specified query filters.

This (`SearchCatalogObjects`) endpoint differs from the [SearchCatalogItems](api-endpoint:Catalog-SearchCatalogItems)
endpoint in the following aspects:

- `SearchCatalogItems` can only search for items or item variations, whereas `SearchCatalogObjects` can search for any type of catalog objects.
- `SearchCatalogItems` supports the custom attribute query filters to return items or item variations that contain custom attribute values, where `SearchCatalogObjects` does not.
- `SearchCatalogItems` does not support the `include_deleted_objects` filter to search for deleted items or item variations, whereas `SearchCatalogObjects` does.
- The both endpoints have different call conventions, including the query filter formats.

The `object_types` parameter is specified as a list of [CatalogObjectType](entity:CatalogObjectType) values.
Always specify `object_types` explicitly. When upgrading to a newer API version, omitting
`object_types` may cause new object types to appear in results that were not returned under
the previous version.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.search_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.search_catalog_objects(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchCatalogObjectsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchCatalogObjectsRequest](square/models/search_catalog_objects_request.py) \| [SearchCatalogObjectsRequestDict](square/models/search_catalog_objects_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchCatalogObjectsResponse](square/models/search_catalog_objects_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchCatalogObjectsResponse](square/models/search_catalog_objects_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_catalog_image(image_id: str, *, request: UpdateCatalogImageRequest | UpdateCatalogImageRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateCatalogImageResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads a new image file to replace the existing one in the specified [CatalogImage](entity:CatalogImage) object.

This `UpdateCatalogImage` endpoint accepts HTTP multipart/form-data requests with a JSON part and an image file part in
JPEG, PJPEG, PNG, or GIF format. The maximum file size is 15MB.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.update_catalog_image(image_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCatalogImageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.update_catalog_image(image_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCatalogImageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>image_id</code> | <code>str</code> | The ID of the `CatalogImage` object to update the encapsulated image file. |
| <code>request</code> | <code>[UpdateCatalogImageRequest](square/models/update_catalog_image_request.py) \| [UpdateCatalogImageRequestDict](square/models/update_catalog_image_request.py) \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>image_file</code> | <code>bytes \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateCatalogImageResponse](square/models/update_catalog_image_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateCatalogImageResponse](square/models/update_catalog_image_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_item_modifier_lists(body: UpdateItemModifierListsRequest | UpdateItemModifierListsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateItemModifierListsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the [CatalogModifierList](entity:CatalogModifierList) objects
that apply to the targeted [CatalogItem](entity:CatalogItem) without having
to perform an upsert on the entire item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.update_item_modifier_lists(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateItemModifierListsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.update_item_modifier_lists(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateItemModifierListsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpdateItemModifierListsRequest](square/models/update_item_modifier_lists_request.py) \| [UpdateItemModifierListsRequestDict](square/models/update_item_modifier_lists_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateItemModifierListsResponse](square/models/update_item_modifier_lists_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateItemModifierListsResponse](square/models/update_item_modifier_lists_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_item_taxes(body: UpdateItemTaxesRequest | UpdateItemTaxesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateItemTaxesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the [CatalogTax](entity:CatalogTax) objects that apply to the
targeted [CatalogItem](entity:CatalogItem) without having to perform an
upsert on the entire item.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.update_item_taxes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateItemTaxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.update_item_taxes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateItemTaxesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpdateItemTaxesRequest](square/models/update_item_taxes_request.py) \| [UpdateItemTaxesRequestDict](square/models/update_item_taxes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateItemTaxesResponse](square/models/update_item_taxes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateItemTaxesResponse](square/models/update_item_taxes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_catalog_object(body: UpsertCatalogObjectRequest | UpsertCatalogObjectRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertCatalogObjectResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new or updates the specified [CatalogObject](entity:CatalogObject).

This endpoint uses full-replacement semantics. The client must send the complete object, and any
field absent from the request is interpreted as an intentional clear. This logic applies to
nested objects as well. For example, omitting inlined children like variations will delete them.

To ensure consistency, only one update request is processed at a time per seller account.
While one (batch or non-batch) update request is being processed, other (batched and non-batched)
update requests are rejected with the `429` error code.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.catalog.with_raw_response.upsert_catalog_object(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertCatalogObjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.catalog.with_raw_response.upsert_catalog_object(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertCatalogObjectResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpsertCatalogObjectRequest](square/models/upsert_catalog_object_request.py) \| [UpsertCatalogObjectRequestDict](square/models/upsert_catalog_object_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertCatalogObjectResponse](square/models/upsert_catalog_object_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertCatalogObjectResponse](square/models/upsert_catalog_object_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Channels

> Source: [Channels](square/apis/channels.py)

<details>
<summary><code>def bulk_retrieve_channels(body: BulkRetrieveChannelsRequest | BulkRetrieveChannelsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkRetrieveChannelsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `POST` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.channels.with_raw_response.bulk_retrieve_channels(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveChannelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.channels.with_raw_response.bulk_retrieve_channels(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveChannelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkRetrieveChannelsRequest](square/models/bulk_retrieve_channels_request.py) \| [BulkRetrieveChannelsRequestDict](square/models/bulk_retrieve_channels_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkRetrieveChannelsResponse](square/models/bulk_retrieve_channels_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkRetrieveChannelsResponse](square/models/bulk_retrieve_channels_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_channels(*, reference_type: ReferenceTypeOrStr | None = None, reference_id: str | None = None, status: ChannelStatusOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListChannelsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.channels.with_raw_response.list_channels()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListChannelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.channels.with_raw_response.list_channels()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListChannelsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reference_type</code> | <code>[ReferenceTypeOrStr](square/models/enums/reference_type.py) \| None</code> | Type of reference associated to channel<br>**Default**: <code>None</code> |
| <code>reference_id</code> | <code>str \| None</code> | id of reference associated to channel<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[ChannelStatusOrStr](square/models/enums/channel_status.py) \| None</code> | Status of channel<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | Cursor to fetch the next result<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | Maximum number of results to return.<br>When not provided the returned results will be cap at 100 channels.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListChannelsResponse](square/models/list_channels_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListChannelsResponse](square/models/list_channels_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_channel(channel_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveChannelResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.channels.with_raw_response.retrieve_channel(channel_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveChannelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.channels.with_raw_response.retrieve_channel(channel_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveChannelResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>channel_id</code> | <code>str</code> | A channel id |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveChannelResponse](square/models/retrieve_channel_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveChannelResponse](square/models/retrieve_channel_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CheckoutApi

> Source: [CheckoutApi](square/apis/checkout_api.py)

<details>
<summary><code>def create_checkout(location_id: str, body: CreateCheckoutRequest | CreateCheckoutRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCheckoutResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Links a `checkoutId` to a `checkout_page_url` that customers are
directed to in order to provide their payment information using a
payment processing workflow hosted on connect.squareup.com. 

NOTE: The Checkout API has been updated with new features. 
For more information, see [Checkout API highlights](https://developer.squareup.com/docs/checkout-api#checkout-api-highlights).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.create_checkout(location_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.create_checkout(location_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the business location to associate the checkout with. |
| <code>body</code> | <code>[CreateCheckoutRequest](square/models/create_checkout_request.py) \| [CreateCheckoutRequestDict](square/models/create_checkout_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCheckoutResponse](square/models/create_checkout_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCheckoutResponse](square/models/create_checkout_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_payment_link(body: CreatePaymentLinkRequest | CreatePaymentLinkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreatePaymentLinkResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to pay for goods and services.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.create_payment_link(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreatePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.create_payment_link(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreatePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreatePaymentLinkRequest](square/models/create_payment_link_request.py) \| [CreatePaymentLinkRequestDict](square/models/create_payment_link_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreatePaymentLinkResponse](square/models/create_payment_link_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreatePaymentLinkResponse](square/models/create_payment_link_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_payment_link(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeletePaymentLinkResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a payment link.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.delete_payment_link(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeletePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.delete_payment_link(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeletePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the payment link to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeletePaymentLinkResponse](square/models/delete_payment_link_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeletePaymentLinkResponse](square/models/delete_payment_link_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_payment_links(*, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPaymentLinksResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all payment links.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.list_payment_links()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPaymentLinksResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.list_payment_links()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPaymentLinksResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>If a cursor is not provided, the endpoint returns the first page of the results.<br>For more  information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | A limit on the number of results to return per page. The limit is advisory and<br>the implementation might return more or less results. If the supplied limit is negative, zero, or<br>greater than the maximum limit of 1000, it is ignored.<br><br>Default value: `100`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListPaymentLinksResponse](square/models/list_payment_links_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPaymentLinksResponse](square/models/list_payment_links_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location_settings(location_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLocationSettingsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the location-level settings for a Square-hosted checkout page.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.retrieve_location_settings(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.retrieve_location_settings(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location for which to retrieve settings. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLocationSettingsResponse](square/models/retrieve_location_settings_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLocationSettingsResponse](square/models/retrieve_location_settings_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_merchant_settings(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveMerchantSettingsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the merchant-level settings for a Square-hosted checkout page.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.retrieve_merchant_settings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.retrieve_merchant_settings()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveMerchantSettingsResponse](square/models/retrieve_merchant_settings_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveMerchantSettingsResponse](square/models/retrieve_merchant_settings_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_payment_link(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrievePaymentLinkResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a payment link.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.retrieve_payment_link(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrievePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.retrieve_payment_link(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrievePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of link to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrievePaymentLinkResponse](square/models/retrieve_payment_link_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrievePaymentLinkResponse](square/models/retrieve_payment_link_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_location_settings(location_id: str, body: UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateLocationSettingsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the location-level settings for a Square-hosted checkout page.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.update_location_settings(location_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateLocationSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.update_location_settings(location_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateLocationSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location for which to retrieve settings. |
| <code>body</code> | <code>[UpdateLocationSettingsRequest](square/models/update_location_settings_request.py) \| [UpdateLocationSettingsRequestDict](square/models/update_location_settings_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateLocationSettingsResponse](square/models/update_location_settings_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateLocationSettingsResponse](square/models/update_location_settings_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_merchant_settings(body: UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateMerchantSettingsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the merchant-level settings for a Square-hosted checkout page.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.update_merchant_settings(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateMerchantSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.update_merchant_settings(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateMerchantSettingsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpdateMerchantSettingsRequest](square/models/update_merchant_settings_request.py) \| [UpdateMerchantSettingsRequestDict](square/models/update_merchant_settings_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateMerchantSettingsResponse](square/models/update_merchant_settings_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateMerchantSettingsResponse](square/models/update_merchant_settings_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_payment_link(id: str, body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdatePaymentLinkResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a payment link. You can update the `payment_link` fields such as
`description`, `checkout_options`, and  `pre_populated_data`.
You cannot update other fields such as the `order_id`, `version`, `URL`, or `timestamp` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.checkout_api.with_raw_response.update_payment_link(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.checkout_api.with_raw_response.update_payment_link(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatePaymentLinkResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the payment link to update. |
| <code>body</code> | <code>[UpdatePaymentLinkRequest](square/models/update_payment_link_request.py) \| [UpdatePaymentLinkRequestDict](square/models/update_payment_link_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdatePaymentLinkResponse](square/models/update_payment_link_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdatePaymentLinkResponse](square/models/update_payment_link_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CustomerCustomAttributes

> Source: [CustomerCustomAttributes](square/apis/customer_custom_attributes.py)

<details>
<summary><code>def bulk_upsert_customer_custom_attributes(body: BulkUpsertCustomerCustomAttributesRequest | BulkUpsertCustomerCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpsertCustomerCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates [custom attributes](entity:CustomAttribute) for customer profiles as a bulk operation.

Use this endpoint to set the value of one or more custom attributes for one or more customer profiles.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateCustomerCustomAttributeDefinition](api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition) endpoint.

This `BulkUpsertCustomerCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a customer ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.bulk_upsert_customer_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertCustomerCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.bulk_upsert_customer_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertCustomerCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpsertCustomerCustomAttributesRequest](square/models/bulk_upsert_customer_custom_attributes_request.py) \| [BulkUpsertCustomerCustomAttributesRequestDict](square/models/bulk_upsert_customer_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpsertCustomerCustomAttributesResponse](square/models/bulk_upsert_customer_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpsertCustomerCustomAttributesResponse](square/models/bulk_upsert_customer_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_customer_custom_attribute_definition(body: CreateCustomerCustomAttributeDefinitionRequest | CreateCustomerCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCustomerCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a customer-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with customer profiles.

A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertCustomerCustomAttribute](api-endpoint:CustomerCustomAttributes-UpsertCustomerCustomAttribute) or
[BulkUpsertCustomerCustomAttributes](api-endpoint:CustomerCustomAttributes-BulkUpsertCustomerCustomAttributes)
to set the custom attribute for customer profiles in the seller's Customer Directory.

Sellers can view all custom attributes in exported customer data, including those set to
`VISIBILITY_HIDDEN`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.create_customer_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.create_customer_custom_attribute_definition(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCustomerCustomAttributeDefinitionRequest](square/models/create_customer_custom_attribute_definition_request.py) \| [CreateCustomerCustomAttributeDefinitionRequestDict](square/models/create_customer_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCustomerCustomAttributeDefinitionResponse](square/models/create_customer_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCustomerCustomAttributeDefinitionResponse](square/models/create_customer_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_customer_custom_attribute(customer_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteCustomerCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a customer profile.

To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.delete_customer_custom_attribute(customer_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.delete_customer_custom_attribute(
    customer_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the target [customer profile](entity:Customer). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteCustomerCustomAttributeResponse](square/models/delete_customer_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteCustomerCustomAttributeResponse](square/models/delete_customer_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_customer_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteCustomerCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a customer-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

Deleting a custom attribute definition also deletes the corresponding custom attribute from
all customer profiles in the seller's Customer Directory.

Only the definition owner can delete a custom attribute definition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.delete_customer_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.delete_customer_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteCustomerCustomAttributeDefinitionResponse](square/models/delete_customer_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteCustomerCustomAttributeDefinitionResponse](square/models/delete_customer_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customer_custom_attribute_definitions(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCustomerCustomAttributeDefinitionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the customer-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.

When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that
seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.list_customer_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.list_customer_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCustomerCustomAttributeDefinitionsResponse](square/models/list_customer_custom_attribute_definitions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCustomerCustomAttributeDefinitionsResponse](square/models/list_customer_custom_attribute_definitions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customer_custom_attributes(customer_id: str, *, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCustomerCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with a customer profile.

You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.

When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.list_customer_custom_attributes(customer_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.list_customer_custom_attributes(customer_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the target [customer profile](entity:Customer). |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>with_definitions</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCustomerCustomAttributesResponse](square/models/list_customer_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCustomerCustomAttributesResponse](square/models/list_customer_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_customer_custom_attribute(customer_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCustomerCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with a customer profile.

You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.

To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.retrieve_customer_custom_attribute(customer_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.retrieve_customer_custom_attribute(
    customer_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the target [customer profile](entity:Customer). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>with_definition</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCustomerCustomAttributeResponse](square/models/retrieve_customer_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCustomerCustomAttributeResponse](square/models/retrieve_customer_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_customer_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCustomerCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a customer-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.retrieve_customer_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.retrieve_customer_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCustomerCustomAttributeDefinitionResponse](square/models/retrieve_customer_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCustomerCustomAttributeDefinitionResponse](square/models/retrieve_customer_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_customer_custom_attribute_definition(key: str, body: UpdateCustomerCustomAttributeDefinitionRequest | UpdateCustomerCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateCustomerCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a customer-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.

Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.

Only the definition owner can update a custom attribute definition. Note that sellers can view
all custom attributes in exported customer data, including those set to `VISIBILITY_HIDDEN`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.update_customer_custom_attribute_definition(key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.update_customer_custom_attribute_definition(
    key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCustomerCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to update. |
| <code>body</code> | <code>[UpdateCustomerCustomAttributeDefinitionRequest](square/models/update_customer_custom_attribute_definition_request.py) \| [UpdateCustomerCustomAttributeDefinitionRequestDict](square/models/update_customer_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateCustomerCustomAttributeDefinitionResponse](square/models/update_customer_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateCustomerCustomAttributeDefinitionResponse](square/models/update_customer_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_customer_custom_attribute(customer_id: str, key: str, body: UpsertCustomerCustomAttributeRequest | UpsertCustomerCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertCustomerCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for a customer profile.

Use this endpoint to set the value of a custom attribute for a specified customer profile.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateCustomerCustomAttributeDefinition](api-endpoint:CustomerCustomAttributes-CreateCustomerCustomAttributeDefinition) endpoint.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_custom_attributes.with_raw_response.upsert_customer_custom_attribute(customer_id, key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertCustomerCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_custom_attributes.with_raw_response.upsert_customer_custom_attribute(
    customer_id, key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertCustomerCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the target [customer profile](entity:Customer). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| <code>body</code> | <code>[UpsertCustomerCustomAttributeRequest](square/models/upsert_customer_custom_attribute_request.py) \| [UpsertCustomerCustomAttributeRequestDict](square/models/upsert_customer_custom_attribute_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertCustomerCustomAttributeResponse](square/models/upsert_customer_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertCustomerCustomAttributeResponse](square/models/upsert_customer_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CustomerGroups

> Source: [CustomerGroups](square/apis/customer_groups.py)

<details>
<summary><code>def create_customer_group(body: CreateCustomerGroupRequest | CreateCustomerGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCustomerGroupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new customer group for a business.

The request must include the `name` value of the group.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_groups.with_raw_response.create_customer_group(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_groups.with_raw_response.create_customer_group(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCustomerGroupRequest](square/models/create_customer_group_request.py) \| [CreateCustomerGroupRequestDict](square/models/create_customer_group_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCustomerGroupResponse](square/models/create_customer_group_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCustomerGroupResponse](square/models/create_customer_group_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_customer_group(group_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteCustomerGroupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a customer group as identified by the `group_id` value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_groups.with_raw_response.delete_customer_group(group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_groups.with_raw_response.delete_customer_group(group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>group_id</code> | <code>str</code> | The ID of the customer group to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteCustomerGroupResponse](square/models/delete_customer_group_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteCustomerGroupResponse](square/models/delete_customer_group_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customer_groups(*, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCustomerGroupsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the list of customer groups of a business.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_groups.with_raw_response.list_customer_groups()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerGroupsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_groups.with_raw_response.list_customer_groups()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerGroupsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.<br>If the limit is less than 1 or greater than 50, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 50.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCustomerGroupsResponse](square/models/list_customer_groups_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCustomerGroupsResponse](square/models/list_customer_groups_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_customer_group(group_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCustomerGroupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific customer group as identified by the `group_id` value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_groups.with_raw_response.retrieve_customer_group(group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_groups.with_raw_response.retrieve_customer_group(group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>group_id</code> | <code>str</code> | The ID of the customer group to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCustomerGroupResponse](square/models/retrieve_customer_group_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCustomerGroupResponse](square/models/retrieve_customer_group_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_customer_group(group_id: str, body: UpdateCustomerGroupRequest | UpdateCustomerGroupRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateCustomerGroupResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a customer group as identified by the `group_id` value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_groups.with_raw_response.update_customer_group(group_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_groups.with_raw_response.update_customer_group(group_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCustomerGroupResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>group_id</code> | <code>str</code> | The ID of the customer group to update. |
| <code>body</code> | <code>[UpdateCustomerGroupRequest](square/models/update_customer_group_request.py) \| [UpdateCustomerGroupRequestDict](square/models/update_customer_group_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateCustomerGroupResponse](square/models/update_customer_group_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateCustomerGroupResponse](square/models/update_customer_group_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## CustomerSegments

> Source: [CustomerSegments](square/apis/customer_segments.py)

<details>
<summary><code>def list_customer_segments(*, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCustomerSegmentsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the list of customer segments of a business.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_segments.with_raw_response.list_customer_segments()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerSegmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_segments.with_raw_response.list_customer_segments()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomerSegmentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by previous calls to `ListCustomerSegments`.<br>This cursor is used to retrieve the next set of query results.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.<br>If the specified limit is less than 1 or greater than 50, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 50.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCustomerSegmentsResponse](square/models/list_customer_segments_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCustomerSegmentsResponse](square/models/list_customer_segments_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_customer_segment(segment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCustomerSegmentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific customer segment as identified by the `segment_id` value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customer_segments.with_raw_response.retrieve_customer_segment(segment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerSegmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customer_segments.with_raw_response.retrieve_customer_segment(segment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerSegmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>segment_id</code> | <code>str</code> | The Square-issued ID of the customer segment. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCustomerSegmentResponse](square/models/retrieve_customer_segment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCustomerSegmentResponse](square/models/retrieve_customer_segment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Customers

> Source: [Customers](square/apis/customers.py)

<details>
<summary><code>def add_group_to_customer(customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AddGroupToCustomerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a group membership to a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.add_group_to_customer(customer_id, group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AddGroupToCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.add_group_to_customer(customer_id, group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AddGroupToCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the customer to add to a group. |
| <code>group_id</code> | <code>str</code> | The ID of the customer group to add the customer to. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[AddGroupToCustomerResponse](square/models/add_group_to_customer_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AddGroupToCustomerResponse](square/models/add_group_to_customer_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_create_customers(body: BulkCreateCustomersRequest | BulkCreateCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkCreateCustomersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple [customer profiles](entity:Customer) for a business.

This endpoint takes a map of individual create requests and returns a map of responses.

You must provide at least one of the following values in each create request:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.bulk_create_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkCreateCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.bulk_create_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkCreateCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkCreateCustomersRequest](square/models/bulk_create_customers_request.py) \| [BulkCreateCustomersRequestDict](square/models/bulk_create_customers_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkCreateCustomersResponse](square/models/bulk_create_customers_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkCreateCustomersResponse](square/models/bulk_create_customers_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_delete_customers(body: BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkDeleteCustomersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes multiple customer profiles.

The endpoint takes a list of customer IDs and returns a map of responses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.bulk_delete_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.bulk_delete_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkDeleteCustomersRequest](square/models/bulk_delete_customers_request.py) \| [BulkDeleteCustomersRequestDict](square/models/bulk_delete_customers_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkDeleteCustomersResponse](square/models/bulk_delete_customers_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkDeleteCustomersResponse](square/models/bulk_delete_customers_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_retrieve_customers(body: BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkRetrieveCustomersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves multiple customer profiles.

This endpoint takes a list of customer IDs and returns a map of responses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.bulk_retrieve_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.bulk_retrieve_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkRetrieveCustomersRequest](square/models/bulk_retrieve_customers_request.py) \| [BulkRetrieveCustomersRequestDict](square/models/bulk_retrieve_customers_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkRetrieveCustomersResponse](square/models/bulk_retrieve_customers_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkRetrieveCustomersResponse](square/models/bulk_retrieve_customers_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_update_customers(body: BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpdateCustomersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates multiple customer profiles.

This endpoint takes a map of individual update requests and returns a map of responses.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.bulk_update_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.bulk_update_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpdateCustomersRequest](square/models/bulk_update_customers_request.py) \| [BulkUpdateCustomersRequestDict](square/models/bulk_update_customers_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpdateCustomersResponse](square/models/bulk_update_customers_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpdateCustomersResponse](square/models/bulk_update_customers_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_customer(body: CreateCustomerRequest | CreateCustomerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCustomerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new customer for a business.

You must provide at least one of the following values in your request to this
endpoint:

- `given_name`
- `family_name`
- `company_name`
- `email_address`
- `phone_number`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.create_customer(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.create_customer(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateCustomerRequest](square/models/create_customer_request.py) \| [CreateCustomerRequestDict](square/models/create_customer_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCustomerResponse](square/models/create_customer_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCustomerResponse](square/models/create_customer_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_customer_card(customer_id: str, body: CreateCustomerCardRequest | CreateCustomerCardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateCustomerCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a card on file to an existing customer.

As with charges, calls to `CreateCustomerCard` are idempotent. Multiple
calls with the same card nonce return the same card record that was created
with the provided nonce during the _first_ call.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.create_customer_card(customer_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.create_customer_card(customer_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateCustomerCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The Square ID of the customer profile the card is linked to. |
| <code>body</code> | <code>[CreateCustomerCardRequest](square/models/create_customer_card_request.py) \| [CreateCustomerCardRequestDict](square/models/create_customer_card_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateCustomerCardResponse](square/models/create_customer_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateCustomerCardResponse](square/models/create_customer_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_customer(customer_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteCustomerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a customer profile from a business.

To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.delete_customer(customer_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.delete_customer(customer_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the customer to delete. |
| <code>version</code> | <code>int \| None</code> | The current version of the customer profile.<br><br>As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteCustomerResponse](square/models/delete_customer_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteCustomerResponse](square/models/delete_customer_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_customer_card(customer_id: str, card_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteCustomerCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a card on file from a customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.delete_customer_card(customer_id, card_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.delete_customer_card(customer_id, card_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteCustomerCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the customer that the card on file belongs to. |
| <code>card_id</code> | <code>str</code> | The ID of the card on file to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteCustomerCardResponse](square/models/delete_customer_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteCustomerCardResponse](square/models/delete_customer_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_customers(*, cursor: str | None = None, limit: int | None = None, sort_field: CustomerSortFieldOrStr | None = None, sort_order: SortOrderOrStr | None = None, count: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListCustomersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists customer profiles associated with a Square account.

Under normal operating conditions, newly created or updated customer profiles become available
for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.list_customers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.list_customers()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.<br>If the specified limit is less than 1 or greater than 100, Square returns a `400 VALUE_TOO_LOW` or `400 VALUE_TOO_HIGH` error. The default value is 100.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>sort_field</code> | <code>[CustomerSortFieldOrStr](square/models/enums/customer_sort_field.py) \| None</code> | Indicates how customers should be sorted.<br><br>The default value is `DEFAULT`.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | Indicates whether customers should be sorted in ascending (`ASC`) or<br>descending (`DESC`) order.<br><br>The default value is `ASC`.<br>**Default**: <code>None</code> |
| <code>count</code> | <code>bool \| None</code> | Indicates whether to return the total count of customers in the `count` field of the response.<br><br>The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListCustomersResponse](square/models/list_customers_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListCustomersResponse](square/models/list_customers_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def remove_group_from_customer(customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RemoveGroupFromCustomerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes a group membership from a customer.

The customer is identified by the `customer_id` value
and the customer group is identified by the `group_id` value.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.remove_group_from_customer(customer_id, group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RemoveGroupFromCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.remove_group_from_customer(customer_id, group_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RemoveGroupFromCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the customer to remove from the group. |
| <code>group_id</code> | <code>str</code> | The ID of the customer group to remove the customer from. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RemoveGroupFromCustomerResponse](square/models/remove_group_from_customer_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RemoveGroupFromCustomerResponse](square/models/remove_group_from_customer_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_customer(customer_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveCustomerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details for a single customer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.retrieve_customer(customer_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.retrieve_customer(customer_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the customer to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveCustomerResponse](square/models/retrieve_customer_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveCustomerResponse](square/models/retrieve_customer_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_customers(body: SearchCustomersRequest | SearchCustomersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchCustomersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches the customer profiles associated with a Square account using one or more supported query filters.

Calling `SearchCustomers` without any explicit query filter returns all
customer profiles ordered alphabetically based on `given_name` and
`family_name`.

Under normal operating conditions, newly created or updated customer profiles become available
for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated
profiles can take closer to one minute or longer, especially during network incidents and outages.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.search_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.search_customers(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchCustomersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchCustomersRequest](square/models/search_customers_request.py) \| [SearchCustomersRequestDict](square/models/search_customers_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchCustomersResponse](square/models/search_customers_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchCustomersResponse](square/models/search_customers_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_customer(customer_id: str, body: UpdateCustomerRequest | UpdateCustomerRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateCustomerResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required in the request.
To add or update a field, specify the new value. To remove a field, specify `null`.

To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.customers.with_raw_response.update_customer(customer_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.customers.with_raw_response.update_customer(customer_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateCustomerResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>customer_id</code> | <code>str</code> | The ID of the customer to update. |
| <code>body</code> | <code>[UpdateCustomerRequest](square/models/update_customer_request.py) \| [UpdateCustomerRequestDict](square/models/update_customer_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateCustomerResponse](square/models/update_customer_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateCustomerResponse](square/models/update_customer_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Devices

> Source: [Devices](square/apis/devices.py)

<details>
<summary><code>def create_device_code(body: CreateDeviceCodeRequest | CreateDeviceCodeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateDeviceCodeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a DeviceCode that can be used to login to a Square Terminal device to enter the connected
terminal mode.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices.with_raw_response.create_device_code(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateDeviceCodeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices.with_raw_response.create_device_code(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateDeviceCodeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateDeviceCodeRequest](square/models/create_device_code_request.py) \| [CreateDeviceCodeRequestDict](square/models/create_device_code_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateDeviceCodeResponse](square/models/create_device_code_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateDeviceCodeResponse](square/models/create_device_code_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device(device_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetDeviceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves Device with the associated `device_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices.with_raw_response.get_device(device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeviceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices.with_raw_response.get_device(device_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeviceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>device_id</code> | <code>str</code> | The unique ID for the desired `Device`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetDeviceResponse](square/models/get_device_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetDeviceResponse](square/models/get_device_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_device_code(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetDeviceCodeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves DeviceCode with the associated ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices.with_raw_response.get_device_code(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeviceCodeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices.with_raw_response.get_device_code(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetDeviceCodeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The unique identifier for the device code. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetDeviceCodeResponse](square/models/get_device_code_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetDeviceCodeResponse](square/models/get_device_code_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_device_codes(*, cursor: str | None = None, location_id: str | None = None, product_type: ProductTypeOrStr | None = None, status: DeviceCodeStatusOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListDeviceCodesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all DeviceCodes associated with the merchant.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices.with_raw_response.list_device_codes()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDeviceCodesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices.with_raw_response.list_device_codes()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDeviceCodesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | If specified, only returns DeviceCodes of the specified location.<br>Returns DeviceCodes of all locations if empty.<br>**Default**: <code>None</code> |
| <code>product_type</code> | <code>[ProductTypeOrStr](square/models/enums/product_type.py) \| None</code> | If specified, only returns DeviceCodes targeting the specified product type.<br>Returns DeviceCodes of all product types if empty.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[DeviceCodeStatusOrStr](square/models/enums/device_code_status.py) \| None</code> | If specified, returns DeviceCodes with the specified statuses.<br>Returns DeviceCodes of status `PAIRED` and `UNPAIRED` if empty.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListDeviceCodesResponse](square/models/list_device_codes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListDeviceCodesResponse](square/models/list_device_codes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_devices(*, cursor: str | None = None, sort_order: SortOrderOrStr | None = None, limit: int | None = None, location_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListDevicesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

List devices associated with the merchant. Currently, only Terminal API
devices are supported.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.devices.with_raw_response.list_devices()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDevicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.devices.with_raw_response.list_devices()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDevicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>See [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination) for more information.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | The order in which results are listed.<br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of results to return in a single page.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | If present, only returns devices at the target location.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListDevicesResponse](square/models/list_devices_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListDevicesResponse](square/models/list_devices_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Disputes

> Source: [Disputes](square/apis/disputes.py)

<details>
<summary><code>def accept_dispute(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AcceptDisputeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and
updates the dispute state to ACCEPTED.

Square debits the disputed amount from the seller’s Square account. If the Square account
does not have sufficient funds, Square debits the associated bank account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.accept_dispute(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AcceptDisputeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.accept_dispute(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AcceptDisputeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute you want to accept. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[AcceptDisputeResponse](square/models/accept_dispute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AcceptDisputeResponse](square/models/accept_dispute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_dispute_evidence_file(dispute_id: str, *, request: CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateDisputeEvidenceFileResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP
multipart/form-data file uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.create_dispute_evidence_file(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateDisputeEvidenceFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.create_dispute_evidence_file(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateDisputeEvidenceFileResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute for which you want to upload evidence. |
| <code>request</code> | <code>[CreateDisputeEvidenceFileRequest](square/models/create_dispute_evidence_file_request.py) \| [CreateDisputeEvidenceFileRequestDict](square/models/create_dispute_evidence_file_request.py) \| None</code> | Defines the parameters for a `CreateDisputeEvidenceFile` request.<br>**Default**: <code>None</code> |
| <code>image_file</code> | <code>bytes \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateDisputeEvidenceFileResponse](square/models/create_dispute_evidence_file_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateDisputeEvidenceFileResponse](square/models/create_dispute_evidence_file_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_dispute_evidence_text(dispute_id: str, body: CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateDisputeEvidenceTextResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads text to use as evidence for a dispute challenge.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.create_dispute_evidence_text(dispute_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateDisputeEvidenceTextResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.create_dispute_evidence_text(dispute_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateDisputeEvidenceTextResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute for which you want to upload evidence. |
| <code>body</code> | <code>[CreateDisputeEvidenceTextRequest](square/models/create_dispute_evidence_text_request.py) \| [CreateDisputeEvidenceTextRequestDict](square/models/create_dispute_evidence_text_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateDisputeEvidenceTextResponse](square/models/create_dispute_evidence_text_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateDisputeEvidenceTextResponse](square/models/create_dispute_evidence_text_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_dispute_evidence(dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteDisputeEvidenceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes specified evidence from a dispute.
Square does not send the bank any evidence that is removed.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.delete_dispute_evidence(dispute_id, evidence_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteDisputeEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.delete_dispute_evidence(dispute_id, evidence_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteDisputeEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute from which you want to remove evidence. |
| <code>evidence_id</code> | <code>str</code> | The ID of the evidence you want to remove. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteDisputeEvidenceResponse](square/models/delete_dispute_evidence_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteDisputeEvidenceResponse](square/models/delete_dispute_evidence_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_dispute_evidence(dispute_id: str, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListDisputeEvidenceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of evidence associated with a dispute.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.list_dispute_evidence(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDisputeEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.list_dispute_evidence(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDisputeEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute. |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListDisputeEvidenceResponse](square/models/list_dispute_evidence_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListDisputeEvidenceResponse](square/models/list_dispute_evidence_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_disputes(*, cursor: str | None = None, states: DisputeStateOrStr | None = None, location_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListDisputesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of disputes associated with a particular account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.list_disputes()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDisputesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.list_disputes()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListDisputesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>states</code> | <code>[DisputeStateOrStr](square/models/enums/dispute_state.py) \| None</code> | The dispute states used to filter the result. If not specified, the endpoint returns all disputes.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | The ID of the location for which to return a list of disputes.<br>If not specified, the endpoint returns disputes associated with all locations.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListDisputesResponse](square/models/list_disputes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListDisputesResponse](square/models/list_disputes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_dispute(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveDisputeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns details about a specific dispute.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.retrieve_dispute(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveDisputeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.retrieve_dispute(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveDisputeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute you want more details about. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveDisputeResponse](square/models/retrieve_dispute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveDisputeResponse](square/models/retrieve_dispute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_dispute_evidence(dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveDisputeEvidenceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the metadata for the evidence specified in the request URL path.

You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be downloaded after you upload it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.retrieve_dispute_evidence(dispute_id, evidence_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveDisputeEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.retrieve_dispute_evidence(dispute_id, evidence_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveDisputeEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute from which you want to retrieve evidence metadata. |
| <code>evidence_id</code> | <code>str</code> | The ID of the evidence to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveDisputeEvidenceResponse](square/models/retrieve_dispute_evidence_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveDisputeEvidenceResponse](square/models/retrieve_dispute_evidence_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def submit_evidence(dispute_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SubmitEvidenceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Submits evidence to the cardholder's bank.

The evidence submitted by this endpoint includes evidence uploaded
using the [CreateDisputeEvidenceFile](api-endpoint:Disputes-CreateDisputeEvidenceFile) and
[CreateDisputeEvidenceText](api-endpoint:Disputes-CreateDisputeEvidenceText) endpoints and
evidence automatically provided by Square, when available. Evidence cannot be removed from
a dispute after submission.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.disputes.with_raw_response.submit_evidence(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SubmitEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.disputes.with_raw_response.submit_evidence(dispute_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SubmitEvidenceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>dispute_id</code> | <code>str</code> | The ID of the dispute for which you want to submit evidence. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SubmitEvidenceResponse](square/models/submit_evidence_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SubmitEvidenceResponse](square/models/submit_evidence_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Employees

> Source: [Employees](square/apis/employees.py)

<details>
<summary><code>def list_employees(*, location_id: str | None = None, status: EmployeeStatusOrStr | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListEmployeesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.employees.with_raw_response.list_employees()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEmployeesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.employees.with_raw_response.list_employees()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEmployeesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[EmployeeStatusOrStr](square/models/enums/employee_status.py) \| None</code> | Specifies the EmployeeStatus to filter the employee by.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The number of employees to be returned on each page.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The token required to retrieve the specified page of results.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListEmployeesResponse](square/models/list_employees_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListEmployeesResponse](square/models/list_employees_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_employee(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveEmployeeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Send a `GET` request.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.employees.with_raw_response.retrieve_employee(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveEmployeeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.employees.with_raw_response.retrieve_employee(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveEmployeeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | UUID for the employee that was requested. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveEmployeeResponse](square/models/retrieve_employee_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveEmployeeResponse](square/models/retrieve_employee_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Events

> Source: [Events](square/apis/events.py)

<details>
<summary><code>def disable_events(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DisableEventsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Disables events to prevent them from being searchable.
All events are disabled by default. You must enable events to make them searchable.
Disabling events for a specific time period prevents them from being searchable, even if you re-enable them later.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.events.with_raw_response.disable_events()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisableEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.events.with_raw_response.disable_events()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DisableEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DisableEventsResponse](square/models/disable_events_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DisableEventsResponse](square/models/disable_events_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def enable_events(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[EnableEventsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables events to make them searchable. Only events that occur while in the enabled state are searchable.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.events.with_raw_response.enable_events()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EnableEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.events.with_raw_response.enable_events()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type EnableEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[EnableEventsResponse](square/models/enable_events_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[EnableEventsResponse](square/models/enable_events_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_event_types(*, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListEventTypesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all event types that you can subscribe to as webhooks or query using the Events API.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.events.with_raw_response.list_event_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEventTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.events.with_raw_response.list_event_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEventTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_version</code> | <code>str \| None</code> | The API version for which to list event types. Setting this field overrides the default version used by the application.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListEventTypesResponse](square/models/list_event_types_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListEventTypesResponse](square/models/list_event_types_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_events(body: SearchEventsRequest | SearchEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchEventsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search for Square API events that occur within a 28-day timeframe.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.events.with_raw_response.search_events(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.events.with_raw_response.search_events(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchEventsRequest](square/models/search_events_request.py) \| [SearchEventsRequestDict](square/models/search_events_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchEventsResponse](square/models/search_events_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchEventsResponse](square/models/search_events_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## GiftCardActivities

> Source: [GiftCardActivities](square/apis/gift_card_activities.py)

<details>
<summary><code>def create_gift_card_activity(body: CreateGiftCardActivityRequest | CreateGiftCardActivityRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateGiftCardActivityResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a gift card activity to manage the balance or state of a [gift card](entity:GiftCard).
For example, create an `ACTIVATE` activity to activate a gift card with an initial balance before first use.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_card_activities.with_raw_response.create_gift_card_activity(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateGiftCardActivityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_card_activities.with_raw_response.create_gift_card_activity(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateGiftCardActivityResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateGiftCardActivityRequest](square/models/create_gift_card_activity_request.py) \| [CreateGiftCardActivityRequestDict](square/models/create_gift_card_activity_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateGiftCardActivityResponse](square/models/create_gift_card_activity_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateGiftCardActivityResponse](square/models/create_gift_card_activity_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_gift_card_activities(*, gift_card_id: str | None = None, type_: str | None = None, location_id: str | None = None, begin_time: str | None = None, end_time: str | None = None, limit: int | None = None, cursor: str | None = None, sort_order: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListGiftCardActivitiesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists gift card activities. By default, you get gift card activities for all
gift cards in the seller's account. You can optionally specify query parameters to
filter the list. For example, you can get a list of gift card activities for a gift card,
for all gift cards in a specific region, or for activities within a time window.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_card_activities.with_raw_response.list_gift_card_activities()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListGiftCardActivitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_card_activities.with_raw_response.list_gift_card_activities()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListGiftCardActivitiesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>gift_card_id</code> | <code>str \| None</code> | If a gift card ID is provided, the endpoint returns activities related <br>to the specified gift card. Otherwise, the endpoint returns all gift card activities for <br>the seller.<br>**Default**: <code>None</code> |
| <code>type_</code> | <code>str \| None</code> | If a [type](entity:GiftCardActivityType) is provided, the endpoint returns gift card activities of the specified type. <br>Otherwise, the endpoint returns all types of gift card activities.<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | If a location ID is provided, the endpoint returns gift card activities for the specified location. <br>Otherwise, the endpoint returns gift card activities for all locations.<br>**Default**: <code>None</code> |
| <code>begin_time</code> | <code>str \| None</code> | The timestamp for the beginning of the reporting period, in RFC 3339 format.<br>This start time is inclusive. The default value is the current time minus one year.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>str \| None</code> | The timestamp for the end of the reporting period, in RFC 3339 format.<br>This end time is inclusive. The default value is the current time.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | If a limit is provided, the endpoint returns the specified number <br>of results (or fewer) per page. The maximum value is 100. The default value is 50.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>If a cursor is not provided, the endpoint returns the first page of the results.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>str \| None</code> | The order in which the endpoint returns the activities, based on `created_at`.<br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListGiftCardActivitiesResponse](square/models/list_gift_card_activities_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListGiftCardActivitiesResponse](square/models/list_gift_card_activities_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## GiftCards

> Source: [GiftCards](square/apis/gift_cards.py)

<details>
<summary><code>def create_gift_card(body: CreateGiftCardRequest | CreateGiftCardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateGiftCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a digital gift card or registers a physical (plastic) gift card. The resulting gift card
has a `PENDING` state. To activate a gift card so that it can be redeemed for purchases, call
[CreateGiftCardActivity](api-endpoint:GiftCardActivities-CreateGiftCardActivity) and create an `ACTIVATE`
activity with the initial balance. Alternatively, you can use [RefundPayment](api-endpoint:Refunds-RefundPayment)
to refund a payment to the new gift card.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.create_gift_card(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.create_gift_card(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateGiftCardRequest](square/models/create_gift_card_request.py) \| [CreateGiftCardRequestDict](square/models/create_gift_card_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateGiftCardResponse](square/models/create_gift_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateGiftCardResponse](square/models/create_gift_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def link_customer_to_gift_card(gift_card_id: str, body: LinkCustomerToGiftCardRequest | LinkCustomerToGiftCardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[LinkCustomerToGiftCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Links a customer to a gift card, which is also referred to as adding a card on file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.link_customer_to_gift_card(gift_card_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkCustomerToGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.link_customer_to_gift_card(gift_card_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type LinkCustomerToGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>gift_card_id</code> | <code>str</code> | The ID of the gift card to be linked. |
| <code>body</code> | <code>[LinkCustomerToGiftCardRequest](square/models/link_customer_to_gift_card_request.py) \| [LinkCustomerToGiftCardRequestDict](square/models/link_customer_to_gift_card_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[LinkCustomerToGiftCardResponse](square/models/link_customer_to_gift_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[LinkCustomerToGiftCardResponse](square/models/link_customer_to_gift_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_gift_cards(*, type_: str | None = None, state: str | None = None, limit: int | None = None, cursor: str | None = None, customer_id: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListGiftCardsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all gift cards. You can specify optional filters to retrieve 
a subset of the gift cards. Results are sorted by `created_at` in ascending order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.list_gift_cards()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListGiftCardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.list_gift_cards()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListGiftCardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>type_</code> | <code>str \| None</code> | If a [type](entity:GiftCardType) is provided, the endpoint returns gift cards of the specified type.<br>Otherwise, the endpoint returns gift cards of all types.<br>**Default**: <code>None</code> |
| <code>state</code> | <code>str \| None</code> | If a [state](entity:GiftCardStatus) is provided, the endpoint returns the gift cards in the specified state.<br>Otherwise, the endpoint returns the gift cards of all states.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | If a limit is provided, the endpoint returns only the specified number of results per page.<br>The maximum value is 200. The default value is 30.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>If a cursor is not provided, the endpoint returns the first page of the results. <br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>customer_id</code> | <code>str \| None</code> | If a customer ID is provided, the endpoint returns only the gift cards linked to the specified customer.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListGiftCardsResponse](square/models/list_gift_cards_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListGiftCardsResponse](square/models/list_gift_cards_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_gift_card(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveGiftCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a gift card using the gift card ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.retrieve_gift_card(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.retrieve_gift_card(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the gift card to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveGiftCardResponse](square/models/retrieve_gift_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveGiftCardResponse](square/models/retrieve_gift_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_gift_card_from_gan(body: RetrieveGiftCardFromGanrequest | RetrieveGiftCardFromGanrequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveGiftCardFromGanresponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a gift card using the gift card account number (GAN).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.retrieve_gift_card_from_gan(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveGiftCardFromGanresponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.retrieve_gift_card_from_gan(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveGiftCardFromGanresponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RetrieveGiftCardFromGanrequest](square/models/retrieve_gift_card_from_ganrequest.py) \| [RetrieveGiftCardFromGanrequestDict](square/models/retrieve_gift_card_from_ganrequest.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveGiftCardFromGanresponse](square/models/retrieve_gift_card_from_ganresponse.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveGiftCardFromGanresponse](square/models/retrieve_gift_card_from_ganresponse.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_gift_card_from_nonce(body: RetrieveGiftCardFromNonceRequest | RetrieveGiftCardFromNonceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveGiftCardFromNonceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a gift card using a secure payment token that represents the gift card.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.retrieve_gift_card_from_nonce(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveGiftCardFromNonceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.retrieve_gift_card_from_nonce(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveGiftCardFromNonceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RetrieveGiftCardFromNonceRequest](square/models/retrieve_gift_card_from_nonce_request.py) \| [RetrieveGiftCardFromNonceRequestDict](square/models/retrieve_gift_card_from_nonce_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveGiftCardFromNonceResponse](square/models/retrieve_gift_card_from_nonce_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveGiftCardFromNonceResponse](square/models/retrieve_gift_card_from_nonce_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def unlink_customer_from_gift_card(gift_card_id: str, body: UnlinkCustomerFromGiftCardRequest | UnlinkCustomerFromGiftCardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UnlinkCustomerFromGiftCardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Unlinks a customer from a gift card, which is also referred to as removing a card on file.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.gift_cards.with_raw_response.unlink_customer_from_gift_card(gift_card_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnlinkCustomerFromGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.gift_cards.with_raw_response.unlink_customer_from_gift_card(gift_card_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UnlinkCustomerFromGiftCardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>gift_card_id</code> | <code>str</code> | The ID of the gift card to be unlinked. |
| <code>body</code> | <code>[UnlinkCustomerFromGiftCardRequest](square/models/unlink_customer_from_gift_card_request.py) \| [UnlinkCustomerFromGiftCardRequestDict](square/models/unlink_customer_from_gift_card_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UnlinkCustomerFromGiftCardResponse](square/models/unlink_customer_from_gift_card_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UnlinkCustomerFromGiftCardResponse](square/models/unlink_customer_from_gift_card_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Inventory

> Source: [Inventory](square/apis/inventory.py)

<details>
<summary><code>def batch_change_inventory(body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchChangeInventoryResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Applies adjustments and counts to the provided item quantities.

On success: returns the current calculated counts for all objects
referenced in the request.
On failure: returns a list of related errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.batch_change_inventory(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchChangeInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.batch_change_inventory(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchChangeInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchChangeInventoryRequest](square/models/batch_change_inventory_request.py) \| [BatchChangeInventoryRequestDict](square/models/batch_change_inventory_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchChangeInventoryResponse](square/models/batch_change_inventory_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchChangeInventoryResponse](square/models/batch_change_inventory_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def batch_retrieve_inventory_changes(body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchRetrieveInventoryChangesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns historical physical counts and adjustments based on the
provided filter criteria.

Results are paginated and sorted in ascending order according their
`occurred_at` timestamp (oldest first).

BatchRetrieveInventoryChanges is a catch-all query endpoint for queries
that cannot be handled by other, simpler endpoints.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.batch_retrieve_inventory_changes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryChangesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.batch_retrieve_inventory_changes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryChangesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchRetrieveInventoryChangesRequest](square/models/batch_retrieve_inventory_changes_request.py) \| [BatchRetrieveInventoryChangesRequestDict](square/models/batch_retrieve_inventory_changes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchRetrieveInventoryChangesResponse](square/models/batch_retrieve_inventory_changes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchRetrieveInventoryChangesResponse](square/models/batch_retrieve_inventory_changes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def batch_retrieve_inventory_counts(body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchRetrieveInventoryCountsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns current counts for the provided
[CatalogObject](entity:CatalogObject)s at the requested
[Location](entity:Location)s.

Results are paginated and sorted in descending order according to their
`calculated_at` timestamp (newest first).

When `updated_after` is specified, only counts that have changed since that
time (based on the server timestamp for the most recent change) are
returned. This allows clients to perform a "sync" operation, for example
in response to receiving a Webhook notification.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.batch_retrieve_inventory_counts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.batch_retrieve_inventory_counts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchRetrieveInventoryCountsRequest](square/models/batch_retrieve_inventory_counts_request.py) \| [BatchRetrieveInventoryCountsRequestDict](square/models/batch_retrieve_inventory_counts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchRetrieveInventoryCountsResponse](square/models/batch_retrieve_inventory_counts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchRetrieveInventoryCountsResponse](square/models/batch_retrieve_inventory_counts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_inventory_adjustment_reason(body: CreateInventoryAdjustmentReasonRequest | CreateInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateInventoryAdjustmentReasonResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a custom inventory adjustment reason.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.create_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.create_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateInventoryAdjustmentReasonRequest](square/models/create_inventory_adjustment_reason_request.py) \| [CreateInventoryAdjustmentReasonRequestDict](square/models/create_inventory_adjustment_reason_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateInventoryAdjustmentReasonResponse](square/models/create_inventory_adjustment_reason_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateInventoryAdjustmentReasonResponse](square/models/create_inventory_adjustment_reason_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_inventory_adjustment_reason(body: DeleteInventoryAdjustmentReasonRequest | DeleteInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteInventoryAdjustmentReasonResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Soft deletes a custom inventory adjustment reason.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.delete_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.delete_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[DeleteInventoryAdjustmentReasonRequest](square/models/delete_inventory_adjustment_reason_request.py) \| [DeleteInventoryAdjustmentReasonRequestDict](square/models/delete_inventory_adjustment_reason_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteInventoryAdjustmentReasonResponse](square/models/delete_inventory_adjustment_reason_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteInventoryAdjustmentReasonResponse](square/models/delete_inventory_adjustment_reason_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deprecated_batch_change_inventory(body: BatchChangeInventoryRequest | BatchChangeInventoryRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchChangeInventoryResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated version of [BatchChangeInventory](api-endpoint:Inventory-BatchChangeInventory) after the endpoint URL
is updated to conform to the standard convention.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.deprecated_batch_change_inventory(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchChangeInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.deprecated_batch_change_inventory(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchChangeInventoryResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchChangeInventoryRequest](square/models/batch_change_inventory_request.py) \| [BatchChangeInventoryRequestDict](square/models/batch_change_inventory_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchChangeInventoryResponse](square/models/batch_change_inventory_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchChangeInventoryResponse](square/models/batch_change_inventory_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deprecated_batch_retrieve_inventory_changes(body: BatchRetrieveInventoryChangesRequest | BatchRetrieveInventoryChangesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchRetrieveInventoryChangesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated version of [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges) after the endpoint URL
is updated to conform to the standard convention.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.deprecated_batch_retrieve_inventory_changes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryChangesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.deprecated_batch_retrieve_inventory_changes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryChangesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchRetrieveInventoryChangesRequest](square/models/batch_retrieve_inventory_changes_request.py) \| [BatchRetrieveInventoryChangesRequestDict](square/models/batch_retrieve_inventory_changes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchRetrieveInventoryChangesResponse](square/models/batch_retrieve_inventory_changes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchRetrieveInventoryChangesResponse](square/models/batch_retrieve_inventory_changes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deprecated_batch_retrieve_inventory_counts(body: BatchRetrieveInventoryCountsRequest | BatchRetrieveInventoryCountsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchRetrieveInventoryCountsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated version of [BatchRetrieveInventoryCounts](api-endpoint:Inventory-BatchRetrieveInventoryCounts) after the endpoint URL
is updated to conform to the standard convention.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.deprecated_batch_retrieve_inventory_counts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.deprecated_batch_retrieve_inventory_counts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveInventoryCountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchRetrieveInventoryCountsRequest](square/models/batch_retrieve_inventory_counts_request.py) \| [BatchRetrieveInventoryCountsRequestDict](square/models/batch_retrieve_inventory_counts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchRetrieveInventoryCountsResponse](square/models/batch_retrieve_inventory_counts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchRetrieveInventoryCountsResponse](square/models/batch_retrieve_inventory_counts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deprecated_retrieve_inventory_adjustment(adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryAdjustmentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated version of [RetrieveInventoryAdjustment](api-endpoint:Inventory-RetrieveInventoryAdjustment) after the endpoint URL
is updated to conform to the standard convention.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.deprecated_retrieve_inventory_adjustment(adjustment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryAdjustmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.deprecated_retrieve_inventory_adjustment(adjustment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryAdjustmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>adjustment_id</code> | <code>str</code> | ID of the [InventoryAdjustment](entity:InventoryAdjustment) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryAdjustmentResponse](square/models/retrieve_inventory_adjustment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryAdjustmentResponse](square/models/retrieve_inventory_adjustment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def deprecated_retrieve_inventory_physical_count(physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deprecated version of [RetrieveInventoryPhysicalCount](api-endpoint:Inventory-RetrieveInventoryPhysicalCount) after the endpoint URL
is updated to conform to the standard convention.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.deprecated_retrieve_inventory_physical_count(physical_count_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryPhysicalCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.deprecated_retrieve_inventory_physical_count(physical_count_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryPhysicalCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>physical_count_id</code> | <code>str</code> | ID of the<br>[InventoryPhysicalCount](entity:InventoryPhysicalCount) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryPhysicalCountResponse](square/models/retrieve_inventory_physical_count_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryPhysicalCountResponse](square/models/retrieve_inventory_physical_count_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_inventory_adjustment_reasons(*, include_deleted: bool | None = False, include_system_codes: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListInventoryAdjustmentReasonsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the standard and custom inventory adjustment reasons available
to the seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.list_inventory_adjustment_reasons()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInventoryAdjustmentReasonsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.list_inventory_adjustment_reasons()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInventoryAdjustmentReasonsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>include_deleted</code> | <code>bool \| None</code> | Indicates whether the response should include deleted custom inventory<br>adjustment reasons. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>include_system_codes</code> | <code>bool \| None</code> | Indicates whether the response should include Square-generated system<br>inventory adjustment reason codes that cannot be used to write adjustments<br>from the Connect API, such as `SALE`, `RECOUNT`, `TRANSFER`, `IN_TRANSIT`,<br>and `CANCELED_SALE`. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListInventoryAdjustmentReasonsResponse](square/models/list_inventory_adjustment_reasons_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListInventoryAdjustmentReasonsResponse](square/models/list_inventory_adjustment_reasons_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def restore_inventory_adjustment_reason(body: RestoreInventoryAdjustmentReasonRequest | RestoreInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RestoreInventoryAdjustmentReasonResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Restores a soft-deleted custom inventory adjustment reason.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.restore_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RestoreInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.restore_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RestoreInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RestoreInventoryAdjustmentReasonRequest](square/models/restore_inventory_adjustment_reason_request.py) \| [RestoreInventoryAdjustmentReasonRequestDict](square/models/restore_inventory_adjustment_reason_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RestoreInventoryAdjustmentReasonResponse](square/models/restore_inventory_adjustment_reason_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RestoreInventoryAdjustmentReasonResponse](square/models/restore_inventory_adjustment_reason_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_inventory_adjustment(adjustment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryAdjustmentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the [InventoryAdjustment](entity:InventoryAdjustment) object
with the provided `adjustment_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.retrieve_inventory_adjustment(adjustment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryAdjustmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.retrieve_inventory_adjustment(adjustment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryAdjustmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>adjustment_id</code> | <code>str</code> | ID of the [InventoryAdjustment](entity:InventoryAdjustment) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryAdjustmentResponse](square/models/retrieve_inventory_adjustment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryAdjustmentResponse](square/models/retrieve_inventory_adjustment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_inventory_adjustment_reason(body: RetrieveInventoryAdjustmentReasonRequest | RetrieveInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryAdjustmentReasonResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the inventory adjustment reason identified by the provided
`reason_id`. Deleted custom reasons can be retrieved by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.retrieve_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.retrieve_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RetrieveInventoryAdjustmentReasonRequest](square/models/retrieve_inventory_adjustment_reason_request.py) \| [RetrieveInventoryAdjustmentReasonRequestDict](square/models/retrieve_inventory_adjustment_reason_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryAdjustmentReasonResponse](square/models/retrieve_inventory_adjustment_reason_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryAdjustmentReasonResponse](square/models/retrieve_inventory_adjustment_reason_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_inventory_changes(catalog_object_id: str, *, location_ids: str | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryChangesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a set of physical counts and inventory adjustments for the
provided [CatalogObject](entity:CatalogObject) at the requested
[Location](entity:Location)s.

You can achieve the same result by calling [BatchRetrieveInventoryChanges](api-endpoint:Inventory-BatchRetrieveInventoryChanges)
and having the `catalog_object_ids` list contain a single element of the `CatalogObject` ID.

Results are paginated and sorted in descending order according to their
`occurred_at` timestamp (newest first).

There are no limits on how far back the caller can page. This endpoint can be
used to display recent changes for a specific item. For more
sophisticated queries, use a batch endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.retrieve_inventory_changes(catalog_object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryChangesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.retrieve_inventory_changes(catalog_object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryChangesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>catalog_object_id</code> | <code>str</code> | ID of the [CatalogObject](entity:CatalogObject) to retrieve. |
| <code>location_ids</code> | <code>str \| None</code> | The [Location](entity:Location) IDs to look up as a comma-separated<br>list. An empty list queries all locations.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryChangesResponse](square/models/retrieve_inventory_changes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryChangesResponse](square/models/retrieve_inventory_changes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_inventory_count(catalog_object_id: str, *, location_ids: str | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryCountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the current calculated stock count for a given
[CatalogObject](entity:CatalogObject) at a given set of
[Location](entity:Location)s. Responses are paginated and unsorted.
For more sophisticated queries, use a batch endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.retrieve_inventory_count(catalog_object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.retrieve_inventory_count(catalog_object_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>catalog_object_id</code> | <code>str</code> | ID of the [CatalogObject](entity:CatalogObject) to retrieve. |
| <code>location_ids</code> | <code>str \| None</code> | The [Location](entity:Location) IDs to look up as a comma-separated<br>list. An empty list queries all locations.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for the original query.<br><br>See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryCountResponse](square/models/retrieve_inventory_count_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryCountResponse](square/models/retrieve_inventory_count_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_inventory_physical_count(physical_count_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveInventoryPhysicalCountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns the [InventoryPhysicalCount](entity:InventoryPhysicalCount)
object with the provided `physical_count_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.retrieve_inventory_physical_count(physical_count_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryPhysicalCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.retrieve_inventory_physical_count(physical_count_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveInventoryPhysicalCountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>physical_count_id</code> | <code>str</code> | ID of the<br>[InventoryPhysicalCount](entity:InventoryPhysicalCount) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveInventoryPhysicalCountResponse](square/models/retrieve_inventory_physical_count_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveInventoryPhysicalCountResponse](square/models/retrieve_inventory_physical_count_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_inventory_adjustment(body: UpdateInventoryAdjustmentRequest | UpdateInventoryAdjustmentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateInventoryAdjustmentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Applies an update to the provided adjustment.

On success: returns the newly updated adjustment.
On failure: returns a list of related errors.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.update_inventory_adjustment(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInventoryAdjustmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.update_inventory_adjustment(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInventoryAdjustmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpdateInventoryAdjustmentRequest](square/models/update_inventory_adjustment_request.py) \| [UpdateInventoryAdjustmentRequestDict](square/models/update_inventory_adjustment_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateInventoryAdjustmentResponse](square/models/update_inventory_adjustment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateInventoryAdjustmentResponse](square/models/update_inventory_adjustment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_inventory_adjustment_reason(body: UpdateInventoryAdjustmentReasonRequest | UpdateInventoryAdjustmentReasonRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateInventoryAdjustmentReasonResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a custom inventory adjustment reason.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.inventory.with_raw_response.update_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.inventory.with_raw_response.update_inventory_adjustment_reason(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInventoryAdjustmentReasonResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[UpdateInventoryAdjustmentReasonRequest](square/models/update_inventory_adjustment_reason_request.py) \| [UpdateInventoryAdjustmentReasonRequestDict](square/models/update_inventory_adjustment_reason_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateInventoryAdjustmentReasonResponse](square/models/update_inventory_adjustment_reason_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateInventoryAdjustmentReasonResponse](square/models/update_inventory_adjustment_reason_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Invoices

> Source: [Invoices](square/apis/invoices.py)

<details>
<summary><code>def cancel_invoice(invoice_id: str, body: CancelInvoiceRequest | CancelInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelInvoiceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels an invoice. The seller cannot collect payments for 
the canceled invoice.

You cannot cancel an invoice in the `DRAFT` state or in a terminal state: `PAID`, `REFUNDED`, `CANCELED`, or `FAILED`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.cancel_invoice(invoice_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.cancel_invoice(invoice_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the [invoice](entity:Invoice) to cancel. |
| <code>body</code> | <code>[CancelInvoiceRequest](square/models/cancel_invoice_request.py) \| [CancelInvoiceRequestDict](square/models/cancel_invoice_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelInvoiceResponse](square/models/cancel_invoice_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelInvoiceResponse](square/models/cancel_invoice_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_invoice(body: CreateInvoiceRequest | CreateInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateInvoiceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a draft [invoice](entity:Invoice) 
for an order created using the Orders API.

A draft invoice remains in your account and no action is taken. 
You must publish the invoice before Square can process it (send it to the customer's email address or charge the customer’s card on file).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.create_invoice(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.create_invoice(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateInvoiceRequest](square/models/create_invoice_request.py) \| [CreateInvoiceRequestDict](square/models/create_invoice_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateInvoiceResponse](square/models/create_invoice_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateInvoiceResponse](square/models/create_invoice_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_invoice_attachment(invoice_id: str, *, request: CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None = None, image_file: bytes | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateInvoiceAttachmentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Uploads a file and attaches it to an invoice. This endpoint accepts HTTP multipart/form-data file uploads
with a JSON `request` part and a `file` part. The `file` part must be a `readable stream` that contains a file
in a supported format: GIF, JPEG, PNG, TIFF, BMP, or PDF.

Invoices can have up to 10 attachments with a total file size of 25 MB. Attachments can be added only to invoices
in the `DRAFT`, `SCHEDULED`, `UNPAID`, or `PARTIALLY_PAID` state.

__NOTE:__ When testing in the Sandbox environment, the total file size is limited to 1 KB.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.create_invoice_attachment(invoice_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInvoiceAttachmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.create_invoice_attachment(invoice_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateInvoiceAttachmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the [invoice](entity:Invoice) to attach the file to. |
| <code>request</code> | <code>[CreateInvoiceAttachmentRequest](square/models/create_invoice_attachment_request.py) \| [CreateInvoiceAttachmentRequestDict](square/models/create_invoice_attachment_request.py) \| None</code> | Represents a [CreateInvoiceAttachment](api-endpoint:Invoices-CreateInvoiceAttachment) request.<br>**Default**: <code>None</code> |
| <code>image_file</code> | <code>bytes \| None</code> | Value sent with the request.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateInvoiceAttachmentResponse](square/models/create_invoice_attachment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateInvoiceAttachmentResponse](square/models/create_invoice_attachment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_invoice(invoice_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteInvoiceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes the specified invoice. When an invoice is deleted, the 
associated order status changes to CANCELED. You can only delete a draft 
invoice (you cannot delete a published invoice, including one that is scheduled for processing).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.delete_invoice(invoice_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.delete_invoice(invoice_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the invoice to delete. |
| <code>version</code> | <code>int \| None</code> | The version of the [invoice](entity:Invoice) to delete.<br>If you do not know the version, you can call [GetInvoice](api-endpoint:Invoices-GetInvoice) or <br>[ListInvoices](api-endpoint:Invoices-ListInvoices).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteInvoiceResponse](square/models/delete_invoice_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteInvoiceResponse](square/models/delete_invoice_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_invoice_attachment(invoice_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteInvoiceAttachmentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes an attachment from an invoice and permanently deletes the file. Attachments can be removed only
from invoices in the `DRAFT`, `SCHEDULED`, `UNPAID`, or `PARTIALLY_PAID` state.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.delete_invoice_attachment(invoice_id, attachment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteInvoiceAttachmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.delete_invoice_attachment(invoice_id, attachment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteInvoiceAttachmentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the [invoice](entity:Invoice) to delete the attachment from. |
| <code>attachment_id</code> | <code>str</code> | The ID of the [attachment](entity:InvoiceAttachment) to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteInvoiceAttachmentResponse](square/models/delete_invoice_attachment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteInvoiceAttachmentResponse](square/models/delete_invoice_attachment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_invoice(invoice_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetInvoiceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves an invoice by invoice ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.get_invoice(invoice_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.get_invoice(invoice_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the invoice to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetInvoiceResponse](square/models/get_invoice_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetInvoiceResponse](square/models/get_invoice_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_invoices(location_id: str, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListInvoicesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of invoices for a given location. The response 
is paginated. If truncated, the response includes a `cursor` that you    
use in a subsequent request to retrieve the next set of invoices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.list_invoices(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInvoicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.list_invoices(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListInvoicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location for which to list invoices. |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint. <br>Provide this cursor to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of invoices to return (200 is the maximum `limit`). <br>If not provided, the server uses a default limit of 100 invoices.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListInvoicesResponse](square/models/list_invoices_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListInvoicesResponse](square/models/list_invoices_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def publish_invoice(invoice_id: str, body: PublishInvoiceRequest | PublishInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PublishInvoiceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Publishes the specified draft invoice. 

After an invoice is published, Square 
follows up based on the invoice configuration. For example, Square 
sends the invoice to the customer's email address, charges the customer's card on file, or does 
nothing. Square also makes the invoice available on a Square-hosted invoice page. 

The invoice `status` also changes from `DRAFT` to a status 
based on the invoice configuration. For example, the status changes to `UNPAID` if 
Square emails the invoice or `PARTIALLY_PAID` if Square charges a card on file for a portion of the 
invoice amount.

In addition to the required `ORDERS_WRITE` and `INVOICES_WRITE` permissions, `CUSTOMERS_READ`
and `PAYMENTS_WRITE` are required when publishing invoices configured for card-on-file payments.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.publish_invoice(invoice_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PublishInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.publish_invoice(invoice_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PublishInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the invoice to publish. |
| <code>body</code> | <code>[PublishInvoiceRequest](square/models/publish_invoice_request.py) \| [PublishInvoiceRequestDict](square/models/publish_invoice_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[PublishInvoiceResponse](square/models/publish_invoice_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PublishInvoiceResponse](square/models/publish_invoice_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_invoices(body: SearchInvoicesRequest | SearchInvoicesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchInvoicesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for invoices from a location specified in 
the filter. You can optionally specify customers in the filter for whom to 
retrieve invoices. In the current implementation, you can only specify one location and 
optionally one customer.

The response is paginated. If truncated, the response includes a `cursor` 
that you use in a subsequent request to retrieve the next set of invoices.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.search_invoices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchInvoicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.search_invoices(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchInvoicesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchInvoicesRequest](square/models/search_invoices_request.py) \| [SearchInvoicesRequestDict](square/models/search_invoices_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchInvoicesResponse](square/models/search_invoices_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchInvoicesResponse](square/models/search_invoices_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_invoice(invoice_id: str, body: UpdateInvoiceRequest | UpdateInvoiceRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateInvoiceResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an invoice. This endpoint supports sparse updates, so you only need
to specify the fields you want to change along with the required `version` field.
Some restrictions apply to updating invoices. For example, you cannot change the
`order_id` or `location_id` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.invoices.with_raw_response.update_invoice(invoice_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.invoices.with_raw_response.update_invoice(invoice_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateInvoiceResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>invoice_id</code> | <code>str</code> | The ID of the invoice to update. |
| <code>body</code> | <code>[UpdateInvoiceRequest](square/models/update_invoice_request.py) \| [UpdateInvoiceRequestDict](square/models/update_invoice_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateInvoiceResponse](square/models/update_invoice_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateInvoiceResponse](square/models/update_invoice_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Labor

> Source: [Labor](square/apis/labor.py)

<details>
<summary><code>def bulk_publish_scheduled_shifts(body: BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkPublishScheduledShiftsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Publishes 1 - 100 scheduled shifts. This endpoint takes a map of individual publish
requests and returns a map of responses. When a scheduled shift is published, Square keeps
the `draft_shift_details` field as is and copies it to the `published_shift_details` field.

The minimum `start_at` and maximum `end_at` timestamps of all shifts in a
`BulkPublishScheduledShifts` request must fall within a two-week period.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.bulk_publish_scheduled_shifts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkPublishScheduledShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.bulk_publish_scheduled_shifts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkPublishScheduledShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkPublishScheduledShiftsRequest](square/models/bulk_publish_scheduled_shifts_request.py) \| [BulkPublishScheduledShiftsRequestDict](square/models/bulk_publish_scheduled_shifts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkPublishScheduledShiftsResponse](square/models/bulk_publish_scheduled_shifts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkPublishScheduledShiftsResponse](square/models/bulk_publish_scheduled_shifts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_break_type(body: CreateBreakTypeRequest | CreateBreakTypeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateBreakTypeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new `BreakType`.

A `BreakType` is a template for creating `Break` objects.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `break_name`
- `expected_duration`
- `is_paid`

You can only have three `BreakType` instances per location. If you attempt to add a fourth
`BreakType` for a location, an `INVALID_REQUEST_ERROR` "Exceeded limit of 3 breaks per location."
is returned.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.create_break_type(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.create_break_type(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateBreakTypeRequest](square/models/create_break_type_request.py) \| [CreateBreakTypeRequestDict](square/models/create_break_type_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateBreakTypeResponse](square/models/create_break_type_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateBreakTypeResponse](square/models/create_break_type_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_scheduled_shift(body: CreateScheduledShiftRequest | CreateScheduledShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateScheduledShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a scheduled shift by providing draft shift details such as job ID,
team member assignment, and start and end times.

The following `draft_shift_details` fields are required:
- `location_id`
- `job_id`
- `start_at`
- `end_at`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.create_scheduled_shift(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.create_scheduled_shift(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateScheduledShiftRequest](square/models/create_scheduled_shift_request.py) \| [CreateScheduledShiftRequestDict](square/models/create_scheduled_shift_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateScheduledShiftResponse](square/models/create_scheduled_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateScheduledShiftResponse](square/models/create_scheduled_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_shift(body: CreateShiftRequest | CreateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new `Shift`.

A `Shift` represents a complete workday for a single team member.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `team_member_id`
- `start_at`

An attempt to create a new `Shift` can result in a `BAD_REQUEST` error when:
- The `status` of the new `Shift` is `OPEN` and the team member has another
shift with an `OPEN` status.
- The `start_at` date is in the future.
- The `start_at` or `end_at` date overlaps another shift for the same team member.
- The `Break` instances are set in the request and a break `start_at`
is before the `Shift.start_at`, a break `end_at` is after
the `Shift.end_at`, or both.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.create_shift(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.create_shift(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateShiftRequest](square/models/create_shift_request.py) \| [CreateShiftRequestDict](square/models/create_shift_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateShiftResponse](square/models/create_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateShiftResponse](square/models/create_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_timecard(body: CreateTimecardRequest | CreateTimecardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTimecardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new `Timecard`.

A `Timecard` represents a complete workday for a single team member.
You must provide the following values in your request to this
endpoint:

- `location_id`
- `team_member_id`
- `start_at`

An attempt to create a new `Timecard` can result in a `BAD_REQUEST` error when:
- The `status` of the new `Timecard` is `OPEN` and the team member has another
timecard with an `OPEN` status.
- The `start_at` date is in the future.
- The `start_at` or `end_at` date overlaps another timecard for the same team member.
- The `Break` instances are set in the request and a break `start_at`
is before the `Timecard.start_at`, a break `end_at` is after
the `Timecard.end_at`, or both.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.create_timecard(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.create_timecard(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTimecardRequest](square/models/create_timecard_request.py) \| [CreateTimecardRequestDict](square/models/create_timecard_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateTimecardResponse](square/models/create_timecard_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTimecardResponse](square/models/create_timecard_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_break_type(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteBreakTypeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an existing `BreakType`.

A `BreakType` can be deleted even if it is referenced from a `Shift`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.delete_break_type(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.delete_break_type(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `BreakType` being deleted. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteBreakTypeResponse](square/models/delete_break_type_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteBreakTypeResponse](square/models/delete_break_type_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_shift(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a `Shift`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.delete_shift(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.delete_shift(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `Shift` being deleted. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteShiftResponse](square/models/delete_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteShiftResponse](square/models/delete_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_timecard(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteTimecardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a `Timecard`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.delete_timecard(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.delete_timecard(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `Timecard` being deleted. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteTimecardResponse](square/models/delete_timecard_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteTimecardResponse](square/models/delete_timecard_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_break_type(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetBreakTypeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single `BreakType` specified by `id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.get_break_type(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.get_break_type(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `BreakType` being retrieved. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetBreakTypeResponse](square/models/get_break_type_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetBreakTypeResponse](square/models/get_break_type_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_employee_wage(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetEmployeeWageResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single `EmployeeWage` specified by `id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.get_employee_wage(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetEmployeeWageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.get_employee_wage(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetEmployeeWageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `EmployeeWage` being retrieved. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetEmployeeWageResponse](square/models/get_employee_wage_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetEmployeeWageResponse](square/models/get_employee_wage_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_shift(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single `Shift` specified by `id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.get_shift(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.get_shift(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `Shift` being retrieved. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetShiftResponse](square/models/get_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetShiftResponse](square/models/get_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_team_member_wage(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetTeamMemberWageResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single `TeamMemberWage` specified by `id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.get_team_member_wage(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTeamMemberWageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.get_team_member_wage(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTeamMemberWageResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `TeamMemberWage` being retrieved. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetTeamMemberWageResponse](square/models/get_team_member_wage_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetTeamMemberWageResponse](square/models/get_team_member_wage_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_break_types(*, location_id: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListBreakTypesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of `BreakType` instances for a business.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.list_break_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBreakTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.list_break_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListBreakTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str \| None</code> | Filter the returned `BreakType` results to only those that are associated with the<br>specified location.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of `BreakType` results to return per page. The number can range between 1<br>and 200. The default is 200.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pointer to the next page of `BreakType` results to fetch.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListBreakTypesResponse](square/models/list_break_types_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListBreakTypesResponse](square/models/list_break_types_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_employee_wages(*, employee_id: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListEmployeeWagesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of `EmployeeWage` instances for a business.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.list_employee_wages()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEmployeeWagesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.list_employee_wages()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListEmployeeWagesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>employee_id</code> | <code>str \| None</code> | Filter the returned wages to only those that are associated with the specified employee.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of `EmployeeWage` results to return per page. The number can range between<br>1 and 200. The default is 200.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pointer to the next page of `EmployeeWage` results to fetch.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListEmployeeWagesResponse](square/models/list_employee_wages_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListEmployeeWagesResponse](square/models/list_employee_wages_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_team_member_wages(*, team_member_id: str | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListTeamMemberWagesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of `TeamMemberWage` instances for a business.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.list_team_member_wages()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTeamMemberWagesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.list_team_member_wages()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTeamMemberWagesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_member_id</code> | <code>str \| None</code> | Filter the returned wages to only those that are associated with the<br>specified team member.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of `TeamMemberWage` results to return per page. The number can range between<br>1 and 200. The default is 200.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pointer to the next page of `EmployeeWage` results to fetch.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListTeamMemberWagesResponse](square/models/list_team_member_wages_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListTeamMemberWagesResponse](square/models/list_team_member_wages_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_workweek_configs(*, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListWorkweekConfigsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of `WorkweekConfig` instances for a business.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.list_workweek_configs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListWorkweekConfigsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.list_workweek_configs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListWorkweekConfigsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>limit</code> | <code>int \| None</code> | The maximum number of `WorkweekConfigs` results to return per page.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pointer to the next page of `WorkweekConfig` results to fetch.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListWorkweekConfigsResponse](square/models/list_workweek_configs_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListWorkweekConfigsResponse](square/models/list_workweek_configs_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def publish_scheduled_shift(id: str, body: PublishScheduledShiftRequest | PublishScheduledShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PublishScheduledShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Publishes a scheduled shift. When a scheduled shift is published, Square keeps the
`draft_shift_details` field as is and copies it to the `published_shift_details` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.publish_scheduled_shift(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PublishScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.publish_scheduled_shift(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PublishScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the scheduled shift to publish. |
| <code>body</code> | <code>[PublishScheduledShiftRequest](square/models/publish_scheduled_shift_request.py) \| [PublishScheduledShiftRequestDict](square/models/publish_scheduled_shift_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[PublishScheduledShiftResponse](square/models/publish_scheduled_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PublishScheduledShiftResponse](square/models/publish_scheduled_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_scheduled_shift(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveScheduledShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a scheduled shift by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.retrieve_scheduled_shift(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.retrieve_scheduled_shift(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the scheduled shift to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveScheduledShiftResponse](square/models/retrieve_scheduled_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveScheduledShiftResponse](square/models/retrieve_scheduled_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_timecard(id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveTimecardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a single `Timecard` specified by `id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.retrieve_timecard(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.retrieve_timecard(id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `Timecard` being retrieved. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveTimecardResponse](square/models/retrieve_timecard_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveTimecardResponse](square/models/retrieve_timecard_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_scheduled_shifts(body: SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchScheduledShiftsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of scheduled shifts, with optional filter and sort settings.
By default, results are sorted by `start_at` in ascending order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.search_scheduled_shifts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchScheduledShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.search_scheduled_shifts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchScheduledShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchScheduledShiftsRequest](square/models/search_scheduled_shifts_request.py) \| [SearchScheduledShiftsRequestDict](square/models/search_scheduled_shifts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchScheduledShiftsResponse](square/models/search_scheduled_shifts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchScheduledShiftsResponse](square/models/search_scheduled_shifts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_shifts(body: SearchShiftsRequest | SearchShiftsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchShiftsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of `Shift` records for a business.
The list to be returned can be filtered by:
- Location IDs
- Team member IDs
- Shift status (`OPEN` or `CLOSED`)
- Shift start
- Shift end
- Workday details

The list can be sorted by:
- `START_AT`
- `END_AT`
- `CREATED_AT`
- `UPDATED_AT`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.search_shifts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.search_shifts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchShiftsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchShiftsRequest](square/models/search_shifts_request.py) \| [SearchShiftsRequestDict](square/models/search_shifts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchShiftsResponse](square/models/search_shifts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchShiftsResponse](square/models/search_shifts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_timecards(body: SearchTimecardsRequest | SearchTimecardsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchTimecardsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of `Timecard` records for a business.
The list to be returned can be filtered by:
- Location IDs
- Team member IDs
- Timecard status (`OPEN` or `CLOSED`)
- Timecard start
- Timecard end
- Workday details

The list can be sorted by:
- `START_AT`
- `END_AT`
- `CREATED_AT`
- `UPDATED_AT`

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.search_timecards(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTimecardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.search_timecards(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTimecardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchTimecardsRequest](square/models/search_timecards_request.py) \| [SearchTimecardsRequestDict](square/models/search_timecards_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchTimecardsResponse](square/models/search_timecards_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchTimecardsResponse](square/models/search_timecards_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_break_type(id: str, body: UpdateBreakTypeRequest | UpdateBreakTypeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateBreakTypeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing `BreakType`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.update_break_type(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.update_break_type(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateBreakTypeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `BreakType` being updated. |
| <code>body</code> | <code>[UpdateBreakTypeRequest](square/models/update_break_type_request.py) \| [UpdateBreakTypeRequestDict](square/models/update_break_type_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateBreakTypeResponse](square/models/update_break_type_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateBreakTypeResponse](square/models/update_break_type_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_scheduled_shift(id: str, body: UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateScheduledShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the draft shift details for a scheduled shift. This endpoint supports
sparse updates, so only new, changed, or removed fields are required in the request.
You must publish the shift to make updates public.

You can make the following updates to `draft_shift_details`:
- Change the `location_id`, `job_id`, `start_at`, and `end_at` fields.
- Add, change, or clear the `team_member_id` and `notes` fields. To clear these fields,
set the value to null.
- Change the `is_deleted` field. To delete a scheduled shift, set `is_deleted` to true
and then publish the shift.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.update_scheduled_shift(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.update_scheduled_shift(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateScheduledShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the scheduled shift to update. |
| <code>body</code> | <code>[UpdateScheduledShiftRequest](square/models/update_scheduled_shift_request.py) \| [UpdateScheduledShiftRequestDict](square/models/update_scheduled_shift_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateScheduledShiftResponse](square/models/update_scheduled_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateScheduledShiftResponse](square/models/update_scheduled_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_shift(id: str, body: UpdateShiftRequest | UpdateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateShiftResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing `Shift`.

When adding a `Break` to a `Shift`, any earlier `Break` instances in the `Shift` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Shift`, all `Break` instances in the `Shift` must be complete with `end_at`
set on each `Break`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.update_shift(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.update_shift(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateShiftResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the object being updated. |
| <code>body</code> | <code>[UpdateShiftRequest](square/models/update_shift_request.py) \| [UpdateShiftRequestDict](square/models/update_shift_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateShiftResponse](square/models/update_shift_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateShiftResponse](square/models/update_shift_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_timecard(id: str, body: UpdateTimecardRequest | UpdateTimecardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateTimecardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing `Timecard`.

When adding a `Break` to a `Timecard`, any earlier `Break` instances in the `Timecard` have
the `end_at` property set to a valid RFC-3339 datetime string.

When closing a `Timecard`, all `Break` instances in the `Timecard` must be complete with `end_at`
set on each `Break`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.update_timecard(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.update_timecard(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateTimecardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The ID of the object being updated. |
| <code>body</code> | <code>[UpdateTimecardRequest](square/models/update_timecard_request.py) \| [UpdateTimecardRequestDict](square/models/update_timecard_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateTimecardResponse](square/models/update_timecard_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateTimecardResponse](square/models/update_timecard_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_workweek_config(id: str, body: UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateWorkweekConfigResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a `WorkweekConfig`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.labor.with_raw_response.update_workweek_config(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWorkweekConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.labor.with_raw_response.update_workweek_config(id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWorkweekConfigResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>id</code> | <code>str</code> | The UUID for the `WorkweekConfig` object being updated. |
| <code>body</code> | <code>[UpdateWorkweekConfigRequest](square/models/update_workweek_config_request.py) \| [UpdateWorkweekConfigRequestDict](square/models/update_workweek_config_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateWorkweekConfigResponse](square/models/update_workweek_config_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateWorkweekConfigResponse](square/models/update_workweek_config_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## LocationCustomAttributes

> Source: [LocationCustomAttributes](square/apis/location_custom_attributes.py)

<details>
<summary><code>def bulk_delete_location_custom_attributes(body: BulkDeleteLocationCustomAttributesRequest | BulkDeleteLocationCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkDeleteLocationCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes [custom attributes](entity:CustomAttribute) for locations as a bulk operation.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.bulk_delete_location_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteLocationCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.bulk_delete_location_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteLocationCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkDeleteLocationCustomAttributesRequest](square/models/bulk_delete_location_custom_attributes_request.py) \| [BulkDeleteLocationCustomAttributesRequestDict](square/models/bulk_delete_location_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkDeleteLocationCustomAttributesResponse](square/models/bulk_delete_location_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkDeleteLocationCustomAttributesResponse](square/models/bulk_delete_location_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_upsert_location_custom_attributes(body: BulkUpsertLocationCustomAttributesRequest | BulkUpsertLocationCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpsertLocationCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates [custom attributes](entity:CustomAttribute) for locations as a bulk operation.
Use this endpoint to set the value of one or more custom attributes for one or more locations.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateLocationCustomAttributeDefinition](api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition) endpoint.
This `BulkUpsertLocationCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a location ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.bulk_upsert_location_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertLocationCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.bulk_upsert_location_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertLocationCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpsertLocationCustomAttributesRequest](square/models/bulk_upsert_location_custom_attributes_request.py) \| [BulkUpsertLocationCustomAttributesRequestDict](square/models/bulk_upsert_location_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpsertLocationCustomAttributesResponse](square/models/bulk_upsert_location_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpsertLocationCustomAttributesResponse](square/models/bulk_upsert_location_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_location_custom_attribute_definition(body: CreateLocationCustomAttributeDefinitionRequest | CreateLocationCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateLocationCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a location-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with locations.
A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertLocationCustomAttribute](api-endpoint:LocationCustomAttributes-UpsertLocationCustomAttribute) or
[BulkUpsertLocationCustomAttributes](api-endpoint:LocationCustomAttributes-BulkUpsertLocationCustomAttributes)
to set the custom attribute for locations.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.create_location_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.create_location_custom_attribute_definition(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateLocationCustomAttributeDefinitionRequest](square/models/create_location_custom_attribute_definition_request.py) \| [CreateLocationCustomAttributeDefinitionRequestDict](square/models/create_location_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateLocationCustomAttributeDefinitionResponse](square/models/create_location_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateLocationCustomAttributeDefinitionResponse](square/models/create_location_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_location_custom_attribute(location_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteLocationCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a location.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.delete_location_custom_attribute(location_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteLocationCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.delete_location_custom_attribute(
    location_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteLocationCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the target [location](entity:Location). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteLocationCustomAttributeResponse](square/models/delete_location_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteLocationCustomAttributeResponse](square/models/delete_location_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_location_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteLocationCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a location-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
Deleting a custom attribute definition also deletes the corresponding custom attribute from
all locations.
Only the definition owner can delete a custom attribute definition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.delete_location_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.delete_location_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteLocationCustomAttributeDefinitionResponse](square/models/delete_location_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteLocationCustomAttributeDefinitionResponse](square/models/delete_location_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_location_custom_attribute_definitions(*, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListLocationCustomAttributeDefinitionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the location-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.
When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.list_location_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.list_location_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>visibility_filter</code> | <code>[VisibilityFilterOrStr](square/models/enums/visibility_filter.py) \| None</code> | Filters the `CustomAttributeDefinition` results by their `visibility` values.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListLocationCustomAttributeDefinitionsResponse](square/models/list_location_custom_attribute_definitions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListLocationCustomAttributeDefinitionsResponse](square/models/list_location_custom_attribute_definitions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_location_custom_attributes(location_id: str, *, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListLocationCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with a location.
You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.
When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.list_location_custom_attributes(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.list_location_custom_attributes(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the target [location](entity:Location). |
| <code>visibility_filter</code> | <code>[VisibilityFilterOrStr](square/models/enums/visibility_filter.py) \| None</code> | Filters the `CustomAttributeDefinition` results by their `visibility` values.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>with_definitions</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListLocationCustomAttributesResponse](square/models/list_location_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListLocationCustomAttributesResponse](square/models/list_location_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location_custom_attribute(location_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLocationCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with a location.
You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.
To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.retrieve_location_custom_attribute(location_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.retrieve_location_custom_attribute(
    location_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the target [location](entity:Location). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>with_definition</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLocationCustomAttributeResponse](square/models/retrieve_location_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLocationCustomAttributeResponse](square/models/retrieve_location_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLocationCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a location-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.retrieve_location_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.retrieve_location_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLocationCustomAttributeDefinitionResponse](square/models/retrieve_location_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLocationCustomAttributeDefinitionResponse](square/models/retrieve_location_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_location_custom_attribute_definition(key: str, body: UpdateLocationCustomAttributeDefinitionRequest | UpdateLocationCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateLocationCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a location-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.
Only the definition owner can update a custom attribute definition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.update_location_custom_attribute_definition(key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.update_location_custom_attribute_definition(
    key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateLocationCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to update. |
| <code>body</code> | <code>[UpdateLocationCustomAttributeDefinitionRequest](square/models/update_location_custom_attribute_definition_request.py) \| [UpdateLocationCustomAttributeDefinitionRequestDict](square/models/update_location_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateLocationCustomAttributeDefinitionResponse](square/models/update_location_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateLocationCustomAttributeDefinitionResponse](square/models/update_location_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_location_custom_attribute(location_id: str, key: str, body: UpsertLocationCustomAttributeRequest | UpsertLocationCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertLocationCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for a location.
Use this endpoint to set the value of a custom attribute for a specified location.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateLocationCustomAttributeDefinition](api-endpoint:LocationCustomAttributes-CreateLocationCustomAttributeDefinition) endpoint.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.location_custom_attributes.with_raw_response.upsert_location_custom_attribute(location_id, key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertLocationCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.location_custom_attributes.with_raw_response.upsert_location_custom_attribute(
    location_id, key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertLocationCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the target [location](entity:Location). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| <code>body</code> | <code>[UpsertLocationCustomAttributeRequest](square/models/upsert_location_custom_attribute_request.py) \| [UpsertLocationCustomAttributeRequestDict](square/models/upsert_location_custom_attribute_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertLocationCustomAttributeResponse](square/models/upsert_location_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertLocationCustomAttributeResponse](square/models/upsert_location_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Locations

> Source: [Locations](square/apis/locations.py)

<details>
<summary><code>def create_location(body: CreateLocationRequest | CreateLocationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateLocationResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a [location](https://developer.squareup.com/docs/locations-api).
Creating new locations allows for separate configuration of receipt layouts, item prices,
and sales reports. Developers can use locations to separate sales activity through applications
that integrate with Square from sales activity elsewhere in a seller's account.
Locations created programmatically with the Locations API last forever and
are visible to the seller for their own management. Therefore, ensure that
each location has a sensible and unique name.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.locations.with_raw_response.create_location(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLocationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.locations.with_raw_response.create_location(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLocationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateLocationRequest](square/models/create_location_request.py) \| [CreateLocationRequestDict](square/models/create_location_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateLocationResponse](square/models/create_location_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateLocationResponse](square/models/create_location_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_locations(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListLocationsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides details about all of the seller's [locations](https://developer.squareup.com/docs/locations-api),
including those with an inactive status. Locations are listed alphabetically by `name`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.locations.with_raw_response.list_locations()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.locations.with_raw_response.list_locations()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLocationsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListLocationsResponse](square/models/list_locations_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListLocationsResponse](square/models/list_locations_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_location(location_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLocationResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves details of a single location. Specify "main"
as the location ID to retrieve details of the [main location](https://developer.squareup.com/docs/locations-api#about-the-main-location).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.locations.with_raw_response.retrieve_location(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.locations.with_raw_response.retrieve_location(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLocationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location to retrieve. Specify the string<br>"main" to return the main location. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLocationResponse](square/models/retrieve_location_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLocationResponse](square/models/retrieve_location_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_location(location_id: str, body: UpdateLocationRequest | UpdateLocationRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateLocationResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a [location](https://developer.squareup.com/docs/locations-api).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.locations.with_raw_response.update_location(location_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateLocationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.locations.with_raw_response.update_location(location_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateLocationResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location to update. |
| <code>body</code> | <code>[UpdateLocationRequest](square/models/update_location_request.py) \| [UpdateLocationRequestDict](square/models/update_location_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateLocationResponse](square/models/update_location_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateLocationResponse](square/models/update_location_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Loyalty

> Source: [Loyalty](square/apis/loyalty.py)

<details>
<summary><code>def accumulate_loyalty_points(account_id: str, body: AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AccumulateLoyaltyPointsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds points earned from a purchase to a [loyalty account](entity:LoyaltyAccount).

- If you are using the Orders API to manage orders, provide the `order_id`. Square reads the order
to compute the points earned from both the base loyalty program and an associated
[loyalty promotion](entity:LoyaltyPromotion). For purchases that qualify for multiple accrual
rules, Square computes points based on the accrual rule that grants the most points.
For purchases that qualify for multiple promotions, Square computes points based on the most
recently created promotion. A purchase must first qualify for program points to be eligible for promotion points.

- If you are not using the Orders API to manage orders, provide `points` with the number of points to add.
You must first perform a client-side computation of the points earned from the loyalty program and
loyalty promotion. For spend-based and visit-based programs, you can call [CalculateLoyaltyPoints](api-endpoint:Loyalty-CalculateLoyaltyPoints)
to compute the points earned from the base loyalty program. For information about computing points earned from a loyalty promotion, see
[Calculating promotion points](https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.accumulate_loyalty_points(account_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccumulateLoyaltyPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.accumulate_loyalty_points(account_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AccumulateLoyaltyPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str</code> | The ID of the target [loyalty account](entity:LoyaltyAccount). |
| <code>body</code> | <code>[AccumulateLoyaltyPointsRequest](square/models/accumulate_loyalty_points_request.py) \| [AccumulateLoyaltyPointsRequestDict](square/models/accumulate_loyalty_points_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[AccumulateLoyaltyPointsResponse](square/models/accumulate_loyalty_points_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AccumulateLoyaltyPointsResponse](square/models/accumulate_loyalty_points_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def adjust_loyalty_points(account_id: str, body: AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[AdjustLoyaltyPointsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds points to or subtracts points from a buyer's account.

Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
[AccumulateLoyaltyPoints](api-endpoint:Loyalty-AccumulateLoyaltyPoints)
to add points when a buyer pays for the purchase.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.adjust_loyalty_points(account_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AdjustLoyaltyPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.adjust_loyalty_points(account_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type AdjustLoyaltyPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str</code> | The ID of the target [loyalty account](entity:LoyaltyAccount). |
| <code>body</code> | <code>[AdjustLoyaltyPointsRequest](square/models/adjust_loyalty_points_request.py) \| [AdjustLoyaltyPointsRequestDict](square/models/adjust_loyalty_points_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[AdjustLoyaltyPointsResponse](square/models/adjust_loyalty_points_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[AdjustLoyaltyPointsResponse](square/models/adjust_loyalty_points_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calculate_loyalty_points(program_id: str, body: CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CalculateLoyaltyPointsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Calculates the number of points a buyer can earn from a purchase. Applications might call this endpoint
to display the points to the buyer.

- If you are using the Orders API to manage orders, provide the `order_id` and (optional) `loyalty_account_id`.
Square reads the order to compute the points earned from the base loyalty program and an associated
[loyalty promotion](entity:LoyaltyPromotion).

- If you are not using the Orders API to manage orders, provide `transaction_amount_money` with the
purchase amount. Square uses this amount to calculate the points earned from the base loyalty program,
but not points earned from a loyalty promotion. For spend-based and visit-based programs, the `tax_mode`
setting of the accrual rule indicates how taxes should be treated for loyalty points accrual.
If the purchase qualifies for program points, call
[ListLoyaltyPromotions](api-endpoint:Loyalty-ListLoyaltyPromotions) and perform a client-side computation
to calculate whether the purchase also qualifies for promotion points. For more information, see
[Calculating promotion points](https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.calculate_loyalty_points(program_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CalculateLoyaltyPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.calculate_loyalty_points(program_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CalculateLoyaltyPointsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>program_id</code> | <code>str</code> | The ID of the [loyalty program](entity:LoyaltyProgram), which defines the rules for accruing points. |
| <code>body</code> | <code>[CalculateLoyaltyPointsRequest](square/models/calculate_loyalty_points_request.py) \| [CalculateLoyaltyPointsRequestDict](square/models/calculate_loyalty_points_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CalculateLoyaltyPointsResponse](square/models/calculate_loyalty_points_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CalculateLoyaltyPointsResponse](square/models/calculate_loyalty_points_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_loyalty_promotion(promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelLoyaltyPromotionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a loyalty promotion. Use this endpoint to cancel an `ACTIVE` promotion earlier than the
end date, cancel an `ACTIVE` promotion when an end date is not specified, or cancel a `SCHEDULED` promotion.
Because updating a promotion is not supported, you can also use this endpoint to cancel a promotion before
you create a new one.

This endpoint sets the loyalty promotion to the `CANCELED` state

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.cancel_loyalty_promotion(promotion_id, program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelLoyaltyPromotionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.cancel_loyalty_promotion(promotion_id, program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelLoyaltyPromotionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>promotion_id</code> | <code>str</code> | The ID of the [loyalty promotion](entity:LoyaltyPromotion) to cancel. You can cancel a<br>promotion that has an `ACTIVE` or `SCHEDULED` status. |
| <code>program_id</code> | <code>str</code> | The ID of the base [loyalty program](entity:LoyaltyProgram). |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelLoyaltyPromotionResponse](square/models/cancel_loyalty_promotion_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelLoyaltyPromotionResponse](square/models/cancel_loyalty_promotion_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_loyalty_account(body: CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateLoyaltyAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a loyalty account. To create a loyalty account, you must provide the `program_id` and a `mapping` with the `phone_number` of the buyer.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.create_loyalty_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLoyaltyAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.create_loyalty_account(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLoyaltyAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateLoyaltyAccountRequest](square/models/create_loyalty_account_request.py) \| [CreateLoyaltyAccountRequestDict](square/models/create_loyalty_account_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateLoyaltyAccountResponse](square/models/create_loyalty_account_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateLoyaltyAccountResponse](square/models/create_loyalty_account_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_loyalty_promotion(program_id: str, body: CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateLoyaltyPromotionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a loyalty promotion for a [loyalty program](entity:LoyaltyProgram). A loyalty promotion
enables buyers to earn points in addition to those earned from the base loyalty program.

This endpoint sets the loyalty promotion to the `ACTIVE` or `SCHEDULED` status, depending on the
`available_time` setting. A loyalty program can have a maximum of 10 loyalty promotions with an
`ACTIVE` or `SCHEDULED` status.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.create_loyalty_promotion(program_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLoyaltyPromotionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.create_loyalty_promotion(program_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLoyaltyPromotionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>program_id</code> | <code>str</code> | The ID of the [loyalty program](entity:LoyaltyProgram) to associate with the promotion.<br>To get the program ID, call [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram)<br>using the `main` keyword. |
| <code>body</code> | <code>[CreateLoyaltyPromotionRequest](square/models/create_loyalty_promotion_request.py) \| [CreateLoyaltyPromotionRequestDict](square/models/create_loyalty_promotion_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateLoyaltyPromotionResponse](square/models/create_loyalty_promotion_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateLoyaltyPromotionResponse](square/models/create_loyalty_promotion_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_loyalty_reward(body: CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateLoyaltyRewardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a loyalty reward. In the process, the endpoint does following:

- Uses the `reward_tier_id` in the request to determine the number of points
to lock for this reward.
- If the request includes `order_id`, it adds the reward and related discount to the order.

After a reward is created, the points are locked and
not available for the buyer to redeem another reward.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.create_loyalty_reward(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.create_loyalty_reward(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateLoyaltyRewardRequest](square/models/create_loyalty_reward_request.py) \| [CreateLoyaltyRewardRequestDict](square/models/create_loyalty_reward_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateLoyaltyRewardResponse](square/models/create_loyalty_reward_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateLoyaltyRewardResponse](square/models/create_loyalty_reward_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_loyalty_reward(reward_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteLoyaltyRewardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a loyalty reward by doing the following:

- Returns the loyalty points back to the loyalty account.
- If an order ID was specified when the reward was created
(see [CreateLoyaltyReward](api-endpoint:Loyalty-CreateLoyaltyReward)),
it updates the order by removing the reward and related
discounts.

You cannot delete a reward that has reached the terminal state (REDEEMED).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.delete_loyalty_reward(reward_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.delete_loyalty_reward(reward_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reward_id</code> | <code>str</code> | The ID of the [loyalty reward](entity:LoyaltyReward) to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteLoyaltyRewardResponse](square/models/delete_loyalty_reward_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteLoyaltyRewardResponse](square/models/delete_loyalty_reward_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_loyalty_programs(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListLoyaltyProgramsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a list of loyalty programs in the seller's account.
Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

Replaced with [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram) when used with the keyword `main`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.list_loyalty_programs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLoyaltyProgramsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.list_loyalty_programs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLoyaltyProgramsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListLoyaltyProgramsResponse](square/models/list_loyalty_programs_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListLoyaltyProgramsResponse](square/models/list_loyalty_programs_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_loyalty_promotions(program_id: str, *, status: LoyaltyPromotionStatusOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListLoyaltyPromotionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the loyalty promotions associated with a [loyalty program](entity:LoyaltyProgram).
Results are sorted by the `created_at` date in descending order (newest to oldest).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.list_loyalty_promotions(program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLoyaltyPromotionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.list_loyalty_promotions(program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListLoyaltyPromotionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>program_id</code> | <code>str</code> | The ID of the base [loyalty program](entity:LoyaltyProgram). To get the program ID,<br>call [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram) using the `main` keyword. |
| <code>status</code> | <code>[LoyaltyPromotionStatusOrStr](square/models/enums/loyalty_promotion_status.py) \| None</code> | The status to filter the results by. If a status is provided, only loyalty promotions<br>with the specified status are returned. Otherwise, all loyalty promotions associated with<br>the loyalty program are returned.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response.<br>The minimum value is 1 and the maximum value is 30. The default value is 30.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListLoyaltyPromotionsResponse](square/models/list_loyalty_promotions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListLoyaltyPromotionsResponse](square/models/list_loyalty_promotions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def redeem_loyalty_reward(reward_id: str, body: RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RedeemLoyaltyRewardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Redeems a loyalty reward.

The endpoint sets the reward to the `REDEEMED` terminal state.

If you are using your own order processing system (not using the
Orders API), you call this endpoint after the buyer paid for the
purchase.

After the reward reaches the terminal state, it cannot be deleted.
In other words, points used for the reward cannot be returned
to the account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.redeem_loyalty_reward(reward_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RedeemLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.redeem_loyalty_reward(reward_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RedeemLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reward_id</code> | <code>str</code> | The ID of the [loyalty reward](entity:LoyaltyReward) to redeem. |
| <code>body</code> | <code>[RedeemLoyaltyRewardRequest](square/models/redeem_loyalty_reward_request.py) \| [RedeemLoyaltyRewardRequestDict](square/models/redeem_loyalty_reward_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RedeemLoyaltyRewardResponse](square/models/redeem_loyalty_reward_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RedeemLoyaltyRewardResponse](square/models/redeem_loyalty_reward_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_loyalty_account(account_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLoyaltyAccountResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a loyalty account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.retrieve_loyalty_account(account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.retrieve_loyalty_account(account_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyAccountResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>account_id</code> | <code>str</code> | The ID of the [loyalty account](entity:LoyaltyAccount) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLoyaltyAccountResponse](square/models/retrieve_loyalty_account_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLoyaltyAccountResponse](square/models/retrieve_loyalty_account_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_loyalty_program(program_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLoyaltyProgramResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword `main`.

Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and managed from the Seller Dashboard. For more information, see [Loyalty Program Overview](https://developer.squareup.com/docs/loyalty/overview).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.retrieve_loyalty_program(program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyProgramResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.retrieve_loyalty_program(program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyProgramResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>program_id</code> | <code>str</code> | The ID of the loyalty program or the keyword `main`. Either value can be used to retrieve the single loyalty program that belongs to the seller. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLoyaltyProgramResponse](square/models/retrieve_loyalty_program_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLoyaltyProgramResponse](square/models/retrieve_loyalty_program_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_loyalty_promotion(promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLoyaltyPromotionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a loyalty promotion.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.retrieve_loyalty_promotion(promotion_id, program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyPromotionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.retrieve_loyalty_promotion(promotion_id, program_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyPromotionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>promotion_id</code> | <code>str</code> | The ID of the [loyalty promotion](entity:LoyaltyPromotion) to retrieve. |
| <code>program_id</code> | <code>str</code> | The ID of the base [loyalty program](entity:LoyaltyProgram). To get the program ID,<br>call [RetrieveLoyaltyProgram](api-endpoint:Loyalty-RetrieveLoyaltyProgram) using the `main` keyword. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLoyaltyPromotionResponse](square/models/retrieve_loyalty_promotion_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLoyaltyPromotionResponse](square/models/retrieve_loyalty_promotion_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_loyalty_reward(reward_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveLoyaltyRewardResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a loyalty reward.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.retrieve_loyalty_reward(reward_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.retrieve_loyalty_reward(reward_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveLoyaltyRewardResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>reward_id</code> | <code>str</code> | The ID of the [loyalty reward](entity:LoyaltyReward) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveLoyaltyRewardResponse](square/models/retrieve_loyalty_reward_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveLoyaltyRewardResponse](square/models/retrieve_loyalty_reward_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_loyalty_accounts(body: SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchLoyaltyAccountsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for loyalty accounts in a loyalty program.

You can search for a loyalty account using the phone number or customer ID associated with the account. To return all loyalty accounts, specify an empty `query` object or omit it entirely.

Search results are sorted by `created_at` in ascending order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.search_loyalty_accounts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchLoyaltyAccountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.search_loyalty_accounts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchLoyaltyAccountsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchLoyaltyAccountsRequest](square/models/search_loyalty_accounts_request.py) \| [SearchLoyaltyAccountsRequestDict](square/models/search_loyalty_accounts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchLoyaltyAccountsResponse](square/models/search_loyalty_accounts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchLoyaltyAccountsResponse](square/models/search_loyalty_accounts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_loyalty_events(body: SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchLoyaltyEventsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for loyalty events.

A Square loyalty program maintains a ledger of events that occur during the lifetime of a
buyer's loyalty account. Each change in the point balance
(for example, points earned, points redeemed, and points expired) is
recorded in the ledger. Using this endpoint, you can search the ledger for events.

Search results are sorted by `created_at` in descending order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.search_loyalty_events(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchLoyaltyEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.search_loyalty_events(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchLoyaltyEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchLoyaltyEventsRequest](square/models/search_loyalty_events_request.py) \| [SearchLoyaltyEventsRequestDict](square/models/search_loyalty_events_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchLoyaltyEventsResponse](square/models/search_loyalty_events_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchLoyaltyEventsResponse](square/models/search_loyalty_events_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_loyalty_rewards(body: SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchLoyaltyRewardsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for all loyalty accounts.
If you include a `query` object, `loyalty_account_id` is required and `status` is  optional.

If you know a reward ID, use the
[RetrieveLoyaltyReward](api-endpoint:Loyalty-RetrieveLoyaltyReward) endpoint.

Search results are sorted by `updated_at` in descending order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.loyalty.with_raw_response.search_loyalty_rewards(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchLoyaltyRewardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.loyalty.with_raw_response.search_loyalty_rewards(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchLoyaltyRewardsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchLoyaltyRewardsRequest](square/models/search_loyalty_rewards_request.py) \| [SearchLoyaltyRewardsRequestDict](square/models/search_loyalty_rewards_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchLoyaltyRewardsResponse](square/models/search_loyalty_rewards_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchLoyaltyRewardsResponse](square/models/search_loyalty_rewards_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## MerchantCustomAttributes

> Source: [MerchantCustomAttributes](square/apis/merchant_custom_attributes.py)

<details>
<summary><code>def bulk_delete_merchant_custom_attributes(body: BulkDeleteMerchantCustomAttributesRequest | BulkDeleteMerchantCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkDeleteMerchantCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.bulk_delete_merchant_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteMerchantCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.bulk_delete_merchant_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteMerchantCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkDeleteMerchantCustomAttributesRequest](square/models/bulk_delete_merchant_custom_attributes_request.py) \| [BulkDeleteMerchantCustomAttributesRequestDict](square/models/bulk_delete_merchant_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkDeleteMerchantCustomAttributesResponse](square/models/bulk_delete_merchant_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkDeleteMerchantCustomAttributesResponse](square/models/bulk_delete_merchant_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_upsert_merchant_custom_attributes(body: BulkUpsertMerchantCustomAttributesRequest | BulkUpsertMerchantCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpsertMerchantCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates [custom attributes](entity:CustomAttribute) for a merchant as a bulk operation.
Use this endpoint to set the value of one or more custom attributes for a merchant.
A custom attribute is based on a custom attribute definition in a Square seller account, which is
created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
This `BulkUpsertMerchantCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides a merchant ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.bulk_upsert_merchant_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertMerchantCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.bulk_upsert_merchant_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertMerchantCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpsertMerchantCustomAttributesRequest](square/models/bulk_upsert_merchant_custom_attributes_request.py) \| [BulkUpsertMerchantCustomAttributesRequestDict](square/models/bulk_upsert_merchant_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpsertMerchantCustomAttributesResponse](square/models/bulk_upsert_merchant_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpsertMerchantCustomAttributesResponse](square/models/bulk_upsert_merchant_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_merchant_custom_attribute_definition(body: CreateMerchantCustomAttributeDefinitionRequest | CreateMerchantCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateMerchantCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to define a custom attribute that can be associated with a merchant connecting to your application.
A custom attribute definition specifies the `key`, `visibility`, `schema`, and other properties
for a custom attribute. After the definition is created, you can call
[UpsertMerchantCustomAttribute](api-endpoint:MerchantCustomAttributes-UpsertMerchantCustomAttribute) or
[BulkUpsertMerchantCustomAttributes](api-endpoint:MerchantCustomAttributes-BulkUpsertMerchantCustomAttributes)
to set the custom attribute for a merchant.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.create_merchant_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.create_merchant_custom_attribute_definition(
    body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateMerchantCustomAttributeDefinitionRequest](square/models/create_merchant_custom_attribute_definition_request.py) \| [CreateMerchantCustomAttributeDefinitionRequestDict](square/models/create_merchant_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateMerchantCustomAttributeDefinitionResponse](square/models/create_merchant_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateMerchantCustomAttributeDefinitionResponse](square/models/create_merchant_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_merchant_custom_attribute(merchant_id: str, key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteMerchantCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a merchant.
To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.delete_merchant_custom_attribute(merchant_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteMerchantCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.delete_merchant_custom_attribute(
    merchant_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteMerchantCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_id</code> | <code>str</code> | The ID of the target [merchant](entity:Merchant). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to delete. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteMerchantCustomAttributeResponse](square/models/delete_merchant_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteMerchantCustomAttributeResponse](square/models/delete_merchant_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_merchant_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteMerchantCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
Deleting a custom attribute definition also deletes the corresponding custom attribute from
the merchant.
Only the definition owner can delete a custom attribute definition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.delete_merchant_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.delete_merchant_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteMerchantCustomAttributeDefinitionResponse](square/models/delete_merchant_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteMerchantCustomAttributeDefinitionResponse](square/models/delete_merchant_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_merchant_custom_attribute_definitions(*, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListMerchantCustomAttributeDefinitionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the merchant-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.
When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.list_merchant_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMerchantCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.list_merchant_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMerchantCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>visibility_filter</code> | <code>[VisibilityFilterOrStr](square/models/enums/visibility_filter.py) \| None</code> | Filters the `CustomAttributeDefinition` results by their `visibility` values.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListMerchantCustomAttributeDefinitionsResponse](square/models/list_merchant_custom_attribute_definitions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListMerchantCustomAttributeDefinitionsResponse](square/models/list_merchant_custom_attribute_definitions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_merchant_custom_attributes(merchant_id: str, *, visibility_filter: VisibilityFilterOrStr | None = None, limit: int | None = None, cursor: str | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListMerchantCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with a merchant.
You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.
When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.list_merchant_custom_attributes(merchant_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMerchantCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.list_merchant_custom_attributes(merchant_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMerchantCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_id</code> | <code>str</code> | The ID of the target [merchant](entity:Merchant). |
| <code>visibility_filter</code> | <code>[VisibilityFilterOrStr](square/models/enums/visibility_filter.py) \| None</code> | Filters the `CustomAttributeDefinition` results by their `visibility` values.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory.<br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100.<br>The default value is 20. For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint.<br>Provide this cursor to retrieve the next page of results for your original request. For more<br>information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>with_definitions</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListMerchantCustomAttributesResponse](square/models/list_merchant_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListMerchantCustomAttributesResponse](square/models/list_merchant_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_merchant_custom_attribute(merchant_id: str, key: str, *, with_definition: bool | None = False, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveMerchantCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with a merchant.
You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.
To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.retrieve_merchant_custom_attribute(merchant_id, key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.retrieve_merchant_custom_attribute(
    merchant_id, key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_id</code> | <code>str</code> | The ID of the target [merchant](entity:Merchant). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to retrieve. This key must match the `key` of a custom<br>attribute definition in the Square seller account. If the requesting application is not the<br>definition owner, you must use the qualified key. |
| <code>with_definition</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of<br>the custom attribute. Set this parameter to `true` to get the name and description of the custom<br>attribute, information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute, which is used for strongly consistent reads to<br>guarantee that you receive the most up-to-date data. When included in the request, Square<br>returns the specified version or a higher version if one exists. If the specified version is<br>higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveMerchantCustomAttributeResponse](square/models/retrieve_merchant_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveMerchantCustomAttributeResponse](square/models/retrieve_merchant_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_merchant_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveMerchantCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.
To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.retrieve_merchant_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.retrieve_merchant_custom_attribute_definition(
    key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to retrieve. If the requesting application<br>is not the definition owner, you must use the qualified key. |
| <code>version</code> | <code>int \| None</code> | The current version of the custom attribute definition, which is used for strongly consistent<br>reads to guarantee that you receive the most up-to-date data. When included in the request,<br>Square returns the specified version or a higher version if one exists. If the specified version<br>is higher than the current version, Square returns a `BAD_REQUEST` error.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveMerchantCustomAttributeDefinitionResponse](square/models/retrieve_merchant_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveMerchantCustomAttributeDefinitionResponse](square/models/retrieve_merchant_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_merchant_custom_attribute_definition(key: str, body: UpdateMerchantCustomAttributeDefinitionRequest | UpdateMerchantCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateMerchantCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a merchant-related [custom attribute definition](entity:CustomAttributeDefinition) for a Square seller account.
Use this endpoint to update the following fields: `name`, `description`, `visibility`, or the
`schema` for a `Selection` data type.
Only the definition owner can update a custom attribute definition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.update_merchant_custom_attribute_definition(key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.update_merchant_custom_attribute_definition(
    key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateMerchantCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to update. |
| <code>body</code> | <code>[UpdateMerchantCustomAttributeDefinitionRequest](square/models/update_merchant_custom_attribute_definition_request.py) \| [UpdateMerchantCustomAttributeDefinitionRequestDict](square/models/update_merchant_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateMerchantCustomAttributeDefinitionResponse](square/models/update_merchant_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateMerchantCustomAttributeDefinitionResponse](square/models/update_merchant_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_merchant_custom_attribute(merchant_id: str, key: str, body: UpsertMerchantCustomAttributeRequest | UpsertMerchantCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertMerchantCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for a merchant.
Use this endpoint to set the value of a custom attribute for a specified merchant.
A custom attribute is based on a custom attribute definition in a Square seller account, which
is created using the [CreateMerchantCustomAttributeDefinition](api-endpoint:MerchantCustomAttributes-CreateMerchantCustomAttributeDefinition) endpoint.
To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchant_custom_attributes.with_raw_response.upsert_merchant_custom_attribute(merchant_id, key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertMerchantCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchant_custom_attributes.with_raw_response.upsert_merchant_custom_attribute(
    merchant_id, key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertMerchantCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_id</code> | <code>str</code> | The ID of the target [merchant](entity:Merchant). |
| <code>key</code> | <code>str</code> | The key of the custom attribute to create or update. This key must match the `key` of a<br>custom attribute definition in the Square seller account. If the requesting application is not<br>the definition owner, you must use the qualified key. |
| <code>body</code> | <code>[UpsertMerchantCustomAttributeRequest](square/models/upsert_merchant_custom_attribute_request.py) \| [UpsertMerchantCustomAttributeRequestDict](square/models/upsert_merchant_custom_attribute_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertMerchantCustomAttributeResponse](square/models/upsert_merchant_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertMerchantCustomAttributeResponse](square/models/upsert_merchant_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Merchants

> Source: [Merchants](square/apis/merchants.py)

<details>
<summary><code>def list_merchants(*, cursor: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListMerchantsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides details about the merchant associated with a given access token.

The access token used to connect your application to a Square seller is associated
with a single merchant. That means that `ListMerchants` returns a list
with a single `Merchant` object. You can specify your personal access token
to get your own merchant information or specify an OAuth token to get the
information for the merchant that granted your application access.

If you know the merchant ID, you can also use the [RetrieveMerchant](api-endpoint:Merchants-RetrieveMerchant)
endpoint to retrieve the merchant information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchants.with_raw_response.list_merchants()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMerchantsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchants.with_raw_response.list_merchants()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListMerchantsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>int \| None</code> | The cursor generated by the previous response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListMerchantsResponse](square/models/list_merchants_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListMerchantsResponse](square/models/list_merchants_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_merchant(merchant_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveMerchantResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the `Merchant` object for the given `merchant_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.merchants.with_raw_response.retrieve_merchant(merchant_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.merchants.with_raw_response.retrieve_merchant(merchant_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveMerchantResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>merchant_id</code> | <code>str</code> | The ID of the merchant to retrieve. If the string "me" is supplied as the ID,<br>then retrieve the merchant that is currently accessible to this call. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveMerchantResponse](square/models/retrieve_merchant_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveMerchantResponse](square/models/retrieve_merchant_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Oauth

> Source: [Oauth](square/apis/oauth.py)

<details>
<summary><code>def obtain_token(body: ObtainTokenRequest | ObtainTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ObtainTokenResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns an OAuth access token and refresh token using the `authorization_code`
or `refresh_token` grant type.

When `grant_type` is `authorization_code`:
- With the [code flow](https://developer.squareup.com/docs/oauth-api/overview#code-flow),
provide `code`, `client_id`, and `client_secret`.
- With the [PKCE flow](https://developer.squareup.com/docs/oauth-api/overview#pkce-flow),
provide `code`, `client_id`, and `code_verifier`. 

When `grant_type` is `refresh_token`:
- With the code flow, provide `refresh_token`, `client_id`, and `client_secret`.
The response returns the same refresh token provided in the request.
- With the PKCE flow, provide `refresh_token` and `client_id`. The response returns
a new refresh token.

You can use the `scopes` parameter to limit the set of permissions authorized by the
access token. You can use the `short_lived` parameter to create an access token that
expires in 24 hours.

__Important:__ OAuth tokens should be encrypted and stored on a secure server.
Application clients should never interact directly with OAuth tokens.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.obtain_token(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ObtainTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.oauth.with_raw_response.obtain_token(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ObtainTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[ObtainTokenRequest](square/models/obtain_token_request.py) \| [ObtainTokenRequestDict](square/models/obtain_token_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ObtainTokenResponse](square/models/obtain_token_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ObtainTokenResponse](square/models/obtain_token_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_token_status(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveTokenStatusResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns information about an [OAuth access token](https://developer.squareup.com/docs/build-basics/access-tokens#get-an-oauth-access-token) or an application’s [personal access token](https://developer.squareup.com/docs/build-basics/access-tokens#get-a-personal-access-token).

Add the access token to the Authorization header of the request.

__Important:__ The `Authorization` header you provide to this endpoint must have the following format:

``
Authorization: Bearer ACCESS_TOKEN
``

where `ACCESS_TOKEN` is a
[valid production authorization credential](https://developer.squareup.com/docs/build-basics/access-tokens).

If the access token is expired or not a valid access token, the endpoint returns an `UNAUTHORIZED` error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.retrieve_token_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTokenStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.oauth.with_raw_response.retrieve_token_status()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTokenStatusResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveTokenStatusResponse](square/models/retrieve_token_status_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveTokenStatusResponse](square/models/retrieve_token_status_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def revoke_token(body: RevokeTokenRequest | RevokeTokenRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RevokeTokenResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Revokes an access token generated with the OAuth flow.

If an account has more than one OAuth access token for your application, this
endpoint revokes all of them, regardless of which token you specify. 

__Important:__ The `Authorization` header for this endpoint must have the
following format:

``
Authorization: Client APPLICATION_SECRET
``

Replace `APPLICATION_SECRET` with the application secret on the **OAuth**
page for your application in the Developer Dashboard.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.oauth.with_raw_response.revoke_token(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevokeTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.oauth.with_raw_response.revoke_token(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RevokeTokenResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RevokeTokenRequest](square/models/revoke_token_request.py) \| [RevokeTokenRequestDict](square/models/revoke_token_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RevokeTokenResponse](square/models/revoke_token_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RevokeTokenResponse](square/models/revoke_token_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## OrderCustomAttributes

> Source: [OrderCustomAttributes](square/apis/order_custom_attributes.py)

<details>
<summary><code>def bulk_delete_order_custom_attributes(body: BulkDeleteOrderCustomAttributesRequest | BulkDeleteOrderCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkDeleteOrderCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes order [custom attributes](entity:CustomAttribute) as a bulk operation.

Use this endpoint to delete one or more custom attributes from one or more orders.
A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

This `BulkDeleteOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual delete
requests and returns a map of individual delete responses. Each delete request has a unique ID
and provides an order ID and custom attribute. Each delete response is returned with the ID
of the corresponding request.

To delete a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.bulk_delete_order_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteOrderCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.bulk_delete_order_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkDeleteOrderCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkDeleteOrderCustomAttributesRequest](square/models/bulk_delete_order_custom_attributes_request.py) \| [BulkDeleteOrderCustomAttributesRequestDict](square/models/bulk_delete_order_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkDeleteOrderCustomAttributesResponse](square/models/bulk_delete_order_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkDeleteOrderCustomAttributesResponse](square/models/bulk_delete_order_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_upsert_order_custom_attributes(body: BulkUpsertOrderCustomAttributesRequest | BulkUpsertOrderCustomAttributesRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpsertOrderCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates order [custom attributes](entity:CustomAttribute) as a bulk operation.

Use this endpoint to delete one or more custom attributes from one or more orders.
A custom attribute is based on a custom attribute definition in a Square seller account.  (To create a
custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

This `BulkUpsertOrderCustomAttributes` endpoint accepts a map of 1 to 25 individual upsert
requests and returns a map of individual upsert responses. Each upsert request has a unique ID
and provides an order ID and custom attribute. Each upsert response is returned with the ID
of the corresponding request.

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.bulk_upsert_order_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertOrderCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.bulk_upsert_order_custom_attributes(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpsertOrderCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpsertOrderCustomAttributesRequest](square/models/bulk_upsert_order_custom_attributes_request.py) \| [BulkUpsertOrderCustomAttributesRequestDict](square/models/bulk_upsert_order_custom_attributes_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpsertOrderCustomAttributesResponse](square/models/bulk_upsert_order_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpsertOrderCustomAttributesResponse](square/models/bulk_upsert_order_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_order_custom_attribute_definition(body: CreateOrderCustomAttributeDefinitionRequest | CreateOrderCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateOrderCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates an order-related custom attribute definition.  Use this endpoint to
define a custom attribute that can be associated with orders.

After creating a custom attribute definition, you can set the custom attribute for orders
in the Square seller account.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.create_order_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.create_order_custom_attribute_definition(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateOrderCustomAttributeDefinitionRequest](square/models/create_order_custom_attribute_definition_request.py) \| [CreateOrderCustomAttributeDefinitionRequestDict](square/models/create_order_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateOrderCustomAttributeDefinitionResponse](square/models/create_order_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateOrderCustomAttributeDefinitionResponse](square/models/create_order_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_order_custom_attribute(order_id: str, custom_attribute_key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteOrderCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a [custom attribute](entity:CustomAttribute) associated with a customer profile.

To delete a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.delete_order_custom_attribute(order_id, custom_attribute_key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteOrderCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.delete_order_custom_attribute(
    order_id, custom_attribute_key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteOrderCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the target [order](entity:Order). |
| <code>custom_attribute_key</code> | <code>str</code> | The key of the custom attribute to delete.  This key must match the key of an<br>existing custom attribute definition. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteOrderCustomAttributeResponse](square/models/delete_order_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteOrderCustomAttributeResponse](square/models/delete_order_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_order_custom_attribute_definition(key: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteOrderCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes an order-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

Only the definition owner can delete a custom attribute definition.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.delete_order_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.delete_order_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteOrderCustomAttributeDefinitionResponse](square/models/delete_order_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteOrderCustomAttributeDefinitionResponse](square/models/delete_order_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_order_custom_attribute_definitions(*, visibility_filter: VisibilityFilterOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListOrderCustomAttributeDefinitionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the order-related [custom attribute definitions](entity:CustomAttributeDefinition) that belong to a Square seller account.

When all response pages are retrieved, the results include all custom attribute definitions
that are visible to the requesting application, including those that are created by other
applications and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that
seller-defined custom attributes (also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.list_order_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListOrderCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.list_order_custom_attribute_definitions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListOrderCustomAttributeDefinitionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>visibility_filter</code> | <code>[VisibilityFilterOrStr](square/models/enums/visibility_filter.py) \| None</code> | Requests that all of the custom attributes be returned, or only those that are read-only or read-write.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint. <br>Provide this cursor to retrieve the next page of results for your original request. <br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory. <br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. <br>The default value is 20.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListOrderCustomAttributeDefinitionsResponse](square/models/list_order_custom_attribute_definitions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListOrderCustomAttributeDefinitionsResponse](square/models/list_order_custom_attribute_definitions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_order_custom_attributes(order_id: str, *, visibility_filter: VisibilityFilterOrStr | None = None, cursor: str | None = None, limit: int | None = None, with_definitions: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListOrderCustomAttributesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the [custom attributes](entity:CustomAttribute) associated with an order.

You can use the `with_definitions` query parameter to also retrieve custom attribute definitions
in the same call.

When all response pages are retrieved, the results include all custom attributes that are
visible to the requesting application, including those that are owned by other applications
and set to `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.list_order_custom_attributes(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListOrderCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.list_order_custom_attributes(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListOrderCustomAttributesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the target [order](entity:Order). |
| <code>visibility_filter</code> | <code>[VisibilityFilterOrStr](square/models/enums/visibility_filter.py) \| None</code> | Requests that all of the custom attributes be returned, or only those that are read-only or read-write.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | The cursor returned in the paged response from the previous call to this endpoint. <br>Provide this cursor to retrieve the next page of results for your original request. <br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to return in a single paged response. This limit is advisory. <br>The response might contain more or fewer results. The minimum value is 1 and the maximum value is 100. <br>The default value is 20.<br>For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).<br>**Default**: <code>None</code> |
| <code>with_definitions</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each<br>custom attribute. Set this parameter to `true` to get the name and description of each custom attribute, <br>information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListOrderCustomAttributesResponse](square/models/list_order_custom_attributes_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListOrderCustomAttributesResponse](square/models/list_order_custom_attributes_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_order_custom_attribute(order_id: str, custom_attribute_key: str, *, version: int | None = None, with_definition: bool | None = False, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveOrderCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a [custom attribute](entity:CustomAttribute) associated with an order.

You can use the `with_definition` query parameter to also retrieve the custom attribute definition
in the same call.

To retrieve a custom attribute owned by another application, the `visibility` setting must be
`VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.retrieve_order_custom_attribute(
    order_id, custom_attribute_key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveOrderCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.retrieve_order_custom_attribute(
    order_id, custom_attribute_key
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveOrderCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the target [order](entity:Order). |
| <code>custom_attribute_key</code> | <code>str</code> | The key of the custom attribute to retrieve.  This key must match the key of an<br>existing custom attribute definition. |
| <code>version</code> | <code>int \| None</code> | To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)<br>control, include this optional field and specify the current version of the custom attribute.<br>**Default**: <code>None</code> |
| <code>with_definition</code> | <code>bool \| None</code> | Indicates whether to return the [custom attribute definition](entity:CustomAttributeDefinition) in the `definition` field of each <br>custom attribute. Set this parameter to `true` to get the name and description of each custom attribute, <br>information about the data type, or other definition details. The default value is `false`.<br>**Default**: <code>False</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveOrderCustomAttributeResponse](square/models/retrieve_order_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveOrderCustomAttributeResponse](square/models/retrieve_order_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_order_custom_attribute_definition(key: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveOrderCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves an order-related [custom attribute definition](entity:CustomAttributeDefinition) from a Square seller account.

To retrieve a custom attribute definition created by another application, the `visibility`
setting must be `VISIBILITY_READ_ONLY` or `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.retrieve_order_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.retrieve_order_custom_attribute_definition(key)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to retrieve. |
| <code>version</code> | <code>int \| None</code> | To enable [optimistic concurrency](https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency)<br>control, include this optional field and specify the current version of the custom attribute.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveOrderCustomAttributeDefinitionResponse](square/models/retrieve_order_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveOrderCustomAttributeDefinitionResponse](square/models/retrieve_order_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_order_custom_attribute_definition(key: str, body: UpdateOrderCustomAttributeDefinitionRequest | UpdateOrderCustomAttributeDefinitionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateOrderCustomAttributeDefinitionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an order-related custom attribute definition for a Square seller account.

Only the definition owner can update a custom attribute definition. Note that sellers can view all custom attributes in exported customer data, including those set to `VISIBILITY_HIDDEN`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.update_order_custom_attribute_definition(key, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.update_order_custom_attribute_definition(
    key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateOrderCustomAttributeDefinitionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>key</code> | <code>str</code> | The key of the custom attribute definition to update. |
| <code>body</code> | <code>[UpdateOrderCustomAttributeDefinitionRequest](square/models/update_order_custom_attribute_definition_request.py) \| [UpdateOrderCustomAttributeDefinitionRequestDict](square/models/update_order_custom_attribute_definition_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateOrderCustomAttributeDefinitionResponse](square/models/update_order_custom_attribute_definition_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateOrderCustomAttributeDefinitionResponse](square/models/update_order_custom_attribute_definition_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_order_custom_attribute(order_id: str, custom_attribute_key: str, body: UpsertOrderCustomAttributeRequest | UpsertOrderCustomAttributeRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertOrderCustomAttributeResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates a [custom attribute](entity:CustomAttribute) for an order.

Use this endpoint to set the value of a custom attribute for a specific order.
A custom attribute is based on a custom attribute definition in a Square seller account. (To create a
custom attribute definition, use the [CreateOrderCustomAttributeDefinition](api-endpoint:OrderCustomAttributes-CreateOrderCustomAttributeDefinition) endpoint.)

To create or update a custom attribute owned by another application, the `visibility` setting
must be `VISIBILITY_READ_WRITE_VALUES`. Note that seller-defined custom attributes
(also known as custom fields) are always set to `VISIBILITY_READ_WRITE_VALUES`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.order_custom_attributes.with_raw_response.upsert_order_custom_attribute(
    order_id, custom_attribute_key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertOrderCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.order_custom_attributes.with_raw_response.upsert_order_custom_attribute(
    order_id, custom_attribute_key, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertOrderCustomAttributeResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the target [order](entity:Order). |
| <code>custom_attribute_key</code> | <code>str</code> | The key of the custom attribute to create or update.  This key must match the key <br>of an existing custom attribute definition. |
| <code>body</code> | <code>[UpsertOrderCustomAttributeRequest](square/models/upsert_order_custom_attribute_request.py) \| [UpsertOrderCustomAttributeRequestDict](square/models/upsert_order_custom_attribute_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertOrderCustomAttributeResponse](square/models/upsert_order_custom_attribute_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertOrderCustomAttributeResponse](square/models/upsert_order_custom_attribute_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Orders

> Source: [Orders](square/apis/orders.py)

<details>
<summary><code>def batch_retrieve_orders(body: BatchRetrieveOrdersRequest | BatchRetrieveOrdersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BatchRetrieveOrdersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a set of [orders](entity:Order) by their IDs.

If a given order ID does not exist, the ID is ignored instead of generating an error.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.batch_retrieve_orders(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.batch_retrieve_orders(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BatchRetrieveOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BatchRetrieveOrdersRequest](square/models/batch_retrieve_orders_request.py) \| [BatchRetrieveOrdersRequestDict](square/models/batch_retrieve_orders_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BatchRetrieveOrdersResponse](square/models/batch_retrieve_orders_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BatchRetrieveOrdersResponse](square/models/batch_retrieve_orders_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def calculate_order(body: CalculateOrderRequest | CalculateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CalculateOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enables applications to preview order pricing without creating an order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.calculate_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CalculateOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.calculate_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CalculateOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CalculateOrderRequest](square/models/calculate_order_request.py) \| [CalculateOrderRequestDict](square/models/calculate_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CalculateOrderResponse](square/models/calculate_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CalculateOrderResponse](square/models/calculate_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def clone_order(body: CloneOrderRequest | CloneOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CloneOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new order, in the `DRAFT` state, by duplicating an existing order. The newly created order has
only the core fields (such as line items, taxes, and discounts) copied from the original order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.clone_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CloneOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.clone_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CloneOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CloneOrderRequest](square/models/clone_order_request.py) \| [CloneOrderRequestDict](square/models/clone_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CloneOrderResponse](square/models/clone_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CloneOrderResponse](square/models/clone_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_order(body: CreateOrderRequest | CreateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new [order](entity:Order) that can include information about products for
purchase and settings to apply to the purchase.

To pay for a created order, see
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

You can modify open orders using the [UpdateOrder](api-endpoint:Orders-UpdateOrder) endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.create_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.create_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateOrderRequest](square/models/create_order_request.py) \| [CreateOrderRequestDict](square/models/create_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateOrderResponse](square/models/create_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateOrderResponse](square/models/create_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pay_order(order_id: str, body: PayOrderRequest | PayOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PayOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Pay for an [order](entity:Order) using one or more approved [payments](entity:Payment)
or settle an order with a total of `0`.

The total of the `payment_ids` listed in the request must be equal to the order
total. Orders with a total amount of `0` can be marked as paid by specifying an empty
array of `payment_ids` in the request.

To be used with `PayOrder`, a payment must:

- Reference the order by specifying the `order_id` when [creating the payment](api-endpoint:Payments-CreatePayment).
Any approved payments that reference the same `order_id` not specified in the
`payment_ids` is canceled.
- Be approved with [delayed capture](https://developer.squareup.com/docs/payments-api/take-payments/card-payments/delayed-capture).
Using a delayed capture payment with `PayOrder` completes the approved payment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.pay_order(order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PayOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.pay_order(order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PayOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the order being paid. |
| <code>body</code> | <code>[PayOrderRequest](square/models/pay_order_request.py) \| [PayOrderRequestDict](square/models/pay_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[PayOrderResponse](square/models/pay_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PayOrderResponse](square/models/pay_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_order(order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves an [Order](entity:Order) by ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.retrieve_order(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.retrieve_order(order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the order to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveOrderResponse](square/models/retrieve_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveOrderResponse](square/models/retrieve_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_orders(body: SearchOrdersRequest | SearchOrdersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchOrdersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Search all orders for one or more locations. Orders include all sales,
returns, and exchanges regardless of how or when they entered the Square
ecosystem (such as Point of Sale, Invoices, and Connect APIs).

`SearchOrders` requests need to specify which locations to search and define a
[SearchOrdersQuery](entity:SearchOrdersQuery) object that controls
how to sort or filter the results. Your `SearchOrdersQuery` can:

  Set filter criteria.
  Set the sort order.
  Determine whether to return results as complete `Order` objects or as
[OrderEntry](entity:OrderEntry) objects.

Note that details for orders processed with Square Point of Sale while in
offline mode might not be transmitted to Square for up to 72 hours. Offline
orders have a `created_at` value that reflects the time the order was created,
not the time it was subsequently transmitted to Square.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.search_orders(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.search_orders(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchOrdersRequest](square/models/search_orders_request.py) \| [SearchOrdersRequestDict](square/models/search_orders_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchOrdersResponse](square/models/search_orders_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchOrdersResponse](square/models/search_orders_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_order(order_id: str, body: UpdateOrderRequest | UpdateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an open [order](entity:Order) by adding, replacing, or deleting
fields. Orders with a `COMPLETED` or `CANCELED` state cannot be updated.

An `UpdateOrder` request requires the following:

- The `order_id` in the endpoint path, identifying the order to update.
- The latest `version` of the order to update.
- The [sparse order](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#sparse-order-objects)
containing only the fields to update and the version to which the update is
being applied.
- If deleting fields, the [dot notation paths](https://developer.squareup.com/docs/orders-api/manage-orders/update-orders#identifying-fields-to-delete)
identifying the fields to clear.

To pay for an order, see
[Pay for Orders](https://developer.squareup.com/docs/orders-api/pay-for-orders).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.orders.with_raw_response.update_order(order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.orders.with_raw_response.update_order(order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>order_id</code> | <code>str</code> | The ID of the order to update. |
| <code>body</code> | <code>[UpdateOrderRequest](square/models/update_order_request.py) \| [UpdateOrderRequestDict](square/models/update_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateOrderResponse](square/models/update_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateOrderResponse](square/models/update_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Payments

> Source: [Payments](square/apis/payments.py)

<details>
<summary><code>def cancel_payment(payment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelPaymentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels (voids) a payment. You can use this endpoint to cancel a payment with 
the APPROVED `status`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.cancel_payment(payment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelPaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.cancel_payment(payment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelPaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_id</code> | <code>str</code> | The ID of the payment to cancel. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelPaymentResponse](square/models/cancel_payment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelPaymentResponse](square/models/cancel_payment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_payment_by_idempotency_key(body: CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelPaymentByIdempotencyKeyResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels (voids) a payment identified by the idempotency key that is specified in the
request.

Use this method when the status of a `CreatePayment` request is unknown (for example, after you send a
`CreatePayment` request, a network error occurs and you do not get a response). In this case, you can
direct Square to cancel the payment using this endpoint. In the request, you provide the same
idempotency key that you provided in your `CreatePayment` request that you want to cancel. After
canceling the payment, you can submit your `CreatePayment` request again.

Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint
returns successfully.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.cancel_payment_by_idempotency_key(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelPaymentByIdempotencyKeyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.cancel_payment_by_idempotency_key(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelPaymentByIdempotencyKeyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CancelPaymentByIdempotencyKeyRequest](square/models/cancel_payment_by_idempotency_key_request.py) \| [CancelPaymentByIdempotencyKeyRequestDict](square/models/cancel_payment_by_idempotency_key_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelPaymentByIdempotencyKeyResponse](square/models/cancel_payment_by_idempotency_key_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelPaymentByIdempotencyKeyResponse](square/models/cancel_payment_by_idempotency_key_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def complete_payment(payment_id: str, body: CompletePaymentRequest | CompletePaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CompletePaymentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Completes (captures) a payment.
By default, payments are set to complete immediately after they are created.

You can use this endpoint to complete a payment with the APPROVED `status`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.complete_payment(payment_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompletePaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.complete_payment(payment_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CompletePaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_id</code> | <code>str</code> | The unique ID identifying the payment to be completed. |
| <code>body</code> | <code>[CompletePaymentRequest](square/models/complete_payment_request.py) \| [CompletePaymentRequestDict](square/models/complete_payment_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CompletePaymentResponse](square/models/complete_payment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CompletePaymentResponse](square/models/complete_payment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_payment(body: CreatePaymentRequest | CreatePaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreatePaymentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a payment using the provided source. You can use this endpoint 
to charge a card (credit/debit card or    
Square gift card) or record a payment that the seller received outside of Square 
(cash payment from a buyer or a payment that an external entity 
processed on behalf of the seller).

The endpoint creates a 
`Payment` object and returns it in the response.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.create_payment(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreatePaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.create_payment(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreatePaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreatePaymentRequest](square/models/create_payment_request.py) \| [CreatePaymentRequestDict](square/models/create_payment_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreatePaymentResponse](square/models/create_payment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreatePaymentResponse](square/models/create_payment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_payment(payment_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPaymentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves details for a specific payment.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.get_payment(payment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.get_payment(payment_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_id</code> | <code>str</code> | A unique ID for the desired payment. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetPaymentResponse](square/models/get_payment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPaymentResponse](square/models/get_payment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_payments(*, begin_time: str | None = None, end_time: str | None = None, sort_order: str | None = None, cursor: str | None = None, location_id: str | None = None, total: int | None = None, last_4: str | None = None, card_brand: str | None = None, limit: int | None = None, is_offline_payment: bool | None = False, offline_begin_time: str | None = None, offline_end_time: str | None = None, updated_at_begin_time: str | None = None, updated_at_end_time: str | None = None, sort_field: ListPaymentsRequestSortFieldOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPaymentsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of payments taken by the account making the request.

Results are eventually consistent, and new payments or changes to payments might take several
seconds to appear.

The maximum results per page is 100.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.list_payments()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPaymentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.list_payments()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPaymentsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>begin_time</code> | <code>str \| None</code> | Indicates the start of the time range to retrieve payments for, in RFC 3339 format.<br>The range is determined using the `created_at` field for each Payment.<br>Inclusive. Default: The current time minus one year.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>str \| None</code> | Indicates the end of the time range to retrieve payments for, in RFC 3339 format.  The<br>range is determined using the `created_at` field for each Payment.<br><br>Default: The current time.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>str \| None</code> | The order in which results are listed by `ListPaymentsRequest.sort_field`:<br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | Limit results to the location supplied. By default, results are returned<br>for the default (main) location associated with the seller.<br>**Default**: <code>None</code> |
| <code>total</code> | <code>int \| None</code> | The exact amount in the `total_money` for a payment.<br>**Default**: <code>None</code> |
| <code>last_4</code> | <code>str \| None</code> | The last four digits of a payment card.<br>**Default**: <code>None</code> |
| <code>card_brand</code> | <code>str \| None</code> | The brand of the payment card (for example, VISA).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br><br>The default value of 100 is also the maximum allowed value. If the provided value is <br>greater than 100, it is ignored and the default value is used instead.<br><br>Default: `100`<br>**Default**: <code>None</code> |
| <code>is_offline_payment</code> | <code>bool \| None</code> | Whether the payment was taken offline or not.<br>**Default**: <code>False</code> |
| <code>offline_begin_time</code> | <code>str \| None</code> | Indicates the start of the time range for which to retrieve offline payments, in RFC 3339<br>format for timestamps. The range is determined using the<br>`offline_payment_details.client_created_at` field for each Payment. If set, payments without a<br>value set in `offline_payment_details.client_created_at` will not be returned.<br><br>Default: The current time.<br>**Default**: <code>None</code> |
| <code>offline_end_time</code> | <code>str \| None</code> | Indicates the end of the time range for which to retrieve offline payments, in RFC 3339<br>format for timestamps. The range is determined using the<br>`offline_payment_details.client_created_at` field for each Payment. If set, payments without a<br>value set in `offline_payment_details.client_created_at` will not be returned.<br><br>Default: The current time.<br>**Default**: <code>None</code> |
| <code>updated_at_begin_time</code> | <code>str \| None</code> | Indicates the start of the time range to retrieve payments for, in RFC 3339 format.  The<br>range is determined using the `updated_at` field for each Payment.<br>**Default**: <code>None</code> |
| <code>updated_at_end_time</code> | <code>str \| None</code> | Indicates the end of the time range to retrieve payments for, in RFC 3339 format.  The<br>range is determined using the `updated_at` field for each Payment.<br>**Default**: <code>None</code> |
| <code>sort_field</code> | <code>[ListPaymentsRequestSortFieldOrStr](square/models/enums/list_payments_request_sort_field.py) \| None</code> | The field used to sort results by. The default is `CREATED_AT`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListPaymentsResponse](square/models/list_payments_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPaymentsResponse](square/models/list_payments_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_payment(payment_id: str, body: UpdatePaymentRequest | UpdatePaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdatePaymentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a payment with the APPROVED status.
You can update the `amount_money` and `tip_money` using this endpoint.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payments.with_raw_response.update_payment(payment_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatePaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payments.with_raw_response.update_payment(payment_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdatePaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payment_id</code> | <code>str</code> | The ID of the payment to update. |
| <code>body</code> | <code>[UpdatePaymentRequest](square/models/update_payment_request.py) \| [UpdatePaymentRequestDict](square/models/update_payment_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdatePaymentResponse](square/models/update_payment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdatePaymentResponse](square/models/update_payment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Payouts

> Source: [Payouts](square/apis/payouts.py)

<details>
<summary><code>def get_payout(payout_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPayoutResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves details of a specific payout identified by a payout ID.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payouts.with_raw_response.get_payout(payout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPayoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payouts.with_raw_response.get_payout(payout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPayoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payout_id</code> | <code>str</code> | The ID of the payout to retrieve the information for. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetPayoutResponse](square/models/get_payout_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPayoutResponse](square/models/get_payout_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_payout_entries(payout_id: str, *, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPayoutEntriesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of all payout entries for a specific payout.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payouts.with_raw_response.list_payout_entries(payout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPayoutEntriesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payouts.with_raw_response.list_payout_entries(payout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPayoutEntriesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>payout_id</code> | <code>str</code> | The ID of the payout to retrieve the information for. |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | The order in which payout entries are listed.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>If request parameters change between requests, subsequent results may contain duplicates or missing records.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br>Default: `100`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListPayoutEntriesResponse](square/models/list_payout_entries_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPayoutEntriesResponse](square/models/list_payout_entries_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_payouts(*, location_id: str | None = None, status: PayoutStatusOrStr | None = None, begin_time: str | None = None, end_time: str | None = None, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPayoutsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of all payouts for the default location.
You can filter payouts by location ID, status, time range, and order them in ascending or descending order.
To call this endpoint, set `PAYOUTS_READ` for the OAuth scope.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.payouts.with_raw_response.list_payouts()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPayoutsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.payouts.with_raw_response.list_payouts()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPayoutsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str \| None</code> | The ID of the location for which to list the payouts.<br>By default, payouts are returned for the default (main) location associated with the seller.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>[PayoutStatusOrStr](square/models/enums/payout_status.py) \| None</code> | If provided, only payouts with the given status are returned.<br>**Default**: <code>None</code> |
| <code>begin_time</code> | <code>str \| None</code> | The timestamp for the beginning of the payout creation time, in RFC 3339 format.<br>Inclusive. Default: The current time minus one year.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>str \| None</code> | The timestamp for the end of the payout creation time, in RFC 3339 format.<br>Default: The current time.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | The order in which payouts are listed.<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>If request parameters change between requests, subsequent results may contain duplicates or missing records.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value. If the provided value is<br>greater than 100, it is ignored and the default value is used instead.<br>Default: `100`<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListPayoutsResponse](square/models/list_payouts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPayoutsResponse](square/models/list_payouts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Refunds

> Source: [Refunds](square/apis/refunds.py)

<details>
<summary><code>def get_payment_refund(refund_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetPaymentRefundResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific refund using the `refund_id`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.refunds.with_raw_response.get_payment_refund(refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPaymentRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.refunds.with_raw_response.get_payment_refund(refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetPaymentRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>refund_id</code> | <code>str</code> | The unique ID for the desired `PaymentRefund`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetPaymentRefundResponse](square/models/get_payment_refund_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetPaymentRefundResponse](square/models/get_payment_refund_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_payment_refunds(*, begin_time: str | None = None, end_time: str | None = None, sort_order: str | None = None, cursor: str | None = None, location_id: str | None = None, status: str | None = None, source_type: str | None = None, limit: int | None = None, updated_at_begin_time: str | None = None, updated_at_end_time: str | None = None, sort_field: ListPaymentRefundsRequestSortFieldOrStr | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListPaymentRefundsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a list of refunds for the account making the request.

Results are eventually consistent, and new refunds or changes to refunds might take several
seconds to appear.

The maximum results per page is 100.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.refunds.with_raw_response.list_payment_refunds()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPaymentRefundsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.refunds.with_raw_response.list_payment_refunds()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListPaymentRefundsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>begin_time</code> | <code>str \| None</code> | Indicates the start of the time range to retrieve each `PaymentRefund` for, in RFC 3339 <br>format.  The range is determined using the `created_at` field for each `PaymentRefund`. <br><br>Default: The current time minus one year.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>str \| None</code> | Indicates the end of the time range to retrieve each `PaymentRefund` for, in RFC 3339 <br>format.  The range is determined using the `created_at` field for each `PaymentRefund`.<br><br>Default: The current time.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>str \| None</code> | The order in which results are listed by `PaymentRefund.created_at`:<br>- `ASC` - Oldest to newest.<br>- `DESC` - Newest to oldest (default).<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this cursor to retrieve the next set of results for the original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>location_id</code> | <code>str \| None</code> | Limit results to the location supplied. By default, results are returned<br>for all locations associated with the seller.<br>**Default**: <code>None</code> |
| <code>status</code> | <code>str \| None</code> | If provided, only refunds with the given status are returned.<br>For a list of refund status values, see [PaymentRefund](entity:PaymentRefund).<br><br>Default: If omitted, refunds are returned regardless of their status.<br>**Default**: <code>None</code> |
| <code>source_type</code> | <code>str \| None</code> | If provided, only returns refunds whose payments have the indicated source type.<br>Current values include `CARD`, `BANK_ACCOUNT`, `WALLET`, `CASH`, and `EXTERNAL`.<br>For information about these payment source types, see<br>[Take Payments](https://developer.squareup.com/docs/payments-api/take-payments).<br><br>Default: If omitted, refunds are returned regardless of the source type.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to be returned in a single page.<br><br>It is possible to receive fewer results than the specified limit on a given page.<br><br>If the supplied value is greater than 100, no more than 100 results are returned.<br><br>Default: 100<br>**Default**: <code>None</code> |
| <code>updated_at_begin_time</code> | <code>str \| None</code> | Indicates the start of the time range to retrieve each `PaymentRefund` for, in RFC 3339<br>format.  The range is determined using the `updated_at` field for each `PaymentRefund`.<br><br>Default: If omitted, the time range starts at `begin_time`.<br>**Default**: <code>None</code> |
| <code>updated_at_end_time</code> | <code>str \| None</code> | Indicates the end of the time range to retrieve each `PaymentRefund` for, in RFC 3339<br>format.  The range is determined using the `updated_at` field for each `PaymentRefund`.<br><br>Default: The current time.<br>**Default**: <code>None</code> |
| <code>sort_field</code> | <code>[ListPaymentRefundsRequestSortFieldOrStr](square/models/enums/list_payment_refunds_request_sort_field.py) \| None</code> | The field used to sort results by. The default is `CREATED_AT`.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListPaymentRefundsResponse](square/models/list_payment_refunds_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListPaymentRefundsResponse](square/models/list_payment_refunds_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def refund_payment(body: RefundPaymentRequest | RefundPaymentRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RefundPaymentResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Refunds a payment. You can refund the entire payment amount or a
portion of it. You can use this endpoint to refund a card payment or record a 
refund of a cash or external payment. For more information, see
[Refund Payment](https://developer.squareup.com/docs/payments-api/refund-payments).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.refunds.with_raw_response.refund_payment(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RefundPaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.refunds.with_raw_response.refund_payment(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RefundPaymentResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[RefundPaymentRequest](square/models/refund_payment_request.py) \| [RefundPaymentRequestDict](square/models/refund_payment_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RefundPaymentResponse](square/models/refund_payment_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RefundPaymentResponse](square/models/refund_payment_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Sites

> Source: [Sites](square/apis/sites.py)

<details>
<summary><code>def list_sites(*, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListSitesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists the Square Online sites that belong to a seller. Sites are listed in descending order by the `created_at` date.

__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.sites.with_raw_response.list_sites()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListSitesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.sites.with_raw_response.list_sites()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListSitesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListSitesResponse](square/models/list_sites_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListSitesResponse](square/models/list_sites_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Snippets

> Source: [Snippets](square/apis/snippets.py)

<details>
<summary><code>def delete_snippet(site_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteSnippetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Removes your snippet from a Square Online site.

You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snippets.with_raw_response.delete_snippet(site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteSnippetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.snippets.with_raw_response.delete_snippet(site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteSnippetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>site_id</code> | <code>str</code> | The ID of the site that contains the snippet. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteSnippetResponse](square/models/delete_snippet_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteSnippetResponse](square/models/delete_snippet_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_snippet(site_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveSnippetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves your snippet from a Square Online site. A site can contain snippets from multiple snippet applications, but you can retrieve only the snippet that was added by your application.

You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snippets.with_raw_response.retrieve_snippet(site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveSnippetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.snippets.with_raw_response.retrieve_snippet(site_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveSnippetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>site_id</code> | <code>str</code> | The ID of the site that contains the snippet. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveSnippetResponse](square/models/retrieve_snippet_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveSnippetResponse](square/models/retrieve_snippet_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def upsert_snippet(site_id: str, body: UpsertSnippetRequest | UpsertSnippetRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpsertSnippetResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Adds a snippet to a Square Online site or updates the existing snippet on the site. 
The snippet code is appended to the end of the `head` element on every page of the site, except checkout pages. A snippet application can add one snippet to a given site. 

You can call [ListSites](api-endpoint:Sites-ListSites) to get the IDs of the sites that belong to a seller.


__Note:__ Square Online APIs are publicly available as part of an early access program. For more information, see [Early access program for Square Online APIs](https://developer.squareup.com/docs/online-api#early-access-program-for-square-online-apis).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.snippets.with_raw_response.upsert_snippet(site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertSnippetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.snippets.with_raw_response.upsert_snippet(site_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpsertSnippetResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>site_id</code> | <code>str</code> | The ID of the site where you want to add or update the snippet. |
| <code>body</code> | <code>[UpsertSnippetRequest](square/models/upsert_snippet_request.py) \| [UpsertSnippetRequestDict](square/models/upsert_snippet_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpsertSnippetResponse](square/models/upsert_snippet_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpsertSnippetResponse](square/models/upsert_snippet_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Subscriptions

> Source: [Subscriptions](square/apis/subscriptions.py)

<details>
<summary><code>def bulk_swap_plan(body: BulkSwapPlanRequest | BulkSwapPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkSwapPlanResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a plan variation change for all active subscriptions under a given plan
variation. For more information, see [Swap Subscription Plan Variations](https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.bulk_swap_plan(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSwapPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.bulk_swap_plan(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkSwapPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkSwapPlanRequest](square/models/bulk_swap_plan_request.py) \| [BulkSwapPlanRequestDict](square/models/bulk_swap_plan_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkSwapPlanResponse](square/models/bulk_swap_plan_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkSwapPlanResponse](square/models/bulk_swap_plan_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_subscription(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a `CANCEL` action to cancel an active subscription. This 
sets the `canceled_date` field to the end of the active billing period. After this date, 
the subscription status changes from ACTIVE to CANCELED.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.cancel_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.cancel_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to cancel. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelSubscriptionResponse](square/models/cancel_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelSubscriptionResponse](square/models/cancel_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def change_billing_anchor_date(subscription_id: str, body: ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ChangeBillingAnchorDateResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes the [billing anchor date](https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates)
for a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.change_billing_anchor_date(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangeBillingAnchorDateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.change_billing_anchor_date(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ChangeBillingAnchorDateResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to update the billing anchor date. |
| <code>body</code> | <code>[ChangeBillingAnchorDateRequest](square/models/change_billing_anchor_date_request.py) \| [ChangeBillingAnchorDateRequestDict](square/models/change_billing_anchor_date_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ChangeBillingAnchorDateResponse](square/models/change_billing_anchor_date_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ChangeBillingAnchorDateResponse](square/models/change_billing_anchor_date_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_subscription(body: CreateSubscriptionRequest | CreateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Enrolls a customer in a subscription.

If you provide a card on file in the request, Square charges the card for
the subscription. Otherwise, Square sends an invoice to the customer's email
address. The subscription starts immediately, unless the request includes
the optional `start_date`. Each individual subscription is associated with a particular location.

For more information, see [Create a subscription](https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.create_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.create_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateSubscriptionRequest](square/models/create_subscription_request.py) \| [CreateSubscriptionRequestDict](square/models/create_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateSubscriptionResponse](square/models/create_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateSubscriptionResponse](square/models/create_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_subscription_action(subscription_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteSubscriptionActionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a scheduled action for a subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.delete_subscription_action(subscription_id, action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteSubscriptionActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.delete_subscription_action(subscription_id, action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteSubscriptionActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription the targeted action is to act upon. |
| <code>action_id</code> | <code>str</code> | The ID of the targeted action to be deleted. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteSubscriptionActionResponse](square/models/delete_subscription_action_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteSubscriptionActionResponse](square/models/delete_subscription_action_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_subscription_events(subscription_id: str, *, cursor: str | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListSubscriptionEventsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all [events](https://developer.squareup.com/docs/subscriptions-api/actions-events) for a specific subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.list_subscription_events(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListSubscriptionEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.list_subscription_events(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListSubscriptionEventsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to retrieve the events for. |
| <code>cursor</code> | <code>str \| None</code> | When the total number of resulting subscription events exceeds the limit of a paged response, <br>specify the cursor returned from a preceding response here to fetch the next set of results.<br>If the cursor is unset, the response contains the last page of the results.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The upper limit on the number of subscription events to return<br>in a paged response.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListSubscriptionEventsResponse](square/models/list_subscription_events_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListSubscriptionEventsResponse](square/models/list_subscription_events_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def pause_subscription(subscription_id: str, body: PauseSubscriptionRequest | PauseSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[PauseSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a `PAUSE` action to pause an active subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.pause_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PauseSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.pause_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type PauseSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to pause. |
| <code>body</code> | <code>[PauseSubscriptionRequest](square/models/pause_subscription_request.py) \| [PauseSubscriptionRequestDict](square/models/pause_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[PauseSubscriptionResponse](square/models/pause_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[PauseSubscriptionResponse](square/models/pause_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def resume_subscription(subscription_id: str, body: ResumeSubscriptionRequest | ResumeSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ResumeSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a `RESUME` action to resume a paused or a deactivated subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.resume_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResumeSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.resume_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ResumeSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to resume. |
| <code>body</code> | <code>[ResumeSubscriptionRequest](square/models/resume_subscription_request.py) \| [ResumeSubscriptionRequestDict](square/models/resume_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ResumeSubscriptionResponse](square/models/resume_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ResumeSubscriptionResponse](square/models/resume_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_subscription(subscription_id: str, *, include: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.retrieve_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.retrieve_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to retrieve. |
| <code>include</code> | <code>str \| None</code> | A query parameter to specify related information to be included in the response. <br><br>The supported query parameter values are: <br><br>- `actions`: to include scheduled actions on the targeted subscription.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveSubscriptionResponse](square/models/retrieve_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveSubscriptionResponse](square/models/retrieve_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_subscriptions(body: SearchSubscriptionsRequest | SearchSubscriptionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchSubscriptionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for subscriptions.

Results are ordered chronologically by subscription creation date. If
the request specifies more than one location ID,
the endpoint orders the result
by location ID, and then by creation date within each location. If no locations are given
in the query, all locations are searched.

You can also optionally specify `customer_ids` to search by customer.
If left unset, all customers
associated with the specified locations are returned.
If the request specifies customer IDs, the endpoint orders results
first by location, within location by customer ID, and within
customer by subscription creation date.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.search_subscriptions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchSubscriptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.search_subscriptions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchSubscriptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchSubscriptionsRequest](square/models/search_subscriptions_request.py) \| [SearchSubscriptionsRequestDict](square/models/search_subscriptions_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchSubscriptionsResponse](square/models/search_subscriptions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchSubscriptionsResponse](square/models/search_subscriptions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def swap_plan(subscription_id: str, body: SwapPlanRequest | SwapPlanRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SwapPlanResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Schedules a `SWAP_PLAN` action to swap a subscription plan variation in an existing subscription. 
For more information, see [Swap Subscription Plan Variations](https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.swap_plan(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SwapPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.swap_plan(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SwapPlanResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to swap the subscription plan for. |
| <code>body</code> | <code>[SwapPlanRequest](square/models/swap_plan_request.py) \| [SwapPlanRequestDict](square/models/swap_plan_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SwapPlanResponse](square/models/swap_plan_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SwapPlanResponse](square/models/swap_plan_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_subscription(subscription_id: str, body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a subscription by modifying or clearing `subscription` field values.
To clear a field, set its value to `null`.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.subscriptions.with_raw_response.update_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.subscriptions.with_raw_response.update_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | The ID of the subscription to update. |
| <code>body</code> | <code>[UpdateSubscriptionRequest](square/models/update_subscription_request.py) \| [UpdateSubscriptionRequestDict](square/models/update_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateSubscriptionResponse](square/models/update_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateSubscriptionResponse](square/models/update_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Team

> Source: [Team](square/apis/team.py)

<details>
<summary><code>def bulk_create_team_members(body: BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkCreateTeamMembersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates multiple `TeamMember` objects. The created `TeamMember` objects are returned on successful creates.
This process is non-transactional and processes as much of the request as possible. If one of the creates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed create.

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.bulk_create_team_members(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkCreateTeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.bulk_create_team_members(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkCreateTeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkCreateTeamMembersRequest](square/models/bulk_create_team_members_request.py) \| [BulkCreateTeamMembersRequestDict](square/models/bulk_create_team_members_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkCreateTeamMembersResponse](square/models/bulk_create_team_members_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkCreateTeamMembersResponse](square/models/bulk_create_team_members_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_update_team_members(body: BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpdateTeamMembersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates multiple `TeamMember` objects. The updated `TeamMember` objects are returned on successful updates.
This process is non-transactional and processes as much of the request as possible. If one of the updates in
the request cannot be successfully processed, the request is not marked as failed, but the body of the response
contains explicit error information for the failed update.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.bulk_update_team_members(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateTeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.bulk_update_team_members(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateTeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpdateTeamMembersRequest](square/models/bulk_update_team_members_request.py) \| [BulkUpdateTeamMembersRequestDict](square/models/bulk_update_team_members_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpdateTeamMembersResponse](square/models/bulk_update_team_members_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpdateTeamMembersResponse](square/models/bulk_update_team_members_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_job(body: CreateJobRequest | CreateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateJobResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a job in a seller account. A job defines a title and tip eligibility. Note that
compensation is defined in a [job assignment](entity:JobAssignment) in a team member's wage setting.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.create_job(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateJobResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.create_job(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateJobResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateJobRequest](square/models/create_job_request.py) \| [CreateJobRequestDict](square/models/create_job_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateJobResponse](square/models/create_job_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateJobResponse](square/models/create_job_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_team_member(body: CreateTeamMemberRequest | CreateTeamMemberRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTeamMemberResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a single `TeamMember` object. The `TeamMember` object is returned on successful creates.
You must provide the following values in your request to this endpoint:
- `given_name`
- `family_name`

Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.create_team_member(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTeamMemberResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.create_team_member(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTeamMemberResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTeamMemberRequest](square/models/create_team_member_request.py) \| [CreateTeamMemberRequestDict](square/models/create_team_member_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateTeamMemberResponse](square/models/create_team_member_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTeamMemberResponse](square/models/create_team_member_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_jobs(*, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListJobsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists jobs in a seller account. Results are sorted by title in ascending order.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.list_jobs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListJobsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.list_jobs()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListJobsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | The pagination cursor returned by the previous call to this endpoint. Provide this<br>cursor to retrieve the next page of results for your original request. For more information,<br>see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListJobsResponse](square/models/list_jobs_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListJobsResponse](square/models/list_jobs_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_job(job_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveJobResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specified job.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.retrieve_job(job_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveJobResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.retrieve_job(job_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveJobResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>str</code> | The ID of the job to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveJobResponse](square/models/retrieve_job_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveJobResponse](square/models/retrieve_job_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_team_member(team_member_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveTeamMemberResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a `TeamMember` object for the given `TeamMember.id`.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.retrieve_team_member(team_member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTeamMemberResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.retrieve_team_member(team_member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTeamMemberResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_member_id</code> | <code>str</code> | The ID of the team member to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveTeamMemberResponse](square/models/retrieve_team_member_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveTeamMemberResponse](square/models/retrieve_team_member_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_wage_setting(team_member_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveWageSettingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a `WageSetting` object for a team member specified
by `TeamMember.id`. For more information, see
[Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

Square recommends using [RetrieveTeamMember](api-endpoint:Team-RetrieveTeamMember) or [SearchTeamMembers](api-endpoint:Team-SearchTeamMembers)
to get this information directly from the `TeamMember.wage_setting` field.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.retrieve_wage_setting(team_member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveWageSettingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.retrieve_wage_setting(team_member_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveWageSettingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_member_id</code> | <code>str</code> | The ID of the team member for which to retrieve the wage setting. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveWageSettingResponse](square/models/retrieve_wage_setting_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveWageSettingResponse](square/models/retrieve_wage_setting_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_team_members(body: SearchTeamMembersRequest | SearchTeamMembersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchTeamMembersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a paginated list of `TeamMember` objects for a business. 
The list can be filtered by location IDs, `ACTIVE` or `INACTIVE` status, or whether
the team member is the Square account owner.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.search_team_members(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.search_team_members(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTeamMembersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchTeamMembersRequest](square/models/search_team_members_request.py) \| [SearchTeamMembersRequestDict](square/models/search_team_members_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchTeamMembersResponse](square/models/search_team_members_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchTeamMembersResponse](square/models/search_team_members_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_job(job_id: str, body: UpdateJobRequest | UpdateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateJobResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the title or tip eligibility of a job. Changes to the title propagate to all
`JobAssignment`, `Shift`, and `TeamMemberWage` objects that reference the job ID. Changes to
tip eligibility propagate to all `TeamMemberWage` objects that reference the job ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.update_job(job_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateJobResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.update_job(job_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateJobResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>job_id</code> | <code>str</code> | The ID of the job to update. |
| <code>body</code> | <code>[UpdateJobRequest](square/models/update_job_request.py) \| [UpdateJobRequestDict](square/models/update_job_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateJobResponse](square/models/update_job_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateJobResponse](square/models/update_job_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_team_member(team_member_id: str, body: UpdateTeamMemberRequest | UpdateTeamMemberRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateTeamMemberResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a single `TeamMember` object. The `TeamMember` object is returned on successful updates.
Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.update_team_member(team_member_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateTeamMemberResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.update_team_member(team_member_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateTeamMemberResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_member_id</code> | <code>str</code> | The ID of the team member to update. |
| <code>body</code> | <code>[UpdateTeamMemberRequest](square/models/update_team_member_request.py) \| [UpdateTeamMemberRequestDict](square/models/update_team_member_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateTeamMemberResponse](square/models/update_team_member_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateTeamMemberResponse](square/models/update_team_member_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_wage_setting(team_member_id: str, body: UpdateWageSettingRequest | UpdateWageSettingRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateWageSettingResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates or updates a `WageSetting` object. The object is created if a
`WageSetting` with the specified `team_member_id` doesn't exist. Otherwise,
it fully replaces the `WageSetting` object for the team member.
The `WageSetting` is returned on a successful update. For more information, see
[Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

Square recommends using [CreateTeamMember](api-endpoint:Team-CreateTeamMember) or [UpdateTeamMember](api-endpoint:Team-UpdateTeamMember)
to manage the `TeamMember.wage_setting` field directly.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.team.with_raw_response.update_wage_setting(team_member_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWageSettingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.team.with_raw_response.update_wage_setting(team_member_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWageSettingResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>team_member_id</code> | <code>str</code> | The ID of the team member for which to update the `WageSetting` object. |
| <code>body</code> | <code>[UpdateWageSettingRequest](square/models/update_wage_setting_request.py) \| [UpdateWageSettingRequestDict](square/models/update_wage_setting_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateWageSettingResponse](square/models/update_wage_setting_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateWageSettingResponse](square/models/update_wage_setting_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Terminal

> Source: [Terminal](square/apis/terminal.py)

<details>
<summary><code>def cancel_terminal_action(action_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelTerminalActionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a Terminal action request if the status of the request permits it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.cancel_terminal_action(action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.cancel_terminal_action(action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>action_id</code> | <code>str</code> | Unique ID for the desired `TerminalAction`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelTerminalActionResponse](square/models/cancel_terminal_action_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelTerminalActionResponse](square/models/cancel_terminal_action_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_terminal_checkout(checkout_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelTerminalCheckoutResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a Terminal checkout request if the status of the request permits it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.cancel_terminal_checkout(checkout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.cancel_terminal_checkout(checkout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>checkout_id</code> | <code>str</code> | The unique ID for the desired `TerminalCheckout`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelTerminalCheckoutResponse](square/models/cancel_terminal_checkout_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelTerminalCheckoutResponse](square/models/cancel_terminal_checkout_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def cancel_terminal_refund(terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelTerminalRefundResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels an Interac Terminal refund request by refund request ID if the status of the request permits it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.cancel_terminal_refund(terminal_refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.cancel_terminal_refund(terminal_refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>terminal_refund_id</code> | <code>str</code> | The unique ID for the desired `TerminalRefund`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelTerminalRefundResponse](square/models/cancel_terminal_refund_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelTerminalRefundResponse](square/models/cancel_terminal_refund_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_terminal_action(body: CreateTerminalActionRequest | CreateTerminalActionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTerminalActionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Terminal action request and sends it to the specified device.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.create_terminal_action(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.create_terminal_action(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTerminalActionRequest](square/models/create_terminal_action_request.py) \| [CreateTerminalActionRequestDict](square/models/create_terminal_action_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateTerminalActionResponse](square/models/create_terminal_action_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTerminalActionResponse](square/models/create_terminal_action_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_terminal_checkout(body: CreateTerminalCheckoutRequest | CreateTerminalCheckoutRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTerminalCheckoutResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a Terminal checkout request and sends it to the specified device to take a payment
for the requested amount.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.create_terminal_checkout(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.create_terminal_checkout(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTerminalCheckoutRequest](square/models/create_terminal_checkout_request.py) \| [CreateTerminalCheckoutRequestDict](square/models/create_terminal_checkout_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateTerminalCheckoutResponse](square/models/create_terminal_checkout_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTerminalCheckoutResponse](square/models/create_terminal_checkout_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_terminal_refund(body: CreateTerminalRefundRequest | CreateTerminalRefundRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTerminalRefundResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a request to refund an Interac payment completed on a Square Terminal. Refunds for Interac payments on a Square Terminal are supported only for Interac debit cards in Canada. Other refunds for Terminal payments should use the Refunds API. For more information, see [Refunds API](api:Refunds).

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.create_terminal_refund(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.create_terminal_refund(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTerminalRefundRequest](square/models/create_terminal_refund_request.py) \| [CreateTerminalRefundRequestDict](square/models/create_terminal_refund_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateTerminalRefundResponse](square/models/create_terminal_refund_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTerminalRefundResponse](square/models/create_terminal_refund_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dismiss_terminal_action(action_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DismissTerminalActionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Dismisses a Terminal action request if the status and type of the request permits it.

See [Link and Dismiss Actions](https://developer.squareup.com/docs/terminal-api/advanced-features/custom-workflows/link-and-dismiss-actions) for more details.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.dismiss_terminal_action(action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DismissTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.dismiss_terminal_action(action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DismissTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>action_id</code> | <code>str</code> | Unique ID for the `TerminalAction` associated with the action to be dismissed. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DismissTerminalActionResponse](square/models/dismiss_terminal_action_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DismissTerminalActionResponse](square/models/dismiss_terminal_action_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dismiss_terminal_checkout(checkout_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DismissTerminalCheckoutResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Dismisses a Terminal checkout request if the status and type of the request permits it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.dismiss_terminal_checkout(checkout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DismissTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.dismiss_terminal_checkout(checkout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DismissTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>checkout_id</code> | <code>str</code> | Unique ID for the `TerminalCheckout` associated with the checkout to be dismissed. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DismissTerminalCheckoutResponse](square/models/dismiss_terminal_checkout_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DismissTerminalCheckoutResponse](square/models/dismiss_terminal_checkout_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def dismiss_terminal_refund(terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DismissTerminalRefundResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Dismisses a Terminal refund request if the status and type of the request permits it.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.dismiss_terminal_refund(terminal_refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DismissTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.dismiss_terminal_refund(terminal_refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DismissTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>terminal_refund_id</code> | <code>str</code> | Unique ID for the `TerminalRefund` associated with the refund to be dismissed. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DismissTerminalRefundResponse](square/models/dismiss_terminal_refund_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DismissTerminalRefundResponse](square/models/dismiss_terminal_refund_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_terminal_action(action_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetTerminalActionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a Terminal action request by `action_id`. Terminal action requests are available for 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.get_terminal_action(action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.get_terminal_action(action_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTerminalActionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>action_id</code> | <code>str</code> | Unique ID for the desired `TerminalAction`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetTerminalActionResponse](square/models/get_terminal_action_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetTerminalActionResponse](square/models/get_terminal_action_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_terminal_checkout(checkout_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetTerminalCheckoutResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a Terminal checkout request by `checkout_id`. Terminal checkout requests are available for 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.get_terminal_checkout(checkout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.get_terminal_checkout(checkout_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTerminalCheckoutResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>checkout_id</code> | <code>str</code> | The unique ID for the desired `TerminalCheckout`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetTerminalCheckoutResponse](square/models/get_terminal_checkout_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetTerminalCheckoutResponse](square/models/get_terminal_checkout_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def get_terminal_refund(terminal_refund_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[GetTerminalRefundResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves an Interac Terminal refund object by ID. Terminal refund objects are available for 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.get_terminal_refund(terminal_refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.get_terminal_refund(terminal_refund_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type GetTerminalRefundResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>terminal_refund_id</code> | <code>str</code> | The unique ID for the desired `TerminalRefund`. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[GetTerminalRefundResponse](square/models/get_terminal_refund_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[GetTerminalRefundResponse](square/models/get_terminal_refund_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_terminal_actions(body: SearchTerminalActionsRequest | SearchTerminalActionsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchTerminalActionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a filtered list of Terminal action requests created by the account making the request. Terminal action requests are available for 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.search_terminal_actions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTerminalActionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.search_terminal_actions(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTerminalActionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchTerminalActionsRequest](square/models/search_terminal_actions_request.py) \| [SearchTerminalActionsRequestDict](square/models/search_terminal_actions_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchTerminalActionsResponse](square/models/search_terminal_actions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchTerminalActionsResponse](square/models/search_terminal_actions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_terminal_checkouts(body: SearchTerminalCheckoutsRequest | SearchTerminalCheckoutsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchTerminalCheckoutsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Returns a filtered list of Terminal checkout requests created by the application making the request. Only Terminal checkout requests created for the merchant scoped to the OAuth token are returned. Terminal checkout requests are available for 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.search_terminal_checkouts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTerminalCheckoutsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.search_terminal_checkouts(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTerminalCheckoutsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchTerminalCheckoutsRequest](square/models/search_terminal_checkouts_request.py) \| [SearchTerminalCheckoutsRequestDict](square/models/search_terminal_checkouts_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchTerminalCheckoutsResponse](square/models/search_terminal_checkouts_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchTerminalCheckoutsResponse](square/models/search_terminal_checkouts_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_terminal_refunds(body: SearchTerminalRefundsRequest | SearchTerminalRefundsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchTerminalRefundsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a filtered list of Interac Terminal refund requests created by the seller making the request. Terminal refund requests are available for 30 days.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.terminal.with_raw_response.search_terminal_refunds(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTerminalRefundsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.terminal.with_raw_response.search_terminal_refunds(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTerminalRefundsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchTerminalRefundsRequest](square/models/search_terminal_refunds_request.py) \| [SearchTerminalRefundsRequestDict](square/models/search_terminal_refunds_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchTerminalRefundsResponse](square/models/search_terminal_refunds_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchTerminalRefundsResponse](square/models/search_terminal_refunds_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Transactions

> Source: [Transactions](square/apis/transactions.py)

<details>
<summary><code>def capture_transaction(location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CaptureTransactionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Captures a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
endpoint with a `delay_capture` value of `true`.

See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transactions.with_raw_response.capture_transaction(location_id, transaction_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CaptureTransactionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transactions.with_raw_response.capture_transaction(location_id, transaction_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CaptureTransactionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | Value sent with the request. |
| <code>transaction_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CaptureTransactionResponse](square/models/capture_transaction_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CaptureTransactionResponse](square/models/capture_transaction_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_transactions(location_id: str, *, begin_time: str | None = None, end_time: str | None = None, sort_order: SortOrderOrStr | None = None, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListTransactionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists transactions for a particular location.

Transactions include payment information from sales and exchanges and refund
information from returns and exchanges.

Max results per [page](https://developer.squareup.com/docs/working-with-apis/pagination): 50

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transactions.with_raw_response.list_transactions(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTransactionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transactions.with_raw_response.list_transactions(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListTransactionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location to list transactions for. |
| <code>begin_time</code> | <code>str \| None</code> | The beginning of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.<br><br>Default value: The current time minus one year.<br>**Default**: <code>None</code> |
| <code>end_time</code> | <code>str \| None</code> | The end of the requested reporting period, in RFC 3339 format.<br><br>See [Date ranges](https://developer.squareup.com/docs/build-basics/working-with-dates) for details on date inclusivity/exclusivity.<br><br>Default value: The current time.<br>**Default**: <code>None</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | The order in which results are listed in the response (`ASC` for<br>oldest first, `DESC` for newest first).<br><br>Default value: `DESC`<br>**Default**: <code>None</code> |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>See [Paginating results](https://developer.squareup.com/docs/working-with-apis/pagination) for more information.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListTransactionsResponse](square/models/list_transactions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListTransactionsResponse](square/models/list_transactions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_transaction(location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveTransactionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves details for a single transaction.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transactions.with_raw_response.retrieve_transaction(location_id, transaction_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTransactionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transactions.with_raw_response.retrieve_transaction(location_id, transaction_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTransactionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the transaction's associated location. |
| <code>transaction_id</code> | <code>str</code> | The ID of the transaction to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveTransactionResponse](square/models/retrieve_transaction_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveTransactionResponse](square/models/retrieve_transaction_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def void_transaction(location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[VoidTransactionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a transaction that was created with the [Charge](api-endpoint:Transactions-Charge)
endpoint with a `delay_capture` value of `true`.

See [Delayed capture transactions](https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture)
for more information.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transactions.with_raw_response.void_transaction(location_id, transaction_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VoidTransactionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transactions.with_raw_response.void_transaction(location_id, transaction_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type VoidTransactionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | Value sent with the request. |
| <code>transaction_id</code> | <code>str</code> | Value sent with the request. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[VoidTransactionResponse](square/models/void_transaction_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[VoidTransactionResponse](square/models/void_transaction_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## TransferOrderApi

> Source: [TransferOrderApi](square/apis/transfer_order_api.py)

<details>
<summary><code>def cancel_transfer_order(transfer_order_id: str, body: CancelTransferOrderRequest | CancelTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CancelTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Cancels a transfer order in [STARTED](entity:TransferOrderStatus) or 
[PARTIALLY_RECEIVED](entity:TransferOrderStatus) status. Any unreceived quantities will no
longer be receivable and will be immediately returned to the source [Location](entity:Location)'s inventory.

Common reasons for cancellation:
- Items no longer needed at destination
- Source location needs the inventory
- Order created in error

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.cancel_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.cancel_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CancelTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_order_id</code> | <code>str</code> | The ID of the transfer order to cancel. Must be in STARTED or PARTIALLY_RECEIVED status. |
| <code>body</code> | <code>[CancelTransferOrderRequest](square/models/cancel_transfer_order_request.py) \| [CancelTransferOrderRequestDict](square/models/cancel_transfer_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CancelTransferOrderResponse](square/models/cancel_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CancelTransferOrderResponse](square/models/cancel_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_transfer_order(body: CreateTransferOrderRequest | CreateTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a new transfer order in [DRAFT](entity:TransferOrderStatus) status. A transfer order represents the intent 
to move [CatalogItemVariation](entity:CatalogItemVariation)s from one [Location](entity:Location) to another. 
The source and destination locations must be different and must belong to your Square account.

In [DRAFT](entity:TransferOrderStatus) status, you can:
- Add or remove items
- Modify quantities
- Update shipping information
- Delete the entire order via [DeleteTransferOrder](api-endpoint:TransferOrders-DeleteTransferOrder)

The request requires source_location_id and destination_location_id.
Inventory levels are not affected until the order is started via 
[StartTransferOrder](api-endpoint:TransferOrders-StartTransferOrder).

Common integration points:
- Sync with warehouse management systems
- Automate regular stock transfers
- Initialize transfers from inventory optimization systems

Creates a [transfer_order.created](webhook:transfer_order.created) webhook event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.create_transfer_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.create_transfer_order(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateTransferOrderRequest](square/models/create_transfer_order_request.py) \| [CreateTransferOrderRequestDict](square/models/create_transfer_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateTransferOrderResponse](square/models/create_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateTransferOrderResponse](square/models/create_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_transfer_order(transfer_order_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a transfer order in [DRAFT](entity:TransferOrderStatus) status.
Only draft orders can be deleted. Once an order is started via 
[StartTransferOrder](api-endpoint:TransferOrders-StartTransferOrder), it can no longer be deleted.

Creates a [transfer_order.deleted](webhook:transfer_order.deleted) webhook event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.delete_transfer_order(transfer_order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.delete_transfer_order(transfer_order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_order_id</code> | <code>str</code> | The ID of the transfer order to delete |
| <code>version</code> | <code>int \| None</code> | Version for optimistic concurrency<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteTransferOrderResponse](square/models/delete_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteTransferOrderResponse](square/models/delete_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def receive_transfer_order(transfer_order_id: str, body: ReceiveTransferOrderRequest | ReceiveTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ReceiveTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Records receipt of [CatalogItemVariation](entity:CatalogItemVariation)s for a transfer order.
This endpoint supports partial receiving - you can receive items in multiple batches.

For each line item, you can specify:
- Quantity received in good condition (added to destination inventory with [InventoryState](entity:InventoryState) of IN_STOCK)
- Quantity damaged during transit/handling (added to destination inventory with [InventoryState](entity:InventoryState) of WASTE)
- Quantity canceled (returned to source location's inventory)

The order must be in [STARTED](entity:TransferOrderStatus) or [PARTIALLY_RECEIVED](entity:TransferOrderStatus) status.
Received quantities are added to the destination [Location](entity:Location)'s inventory according to their condition.
Canceled quantities are immediately returned to the source [Location](entity:Location)'s inventory.

When all items are either received, damaged, or canceled, the order moves to
[COMPLETED](entity:TransferOrderStatus) status.

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.receive_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReceiveTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.receive_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ReceiveTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_order_id</code> | <code>str</code> | The ID of the transfer order to receive items for |
| <code>body</code> | <code>[ReceiveTransferOrderRequest](square/models/receive_transfer_order_request.py) \| [ReceiveTransferOrderRequestDict](square/models/receive_transfer_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ReceiveTransferOrderResponse](square/models/receive_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ReceiveTransferOrderResponse](square/models/receive_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_transfer_order(transfer_order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a specific [TransferOrder](entity:TransferOrder) by ID. Returns the complete
order details including:

- Basic information (status, dates, notes)
- Line items with ordered and received quantities
- Source and destination [Location](entity:Location)s
- Tracking information (if available)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.retrieve_transfer_order(transfer_order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.retrieve_transfer_order(transfer_order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_order_id</code> | <code>str</code> | The ID of the transfer order to retrieve |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveTransferOrderResponse](square/models/retrieve_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveTransferOrderResponse](square/models/retrieve_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_transfer_orders(body: SearchTransferOrdersRequest | SearchTransferOrdersRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchTransferOrdersResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for transfer orders using filters. Returns a paginated list of matching
[TransferOrder](entity:TransferOrder)s sorted by creation date.

Common search scenarios:
- Find orders for a source [Location](entity:Location)
- Find orders for a destination [Location](entity:Location)
- Find orders in a particular [TransferOrderStatus](entity:TransferOrderStatus)

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.search_transfer_orders(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTransferOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.search_transfer_orders(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchTransferOrdersResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchTransferOrdersRequest](square/models/search_transfer_orders_request.py) \| [SearchTransferOrdersRequestDict](square/models/search_transfer_orders_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchTransferOrdersResponse](square/models/search_transfer_orders_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchTransferOrdersResponse](square/models/search_transfer_orders_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def start_transfer_order(transfer_order_id: str, body: StartTransferOrderRequest | StartTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[StartTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Changes a [DRAFT](entity:TransferOrderStatus) transfer order to [STARTED](entity:TransferOrderStatus) status.
This decrements inventory at the source [Location](entity:Location) and marks it as in-transit.

The order must be in [DRAFT](entity:TransferOrderStatus) status and have all required fields populated.
Once started, the order can no longer be deleted, but it can be canceled via 
[CancelTransferOrder](api-endpoint:TransferOrders-CancelTransferOrder).

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.start_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.start_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type StartTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_order_id</code> | <code>str</code> | The ID of the transfer order to start. Must be in DRAFT status. |
| <code>body</code> | <code>[StartTransferOrderRequest](square/models/start_transfer_order_request.py) \| [StartTransferOrderRequestDict](square/models/start_transfer_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[StartTransferOrderResponse](square/models/start_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[StartTransferOrderResponse](square/models/start_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_transfer_order(transfer_order_id: str, body: UpdateTransferOrderRequest | UpdateTransferOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateTransferOrderResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing transfer order. This endpoint supports sparse updates,
allowing you to modify specific fields without affecting others.

Creates a [transfer_order.updated](webhook:transfer_order.updated) webhook event.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.transfer_order_api.with_raw_response.update_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.transfer_order_api.with_raw_response.update_transfer_order(transfer_order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateTransferOrderResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>transfer_order_id</code> | <code>str</code> | The ID of the transfer order to update |
| <code>body</code> | <code>[UpdateTransferOrderRequest](square/models/update_transfer_order_request.py) \| [UpdateTransferOrderRequestDict](square/models/update_transfer_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateTransferOrderResponse](square/models/update_transfer_order_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateTransferOrderResponse](square/models/update_transfer_order_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## V1Transactions

> Source: [V1Transactions](square/apis/v1_transactions.py)

<details>
<summary><code>def v1_list_orders(location_id: str, *, order: SortOrderOrStr | None = None, limit: int | None = None, batch_token: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[list[V1Order], RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides summary information for a merchant's online store orders.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.v1_transactions.with_raw_response.v1_list_orders(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V1Order]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.v1_transactions.with_raw_response.v1_list_orders(location_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type list[V1Order]
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the location to list online store orders for. |
| <code>order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | The order in which payments are listed in the response.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of payments to return in a single response. This value cannot exceed 200.<br>**Default**: <code>None</code> |
| <code>batch_token</code> | <code>str \| None</code> | A pagination cursor to retrieve the next set of results for your<br>original query to the endpoint.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;list&#91;[V1Order](square/models/v1_order.py)&#93;, [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>list&#91;[V1Order](square/models/v1_order.py)&#93;</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def v1_retrieve_order(location_id: str, order_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1Order, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Provides comprehensive information for a single online store order, including the order's history.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.v1_transactions.with_raw_response.v1_retrieve_order(location_id, order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.v1_transactions.with_raw_response.v1_retrieve_order(location_id, order_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the order's associated location. |
| <code>order_id</code> | <code>str</code> | The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[V1Order](square/models/v1_order.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1Order](square/models/v1_order.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def v1_update_order(location_id: str, order_id: str, body: V1UpdateOrderRequest | V1UpdateOrderRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[V1Order, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates the details of an online store order. Every update you perform on an order corresponds to one of three actions:

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.v1_transactions.with_raw_response.v1_update_order(location_id, order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.v1_transactions.with_raw_response.v1_update_order(location_id, order_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type V1Order
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>location_id</code> | <code>str</code> | The ID of the order's associated location. |
| <code>order_id</code> | <code>str</code> | The order's Square-issued ID. You obtain this value from Order objects returned by the List Orders endpoint |
| <code>body</code> | <code>[V1UpdateOrderRequest](square/models/v1_update_order_request.py) \| [V1UpdateOrderRequestDict](square/models/v1_update_order_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[V1Order](square/models/v1_order.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[V1Order](square/models/v1_order.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## Vendors

> Source: [Vendors](square/apis/vendors.py)

<details>
<summary><code>def bulk_create_vendors(body: BulkCreateVendorsRequest | BulkCreateVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkCreateVendorsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates one or more [Vendor](entity:Vendor) objects to represent suppliers to a seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.bulk_create_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkCreateVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.bulk_create_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkCreateVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkCreateVendorsRequest](square/models/bulk_create_vendors_request.py) \| [BulkCreateVendorsRequestDict](square/models/bulk_create_vendors_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkCreateVendorsResponse](square/models/bulk_create_vendors_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkCreateVendorsResponse](square/models/bulk_create_vendors_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_retrieve_vendors(body: BulkRetrieveVendorsRequest | BulkRetrieveVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkRetrieveVendorsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves one or more vendors of specified [Vendor](entity:Vendor) IDs.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.bulk_retrieve_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.bulk_retrieve_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkRetrieveVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkRetrieveVendorsRequest](square/models/bulk_retrieve_vendors_request.py) \| [BulkRetrieveVendorsRequestDict](square/models/bulk_retrieve_vendors_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkRetrieveVendorsResponse](square/models/bulk_retrieve_vendors_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkRetrieveVendorsResponse](square/models/bulk_retrieve_vendors_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def bulk_update_vendors(body: BulkUpdateVendorsRequest | BulkUpdateVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[BulkUpdateVendorsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates one or more of existing [Vendor](entity:Vendor) objects as suppliers to a seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.bulk_update_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.bulk_update_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type BulkUpdateVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[BulkUpdateVendorsRequest](square/models/bulk_update_vendors_request.py) \| [BulkUpdateVendorsRequestDict](square/models/bulk_update_vendors_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[BulkUpdateVendorsResponse](square/models/bulk_update_vendors_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[BulkUpdateVendorsResponse](square/models/bulk_update_vendors_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def create_vendor(body: CreateVendorRequest | CreateVendorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateVendorResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a single [Vendor](entity:Vendor) object to represent a supplier to a seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.create_vendor(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateVendorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.create_vendor(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateVendorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateVendorRequest](square/models/create_vendor_request.py) \| [CreateVendorRequestDict](square/models/create_vendor_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateVendorResponse](square/models/create_vendor_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateVendorResponse](square/models/create_vendor_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_vendor(vendor_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveVendorResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves the vendor of a specified [Vendor](entity:Vendor) ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.retrieve_vendor(vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveVendorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.retrieve_vendor(vendor_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveVendorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | ID of the [Vendor](entity:Vendor) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveVendorResponse](square/models/retrieve_vendor_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveVendorResponse](square/models/retrieve_vendor_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def search_vendors(body: SearchVendorsRequest | SearchVendorsRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[SearchVendorsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Searches for vendors using a filter against supported [Vendor](entity:Vendor) properties and a supported sorter.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.search_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.search_vendors(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type SearchVendorsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[SearchVendorsRequest](square/models/search_vendors_request.py) \| [SearchVendorsRequestDict](square/models/search_vendors_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[SearchVendorsResponse](square/models/search_vendors_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[SearchVendorsResponse](square/models/search_vendors_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_vendor(vendor_id: str, body: UpdateVendorRequest | UpdateVendorRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateVendorResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates an existing [Vendor](entity:Vendor) object as a supplier to a seller.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.vendors.with_raw_response.update_vendor(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateVendorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.vendors.with_raw_response.update_vendor(vendor_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateVendorResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>vendor_id</code> | <code>str</code> | Value sent with the request. |
| <code>body</code> | <code>[UpdateVendorRequest](square/models/update_vendor_request.py) \| [UpdateVendorRequestDict](square/models/update_vendor_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateVendorResponse](square/models/update_vendor_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateVendorResponse](square/models/update_vendor_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

## WebhookSubscriptions

> Source: [WebhookSubscriptions](square/apis/webhook_subscriptions.py)

<details>
<summary><code>def create_webhook_subscription(body: CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[CreateWebhookSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Creates a webhook subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.create_webhook_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.create_webhook_subscription(body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type CreateWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>body</code> | <code>[CreateWebhookSubscriptionRequest](square/models/create_webhook_subscription_request.py) \| [CreateWebhookSubscriptionRequestDict](square/models/create_webhook_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[CreateWebhookSubscriptionResponse](square/models/create_webhook_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[CreateWebhookSubscriptionResponse](square/models/create_webhook_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def delete_webhook_subscription(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[DeleteWebhookSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Deletes a webhook subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.delete_webhook_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.delete_webhook_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type DeleteWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to delete. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[DeleteWebhookSubscriptionResponse](square/models/delete_webhook_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[DeleteWebhookSubscriptionResponse](square/models/delete_webhook_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_webhook_event_types(*, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListWebhookEventTypesResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all webhook event types that can be subscribed to.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.list_webhook_event_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListWebhookEventTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.list_webhook_event_types()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListWebhookEventTypesResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>api_version</code> | <code>str \| None</code> | The API version for which to list event types. Setting this field overrides the default version used by the application.<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListWebhookEventTypesResponse](square/models/list_webhook_event_types_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListWebhookEventTypesResponse](square/models/list_webhook_event_types_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def list_webhook_subscriptions(*, cursor: str | None = None, include_disabled: bool | None = False, sort_order: SortOrderOrStr | None = None, limit: int | None = None, request_options: RequestOptionsOrDict | None = None) -> ApiResult[ListWebhookSubscriptionsResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Lists all webhook subscriptions owned by your application.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.list_webhook_subscriptions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListWebhookSubscriptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.list_webhook_subscriptions()
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type ListWebhookSubscriptionsResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>cursor</code> | <code>str \| None</code> | A pagination cursor returned by a previous call to this endpoint.<br>Provide this to retrieve the next set of results for your original query.<br><br>For more information, see [Pagination](https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination).<br>**Default**: <code>None</code> |
| <code>include_disabled</code> | <code>bool \| None</code> | Includes disabled [Subscription](entity:WebhookSubscription)s.<br>By default, all enabled [Subscription](entity:WebhookSubscription)s are returned.<br>**Default**: <code>False</code> |
| <code>sort_order</code> | <code>[SortOrderOrStr](square/models/enums/sort_order.py) \| None</code> | Sorts the returned list by when the [Subscription](entity:WebhookSubscription) was created with the specified order.<br>This field defaults to ASC.<br>**Default**: <code>None</code> |
| <code>limit</code> | <code>int \| None</code> | The maximum number of results to be returned in a single page.<br>It is possible to receive fewer results than the specified limit on a given page.<br>The default value of 100 is also the maximum allowed value.<br><br>Default: 100<br>**Default**: <code>None</code> |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[ListWebhookSubscriptionsResponse](square/models/list_webhook_subscriptions_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[ListWebhookSubscriptionsResponse](square/models/list_webhook_subscriptions_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def retrieve_webhook_subscription(subscription_id: str, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[RetrieveWebhookSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Retrieves a webhook subscription identified by its ID.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.retrieve_webhook_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.retrieve_webhook_subscription(subscription_id)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type RetrieveWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to retrieve. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[RetrieveWebhookSubscriptionResponse](square/models/retrieve_webhook_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[RetrieveWebhookSubscriptionResponse](square/models/retrieve_webhook_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def test_webhook_subscription(subscription_id: str, body: TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[TestWebhookSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Tests a webhook subscription by sending a test event to the notification URL.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.test_webhook_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TestWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.test_webhook_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type TestWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to test. |
| <code>body</code> | <code>[TestWebhookSubscriptionRequest](square/models/test_webhook_subscription_request.py) \| [TestWebhookSubscriptionRequestDict](square/models/test_webhook_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[TestWebhookSubscriptionResponse](square/models/test_webhook_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[TestWebhookSubscriptionResponse](square/models/test_webhook_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_webhook_subscription(subscription_id: str, body: UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateWebhookSubscriptionResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a webhook subscription.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.update_webhook_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.update_webhook_subscription(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWebhookSubscriptionResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update. |
| <code>body</code> | <code>[UpdateWebhookSubscriptionRequest](square/models/update_webhook_subscription_request.py) \| [UpdateWebhookSubscriptionRequestDict](square/models/update_webhook_subscription_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateWebhookSubscriptionResponse](square/models/update_webhook_subscription_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateWebhookSubscriptionResponse](square/models/update_webhook_subscription_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

<details>
<summary><code>def update_webhook_subscription_signature_key(subscription_id: str, body: UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict, *, request_options: RequestOptionsOrDict | None = None) -> ApiResult[UpdateWebhookSubscriptionSignatureKeyResponse, RawError]</code></summary>

<dl>
<dd>

### Description

<dl>
<dd>

Updates a webhook subscription by replacing the existing signature key with a new one.

</dd>
</dl>

### Usage

<dl>
<dd>

**Sync**

```python
result = client.webhook_subscriptions.with_raw_response.update_webhook_subscription_signature_key(subscription_id, body)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWebhookSubscriptionSignatureKeyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

**Async**

```python
result = await async_client.webhook_subscriptions.with_raw_response.update_webhook_subscription_signature_key(
    subscription_id, body
)
match result:
    case Success(payload=payload):
        ...  # TODO: Handle 'payload' of type UpdateWebhookSubscriptionSignatureKeyResponse
    case Failure(error=error):
        ...  # TODO: Handle 'error' of type RawError
```

</dd>
</dl>

### Parameters

<dl>
<dd>

| Name | Type | Description |
| --- | --- | --- |
| <code>subscription_id</code> | <code>str</code> | [REQUIRED] The ID of the [Subscription](entity:WebhookSubscription) to update. |
| <code>body</code> | <code>[UpdateWebhookSubscriptionSignatureKeyRequest](square/models/update_webhook_subscription_signature_key_request.py) \| [UpdateWebhookSubscriptionSignatureKeyRequestDict](square/models/update_webhook_subscription_signature_key_request.py)</code> | An object containing the fields to POST for the request.<br><br>See the corresponding object definition for field details. |
| <code>request_options</code> | <code>[RequestOptionsOrDict](square/core/request_options.py) \| None</code> | Per-call overrides for this one request, such as a timeout or extra headers. |

</dd>
</dl>

### Response

<dl>
<dd>

**Returns**: <code>[ApiResult](square/core/results.py)&#91;[UpdateWebhookSubscriptionSignatureKeyResponse](square/models/update_webhook_subscription_signature_key_response.py), [RawError](square/core/results.py)&#93;</code>

**On `Success`**: `payload` is <code>[UpdateWebhookSubscriptionSignatureKeyResponse](square/models/update_webhook_subscription_signature_key_response.py)</code> -- Success

**On `Failure`**: `error` is <code>[RawError](square/core/results.py)</code>

</dd>
</dl>

</dd>
</dl>

</details>

