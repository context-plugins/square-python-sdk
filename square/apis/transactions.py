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
    json_decoder,
    param,
    raw_error_response,
)
from ..models.capture_transaction_response import CaptureTransactionResponse
from ..models.enums.sort_order import SortOrderOrStr
from ..models.list_transactions_response import ListTransactionsResponse
from ..models.retrieve_transaction_response import RetrieveTransactionResponse
from ..models.void_transaction_response import VoidTransactionResponse
from ..server.server import Server


class Transactions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TransactionsWithRawResponse(client, server, auth)

    def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CaptureTransactionResponse:
        """Captures a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with
        a ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.capture_transaction(
            location_id, transaction_id, request_options=request_options
        ).unwrap()

    def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTransactionsResponse:
        """Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund information from returns and
        exchanges.

        Max results per `page <https://developer.squareup.com/docs/working-with-apis/pagination>`__: 50

        Args:
            location_id: The ID of the location to list transactions for.
            begin_time: The beginning of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time minus one year.
            end_time: The end of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time.
            sort_order: The order in which results are listed in the response (``ASC`` for oldest first, ``DESC`` for
                newest first). Default value: ``DESC``
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_transactions(
            location_id,
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            request_options=request_options,
        ).unwrap()

    def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTransactionResponse:
        """Retrieves details for a single transaction.

        Args:
            location_id: The ID of the transaction's associated location.
            transaction_id: The ID of the transaction to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_transaction(
            location_id, transaction_id, request_options=request_options
        ).unwrap()

    def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VoidTransactionResponse:
        """Cancels a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with a
        ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.void_transaction(
            location_id, transaction_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TransactionsWithRawResponse:
        return self._with_raw_response


class AsyncTransactions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTransactionsWithRawResponse(client, server, auth)

    async def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CaptureTransactionResponse:
        """Captures a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with
        a ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.capture_transaction(
                location_id, transaction_id, request_options=request_options
            )
        ).unwrap()

    async def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTransactionsResponse:
        """Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund information from returns and
        exchanges.

        Max results per `page <https://developer.squareup.com/docs/working-with-apis/pagination>`__: 50

        Args:
            location_id: The ID of the location to list transactions for.
            begin_time: The beginning of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time minus one year.
            end_time: The end of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time.
            sort_order: The order in which results are listed in the response (``ASC`` for oldest first, ``DESC`` for
                newest first). Default value: ``DESC``
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_transactions(
                location_id,
                begin_time=begin_time,
                end_time=end_time,
                sort_order=sort_order,
                cursor=cursor,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTransactionResponse:
        """Retrieves details for a single transaction.

        Args:
            location_id: The ID of the transaction's associated location.
            transaction_id: The ID of the transaction to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_transaction(
                location_id, transaction_id, request_options=request_options
            )
        ).unwrap()

    async def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> VoidTransactionResponse:
        """Cancels a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with a
        ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.void_transaction(location_id, transaction_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTransactionsWithRawResponse:
        return self._with_raw_response


class TransactionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CaptureTransactionResponse, RawError]:
        """Captures a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with
        a ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/transactions/{transaction_id}/capture"),
            path_params=[param[str]("location_id", location_id), param[str]("transaction_id", transaction_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CaptureTransactionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTransactionsResponse, RawError]:
        """Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund information from returns and
        exchanges.

        Max results per `page <https://developer.squareup.com/docs/working-with-apis/pagination>`__: 50

        Args:
            location_id: The ID of the location to list transactions for.
            begin_time: The beginning of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time minus one year.
            end_time: The end of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time.
            sort_order: The order in which results are listed in the response (``ASC`` for oldest first, ``DESC`` for
                newest first). Default value: ``DESC``
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/transactions"),
            path_params=[param[str]("location_id", location_id)],
            query_params=[
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListTransactionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTransactionResponse, RawError]:
        """Retrieves details for a single transaction.

        Args:
            location_id: The ID of the transaction's associated location.
            transaction_id: The ID of the transaction to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/transactions/{transaction_id}"),
            path_params=[param[str]("location_id", location_id), param[str]("transaction_id", transaction_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTransactionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VoidTransactionResponse, RawError]:
        """Cancels a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with a
        ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/transactions/{transaction_id}/void"),
            path_params=[param[str]("location_id", location_id), param[str]("transaction_id", transaction_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[VoidTransactionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTransactionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def capture_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CaptureTransactionResponse, RawError]:
        """Captures a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with
        a ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/transactions/{transaction_id}/capture"),
            path_params=[param[str]("location_id", location_id), param[str]("transaction_id", transaction_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CaptureTransactionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_transactions(
        self,
        location_id: str,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: SortOrderOrStr | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTransactionsResponse, RawError]:
        """Lists transactions for a particular location.

        Transactions include payment information from sales and exchanges and refund information from returns and
        exchanges.

        Max results per `page <https://developer.squareup.com/docs/working-with-apis/pagination>`__: 50

        Args:
            location_id: The ID of the location to list transactions for.
            begin_time: The beginning of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time minus one year.
            end_time: The end of the requested reporting period, in RFC 3339 format. See `Date ranges
                <https://developer.squareup.com/docs/build-basics/working-with-dates>`__ for details on date
                inclusivity/exclusivity. Default value: The current time.
            sort_order: The order in which results are listed in the response (``ASC`` for oldest first, ``DESC`` for
                newest first). Default value: ``DESC``
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. See `Paginating results
                <https://developer.squareup.com/docs/working-with-apis/pagination>`__ for more information.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/transactions"),
            path_params=[param[str]("location_id", location_id)],
            query_params=[
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListTransactionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTransactionResponse, RawError]:
        """Retrieves details for a single transaction.

        Args:
            location_id: The ID of the transaction's associated location.
            transaction_id: The ID of the transaction to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/locations/{location_id}/transactions/{transaction_id}"),
            path_params=[param[str]("location_id", location_id), param[str]("transaction_id", transaction_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTransactionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def void_transaction(
        self, location_id: str, transaction_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[VoidTransactionResponse, RawError]:
        """Cancels a transaction that was created with the `Charge <api-endpoint:Transactions-Charge>`__ endpoint with a
        ``delay_capture`` value of ``true``.

        See `Delayed capture transactions
        <https://developer.squareup.com/docs/payments/transactions/overview#delayed-capture>`__ for more information.

        Args:
            location_id: Value sent with the request.
            transaction_id: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/transactions/{transaction_id}/void"),
            path_params=[param[str]("location_id", location_id), param[str]("transaction_id", transaction_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[VoidTransactionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
