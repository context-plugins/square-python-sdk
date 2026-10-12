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
from ..models.create_webhook_subscription_request import (
    CreateWebhookSubscriptionRequest,
    CreateWebhookSubscriptionRequestDict,
)
from ..models.create_webhook_subscription_response import CreateWebhookSubscriptionResponse
from ..models.delete_webhook_subscription_response import DeleteWebhookSubscriptionResponse
from ..models.enums.sort_order import SortOrderOrStr
from ..models.list_webhook_event_types_response import ListWebhookEventTypesResponse
from ..models.list_webhook_subscriptions_response import ListWebhookSubscriptionsResponse
from ..models.retrieve_webhook_subscription_response import RetrieveWebhookSubscriptionResponse
from ..models.test_webhook_subscription_request import (
    TestWebhookSubscriptionRequest,
    TestWebhookSubscriptionRequestDict,
)
from ..models.test_webhook_subscription_response import TestWebhookSubscriptionResponse
from ..models.update_webhook_subscription_request import (
    UpdateWebhookSubscriptionRequest,
    UpdateWebhookSubscriptionRequestDict,
)
from ..models.update_webhook_subscription_response import UpdateWebhookSubscriptionResponse
from ..models.update_webhook_subscription_signature_key_request import (
    UpdateWebhookSubscriptionSignatureKeyRequest,
    UpdateWebhookSubscriptionSignatureKeyRequestDict,
)
from ..models.update_webhook_subscription_signature_key_response import UpdateWebhookSubscriptionSignatureKeyResponse
from ..server.server import Server


class WebhookSubscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = WebhookSubscriptionsWithRawResponse(client, server, auth)

    def create_webhook_subscription(
        self,
        body: CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateWebhookSubscriptionResponse:
        """Creates a webhook subscription.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_webhook_subscription(body, request_options=request_options))

    def delete_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteWebhookSubscriptionResponse:
        """Deletes a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.delete_webhook_subscription(subscription_id, request_options=request_options)
        )

    def list_webhook_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListWebhookEventTypesResponse:
        """Lists all webhook event types that can be subscribed to.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_webhook_event_types(api_version=api_version, request_options=request_options)
        )

    def list_webhook_subscriptions(
        self,
        *,
        cursor: str | None = None,
        include_disabled: bool | None = False,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhookSubscriptionsResponse:
        """Lists all webhook subscriptions owned by your application.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            include_disabled: Includes disabled `Subscription <entity:WebhookSubscription>`__s. By default, all enabled
                `Subscription <entity:WebhookSubscription>`__s are returned.
            sort_order: Sorts the returned list by when the `Subscription <entity:WebhookSubscription>`__ was created
                with the specified order. This field defaults to ASC.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. Default: 100
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_webhook_subscriptions(
                cursor=cursor,
                include_disabled=include_disabled,
                sort_order=sort_order,
                limit=limit,
                request_options=request_options,
            ),
        )

    def retrieve_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveWebhookSubscriptionResponse:
        """Retrieves a webhook subscription identified by its ID.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.retrieve_webhook_subscription(subscription_id, request_options=request_options)
        )

    def test_webhook_subscription(
        self,
        subscription_id: str,
        body: TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestWebhookSubscriptionResponse:
        """Tests a webhook subscription by sending a test event to the notification URL.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to test.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.test_webhook_subscription(subscription_id, body, request_options=request_options)
        )

    def update_webhook_subscription(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWebhookSubscriptionResponse:
        """Updates a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_webhook_subscription(subscription_id, body, request_options=request_options)
        )

    def update_webhook_subscription_signature_key(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWebhookSubscriptionSignatureKeyResponse:
        """Updates a webhook subscription by replacing the existing signature key with a new one.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.update_webhook_subscription_signature_key(
                subscription_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> WebhookSubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncWebhookSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncWebhookSubscriptionsWithRawResponse(client, server, auth)

    async def create_webhook_subscription(
        self,
        body: CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateWebhookSubscriptionResponse:
        """Creates a webhook subscription.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_webhook_subscription(body, request_options=request_options))

    async def delete_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteWebhookSubscriptionResponse:
        """Deletes a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.delete_webhook_subscription(subscription_id, request_options=request_options)
        )

    async def list_webhook_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListWebhookEventTypesResponse:
        """Lists all webhook event types that can be subscribed to.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_webhook_event_types(
                api_version=api_version, request_options=request_options
            ),
        )

    async def list_webhook_subscriptions(
        self,
        *,
        cursor: str | None = None,
        include_disabled: bool | None = False,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWebhookSubscriptionsResponse:
        """Lists all webhook subscriptions owned by your application.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            include_disabled: Includes disabled `Subscription <entity:WebhookSubscription>`__s. By default, all enabled
                `Subscription <entity:WebhookSubscription>`__s are returned.
            sort_order: Sorts the returned list by when the `Subscription <entity:WebhookSubscription>`__ was created
                with the specified order. This field defaults to ASC.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. Default: 100
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_webhook_subscriptions(
                cursor=cursor,
                include_disabled=include_disabled,
                sort_order=sort_order,
                limit=limit,
                request_options=request_options,
            ),
        )

    async def retrieve_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveWebhookSubscriptionResponse:
        """Retrieves a webhook subscription identified by its ID.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_webhook_subscription(
                subscription_id, request_options=request_options
            ),
        )

    async def test_webhook_subscription(
        self,
        subscription_id: str,
        body: TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> TestWebhookSubscriptionResponse:
        """Tests a webhook subscription by sending a test event to the notification URL.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to test.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.test_webhook_subscription(
                subscription_id, body, request_options=request_options
            ),
        )

    async def update_webhook_subscription(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWebhookSubscriptionResponse:
        """Updates a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_webhook_subscription(
                subscription_id, body, request_options=request_options
            ),
        )

    async def update_webhook_subscription_signature_key(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWebhookSubscriptionSignatureKeyResponse:
        """Updates a webhook subscription by replacing the existing signature key with a new one.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.update_webhook_subscription_signature_key(
                subscription_id, body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncWebhookSubscriptionsWithRawResponse:
        return self._with_raw_response


class WebhookSubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def create_webhook_subscription(
        self,
        body: CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateWebhookSubscriptionResponse, RawError]:
        """Creates a webhook subscription.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/webhooks/subscriptions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteWebhookSubscriptionResponse, RawError]:
        """Deletes a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_webhook_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListWebhookEventTypesResponse, RawError]:
        """Lists all webhook event types that can be subscribed to.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/webhooks/event-types"),
            query_params=[param[str | None]("api_version", api_version)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListWebhookEventTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_webhook_subscriptions(
        self,
        *,
        cursor: str | None = None,
        include_disabled: bool | None = False,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhookSubscriptionsResponse, RawError]:
        """Lists all webhook subscriptions owned by your application.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            include_disabled: Includes disabled `Subscription <entity:WebhookSubscription>`__s. By default, all enabled
                `Subscription <entity:WebhookSubscription>`__s are returned.
            sort_order: Sorts the returned list by when the `Subscription <entity:WebhookSubscription>`__ was created
                with the specified order. This field defaults to ASC.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. Default: 100
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/webhooks/subscriptions"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[bool | None]("include_disabled", include_disabled),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListWebhookSubscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveWebhookSubscriptionResponse, RawError]:
        """Retrieves a webhook subscription identified by its ID.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def test_webhook_subscription(
        self,
        subscription_id: str,
        body: TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestWebhookSubscriptionResponse, RawError]:
        """Tests a webhook subscription by sending a test event to the notification URL.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to test.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}/test"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[TestWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_webhook_subscription(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWebhookSubscriptionResponse, RawError]:
        """Updates a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_webhook_subscription_signature_key(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWebhookSubscriptionSignatureKeyResponse, RawError]:
        """Updates a webhook subscription by replacing the existing signature key with a new one.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}/signature-key"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateWebhookSubscriptionSignatureKeyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncWebhookSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def create_webhook_subscription(
        self,
        body: CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateWebhookSubscriptionResponse, RawError]:
        """Creates a webhook subscription.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/webhooks/subscriptions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateWebhookSubscriptionRequest | CreateWebhookSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteWebhookSubscriptionResponse, RawError]:
        """Deletes a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[DeleteWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_webhook_event_types(
        self, *, api_version: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListWebhookEventTypesResponse, RawError]:
        """Lists all webhook event types that can be subscribed to.

        Args:
            api_version: The API version for which to list event types. Setting this field overrides the default version
                used by the application.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/webhooks/event-types"),
            query_params=[param[str | None]("api_version", api_version)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListWebhookEventTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_webhook_subscriptions(
        self,
        *,
        cursor: str | None = None,
        include_disabled: bool | None = False,
        sort_order: SortOrderOrStr | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWebhookSubscriptionsResponse, RawError]:
        """Lists all webhook subscriptions owned by your application.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next
                set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            include_disabled: Includes disabled `Subscription <entity:WebhookSubscription>`__s. By default, all enabled
                `Subscription <entity:WebhookSubscription>`__s are returned.
            sort_order: Sorts the returned list by when the `Subscription <entity:WebhookSubscription>`__ was created
                with the specified order. This field defaults to ASC.
            limit: The maximum number of results to be returned in a single page. It is possible to receive fewer
                results than the specified limit on a given page. The default value of 100 is also the maximum allowed
                value. Default: 100
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/webhooks/subscriptions"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[bool | None]("include_disabled", include_disabled),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListWebhookSubscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_webhook_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveWebhookSubscriptionResponse, RawError]:
        """Retrieves a webhook subscription identified by its ID.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def test_webhook_subscription(
        self,
        subscription_id: str,
        body: TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[TestWebhookSubscriptionResponse, RawError]:
        """Tests a webhook subscription by sending a test event to the notification URL.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to test.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}/test"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TestWebhookSubscriptionRequest | TestWebhookSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[TestWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_webhook_subscription(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWebhookSubscriptionResponse, RawError]:
        """Updates a webhook subscription.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateWebhookSubscriptionRequest | UpdateWebhookSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateWebhookSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_webhook_subscription_signature_key(
        self,
        subscription_id: str,
        body: UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWebhookSubscriptionSignatureKeyResponse, RawError]:
        """Updates a webhook subscription by replacing the existing signature key with a new one.

        Args:
            subscription_id: [REQUIRED] The ID of the `Subscription <entity:WebhookSubscription>`__ to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/webhooks/subscriptions/{subscription_id}/signature-key"),
            path_params=[param[str]("subscription_id", subscription_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                UpdateWebhookSubscriptionSignatureKeyRequest | UpdateWebhookSubscriptionSignatureKeyRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[UpdateWebhookSubscriptionSignatureKeyResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
