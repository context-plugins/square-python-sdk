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
from ..models.create_checkout_request import CreateCheckoutRequest, CreateCheckoutRequestDict
from ..models.create_checkout_response import CreateCheckoutResponse
from ..models.create_payment_link_request import CreatePaymentLinkRequest, CreatePaymentLinkRequestDict
from ..models.create_payment_link_response import CreatePaymentLinkResponse
from ..models.delete_payment_link_response import DeletePaymentLinkResponse
from ..models.list_payment_links_response import ListPaymentLinksResponse
from ..models.retrieve_location_settings_response import RetrieveLocationSettingsResponse
from ..models.retrieve_merchant_settings_response import RetrieveMerchantSettingsResponse
from ..models.retrieve_payment_link_response import RetrievePaymentLinkResponse
from ..models.update_location_settings_request import UpdateLocationSettingsRequest, UpdateLocationSettingsRequestDict
from ..models.update_location_settings_response import UpdateLocationSettingsResponse
from ..models.update_merchant_settings_request import UpdateMerchantSettingsRequest, UpdateMerchantSettingsRequestDict
from ..models.update_merchant_settings_response import UpdateMerchantSettingsResponse
from ..models.update_payment_link_request import UpdatePaymentLinkRequest, UpdatePaymentLinkRequestDict
from ..models.update_payment_link_response import UpdatePaymentLinkResponse
from ..server.server import Server


class CheckoutApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CheckoutApiWithRawResponse(client, server, auth)

    def create_checkout(
        self,
        location_id: str,
        body: CreateCheckoutRequest | CreateCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCheckoutResponse:
        """Links a ``checkoutId`` to a ``checkout_page_url`` that customers are directed to in order to provide their
        payment information using a payment processing workflow hosted on connect.squareup.com.

        NOTE: The Checkout API has been updated with new features. For more information, see `Checkout API highlights
        <https://developer.squareup.com/docs/checkout-api#checkout-api-highlights>`__.

        Args:
            location_id: The ID of the business location to associate the checkout with.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_checkout(location_id, body, request_options=request_options))

    def create_payment_link(
        self,
        body: CreatePaymentLinkRequest | CreatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePaymentLinkResponse:
        """Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to
        pay for goods and services.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_payment_link(body, request_options=request_options))

    def delete_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeletePaymentLinkResponse:
        """Deletes a payment link.

        Args:
            id_: The ID of the payment link to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_payment_link(id_, request_options=request_options))

    def list_payment_links(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPaymentLinksResponse:
        """Lists all payment links.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: A limit on the number of results to return per page. The limit is advisory and the implementation
                might return more or less results. If the supplied limit is negative, zero, or greater than the maximum
                limit of 1000, it is ignored. Default value: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_payment_links(cursor=cursor, limit=limit, request_options=request_options)
        )

    def retrieve_location_settings(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationSettingsResponse:
        """Retrieves the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_location_settings(location_id, request_options=request_options))

    def retrieve_merchant_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveMerchantSettingsResponse:
        """Retrieves the merchant-level settings for a Square-hosted checkout page.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_merchant_settings(request_options=request_options))

    def retrieve_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrievePaymentLinkResponse:
        """Retrieves a payment link.

        Args:
            id_: The ID of link to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_payment_link(id_, request_options=request_options))

    def update_location_settings(
        self,
        location_id: str,
        body: UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateLocationSettingsResponse:
        """Updates the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_location_settings(location_id, body, request_options=request_options)
        )

    def update_merchant_settings(
        self,
        body: UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateMerchantSettingsResponse:
        """Updates the merchant-level settings for a Square-hosted checkout page.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.update_merchant_settings(body, request_options=request_options))

    def update_payment_link(
        self,
        id_: str,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatePaymentLinkResponse:
        """Updates a payment link. You can update the ``payment_link`` fields such as ``description``,
        ``checkout_options``, and ``pre_populated_data``. You cannot update other fields such as the ``order_id``,
        ``version``, ``URL``, or ``timestamp`` field.

        Args:
            id_: The ID of the payment link to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.update_payment_link(id_, body, request_options=request_options))

    @property
    def with_raw_response(self) -> CheckoutApiWithRawResponse:
        return self._with_raw_response


class AsyncCheckoutApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCheckoutApiWithRawResponse(client, server, auth)

    async def create_checkout(
        self,
        location_id: str,
        body: CreateCheckoutRequest | CreateCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCheckoutResponse:
        """Links a ``checkoutId`` to a ``checkout_page_url`` that customers are directed to in order to provide their
        payment information using a payment processing workflow hosted on connect.squareup.com.

        NOTE: The Checkout API has been updated with new features. For more information, see `Checkout API highlights
        <https://developer.squareup.com/docs/checkout-api#checkout-api-highlights>`__.

        Args:
            location_id: The ID of the business location to associate the checkout with.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_checkout(location_id, body, request_options=request_options))

    async def create_payment_link(
        self,
        body: CreatePaymentLinkRequest | CreatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreatePaymentLinkResponse:
        """Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to
        pay for goods and services.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_payment_link(body, request_options=request_options))

    async def delete_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeletePaymentLinkResponse:
        """Deletes a payment link.

        Args:
            id_: The ID of the payment link to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.delete_payment_link(id_, request_options=request_options))

    async def list_payment_links(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListPaymentLinksResponse:
        """Lists all payment links.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: A limit on the number of results to return per page. The limit is advisory and the implementation
                might return more or less results. If the supplied limit is negative, zero, or greater than the maximum
                limit of 1000, it is ignored. Default value: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_payment_links(
                cursor=cursor, limit=limit, request_options=request_options
            ),
        )

    async def retrieve_location_settings(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationSettingsResponse:
        """Retrieves the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_location_settings(location_id, request_options=request_options)
        )

    async def retrieve_merchant_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveMerchantSettingsResponse:
        """Retrieves the merchant-level settings for a Square-hosted checkout page.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_merchant_settings(request_options=request_options))

    async def retrieve_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrievePaymentLinkResponse:
        """Retrieves a payment link.

        Args:
            id_: The ID of link to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_payment_link(id_, request_options=request_options))

    async def update_location_settings(
        self,
        location_id: str,
        body: UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateLocationSettingsResponse:
        """Updates the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_location_settings(location_id, body, request_options=request_options)
        )

    async def update_merchant_settings(
        self,
        body: UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateMerchantSettingsResponse:
        """Updates the merchant-level settings for a Square-hosted checkout page.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.update_merchant_settings(body, request_options=request_options))

    async def update_payment_link(
        self,
        id_: str,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatePaymentLinkResponse:
        """Updates a payment link. You can update the ``payment_link`` fields such as ``description``,
        ``checkout_options``, and ``pre_populated_data``. You cannot update other fields such as the ``order_id``,
        ``version``, ``URL``, or ``timestamp`` field.

        Args:
            id_: The ID of the payment link to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.update_payment_link(id_, body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncCheckoutApiWithRawResponse:
        return self._with_raw_response


class CheckoutApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_checkout(
        self,
        location_id: str,
        body: CreateCheckoutRequest | CreateCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCheckoutResponse, RawError]:
        """Links a ``checkoutId`` to a ``checkout_page_url`` that customers are directed to in order to provide their
        payment information using a payment processing workflow hosted on connect.squareup.com.

        NOTE: The Checkout API has been updated with new features. For more information, see `Checkout API highlights
        <https://developer.squareup.com/docs/checkout-api#checkout-api-highlights>`__.

        Args:
            location_id: The ID of the business location to associate the checkout with.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/checkouts"),
            path_params=[param[str]("location_id", location_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCheckoutRequest | CreateCheckoutRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_payment_link(
        self,
        body: CreatePaymentLinkRequest | CreatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePaymentLinkResponse, RawError]:
        """Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to
        pay for goods and services.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/online-checkout/payment-links"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePaymentLinkRequest | CreatePaymentLinkRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreatePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeletePaymentLinkResponse, RawError]:
        """Deletes a payment link.

        Args:
            id_: The ID of the payment link to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/online-checkout/payment-links/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeletePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_payment_links(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPaymentLinksResponse, RawError]:
        """Lists all payment links.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: A limit on the number of results to return per page. The limit is advisory and the implementation
                might return more or less results. If the supplied limit is negative, zero, or greater than the maximum
                limit of 1000, it is ignored. Default value: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/payment-links"),
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListPaymentLinksResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_location_settings(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationSettingsResponse, RawError]:
        """Retrieves the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/location-settings/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLocationSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_merchant_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveMerchantSettingsResponse, RawError]:
        """Retrieves the merchant-level settings for a Square-hosted checkout page.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/merchant-settings"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveMerchantSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrievePaymentLinkResponse, RawError]:
        """Retrieves a payment link.

        Args:
            id_: The ID of link to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/payment-links/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrievePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_location_settings(
        self,
        location_id: str,
        body: UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateLocationSettingsResponse, RawError]:
        """Updates the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/online-checkout/location-settings/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateLocationSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_merchant_settings(
        self,
        body: UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateMerchantSettingsResponse, RawError]:
        """Updates the merchant-level settings for a Square-hosted checkout page.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/online-checkout/merchant-settings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateMerchantSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_payment_link(
        self,
        id_: str,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatePaymentLinkResponse, RawError]:
        """Updates a payment link. You can update the ``payment_link`` fields such as ``description``,
        ``checkout_options``, and ``pre_populated_data``. You cannot update other fields such as the ``order_id``,
        ``version``, ``URL``, or ``timestamp`` field.

        Args:
            id_: The ID of the payment link to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/online-checkout/payment-links/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdatePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCheckoutApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_checkout(
        self,
        location_id: str,
        body: CreateCheckoutRequest | CreateCheckoutRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCheckoutResponse, RawError]:
        """Links a ``checkoutId`` to a ``checkout_page_url`` that customers are directed to in order to provide their
        payment information using a payment processing workflow hosted on connect.squareup.com.

        NOTE: The Checkout API has been updated with new features. For more information, see `Checkout API highlights
        <https://developer.squareup.com/docs/checkout-api#checkout-api-highlights>`__.

        Args:
            location_id: The ID of the business location to associate the checkout with.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/locations/{location_id}/checkouts"),
            path_params=[param[str]("location_id", location_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCheckoutRequest | CreateCheckoutRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateCheckoutResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_payment_link(
        self,
        body: CreatePaymentLinkRequest | CreatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreatePaymentLinkResponse, RawError]:
        """Creates a Square-hosted checkout page. Applications can share the resulting payment link with their buyer to
        pay for goods and services.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/online-checkout/payment-links"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreatePaymentLinkRequest | CreatePaymentLinkRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreatePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeletePaymentLinkResponse, RawError]:
        """Deletes a payment link.

        Args:
            id_: The ID of the payment link to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/online-checkout/payment-links/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[DeletePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_payment_links(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListPaymentLinksResponse, RawError]:
        """Lists all payment links.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. If a cursor is not provided, the endpoint returns the
                first page of the results. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: A limit on the number of results to return per page. The limit is advisory and the implementation
                might return more or less results. If the supplied limit is negative, zero, or greater than the maximum
                limit of 1000, it is ignored. Default value: ``100``
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/payment-links"),
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListPaymentLinksResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_location_settings(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationSettingsResponse, RawError]:
        """Retrieves the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/location-settings/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLocationSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_merchant_settings(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveMerchantSettingsResponse, RawError]:
        """Retrieves the merchant-level settings for a Square-hosted checkout page.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/merchant-settings"),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveMerchantSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_payment_link(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrievePaymentLinkResponse, RawError]:
        """Retrieves a payment link.

        Args:
            id_: The ID of link to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/online-checkout/payment-links/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrievePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_location_settings(
        self,
        location_id: str,
        body: UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateLocationSettingsResponse, RawError]:
        """Updates the location-level settings for a Square-hosted checkout page.

        Args:
            location_id: The ID of the location for which to retrieve settings.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/online-checkout/location-settings/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateLocationSettingsRequest | UpdateLocationSettingsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateLocationSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_merchant_settings(
        self,
        body: UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateMerchantSettingsResponse, RawError]:
        """Updates the merchant-level settings for a Square-hosted checkout page.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/online-checkout/merchant-settings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateMerchantSettingsRequest | UpdateMerchantSettingsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateMerchantSettingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_payment_link(
        self,
        id_: str,
        body: UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatePaymentLinkResponse, RawError]:
        """Updates a payment link. You can update the ``payment_link`` fields such as ``description``,
        ``checkout_options``, and ``pre_populated_data``. You cannot update other fields such as the ``order_id``,
        ``version``, ``URL``, or ``timestamp`` field.

        Args:
            id_: The ID of the payment link to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/online-checkout/payment-links/{id}"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdatePaymentLinkRequest | UpdatePaymentLinkRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdatePaymentLinkResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
