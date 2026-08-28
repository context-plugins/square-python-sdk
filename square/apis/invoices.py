from __future__ import annotations

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
    multipart_body,
    param,
    raw_error_response,
)
from ..models.cancel_invoice_request import CancelInvoiceRequest, CancelInvoiceRequestDict
from ..models.cancel_invoice_response import CancelInvoiceResponse
from ..models.create_invoice_attachment_request import (
    CreateInvoiceAttachmentRequest,
    CreateInvoiceAttachmentRequestDict,
)
from ..models.create_invoice_attachment_response import CreateInvoiceAttachmentResponse
from ..models.create_invoice_request import CreateInvoiceRequest, CreateInvoiceRequestDict
from ..models.create_invoice_response import CreateInvoiceResponse
from ..models.delete_invoice_attachment_response import DeleteInvoiceAttachmentResponse
from ..models.delete_invoice_response import DeleteInvoiceResponse
from ..models.get_invoice_response import GetInvoiceResponse
from ..models.list_invoices_response import ListInvoicesResponse
from ..models.publish_invoice_request import PublishInvoiceRequest, PublishInvoiceRequestDict
from ..models.publish_invoice_response import PublishInvoiceResponse
from ..models.search_invoices_request import SearchInvoicesRequest, SearchInvoicesRequestDict
from ..models.search_invoices_response import SearchInvoicesResponse
from ..models.update_invoice_request import UpdateInvoiceRequest, UpdateInvoiceRequestDict
from ..models.update_invoice_response import UpdateInvoiceResponse
from ..server.server import Server


