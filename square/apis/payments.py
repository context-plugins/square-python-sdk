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
from ..models.cancel_payment_by_idempotency_key_request import (
    CancelPaymentByIdempotencyKeyRequest,
    CancelPaymentByIdempotencyKeyRequestDict,
)
from ..models.cancel_payment_by_idempotency_key_response import CancelPaymentByIdempotencyKeyResponse
from ..models.cancel_payment_response import CancelPaymentResponse
from ..models.complete_payment_request import CompletePaymentRequest, CompletePaymentRequestDict
from ..models.complete_payment_response import CompletePaymentResponse
from ..models.create_payment_request import CreatePaymentRequest, CreatePaymentRequestDict
from ..models.create_payment_response import CreatePaymentResponse
from ..models.enums.list_payments_request_sort_field import ListPaymentsRequestSortFieldOrStr
from ..models.get_payment_response import GetPaymentResponse
from ..models.list_payments_response import ListPaymentsResponse
from ..models.update_payment_request import UpdatePaymentRequest, UpdatePaymentRequestDict
from ..models.update_payment_response import UpdatePaymentResponse
from ..server.server import Server


class Payments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentsWithRawResponse(client, server, auth)

    def cancel_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelPaymentResponse:
        """Cancels (voids) a payment. You can use this endpoint to cancel a payment with the APPROVED ``status``.

        Args:
            payment_id: The ID of the payment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_payment(payment_id, request_options=request_options).unwrap()

    def cancel_payment_by_idempotency_key(
        self,
        body: CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelPaymentByIdempotencyKeyResponse:
        """Cancels (voids) a payment identified by the idempotency key that is specified in the request.

        Use this method when the status of a ``CreatePayment`` request is unknown (for example, after you send a
        ``CreatePayment`` request, a network error occurs and you do not get a response). In this case, you can direct
        Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you
        provided in your ``CreatePayment`` request that you want to cancel. After canceling the payment, you can submit
        your ``CreatePayment`` request again.

        Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns
        successfully.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_payment_by_idempotency_key(body, request_options=request_options).unwrap()

    def complete_payment(
        self,
        payment_id: str,
        body: CompletePaymentRequest | CompletePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompletePaymentResponse:
        """Completes (captures) a payment. By default, payments are set to complete immediately after they are created.

        You can use this endpoint to complete a payment with the APPROVED ``status``.

        Args:
            payment_id: The unique ID identifying the payment to be completed.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.complete_payment(payment_id, body, request_options=request_options).unwrap()

    def create_payment(
        self,
        body: CreatePaymentRequest | CreatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePaymentResponse:
        """Creates a payment using the provided source. You can use this endpoint to charge a card (credit/debit card or
        Square gift card) or record a payment that the seller received outside of Square (cash payment from a buyer or a
        payment that an external entity processed on behalf of the seller).

        The endpoint creates a ``Payment`` object and returns it in the response.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_payment(body, request_options=request_options).unwrap()

    def get_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPaymentResponse:
        """Retrieves details for a specific payment.

        Args:
            payment_id: A unique ID for the desired payment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_payment(payment_id, request_options=request_options).unwrap()

    def list_payments(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        total: int | None = None,
        last_4: str | None = None,
        card_brand: str | None = None,
        limit: int | None = None,
        is_offline_payment: bool | None = False,
        offline_begin_time: str | None = None,
        offline_end_time: str | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPaymentsResponse:
        """Retrieves a list of payments taken by the account making the request.

        Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Inclusive. Default: The current time minus
                one year.
            end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Default: The current time.
            sort_order: The order in which results are listed by ``ListPaymentsRequest.sort_field``: - ``ASC`` - Oldest
                to newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for the default (main)
                location associated with the seller.
            total: The exact amount in the ``total_money`` for a payment.
            last_4: The last four digits of a payment card.
            card_brand: The brand of the payment card (for example, VISA).
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            is_offline_payment: Whether the payment was taken offline or not.
            offline_begin_time: Indicates the start of the time range for which to retrieve offline payments, in RFC
                3339 format for timestamps. The range is determined using the
                ``offline_payment_details.client_created_at`` field for each Payment. If set, payments without a value
                set in ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            offline_end_time: Indicates the end of the time range for which to retrieve offline payments, in RFC 3339
                format for timestamps. The range is determined using the ``offline_payment_details.client_created_at``
                field for each Payment. If set, payments without a value set in
                ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            updated_at_begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format.
                The range is determined using the ``updated_at`` field for each Payment.
            updated_at_end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The
                range is determined using the ``updated_at`` field for each Payment.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_payments(
            begin_time=begin_time,
            end_time=end_time,
            sort_order=sort_order,
            cursor=cursor,
            location_id=location_id,
            total=total,
            last_4=last_4,
            card_brand=card_brand,
            limit=limit,
            is_offline_payment=is_offline_payment,
            offline_begin_time=offline_begin_time,
            offline_end_time=offline_end_time,
            updated_at_begin_time=updated_at_begin_time,
            updated_at_end_time=updated_at_end_time,
            sort_field=sort_field,
            request_options=request_options,
        ).unwrap()

    def update_payment(
        self,
        payment_id: str,
        body: UpdatePaymentRequest | UpdatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatePaymentResponse:
        """Updates a payment with the APPROVED status. You can update the ``amount_money`` and ``tip_money`` using this
        endpoint.

        Args:
            payment_id: The ID of the payment to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_payment(payment_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> PaymentsWithRawResponse:
        return self._with_raw_response


class AsyncPayments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentsWithRawResponse(client, server, auth)

    async def cancel_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelPaymentResponse:
        """Cancels (voids) a payment. You can use this endpoint to cancel a payment with the APPROVED ``status``.

        Args:
            payment_id: The ID of the payment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.cancel_payment(payment_id, request_options=request_options)).unwrap()

    async def cancel_payment_by_idempotency_key(
        self,
        body: CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelPaymentByIdempotencyKeyResponse:
        """Cancels (voids) a payment identified by the idempotency key that is specified in the request.

        Use this method when the status of a ``CreatePayment`` request is unknown (for example, after you send a
        ``CreatePayment`` request, a network error occurs and you do not get a response). In this case, you can direct
        Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you
        provided in your ``CreatePayment`` request that you want to cancel. After canceling the payment, you can submit
        your ``CreatePayment`` request again.

        Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns
        successfully.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_payment_by_idempotency_key(body, request_options=request_options)
        ).unwrap()

    async def complete_payment(
        self,
        payment_id: str,
        body: CompletePaymentRequest | CompletePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CompletePaymentResponse:
        """Completes (captures) a payment. By default, payments are set to complete immediately after they are created.

        You can use this endpoint to complete a payment with the APPROVED ``status``.

        Args:
            payment_id: The unique ID identifying the payment to be completed.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.complete_payment(payment_id, body, request_options=request_options)
        ).unwrap()

    async def create_payment(
        self,
        body: CreatePaymentRequest | CreatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePaymentResponse:
        """Creates a payment using the provided source. You can use this endpoint to charge a card (credit/debit card or
        Square gift card) or record a payment that the seller received outside of Square (cash payment from a buyer or a
        payment that an external entity processed on behalf of the seller).

        The endpoint creates a ``Payment`` object and returns it in the response.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_payment(body, request_options=request_options)).unwrap()

    async def get_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPaymentResponse:
        """Retrieves details for a specific payment.

        Args:
            payment_id: A unique ID for the desired payment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_payment(payment_id, request_options=request_options)).unwrap()

    async def list_payments(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        total: int | None = None,
        last_4: str | None = None,
        card_brand: str | None = None,
        limit: int | None = None,
        is_offline_payment: bool | None = False,
        offline_begin_time: str | None = None,
        offline_end_time: str | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPaymentsResponse:
        """Retrieves a list of payments taken by the account making the request.

        Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Inclusive. Default: The current time minus
                one year.
            end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Default: The current time.
            sort_order: The order in which results are listed by ``ListPaymentsRequest.sort_field``: - ``ASC`` - Oldest
                to newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for the default (main)
                location associated with the seller.
            total: The exact amount in the ``total_money`` for a payment.
            last_4: The last four digits of a payment card.
            card_brand: The brand of the payment card (for example, VISA).
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            is_offline_payment: Whether the payment was taken offline or not.
            offline_begin_time: Indicates the start of the time range for which to retrieve offline payments, in RFC
                3339 format for timestamps. The range is determined using the
                ``offline_payment_details.client_created_at`` field for each Payment. If set, payments without a value
                set in ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            offline_end_time: Indicates the end of the time range for which to retrieve offline payments, in RFC 3339
                format for timestamps. The range is determined using the ``offline_payment_details.client_created_at``
                field for each Payment. If set, payments without a value set in
                ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            updated_at_begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format.
                The range is determined using the ``updated_at`` field for each Payment.
            updated_at_end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The
                range is determined using the ``updated_at`` field for each Payment.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_payments(
                begin_time=begin_time,
                end_time=end_time,
                sort_order=sort_order,
                cursor=cursor,
                location_id=location_id,
                total=total,
                last_4=last_4,
                card_brand=card_brand,
                limit=limit,
                is_offline_payment=is_offline_payment,
                offline_begin_time=offline_begin_time,
                offline_end_time=offline_end_time,
                updated_at_begin_time=updated_at_begin_time,
                updated_at_end_time=updated_at_end_time,
                sort_field=sort_field,
                request_options=request_options,
            )
        ).unwrap()

    async def update_payment(
        self,
        payment_id: str,
        body: UpdatePaymentRequest | UpdatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatePaymentResponse:
        """Updates a payment with the APPROVED status. You can update the ``amount_money`` and ``tip_money`` using this
        endpoint.

        Args:
            payment_id: The ID of the payment to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_payment(payment_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentsWithRawResponse:
        return self._with_raw_response


class PaymentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelPaymentResponse, RawError]:
        """Cancels (voids) a payment. You can use this endpoint to cancel a payment with the APPROVED ``status``.

        Args:
            payment_id: The ID of the payment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/{payment_id}/cancel"),
            path_params=[param[str]("payment_id", payment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelPaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancel_payment_by_idempotency_key(
        self,
        body: CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelPaymentByIdempotencyKeyResponse, RawError]:
        """Cancels (voids) a payment identified by the idempotency key that is specified in the request.

        Use this method when the status of a ``CreatePayment`` request is unknown (for example, after you send a
        ``CreatePayment`` request, a network error occurs and you do not get a response). In this case, you can direct
        Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you
        provided in your ``CreatePayment`` request that you want to cancel. After canceling the payment, you can submit
        your ``CreatePayment`` request again.

        Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns
        successfully.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelPaymentByIdempotencyKeyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def complete_payment(
        self,
        payment_id: str,
        body: CompletePaymentRequest | CompletePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompletePaymentResponse, RawError]:
        """Completes (captures) a payment. By default, payments are set to complete immediately after they are created.

        You can use this endpoint to complete a payment with the APPROVED ``status``.

        Args:
            payment_id: The unique ID identifying the payment to be completed.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/{payment_id}/complete"),
            path_params=[param[str]("payment_id", payment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CompletePaymentRequest | CompletePaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CompletePaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_payment(
        self,
        body: CreatePaymentRequest | CreatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePaymentResponse, RawError]:
        """Creates a payment using the provided source. You can use this endpoint to charge a card (credit/debit card or
        Square gift card) or record a payment that the seller received outside of Square (cash payment from a buyer or a
        payment that an external entity processed on behalf of the seller).

        The endpoint creates a ``Payment`` object and returns it in the response.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePaymentRequest | CreatePaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreatePaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPaymentResponse, RawError]:
        """Retrieves details for a specific payment.

        Args:
            payment_id: A unique ID for the desired payment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/{payment_id}"),
            path_params=[param[str]("payment_id", payment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetPaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_payments(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        total: int | None = None,
        last_4: str | None = None,
        card_brand: str | None = None,
        limit: int | None = None,
        is_offline_payment: bool | None = False,
        offline_begin_time: str | None = None,
        offline_end_time: str | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPaymentsResponse, RawError]:
        """Retrieves a list of payments taken by the account making the request.

        Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Inclusive. Default: The current time minus
                one year.
            end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Default: The current time.
            sort_order: The order in which results are listed by ``ListPaymentsRequest.sort_field``: - ``ASC`` - Oldest
                to newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for the default (main)
                location associated with the seller.
            total: The exact amount in the ``total_money`` for a payment.
            last_4: The last four digits of a payment card.
            card_brand: The brand of the payment card (for example, VISA).
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            is_offline_payment: Whether the payment was taken offline or not.
            offline_begin_time: Indicates the start of the time range for which to retrieve offline payments, in RFC
                3339 format for timestamps. The range is determined using the
                ``offline_payment_details.client_created_at`` field for each Payment. If set, payments without a value
                set in ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            offline_end_time: Indicates the end of the time range for which to retrieve offline payments, in RFC 3339
                format for timestamps. The range is determined using the ``offline_payment_details.client_created_at``
                field for each Payment. If set, payments without a value set in
                ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            updated_at_begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format.
                The range is determined using the ``updated_at`` field for each Payment.
            updated_at_end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The
                range is determined using the ``updated_at`` field for each Payment.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments"),
            query_params=[
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[str | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
                param[int | None]("total", total),
                param[str | None]("last_4", last_4),
                param[str | None]("card_brand", card_brand),
                param[int | None]("limit", limit),
                param[bool | None]("is_offline_payment", is_offline_payment),
                param[str | None]("offline_begin_time", offline_begin_time),
                param[str | None]("offline_end_time", offline_end_time),
                param[str | None]("updated_at_begin_time", updated_at_begin_time),
                param[str | None]("updated_at_end_time", updated_at_end_time),
                param[ListPaymentsRequestSortFieldOrStr | None]("sort_field", sort_field),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListPaymentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_payment(
        self,
        payment_id: str,
        body: UpdatePaymentRequest | UpdatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatePaymentResponse, RawError]:
        """Updates a payment with the APPROVED status. You can update the ``amount_money`` and ``tip_money`` using this
        endpoint.

        Args:
            payment_id: The ID of the payment to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/payments/{payment_id}"),
            path_params=[param[str]("payment_id", payment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentRequest | UpdatePaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdatePaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncPaymentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelPaymentResponse, RawError]:
        """Cancels (voids) a payment. You can use this endpoint to cancel a payment with the APPROVED ``status``.

        Args:
            payment_id: The ID of the payment to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/{payment_id}/cancel"),
            path_params=[param[str]("payment_id", payment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelPaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancel_payment_by_idempotency_key(
        self,
        body: CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelPaymentByIdempotencyKeyResponse, RawError]:
        """Cancels (voids) a payment identified by the idempotency key that is specified in the request.

        Use this method when the status of a ``CreatePayment`` request is unknown (for example, after you send a
        ``CreatePayment`` request, a network error occurs and you do not get a response). In this case, you can direct
        Square to cancel the payment using this endpoint. In the request, you provide the same idempotency key that you
        provided in your ``CreatePayment`` request that you want to cancel. After canceling the payment, you can submit
        your ``CreatePayment`` request again.

        Note that if no payment with the specified idempotency key is found, no action is taken and the endpoint returns
        successfully.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/cancel"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelPaymentByIdempotencyKeyRequest | CancelPaymentByIdempotencyKeyRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelPaymentByIdempotencyKeyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def complete_payment(
        self,
        payment_id: str,
        body: CompletePaymentRequest | CompletePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CompletePaymentResponse, RawError]:
        """Completes (captures) a payment. By default, payments are set to complete immediately after they are created.

        You can use this endpoint to complete a payment with the APPROVED ``status``.

        Args:
            payment_id: The unique ID identifying the payment to be completed.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments/{payment_id}/complete"),
            path_params=[param[str]("payment_id", payment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CompletePaymentRequest | CompletePaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CompletePaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_payment(
        self,
        body: CreatePaymentRequest | CreatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePaymentResponse, RawError]:
        """Creates a payment using the provided source. You can use this endpoint to charge a card (credit/debit card or
        Square gift card) or record a payment that the seller received outside of Square (cash payment from a buyer or a
        payment that an external entity processed on behalf of the seller).

        The endpoint creates a ``Payment`` object and returns it in the response.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/payments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePaymentRequest | CreatePaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreatePaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_payment(
        self, payment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPaymentResponse, RawError]:
        """Retrieves details for a specific payment.

        Args:
            payment_id: A unique ID for the desired payment.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments/{payment_id}"),
            path_params=[param[str]("payment_id", payment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetPaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_payments(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        total: int | None = None,
        last_4: str | None = None,
        card_brand: str | None = None,
        limit: int | None = None,
        is_offline_payment: bool | None = False,
        offline_begin_time: str | None = None,
        offline_end_time: str | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPaymentsResponse, RawError]:
        """Retrieves a list of payments taken by the account making the request.

        Results are eventually consistent, and new payments or changes to payments might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Inclusive. Default: The current time minus
                one year.
            end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The range is
                determined using the ``created_at`` field for each Payment. Default: The current time.
            sort_order: The order in which results are listed by ``ListPaymentsRequest.sort_field``: - ``ASC`` - Oldest
                to newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for the default (main)
                location associated with the seller.
            total: The exact amount in the ``total_money`` for a payment.
            last_4: The last four digits of a payment card.
            card_brand: The brand of the payment card (for example, VISA).
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. If the provided value is greater than 100, it is ignored and the default value is used instead.
                Default: ``100``
            is_offline_payment: Whether the payment was taken offline or not.
            offline_begin_time: Indicates the start of the time range for which to retrieve offline payments, in RFC
                3339 format for timestamps. The range is determined using the
                ``offline_payment_details.client_created_at`` field for each Payment. If set, payments without a value
                set in ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            offline_end_time: Indicates the end of the time range for which to retrieve offline payments, in RFC 3339
                format for timestamps. The range is determined using the ``offline_payment_details.client_created_at``
                field for each Payment. If set, payments without a value set in
                ``offline_payment_details.client_created_at`` will not be returned. Default: The current time.
            updated_at_begin_time: Indicates the start of the time range to retrieve payments for, in RFC 3339 format.
                The range is determined using the ``updated_at`` field for each Payment.
            updated_at_end_time: Indicates the end of the time range to retrieve payments for, in RFC 3339 format. The
                range is determined using the ``updated_at`` field for each Payment.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/payments"),
            query_params=[
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[str | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
                param[int | None]("total", total),
                param[str | None]("last_4", last_4),
                param[str | None]("card_brand", card_brand),
                param[int | None]("limit", limit),
                param[bool | None]("is_offline_payment", is_offline_payment),
                param[str | None]("offline_begin_time", offline_begin_time),
                param[str | None]("offline_end_time", offline_end_time),
                param[str | None]("updated_at_begin_time", updated_at_begin_time),
                param[str | None]("updated_at_end_time", updated_at_end_time),
                param[ListPaymentsRequestSortFieldOrStr | None]("sort_field", sort_field),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListPaymentsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_payment(
        self,
        payment_id: str,
        body: UpdatePaymentRequest | UpdatePaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatePaymentResponse, RawError]:
        """Updates a payment with the APPROVED status. You can update the ``amount_money`` and ``tip_money`` using this
        endpoint.

        Args:
            payment_id: The ID of the payment to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/payments/{payment_id}"),
            path_params=[param[str]("payment_id", payment_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentRequest | UpdatePaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdatePaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
