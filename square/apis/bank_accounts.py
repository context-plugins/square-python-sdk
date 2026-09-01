from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    ApiResult,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.create_bank_account_request import CreateBankAccountRequest, CreateBankAccountRequestDict
from ..models.create_bank_account_response import CreateBankAccountResponse
from ..models.disable_bank_account_response import DisableBankAccountResponse
from ..models.get_bank_account_by_v1_id_response import GetBankAccountByV1IdResponse
from ..models.get_bank_account_response import GetBankAccountResponse
from ..models.list_bank_accounts_response import ListBankAccountsResponse
from ..server.server import Server


class BankAccounts:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BankAccountsWithRawResponse(client, server, auth)

    def create_bank_account(
        self,
        body: CreateBankAccountRequest | CreateBankAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBankAccountResponse:
        """Store a bank account on file for a square account

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_bank_account(body, request_options=request_options).unwrap()

    def disable_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisableBankAccountResponse:
        """Disable a bank account.

        Args:
            bank_account_id: The ID of the bank account to disable.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.disable_bank_account(bank_account_id, request_options=request_options).unwrap()

    def get_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBankAccountResponse:
        """Retrieve details of a `BankAccount <entity:BankAccount>`__ bank account linked to a Square account.

        Args:
            bank_account_id: Square-issued ID of the desired ``BankAccount``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_bank_account(bank_account_id, request_options=request_options).unwrap()

    def get_bank_account_by_v1_id(
        self, v1_bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBankAccountByV1IdResponse:
        """Returns details of a `BankAccount <entity:BankAccount>`__ identified by V1 bank account ID.

        Args:
            v1_bank_account_id: Connect V1 ID of the desired ``BankAccount``. For more information, see `Retrieve a bank
                account by using an ID issued by V1 Bank Accounts API
                <https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_bank_account_by_v1_id(
            v1_bank_account_id, request_options=request_options
        ).unwrap()

    def list_bank_accounts(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBankAccountsResponse:
        """Returns a list of `BankAccount <entity:BankAccount>`__ objects linked to a Square account.

        Args:
            cursor: The pagination cursor returned by a previous call to this endpoint. Use it in the next
                ``ListBankAccounts`` request to retrieve the next set of results. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            limit: Upper limit on the number of bank accounts to return in the response. Currently, 1000 is the largest
                supported limit. You can specify a limit of up to 1000 bank accounts. This is also the default limit.
            location_id: Location ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific location.
            customer_id: Customer ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific customer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_bank_accounts(
            cursor=cursor,
            limit=limit,
            location_id=location_id,
            customer_id=customer_id,
            request_options=request_options,
        ).unwrap()

    @property
    def with_raw_response(self) -> BankAccountsWithRawResponse:
        return self._with_raw_response


class AsyncBankAccounts:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBankAccountsWithRawResponse(client, server, auth)

    async def create_bank_account(
        self,
        body: CreateBankAccountRequest | CreateBankAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBankAccountResponse:
        """Store a bank account on file for a square account

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_bank_account(body, request_options=request_options)).unwrap()

    async def disable_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DisableBankAccountResponse:
        """Disable a bank account.

        Args:
            bank_account_id: The ID of the bank account to disable.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.disable_bank_account(bank_account_id, request_options=request_options)
        ).unwrap()

    async def get_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBankAccountResponse:
        """Retrieve details of a `BankAccount <entity:BankAccount>`__ bank account linked to a Square account.

        Args:
            bank_account_id: Square-issued ID of the desired ``BankAccount``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_bank_account(bank_account_id, request_options=request_options)
        ).unwrap()

    async def get_bank_account_by_v1_id(
        self, v1_bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBankAccountByV1IdResponse:
        """Returns details of a `BankAccount <entity:BankAccount>`__ identified by V1 bank account ID.

        Args:
            v1_bank_account_id: Connect V1 ID of the desired ``BankAccount``. For more information, see `Retrieve a bank
                account by using an ID issued by V1 Bank Accounts API
                <https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_bank_account_by_v1_id(v1_bank_account_id, request_options=request_options)
        ).unwrap()

    async def list_bank_accounts(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBankAccountsResponse:
        """Returns a list of `BankAccount <entity:BankAccount>`__ objects linked to a Square account.

        Args:
            cursor: The pagination cursor returned by a previous call to this endpoint. Use it in the next
                ``ListBankAccounts`` request to retrieve the next set of results. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            limit: Upper limit on the number of bank accounts to return in the response. Currently, 1000 is the largest
                supported limit. You can specify a limit of up to 1000 bank accounts. This is also the default limit.
            location_id: Location ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific location.
            customer_id: Customer ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific customer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_bank_accounts(
                cursor=cursor,
                limit=limit,
                location_id=location_id,
                customer_id=customer_id,
                request_options=request_options,
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBankAccountsWithRawResponse:
        return self._with_raw_response


class BankAccountsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_bank_account(
        self,
        body: CreateBankAccountRequest | CreateBankAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBankAccountResponse, RawError]:
        """Store a bank account on file for a square account

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bank-accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateBankAccountRequest | CreateBankAccountRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBankAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def disable_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisableBankAccountResponse, RawError]:
        """Disable a bank account.

        Args:
            bank_account_id: The ID of the bank account to disable.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bank-accounts/{bank_account_id}/disable"),
            path_params=[param[str]("bank_account_id", bank_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DisableBankAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBankAccountResponse, RawError]:
        """Retrieve details of a `BankAccount <entity:BankAccount>`__ bank account linked to a Square account.

        Args:
            bank_account_id: Square-issued ID of the desired ``BankAccount``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bank-accounts/{bank_account_id}"),
            path_params=[param[str]("bank_account_id", bank_account_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetBankAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_bank_account_by_v1_id(
        self, v1_bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBankAccountByV1IdResponse, RawError]:
        """Returns details of a `BankAccount <entity:BankAccount>`__ identified by V1 bank account ID.

        Args:
            v1_bank_account_id: Connect V1 ID of the desired ``BankAccount``. For more information, see `Retrieve a bank
                account by using an ID issued by V1 Bank Accounts API
                <https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bank-accounts/by-v1-id/{v1_bank_account_id}"),
            path_params=[param[str]("v1_bank_account_id", v1_bank_account_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetBankAccountByV1IdResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_bank_accounts(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBankAccountsResponse, RawError]:
        """Returns a list of `BankAccount <entity:BankAccount>`__ objects linked to a Square account.

        Args:
            cursor: The pagination cursor returned by a previous call to this endpoint. Use it in the next
                ``ListBankAccounts`` request to retrieve the next set of results. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            limit: Upper limit on the number of bank accounts to return in the response. Currently, 1000 is the largest
                supported limit. You can specify a limit of up to 1000 bank accounts. This is also the default limit.
            location_id: Location ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific location.
            customer_id: Customer ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific customer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bank-accounts"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
                param[str | None]("location_id", location_id),
                param[str | None]("customer_id", customer_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBankAccountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBankAccountsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_bank_account(
        self,
        body: CreateBankAccountRequest | CreateBankAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBankAccountResponse, RawError]:
        """Store a bank account on file for a square account

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bank-accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateBankAccountRequest | CreateBankAccountRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBankAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def disable_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DisableBankAccountResponse, RawError]:
        """Disable a bank account.

        Args:
            bank_account_id: The ID of the bank account to disable.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bank-accounts/{bank_account_id}/disable"),
            path_params=[param[str]("bank_account_id", bank_account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DisableBankAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_bank_account(
        self, bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBankAccountResponse, RawError]:
        """Retrieve details of a `BankAccount <entity:BankAccount>`__ bank account linked to a Square account.

        Args:
            bank_account_id: Square-issued ID of the desired ``BankAccount``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bank-accounts/{bank_account_id}"),
            path_params=[param[str]("bank_account_id", bank_account_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetBankAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_bank_account_by_v1_id(
        self, v1_bank_account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBankAccountByV1IdResponse, RawError]:
        """Returns details of a `BankAccount <entity:BankAccount>`__ identified by V1 bank account ID.

        Args:
            v1_bank_account_id: Connect V1 ID of the desired ``BankAccount``. For more information, see `Retrieve a bank
                account by using an ID issued by V1 Bank Accounts API
                <https://developer.squareup.com/docs/bank-accounts-api#retrieve-a-bank-account-by-using-an-id-issued-by-v1-bank-accounts-api>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bank-accounts/by-v1-id/{v1_bank_account_id}"),
            path_params=[param[str]("v1_bank_account_id", v1_bank_account_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetBankAccountByV1IdResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_bank_accounts(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        location_id: str | None = None,
        customer_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBankAccountsResponse, RawError]:
        """Returns a list of `BankAccount <entity:BankAccount>`__ objects linked to a Square account.

        Args:
            cursor: The pagination cursor returned by a previous call to this endpoint. Use it in the next
                ``ListBankAccounts`` request to retrieve the next set of results. See the `Pagination
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ guide for more information.
            limit: Upper limit on the number of bank accounts to return in the response. Currently, 1000 is the largest
                supported limit. You can specify a limit of up to 1000 bank accounts. This is also the default limit.
            location_id: Location ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific location.
            customer_id: Customer ID. You can specify this optional filter to retrieve only the linked bank accounts
                belonging to a specific customer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bank-accounts"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
                param[str | None]("location_id", location_id),
                param[str | None]("customer_id", customer_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBankAccountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
