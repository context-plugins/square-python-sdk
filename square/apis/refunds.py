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
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    raw_error_response,
    unwrap,
)
from ..models.enums.list_payment_refunds_request_sort_field import ListPaymentRefundsRequestSortFieldOrStr
from ..models.get_payment_refund_response import GetPaymentRefundResponse
from ..models.list_payment_refunds_response import ListPaymentRefundsResponse
from ..models.refund_payment_request import RefundPaymentRequest, RefundPaymentRequestDict
from ..models.refund_payment_response import RefundPaymentResponse
from ..server.server import Server


class Refunds:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RefundsWithRawResponse(client, server, auth)

    def get_payment_refund(
        self, refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPaymentRefundResponse:
        """Retrieves a specific refund using the ``refund_id``.

        Args:
            refund_id: The unique ID for the desired ``PaymentRefund``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.get_payment_refund(refund_id, request_options=request_options))

    def list_payment_refunds(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        status: str | None = None,
        source_type: str | None = None,
        limit: int | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentRefundsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPaymentRefundsResponse:
        """Retrieves a list of refunds for the account making the request.

        Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The
                current time minus one year.
            end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339 format.
                The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The current
                time.
            sort_order: The order in which results are listed by ``PaymentRefund.created_at``: - ``ASC`` - Oldest to
                newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for all locations
                associated with the seller.
            status: If provided, only refunds with the given status are returned. For a list of refund status values,
                see `PaymentRefund <entity:PaymentRefund>`__. Default: If omitted, refunds are returned regardless of
                their status.
            source_type: If provided, only returns refunds whose payments have the indicated source type. Current values
                include ``CARD``, ``BANK_ACCOUNT``, ``WALLET``, ``CASH``, and ``EXTERNAL``. For information about these
                payment source types, see `Take Payments
                <https://developer.squareup.com/docs/payments-api/take-payments>`__. Default: If omitted, refunds are
                returned regardless of the source type.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. If the supplied value is greater than 100, no more
                than 100 results are returned. Default: 100
            updated_at_begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC
                3339 format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default:
                If omitted, the time range starts at ``begin_time``.
            updated_at_end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default: The
                current time.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_payment_refunds(
                begin_time=begin_time,
                end_time=end_time,
                sort_order=sort_order,
                cursor=cursor,
                location_id=location_id,
                status=status,
                source_type=source_type,
                limit=limit,
                updated_at_begin_time=updated_at_begin_time,
                updated_at_end_time=updated_at_end_time,
                sort_field=sort_field,
                request_options=request_options,
            ),
        )

    def refund_payment(
        self,
        body: RefundPaymentRequest | RefundPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RefundPaymentResponse:
        """Refunds a payment. You can refund the entire payment amount or a portion of it. You can use this endpoint to
        refund a card payment or record a refund of a cash or external payment. For more information, see `Refund
        Payment <https://developer.squareup.com/docs/payments-api/refund-payments>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.refund_payment(body, request_options=request_options))

    @property
    def with_raw_response(self) -> RefundsWithRawResponse:
        return self._with_raw_response


class AsyncRefunds:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRefundsWithRawResponse(client, server, auth)

    async def get_payment_refund(
        self, refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetPaymentRefundResponse:
        """Retrieves a specific refund using the ``refund_id``.

        Args:
            refund_id: The unique ID for the desired ``PaymentRefund``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.get_payment_refund(refund_id, request_options=request_options))

    async def list_payment_refunds(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        status: str | None = None,
        source_type: str | None = None,
        limit: int | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentRefundsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPaymentRefundsResponse:
        """Retrieves a list of refunds for the account making the request.

        Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The
                current time minus one year.
            end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339 format.
                The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The current
                time.
            sort_order: The order in which results are listed by ``PaymentRefund.created_at``: - ``ASC`` - Oldest to
                newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for all locations
                associated with the seller.
            status: If provided, only refunds with the given status are returned. For a list of refund status values,
                see `PaymentRefund <entity:PaymentRefund>`__. Default: If omitted, refunds are returned regardless of
                their status.
            source_type: If provided, only returns refunds whose payments have the indicated source type. Current values
                include ``CARD``, ``BANK_ACCOUNT``, ``WALLET``, ``CASH``, and ``EXTERNAL``. For information about these
                payment source types, see `Take Payments
                <https://developer.squareup.com/docs/payments-api/take-payments>`__. Default: If omitted, refunds are
                returned regardless of the source type.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. If the supplied value is greater than 100, no more
                than 100 results are returned. Default: 100
            updated_at_begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC
                3339 format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default:
                If omitted, the time range starts at ``begin_time``.
            updated_at_end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default: The
                current time.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_payment_refunds(
                begin_time=begin_time,
                end_time=end_time,
                sort_order=sort_order,
                cursor=cursor,
                location_id=location_id,
                status=status,
                source_type=source_type,
                limit=limit,
                updated_at_begin_time=updated_at_begin_time,
                updated_at_end_time=updated_at_end_time,
                sort_field=sort_field,
                request_options=request_options,
            ),
        )

    async def refund_payment(
        self,
        body: RefundPaymentRequest | RefundPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RefundPaymentResponse:
        """Refunds a payment. You can refund the entire payment amount or a portion of it. You can use this endpoint to
        refund a card payment or record a refund of a cash or external payment. For more information, see `Refund
        Payment <https://developer.squareup.com/docs/payments-api/refund-payments>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.refund_payment(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncRefundsWithRawResponse:
        return self._with_raw_response


class RefundsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_payment_refund(
        self, refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPaymentRefundResponse, RawError]:
        """Retrieves a specific refund using the ``refund_id``.

        Args:
            refund_id: The unique ID for the desired ``PaymentRefund``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/refunds/{refund_id}"),
            path_params=[param[str]("refund_id", refund_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetPaymentRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_payment_refunds(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        status: str | None = None,
        source_type: str | None = None,
        limit: int | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentRefundsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPaymentRefundsResponse, RawError]:
        """Retrieves a list of refunds for the account making the request.

        Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The
                current time minus one year.
            end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339 format.
                The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The current
                time.
            sort_order: The order in which results are listed by ``PaymentRefund.created_at``: - ``ASC`` - Oldest to
                newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for all locations
                associated with the seller.
            status: If provided, only refunds with the given status are returned. For a list of refund status values,
                see `PaymentRefund <entity:PaymentRefund>`__. Default: If omitted, refunds are returned regardless of
                their status.
            source_type: If provided, only returns refunds whose payments have the indicated source type. Current values
                include ``CARD``, ``BANK_ACCOUNT``, ``WALLET``, ``CASH``, and ``EXTERNAL``. For information about these
                payment source types, see `Take Payments
                <https://developer.squareup.com/docs/payments-api/take-payments>`__. Default: If omitted, refunds are
                returned regardless of the source type.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. If the supplied value is greater than 100, no more
                than 100 results are returned. Default: 100
            updated_at_begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC
                3339 format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default:
                If omitted, the time range starts at ``begin_time``.
            updated_at_end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default: The
                current time.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/refunds"),
            query_params=[
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[str | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
                param[str | None]("status", status),
                param[str | None]("source_type", source_type),
                param[int | None]("limit", limit),
                param[str | None]("updated_at_begin_time", updated_at_begin_time),
                param[str | None]("updated_at_end_time", updated_at_end_time),
                param[ListPaymentRefundsRequestSortFieldOrStr | None]("sort_field", sort_field),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListPaymentRefundsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def refund_payment(
        self,
        body: RefundPaymentRequest | RefundPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RefundPaymentResponse, RawError]:
        """Refunds a payment. You can refund the entire payment amount or a portion of it. You can use this endpoint to
        refund a card payment or record a refund of a cash or external payment. For more information, see `Refund
        Payment <https://developer.squareup.com/docs/payments-api/refund-payments>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/refunds"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundPaymentRequest | RefundPaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RefundPaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRefundsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_payment_refund(
        self, refund_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetPaymentRefundResponse, RawError]:
        """Retrieves a specific refund using the ``refund_id``.

        Args:
            refund_id: The unique ID for the desired ``PaymentRefund``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/refunds/{refund_id}"),
            path_params=[param[str]("refund_id", refund_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[GetPaymentRefundResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_payment_refunds(
        self,
        *,
        begin_time: str | None = None,
        end_time: str | None = None,
        sort_order: str | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        status: str | None = None,
        source_type: str | None = None,
        limit: int | None = None,
        updated_at_begin_time: str | None = None,
        updated_at_end_time: str | None = None,
        sort_field: ListPaymentRefundsRequestSortFieldOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPaymentRefundsResponse, RawError]:
        """Retrieves a list of refunds for the account making the request.

        Results are eventually consistent, and new refunds or changes to refunds might take several seconds to appear.

        The maximum results per page is 100.

        Args:
            begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The
                current time minus one year.
            end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339 format.
                The range is determined using the ``created_at`` field for each ``PaymentRefund``. Default: The current
                time.
            sort_order: The order in which results are listed by ``PaymentRefund.created_at``: - ``ASC`` - Oldest to
                newest. - ``DESC`` - Newest to oldest (default).
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            location_id: Limit results to the location supplied. By default, results are returned for all locations
                associated with the seller.
            status: If provided, only refunds with the given status are returned. For a list of refund status values,
                see `PaymentRefund <entity:PaymentRefund>`__. Default: If omitted, refunds are returned regardless of
                their status.
            source_type: If provided, only returns refunds whose payments have the indicated source type. Current values
                include ``CARD``, ``BANK_ACCOUNT``, ``WALLET``, ``CASH``, and ``EXTERNAL``. For information about these
                payment source types, see `Take Payments
                <https://developer.squareup.com/docs/payments-api/take-payments>`__. Default: If omitted, refunds are
                returned regardless of the source type.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. If the supplied value is greater than 100, no more
                than 100 results are returned. Default: 100
            updated_at_begin_time: Indicates the start of the time range to retrieve each ``PaymentRefund`` for, in RFC
                3339 format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default:
                If omitted, the time range starts at ``begin_time``.
            updated_at_end_time: Indicates the end of the time range to retrieve each ``PaymentRefund`` for, in RFC 3339
                format. The range is determined using the ``updated_at`` field for each ``PaymentRefund``. Default: The
                current time.
            sort_field: The field used to sort results by. The default is ``CREATED_AT``.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/refunds"),
            query_params=[
                param[str | None]("begin_time", begin_time),
                param[str | None]("end_time", end_time),
                param[str | None]("sort_order", sort_order),
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
                param[str | None]("status", status),
                param[str | None]("source_type", source_type),
                param[int | None]("limit", limit),
                param[str | None]("updated_at_begin_time", updated_at_begin_time),
                param[str | None]("updated_at_end_time", updated_at_end_time),
                param[ListPaymentRefundsRequestSortFieldOrStr | None]("sort_field", sort_field),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListPaymentRefundsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def refund_payment(
        self,
        body: RefundPaymentRequest | RefundPaymentRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RefundPaymentResponse, RawError]:
        """Refunds a payment. You can refund the entire payment amount or a portion of it. You can use this endpoint to
        refund a card payment or record a refund of a cash or external payment. For more information, see `Refund
        Payment <https://developer.squareup.com/docs/payments-api/refund-payments>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/refunds"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RefundPaymentRequest | RefundPaymentRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RefundPaymentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