class Invoices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = InvoicesWithRawResponse(client, server, auth)

    def cancel_invoice(
        self,
        invoice_id: str,
        body: CancelInvoiceRequest | CancelInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInvoiceResponse:
        """Cancels an invoice. The seller cannot collect payments for the canceled invoice.

        You cannot cancel an invoice in the ``DRAFT`` state or in a terminal state: ``PAID``, ``REFUNDED``,
        ``CANCELED``, or ``FAILED``.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to cancel.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_invoice(invoice_id, body, request_options=request_options).unwrap()

    def create_invoice(
        self,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInvoiceResponse:
        """Creates a draft `invoice <entity:Invoice>`__ for an order created using the Orders API.

        A draft invoice remains in your account and no action is taken. You must publish the invoice before Square can
        process it (send it to the customer's email address or charge the customer’s card on file).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_invoice(body, request_options=request_options).unwrap()

    def create_invoice_attachment(
        self,
        invoice_id: str,
        *,
        request: CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInvoiceAttachmentResponse:
        """Uploads a file and attaches it to an invoice. This endpoint accepts HTTP multipart/form-data file uploads
        with a JSON ``request`` part and a ``file`` part. The ``file`` part must be a ``readable stream`` that contains
        a file in a supported format: GIF, JPEG, PNG, TIFF, BMP, or PDF.

        Invoices can have up to 10 attachments with a total file size of 25 MB. Attachments can be added only to
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        __NOTE:__ When testing in the Sandbox environment, the total file size is limited to 1 KB.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to attach the file to.
            request: Represents a `CreateInvoiceAttachment <api-endpoint:Invoices-CreateInvoiceAttachment>`__ request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_invoice_attachment(
            invoice_id, request=request, image_file=image_file, request_options=request_options
        ).unwrap()

    def delete_invoice(
        self, invoice_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteInvoiceResponse:
        """Deletes the specified invoice. When an invoice is deleted, the associated order status changes to CANCELED.
        You can only delete a draft invoice (you cannot delete a published invoice, including one that is scheduled for
        processing).

        Args:
            invoice_id: The ID of the invoice to delete.
            version: The version of the `invoice <entity:Invoice>`__ to delete. If you do not know the version, you can
                call `GetInvoice <api-endpoint:Invoices-GetInvoice>`__ or `ListInvoices
                <api-endpoint:Invoices-ListInvoices>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_invoice(
            invoice_id, version=version, request_options=request_options
        ).unwrap()

    def delete_invoice_attachment(
        self, invoice_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteInvoiceAttachmentResponse:
        """Removes an attachment from an invoice and permanently deletes the file. Attachments can be removed only from
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to delete the attachment from.
            attachment_id: The ID of the `attachment <entity:InvoiceAttachment>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_invoice_attachment(
            invoice_id, attachment_id, request_options=request_options
        ).unwrap()

    def get_invoice(
        self, invoice_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetInvoiceResponse:
        """Retrieves an invoice by invoice ID.

        Args:
            invoice_id: The ID of the invoice to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_invoice(invoice_id, request_options=request_options).unwrap()

    def list_invoices(
        self,
        location_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInvoicesResponse:
        """Returns a list of invoices for a given location. The response is paginated. If truncated, the response
        includes a ``cursor`` that you use in a subsequent request to retrieve the next set of invoices.

        Args:
            location_id: The ID of the location for which to list invoices.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of invoices to return (200 is the maximum ``limit``). If not provided, the server
                uses a default limit of 100 invoices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_invoices(
            location_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def publish_invoice(
        self,
        invoice_id: str,
        body: PublishInvoiceRequest | PublishInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublishInvoiceResponse:
        """Publishes the specified draft invoice.

        After an invoice is published, Square follows up based on the invoice configuration. For example, Square sends
        the invoice to the customer's email address, charges the customer's card on file, or does nothing. Square also
        makes the invoice available on a Square-hosted invoice page.

        The invoice ``status`` also changes from ``DRAFT`` to a status based on the invoice configuration. For example,
        the status changes to ``UNPAID`` if Square emails the invoice or ``PARTIALLY_PAID`` if Square charges a card on
        file for a portion of the invoice amount.

        In addition to the required ``ORDERS_WRITE`` and ``INVOICES_WRITE`` permissions, ``CUSTOMERS_READ`` and
        ``PAYMENTS_WRITE`` are required when publishing invoices configured for card-on-file payments.

        Args:
            invoice_id: The ID of the invoice to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.publish_invoice(invoice_id, body, request_options=request_options).unwrap()

    def search_invoices(
        self,
        body: SearchInvoicesRequest | SearchInvoicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchInvoicesResponse:
        """Searches for invoices from a location specified in the filter. You can optionally specify customers in the
        filter for whom to retrieve invoices. In the current implementation, you can only specify one location and
        optionally one customer.

        The response is paginated. If truncated, the response includes a ``cursor`` that you use in a subsequent request
        to retrieve the next set of invoices.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_invoices(body, request_options=request_options).unwrap()

    def update_invoice(
        self,
        invoice_id: str,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInvoiceResponse:
        """Updates an invoice. This endpoint supports sparse updates, so you only need to specify the fields you want to
        change along with the required ``version`` field. Some restrictions apply to updating invoices. For example, you
        cannot change the ``order_id`` or ``location_id`` field.

        Args:
            invoice_id: The ID of the invoice to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_invoice(invoice_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> InvoicesWithRawResponse:
        return self._with_raw_response


class AsyncInvoices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncInvoicesWithRawResponse(client, server, auth)

    async def cancel_invoice(
        self,
        invoice_id: str,
        body: CancelInvoiceRequest | CancelInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelInvoiceResponse:
        """Cancels an invoice. The seller cannot collect payments for the canceled invoice.

        You cannot cancel an invoice in the ``DRAFT`` state or in a terminal state: ``PAID``, ``REFUNDED``,
        ``CANCELED``, or ``FAILED``.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to cancel.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_invoice(invoice_id, body, request_options=request_options)
        ).unwrap()

    async def create_invoice(
        self,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInvoiceResponse:
        """Creates a draft `invoice <entity:Invoice>`__ for an order created using the Orders API.

        A draft invoice remains in your account and no action is taken. You must publish the invoice before Square can
        process it (send it to the customer's email address or charge the customer’s card on file).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_invoice(body, request_options=request_options)).unwrap()

    async def create_invoice_attachment(
        self,
        invoice_id: str,
        *,
        request: CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateInvoiceAttachmentResponse:
        """Uploads a file and attaches it to an invoice. This endpoint accepts HTTP multipart/form-data file uploads
        with a JSON ``request`` part and a ``file`` part. The ``file`` part must be a ``readable stream`` that contains
        a file in a supported format: GIF, JPEG, PNG, TIFF, BMP, or PDF.

        Invoices can have up to 10 attachments with a total file size of 25 MB. Attachments can be added only to
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        __NOTE:__ When testing in the Sandbox environment, the total file size is limited to 1 KB.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to attach the file to.
            request: Represents a `CreateInvoiceAttachment <api-endpoint:Invoices-CreateInvoiceAttachment>`__ request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_invoice_attachment(
                invoice_id, request=request, image_file=image_file, request_options=request_options
            )
        ).unwrap()

    async def delete_invoice(
        self, invoice_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteInvoiceResponse:
        """Deletes the specified invoice. When an invoice is deleted, the associated order status changes to CANCELED.
        You can only delete a draft invoice (you cannot delete a published invoice, including one that is scheduled for
        processing).

        Args:
            invoice_id: The ID of the invoice to delete.
            version: The version of the `invoice <entity:Invoice>`__ to delete. If you do not know the version, you can
                call `GetInvoice <api-endpoint:Invoices-GetInvoice>`__ or `ListInvoices
                <api-endpoint:Invoices-ListInvoices>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_invoice(invoice_id, version=version, request_options=request_options)
        ).unwrap()

    async def delete_invoice_attachment(
        self, invoice_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteInvoiceAttachmentResponse:
        """Removes an attachment from an invoice and permanently deletes the file. Attachments can be removed only from
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to delete the attachment from.
            attachment_id: The ID of the `attachment <entity:InvoiceAttachment>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_invoice_attachment(
                invoice_id, attachment_id, request_options=request_options
            )
        ).unwrap()

    async def get_invoice(
        self, invoice_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetInvoiceResponse:
        """Retrieves an invoice by invoice ID.

        Args:
            invoice_id: The ID of the invoice to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_invoice(invoice_id, request_options=request_options)).unwrap()

    async def list_invoices(
        self,
        location_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListInvoicesResponse:
        """Returns a list of invoices for a given location. The response is paginated. If truncated, the response
        includes a ``cursor`` that you use in a subsequent request to retrieve the next set of invoices.

        Args:
            location_id: The ID of the location for which to list invoices.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of invoices to return (200 is the maximum ``limit``). If not provided, the server
                uses a default limit of 100 invoices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_invoices(
                location_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def publish_invoice(
        self,
        invoice_id: str,
        body: PublishInvoiceRequest | PublishInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublishInvoiceResponse:
        """Publishes the specified draft invoice.

        After an invoice is published, Square follows up based on the invoice configuration. For example, Square sends
        the invoice to the customer's email address, charges the customer's card on file, or does nothing. Square also
        makes the invoice available on a Square-hosted invoice page.

        The invoice ``status`` also changes from ``DRAFT`` to a status based on the invoice configuration. For example,
        the status changes to ``UNPAID`` if Square emails the invoice or ``PARTIALLY_PAID`` if Square charges a card on
        file for a portion of the invoice amount.

        In addition to the required ``ORDERS_WRITE`` and ``INVOICES_WRITE`` permissions, ``CUSTOMERS_READ`` and
        ``PAYMENTS_WRITE`` are required when publishing invoices configured for card-on-file payments.

        Args:
            invoice_id: The ID of the invoice to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.publish_invoice(invoice_id, body, request_options=request_options)
        ).unwrap()

    async def search_invoices(
        self,
        body: SearchInvoicesRequest | SearchInvoicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchInvoicesResponse:
        """Searches for invoices from a location specified in the filter. You can optionally specify customers in the
        filter for whom to retrieve invoices. In the current implementation, you can only specify one location and
        optionally one customer.

        The response is paginated. If truncated, the response includes a ``cursor`` that you use in a subsequent request
        to retrieve the next set of invoices.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_invoices(body, request_options=request_options)).unwrap()

    async def update_invoice(
        self,
        invoice_id: str,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateInvoiceResponse:
        """Updates an invoice. This endpoint supports sparse updates, so you only need to specify the fields you want to
        change along with the required ``version`` field. Some restrictions apply to updating invoices. For example, you
        cannot change the ``order_id`` or ``location_id`` field.

        Args:
            invoice_id: The ID of the invoice to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_invoice(invoice_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncInvoicesWithRawResponse:
        return self._with_raw_response


class InvoicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def cancel_invoice(
        self,
        invoice_id: str,
        body: CancelInvoiceRequest | CancelInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInvoiceResponse, RawError]:
        """Cancels an invoice. The seller cannot collect payments for the canceled invoice.

        You cannot cancel an invoice in the ``DRAFT`` state or in a terminal state: ``PAID``, ``REFUNDED``,
        ``CANCELED``, or ``FAILED``.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to cancel.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/{invoice_id}/cancel"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=json_body[CancelInvoiceRequest | CancelInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_invoice(
        self,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInvoiceResponse, RawError]:
        """Creates a draft `invoice <entity:Invoice>`__ for an order created using the Orders API.

        A draft invoice remains in your account and no action is taken. You must publish the invoice before Square can
        process it (send it to the customer's email address or charge the customer’s card on file).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices"),
            body=json_body[CreateInvoiceRequest | CreateInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_invoice_attachment(
        self,
        invoice_id: str,
        *,
        request: CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInvoiceAttachmentResponse, RawError]:
        """Uploads a file and attaches it to an invoice. This endpoint accepts HTTP multipart/form-data file uploads
        with a JSON ``request`` part and a ``file`` part. The ``file`` part must be a ``readable stream`` that contains
        a file in a supported format: GIF, JPEG, PNG, TIFF, BMP, or PDF.

        Invoices can have up to 10 attachments with a total file size of 25 MB. Attachments can be added only to
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        __NOTE:__ When testing in the Sandbox environment, the total file size is limited to 1 KB.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to attach the file to.
            request: Represents a `CreateInvoiceAttachment <api-endpoint:Invoices-CreateInvoiceAttachment>`__ request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/{invoice_id}/attachments"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=multipart_body(
                [param[CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None]("request", request)],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateInvoiceAttachmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_invoice(
        self, invoice_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteInvoiceResponse, RawError]:
        """Deletes the specified invoice. When an invoice is deleted, the associated order status changes to CANCELED.
        You can only delete a draft invoice (you cannot delete a published invoice, including one that is scheduled for
        processing).

        Args:
            invoice_id: The ID of the invoice to delete.
            version: The version of the `invoice <entity:Invoice>`__ to delete. If you do not know the version, you can
                call `GetInvoice <api-endpoint:Invoices-GetInvoice>`__ or `ListInvoices
                <api-endpoint:Invoices-ListInvoices>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/invoices/{invoice_id}"),
            path_params=[param[str]("invoice_id", invoice_id)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_invoice_attachment(
        self, invoice_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteInvoiceAttachmentResponse, RawError]:
        """Removes an attachment from an invoice and permanently deletes the file. Attachments can be removed only from
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to delete the attachment from.
            attachment_id: The ID of the `attachment <entity:InvoiceAttachment>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/invoices/{invoice_id}/attachments/{attachment_id}"),
            path_params=[param[str]("invoice_id", invoice_id), param[str]("attachment_id", attachment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteInvoiceAttachmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_invoice(
        self, invoice_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetInvoiceResponse, RawError]:
        """Retrieves an invoice by invoice ID.

        Args:
            invoice_id: The ID of the invoice to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/invoices/{invoice_id}"),
            path_params=[param[str]("invoice_id", invoice_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_invoices(
        self,
        location_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInvoicesResponse, RawError]:
        """Returns a list of invoices for a given location. The response is paginated. If truncated, the response
        includes a ``cursor`` that you use in a subsequent request to retrieve the next set of invoices.

        Args:
            location_id: The ID of the location for which to list invoices.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of invoices to return (200 is the maximum ``limit``). If not provided, the server
                uses a default limit of 100 invoices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/invoices"),
            query_params=[
                param[str]("location_id", location_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def publish_invoice(
        self,
        invoice_id: str,
        body: PublishInvoiceRequest | PublishInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublishInvoiceResponse, RawError]:
        """Publishes the specified draft invoice.

        After an invoice is published, Square follows up based on the invoice configuration. For example, Square sends
        the invoice to the customer's email address, charges the customer's card on file, or does nothing. Square also
        makes the invoice available on a Square-hosted invoice page.

        The invoice ``status`` also changes from ``DRAFT`` to a status based on the invoice configuration. For example,
        the status changes to ``UNPAID`` if Square emails the invoice or ``PARTIALLY_PAID`` if Square charges a card on
        file for a portion of the invoice amount.

        In addition to the required ``ORDERS_WRITE`` and ``INVOICES_WRITE`` permissions, ``CUSTOMERS_READ`` and
        ``PAYMENTS_WRITE`` are required when publishing invoices configured for card-on-file payments.

        Args:
            invoice_id: The ID of the invoice to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/{invoice_id}/publish"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=json_body[PublishInvoiceRequest | PublishInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PublishInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_invoices(
        self,
        body: SearchInvoicesRequest | SearchInvoicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchInvoicesResponse, RawError]:
        """Searches for invoices from a location specified in the filter. You can optionally specify customers in the
        filter for whom to retrieve invoices. In the current implementation, you can only specify one location and
        optionally one customer.

        The response is paginated. If truncated, the response includes a ``cursor`` that you use in a subsequent request
        to retrieve the next set of invoices.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/search"),
            body=json_body[SearchInvoicesRequest | SearchInvoicesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_invoice(
        self,
        invoice_id: str,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInvoiceResponse, RawError]:
        """Updates an invoice. This endpoint supports sparse updates, so you only need to specify the fields you want to
        change along with the required ``version`` field. Some restrictions apply to updating invoices. For example, you
        cannot change the ``order_id`` or ``location_id`` field.

        Args:
            invoice_id: The ID of the invoice to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/invoices/{invoice_id}"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=json_body[UpdateInvoiceRequest | UpdateInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncInvoicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def cancel_invoice(
        self,
        invoice_id: str,
        body: CancelInvoiceRequest | CancelInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelInvoiceResponse, RawError]:
        """Cancels an invoice. The seller cannot collect payments for the canceled invoice.

        You cannot cancel an invoice in the ``DRAFT`` state or in a terminal state: ``PAID``, ``REFUNDED``,
        ``CANCELED``, or ``FAILED``.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to cancel.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/{invoice_id}/cancel"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=json_body[CancelInvoiceRequest | CancelInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_invoice(
        self,
        body: CreateInvoiceRequest | CreateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInvoiceResponse, RawError]:
        """Creates a draft `invoice <entity:Invoice>`__ for an order created using the Orders API.

        A draft invoice remains in your account and no action is taken. You must publish the invoice before Square can
        process it (send it to the customer's email address or charge the customer’s card on file).

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices"),
            body=json_body[CreateInvoiceRequest | CreateInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_invoice_attachment(
        self,
        invoice_id: str,
        *,
        request: CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateInvoiceAttachmentResponse, RawError]:
        """Uploads a file and attaches it to an invoice. This endpoint accepts HTTP multipart/form-data file uploads
        with a JSON ``request`` part and a ``file`` part. The ``file`` part must be a ``readable stream`` that contains
        a file in a supported format: GIF, JPEG, PNG, TIFF, BMP, or PDF.

        Invoices can have up to 10 attachments with a total file size of 25 MB. Attachments can be added only to
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        __NOTE:__ When testing in the Sandbox environment, the total file size is limited to 1 KB.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to attach the file to.
            request: Represents a `CreateInvoiceAttachment <api-endpoint:Invoices-CreateInvoiceAttachment>`__ request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/{invoice_id}/attachments"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=multipart_body(
                [param[CreateInvoiceAttachmentRequest | CreateInvoiceAttachmentRequestDict | None]("request", request)],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateInvoiceAttachmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_invoice(
        self, invoice_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteInvoiceResponse, RawError]:
        """Deletes the specified invoice. When an invoice is deleted, the associated order status changes to CANCELED.
        You can only delete a draft invoice (you cannot delete a published invoice, including one that is scheduled for
        processing).

        Args:
            invoice_id: The ID of the invoice to delete.
            version: The version of the `invoice <entity:Invoice>`__ to delete. If you do not know the version, you can
                call `GetInvoice <api-endpoint:Invoices-GetInvoice>`__ or `ListInvoices
                <api-endpoint:Invoices-ListInvoices>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/invoices/{invoice_id}"),
            path_params=[param[str]("invoice_id", invoice_id)],
            query_params=[param[int | None]("version", version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_invoice_attachment(
        self, invoice_id: str, attachment_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteInvoiceAttachmentResponse, RawError]:
        """Removes an attachment from an invoice and permanently deletes the file. Attachments can be removed only from
        invoices in the ``DRAFT``, ``SCHEDULED``, ``UNPAID``, or ``PARTIALLY_PAID`` state.

        Args:
            invoice_id: The ID of the `invoice <entity:Invoice>`__ to delete the attachment from.
            attachment_id: The ID of the `attachment <entity:InvoiceAttachment>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/invoices/{invoice_id}/attachments/{attachment_id}"),
            path_params=[param[str]("invoice_id", invoice_id), param[str]("attachment_id", attachment_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteInvoiceAttachmentResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_invoice(
        self, invoice_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetInvoiceResponse, RawError]:
        """Retrieves an invoice by invoice ID.

        Args:
            invoice_id: The ID of the invoice to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/invoices/{invoice_id}"),
            path_params=[param[str]("invoice_id", invoice_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_invoices(
        self,
        location_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListInvoicesResponse, RawError]:
        """Returns a list of invoices for a given location. The response is paginated. If truncated, the response
        includes a ``cursor`` that you use in a subsequent request to retrieve the next set of invoices.

        Args:
            location_id: The ID of the location for which to list invoices.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of invoices to return (200 is the maximum ``limit``). If not provided, the server
                uses a default limit of 100 invoices.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/invoices"),
            query_params=[
                param[str]("location_id", location_id),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def publish_invoice(
        self,
        invoice_id: str,
        body: PublishInvoiceRequest | PublishInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublishInvoiceResponse, RawError]:
        """Publishes the specified draft invoice.

        After an invoice is published, Square follows up based on the invoice configuration. For example, Square sends
        the invoice to the customer's email address, charges the customer's card on file, or does nothing. Square also
        makes the invoice available on a Square-hosted invoice page.

        The invoice ``status`` also changes from ``DRAFT`` to a status based on the invoice configuration. For example,
        the status changes to ``UNPAID`` if Square emails the invoice or ``PARTIALLY_PAID`` if Square charges a card on
        file for a portion of the invoice amount.

        In addition to the required ``ORDERS_WRITE`` and ``INVOICES_WRITE`` permissions, ``CUSTOMERS_READ`` and
        ``PAYMENTS_WRITE`` are required when publishing invoices configured for card-on-file payments.

        Args:
            invoice_id: The ID of the invoice to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/{invoice_id}/publish"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=json_body[PublishInvoiceRequest | PublishInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PublishInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_invoices(
        self,
        body: SearchInvoicesRequest | SearchInvoicesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchInvoicesResponse, RawError]:
        """Searches for invoices from a location specified in the filter. You can optionally specify customers in the
        filter for whom to retrieve invoices. In the current implementation, you can only specify one location and
        optionally one customer.

        The response is paginated. If truncated, the response includes a ``cursor`` that you use in a subsequent request
        to retrieve the next set of invoices.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/invoices/search"),
            body=json_body[SearchInvoicesRequest | SearchInvoicesRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchInvoicesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_invoice(
        self,
        invoice_id: str,
        body: UpdateInvoiceRequest | UpdateInvoiceRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateInvoiceResponse, RawError]:
        """Updates an invoice. This endpoint supports sparse updates, so you only need to specify the fields you want to
        change along with the required ``version`` field. Some restrictions apply to updating invoices. For example, you
        cannot change the ``order_id`` or ``location_id`` field.

        Args:
            invoice_id: The ID of the invoice to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/invoices/{invoice_id}"),
            path_params=[param[str]("invoice_id", invoice_id)],
            body=json_body[UpdateInvoiceRequest | UpdateInvoiceRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateInvoiceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
