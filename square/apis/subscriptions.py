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
    param,
    raw_error_response,
)
from ..models.bulk_swap_plan_request import BulkSwapPlanRequest, BulkSwapPlanRequestDict
from ..models.bulk_swap_plan_response import BulkSwapPlanResponse
from ..models.cancel_subscription_response import CancelSubscriptionResponse
from ..models.change_billing_anchor_date_request import (
    ChangeBillingAnchorDateRequest,
    ChangeBillingAnchorDateRequestDict,
)
from ..models.change_billing_anchor_date_response import ChangeBillingAnchorDateResponse
from ..models.create_subscription_request import CreateSubscriptionRequest, CreateSubscriptionRequestDict
from ..models.create_subscription_response import CreateSubscriptionResponse
from ..models.delete_subscription_action_response import DeleteSubscriptionActionResponse
from ..models.list_subscription_events_response import ListSubscriptionEventsResponse
from ..models.pause_subscription_request import PauseSubscriptionRequest, PauseSubscriptionRequestDict
from ..models.pause_subscription_response import PauseSubscriptionResponse
from ..models.resume_subscription_request import ResumeSubscriptionRequest, ResumeSubscriptionRequestDict
from ..models.resume_subscription_response import ResumeSubscriptionResponse
from ..models.retrieve_subscription_response import RetrieveSubscriptionResponse
from ..models.search_subscriptions_request import SearchSubscriptionsRequest, SearchSubscriptionsRequestDict
from ..models.search_subscriptions_response import SearchSubscriptionsResponse
from ..models.swap_plan_request import SwapPlanRequest, SwapPlanRequestDict
from ..models.swap_plan_response import SwapPlanResponse
from ..models.update_subscription_request import UpdateSubscriptionRequest, UpdateSubscriptionRequestDict
from ..models.update_subscription_response import UpdateSubscriptionResponse
from ..server.server import Server


class Subscriptions:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = SubscriptionsWithRawResponse(client, server, auth)

    def bulk_swap_plan(
        self,
        body: BulkSwapPlanRequest | BulkSwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSwapPlanResponse:
        """Schedules a plan variation change for all active subscriptions under a given plan variation. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_swap_plan(body, request_options=request_options).unwrap()

    def cancel_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelSubscriptionResponse:
        """Schedules a ``CANCEL`` action to cancel an active subscription. This sets the ``canceled_date`` field to the
        end of the active billing period. After this date, the subscription status changes from ACTIVE to CANCELED.

        Args:
            subscription_id: The ID of the subscription to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_subscription(subscription_id, request_options=request_options).unwrap()

    def change_billing_anchor_date(
        self,
        subscription_id: str,
        body: ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangeBillingAnchorDateResponse:
        """Changes the `billing anchor date
        <https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates>`__ for a
        subscription.

        Args:
            subscription_id: The ID of the subscription to update the billing anchor date.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.change_billing_anchor_date(
            subscription_id, body, request_options=request_options
        ).unwrap()

    def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateSubscriptionResponse:
        """Enrolls a customer in a subscription.

        If you provide a card on file in the request, Square charges the card for the subscription. Otherwise, Square
        sends an invoice to the customer's email address. The subscription starts immediately, unless the request
        includes the optional ``start_date``. Each individual subscription is associated with a particular location.

        For more information, see `Create a subscription
        <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_subscription(body, request_options=request_options).unwrap()

    def delete_subscription_action(
        self, subscription_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteSubscriptionActionResponse:
        """Deletes a scheduled action for a subscription.

        Args:
            subscription_id: The ID of the subscription the targeted action is to act upon.
            action_id: The ID of the targeted action to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_subscription_action(
            subscription_id, action_id, request_options=request_options
        ).unwrap()

    def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionEventsResponse:
        """Lists all `events <https://developer.squareup.com/docs/subscriptions-api/actions-events>`__ for a specific
        subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve the events for.
            cursor: When the total number of resulting subscription events exceeds the limit of a paged response,
                specify the cursor returned from a preceding response here to fetch the next set of results. If the
                cursor is unset, the response contains the last page of the results. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The upper limit on the number of subscription events to return in a paged response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_subscription_events(
            subscription_id, cursor=cursor, limit=limit, request_options=request_options
        ).unwrap()

    def pause_subscription(
        self,
        subscription_id: str,
        body: PauseSubscriptionRequest | PauseSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PauseSubscriptionResponse:
        """Schedules a ``PAUSE`` action to pause an active subscription.

        Args:
            subscription_id: The ID of the subscription to pause.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.pause_subscription(
            subscription_id, body, request_options=request_options
        ).unwrap()

    def resume_subscription(
        self,
        subscription_id: str,
        body: ResumeSubscriptionRequest | ResumeSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResumeSubscriptionResponse:
        """Schedules a ``RESUME`` action to resume a paused or a deactivated subscription.

        Args:
            subscription_id: The ID of the subscription to resume.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.resume_subscription(
            subscription_id, body, request_options=request_options
        ).unwrap()

    def retrieve_subscription(
        self, subscription_id: str, *, include: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveSubscriptionResponse:
        """Retrieves a specific subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve.
            include: A query parameter to specify related information to be included in the response. The supported
                query parameter values are: - ``actions``: to include scheduled actions on the targeted subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_subscription(
            subscription_id, include=include, request_options=request_options
        ).unwrap()

    def search_subscriptions(
        self,
        body: SearchSubscriptionsRequest | SearchSubscriptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchSubscriptionsResponse:
        """Searches for subscriptions.

        Results are ordered chronologically by subscription creation date. If the request specifies more than one
        location ID, the endpoint orders the result by location ID, and then by creation date within each location. If
        no locations are given in the query, all locations are searched.

        You can also optionally specify ``customer_ids`` to search by customer. If left unset, all customers associated
        with the specified locations are returned. If the request specifies customer IDs, the endpoint orders results
        first by location, within location by customer ID, and within customer by subscription creation date.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_subscriptions(body, request_options=request_options).unwrap()

    def swap_plan(
        self,
        subscription_id: str,
        body: SwapPlanRequest | SwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SwapPlanResponse:
        """Schedules a ``SWAP_PLAN`` action to swap a subscription plan variation in an existing subscription. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            subscription_id: The ID of the subscription to swap the subscription plan for.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.swap_plan(subscription_id, body, request_options=request_options).unwrap()

    def update_subscription(
        self,
        subscription_id: str,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateSubscriptionResponse:
        """Updates a subscription by modifying or clearing ``subscription`` field values. To clear a field, set its
        value to ``null``.

        Args:
            subscription_id: The ID of the subscription to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_subscription(
            subscription_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> SubscriptionsWithRawResponse:
        return self._with_raw_response


class AsyncSubscriptions:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncSubscriptionsWithRawResponse(client, server, auth)

    async def bulk_swap_plan(
        self,
        body: BulkSwapPlanRequest | BulkSwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkSwapPlanResponse:
        """Schedules a plan variation change for all active subscriptions under a given plan variation. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_swap_plan(body, request_options=request_options)).unwrap()

    async def cancel_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelSubscriptionResponse:
        """Schedules a ``CANCEL`` action to cancel an active subscription. This sets the ``canceled_date`` field to the
        end of the active billing period. After this date, the subscription status changes from ACTIVE to CANCELED.

        Args:
            subscription_id: The ID of the subscription to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_subscription(subscription_id, request_options=request_options)
        ).unwrap()

    async def change_billing_anchor_date(
        self,
        subscription_id: str,
        body: ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ChangeBillingAnchorDateResponse:
        """Changes the `billing anchor date
        <https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates>`__ for a
        subscription.

        Args:
            subscription_id: The ID of the subscription to update the billing anchor date.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.change_billing_anchor_date(
                subscription_id, body, request_options=request_options
            )
        ).unwrap()

    async def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateSubscriptionResponse:
        """Enrolls a customer in a subscription.

        If you provide a card on file in the request, Square charges the card for the subscription. Otherwise, Square
        sends an invoice to the customer's email address. The subscription starts immediately, unless the request
        includes the optional ``start_date``. Each individual subscription is associated with a particular location.

        For more information, see `Create a subscription
        <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_subscription(body, request_options=request_options)).unwrap()

    async def delete_subscription_action(
        self, subscription_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteSubscriptionActionResponse:
        """Deletes a scheduled action for a subscription.

        Args:
            subscription_id: The ID of the subscription the targeted action is to act upon.
            action_id: The ID of the targeted action to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_subscription_action(
                subscription_id, action_id, request_options=request_options
            )
        ).unwrap()

    async def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListSubscriptionEventsResponse:
        """Lists all `events <https://developer.squareup.com/docs/subscriptions-api/actions-events>`__ for a specific
        subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve the events for.
            cursor: When the total number of resulting subscription events exceeds the limit of a paged response,
                specify the cursor returned from a preceding response here to fetch the next set of results. If the
                cursor is unset, the response contains the last page of the results. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The upper limit on the number of subscription events to return in a paged response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_subscription_events(
                subscription_id, cursor=cursor, limit=limit, request_options=request_options
            )
        ).unwrap()

    async def pause_subscription(
        self,
        subscription_id: str,
        body: PauseSubscriptionRequest | PauseSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PauseSubscriptionResponse:
        """Schedules a ``PAUSE`` action to pause an active subscription.

        Args:
            subscription_id: The ID of the subscription to pause.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.pause_subscription(subscription_id, body, request_options=request_options)
        ).unwrap()

    async def resume_subscription(
        self,
        subscription_id: str,
        body: ResumeSubscriptionRequest | ResumeSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ResumeSubscriptionResponse:
        """Schedules a ``RESUME`` action to resume a paused or a deactivated subscription.

        Args:
            subscription_id: The ID of the subscription to resume.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.resume_subscription(subscription_id, body, request_options=request_options)
        ).unwrap()

    async def retrieve_subscription(
        self, subscription_id: str, *, include: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveSubscriptionResponse:
        """Retrieves a specific subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve.
            include: A query parameter to specify related information to be included in the response. The supported
                query parameter values are: - ``actions``: to include scheduled actions on the targeted subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_subscription(
                subscription_id, include=include, request_options=request_options
            )
        ).unwrap()

    async def search_subscriptions(
        self,
        body: SearchSubscriptionsRequest | SearchSubscriptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchSubscriptionsResponse:
        """Searches for subscriptions.

        Results are ordered chronologically by subscription creation date. If the request specifies more than one
        location ID, the endpoint orders the result by location ID, and then by creation date within each location. If
        no locations are given in the query, all locations are searched.

        You can also optionally specify ``customer_ids`` to search by customer. If left unset, all customers associated
        with the specified locations are returned. If the request specifies customer IDs, the endpoint orders results
        first by location, within location by customer ID, and within customer by subscription creation date.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_subscriptions(body, request_options=request_options)).unwrap()

    async def swap_plan(
        self,
        subscription_id: str,
        body: SwapPlanRequest | SwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SwapPlanResponse:
        """Schedules a ``SWAP_PLAN`` action to swap a subscription plan variation in an existing subscription. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            subscription_id: The ID of the subscription to swap the subscription plan for.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.swap_plan(subscription_id, body, request_options=request_options)
        ).unwrap()

    async def update_subscription(
        self,
        subscription_id: str,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateSubscriptionResponse:
        """Updates a subscription by modifying or clearing ``subscription`` field values. To clear a field, set its
        value to ``null``.

        Args:
            subscription_id: The ID of the subscription to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_subscription(subscription_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncSubscriptionsWithRawResponse:
        return self._with_raw_response


class SubscriptionsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_swap_plan(
        self,
        body: BulkSwapPlanRequest | BulkSwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSwapPlanResponse, RawError]:
        """Schedules a plan variation change for all active subscriptions under a given plan variation. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/bulk-swap-plan"),
            body=json_body[BulkSwapPlanRequest | BulkSwapPlanRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkSwapPlanResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancel_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelSubscriptionResponse, RawError]:
        """Schedules a ``CANCEL`` action to cancel an active subscription. This sets the ``canceled_date`` field to the
        end of the active billing period. After this date, the subscription status changes from ACTIVE to CANCELED.

        Args:
            subscription_id: The ID of the subscription to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/cancel"),
            path_params=[param[str]("subscription_id", subscription_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def change_billing_anchor_date(
        self,
        subscription_id: str,
        body: ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangeBillingAnchorDateResponse, RawError]:
        """Changes the `billing anchor date
        <https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates>`__ for a
        subscription.

        Args:
            subscription_id: The ID of the subscription to update the billing anchor date.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/billing-anchor"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ChangeBillingAnchorDateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateSubscriptionResponse, RawError]:
        """Enrolls a customer in a subscription.

        If you provide a card on file in the request, Square charges the card for the subscription. Otherwise, Square
        sends an invoice to the customer's email address. The subscription starts immediately, unless the request
        includes the optional ``start_date``. Each individual subscription is associated with a particular location.

        For more information, see `Create a subscription
        <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions"),
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_subscription_action(
        self, subscription_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteSubscriptionActionResponse, RawError]:
        """Deletes a scheduled action for a subscription.

        Args:
            subscription_id: The ID of the subscription the targeted action is to act upon.
            action_id: The ID of the targeted action to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/actions/{action_id}"),
            path_params=[param[str]("subscription_id", subscription_id), param[str]("action_id", action_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteSubscriptionActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionEventsResponse, RawError]:
        """Lists all `events <https://developer.squareup.com/docs/subscriptions-api/actions-events>`__ for a specific
        subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve the events for.
            cursor: When the total number of resulting subscription events exceeds the limit of a paged response,
                specify the cursor returned from a preceding response here to fetch the next set of results. If the
                cursor is unset, the response contains the last page of the results. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The upper limit on the number of subscription events to return in a paged response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/events"),
            path_params=[param[str]("subscription_id", subscription_id)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListSubscriptionEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def pause_subscription(
        self,
        subscription_id: str,
        body: PauseSubscriptionRequest | PauseSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PauseSubscriptionResponse, RawError]:
        """Schedules a ``PAUSE`` action to pause an active subscription.

        Args:
            subscription_id: The ID of the subscription to pause.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/pause"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[PauseSubscriptionRequest | PauseSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PauseSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def resume_subscription(
        self,
        subscription_id: str,
        body: ResumeSubscriptionRequest | ResumeSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResumeSubscriptionResponse, RawError]:
        """Schedules a ``RESUME`` action to resume a paused or a deactivated subscription.

        Args:
            subscription_id: The ID of the subscription to resume.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/resume"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[ResumeSubscriptionRequest | ResumeSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ResumeSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_subscription(
        self, subscription_id: str, *, include: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveSubscriptionResponse, RawError]:
        """Retrieves a specific subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve.
            include: A query parameter to specify related information to be included in the response. The supported
                query parameter values are: - ``actions``: to include scheduled actions on the targeted subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            query_params=[param[str | None]("include", include)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_subscriptions(
        self,
        body: SearchSubscriptionsRequest | SearchSubscriptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchSubscriptionsResponse, RawError]:
        """Searches for subscriptions.

        Results are ordered chronologically by subscription creation date. If the request specifies more than one
        location ID, the endpoint orders the result by location ID, and then by creation date within each location. If
        no locations are given in the query, all locations are searched.

        You can also optionally specify ``customer_ids`` to search by customer. If left unset, all customers associated
        with the specified locations are returned. If the request specifies customer IDs, the endpoint orders results
        first by location, within location by customer ID, and within customer by subscription creation date.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/search"),
            body=json_body[SearchSubscriptionsRequest | SearchSubscriptionsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchSubscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def swap_plan(
        self,
        subscription_id: str,
        body: SwapPlanRequest | SwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SwapPlanResponse, RawError]:
        """Schedules a ``SWAP_PLAN`` action to swap a subscription plan variation in an existing subscription. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            subscription_id: The ID of the subscription to swap the subscription plan for.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/swap-plan"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[SwapPlanRequest | SwapPlanRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SwapPlanResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_subscription(
        self,
        subscription_id: str,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateSubscriptionResponse, RawError]:
        """Updates a subscription by modifying or clearing ``subscription`` field values. To clear a field, set its
        value to ``null``.

        Args:
            subscription_id: The ID of the subscription to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[UpdateSubscriptionRequest | UpdateSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncSubscriptionsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_swap_plan(
        self,
        body: BulkSwapPlanRequest | BulkSwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkSwapPlanResponse, RawError]:
        """Schedules a plan variation change for all active subscriptions under a given plan variation. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/bulk-swap-plan"),
            body=json_body[BulkSwapPlanRequest | BulkSwapPlanRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkSwapPlanResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancel_subscription(
        self, subscription_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelSubscriptionResponse, RawError]:
        """Schedules a ``CANCEL`` action to cancel an active subscription. This sets the ``canceled_date`` field to the
        end of the active billing period. After this date, the subscription status changes from ACTIVE to CANCELED.

        Args:
            subscription_id: The ID of the subscription to cancel.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/cancel"),
            path_params=[param[str]("subscription_id", subscription_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def change_billing_anchor_date(
        self,
        subscription_id: str,
        body: ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ChangeBillingAnchorDateResponse, RawError]:
        """Changes the `billing anchor date
        <https://developer.squareup.com/docs/subscriptions-api/subscription-billing#billing-dates>`__ for a
        subscription.

        Args:
            subscription_id: The ID of the subscription to update the billing anchor date.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/billing-anchor"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[ChangeBillingAnchorDateRequest | ChangeBillingAnchorDateRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ChangeBillingAnchorDateResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_subscription(
        self,
        body: CreateSubscriptionRequest | CreateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateSubscriptionResponse, RawError]:
        """Enrolls a customer in a subscription.

        If you provide a card on file in the request, Square charges the card for the subscription. Otherwise, Square
        sends an invoice to the customer's email address. The subscription starts immediately, unless the request
        includes the optional ``start_date``. Each individual subscription is associated with a particular location.

        For more information, see `Create a subscription
        <https://developer.squareup.com/docs/subscriptions-api/manage-subscriptions#create-a-subscription>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions"),
            body=json_body[CreateSubscriptionRequest | CreateSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_subscription_action(
        self, subscription_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteSubscriptionActionResponse, RawError]:
        """Deletes a scheduled action for a subscription.

        Args:
            subscription_id: The ID of the subscription the targeted action is to act upon.
            action_id: The ID of the targeted action to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/actions/{action_id}"),
            path_params=[param[str]("subscription_id", subscription_id), param[str]("action_id", action_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteSubscriptionActionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_subscription_events(
        self,
        subscription_id: str,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListSubscriptionEventsResponse, RawError]:
        """Lists all `events <https://developer.squareup.com/docs/subscriptions-api/actions-events>`__ for a specific
        subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve the events for.
            cursor: When the total number of resulting subscription events exceeds the limit of a paged response,
                specify the cursor returned from a preceding response here to fetch the next set of results. If the
                cursor is unset, the response contains the last page of the results. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The upper limit on the number of subscription events to return in a paged response.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/events"),
            path_params=[param[str]("subscription_id", subscription_id)],
            query_params=[param[str | None]("cursor", cursor), param[int | None]("limit", limit)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListSubscriptionEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def pause_subscription(
        self,
        subscription_id: str,
        body: PauseSubscriptionRequest | PauseSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PauseSubscriptionResponse, RawError]:
        """Schedules a ``PAUSE`` action to pause an active subscription.

        Args:
            subscription_id: The ID of the subscription to pause.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/pause"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[PauseSubscriptionRequest | PauseSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PauseSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def resume_subscription(
        self,
        subscription_id: str,
        body: ResumeSubscriptionRequest | ResumeSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ResumeSubscriptionResponse, RawError]:
        """Schedules a ``RESUME`` action to resume a paused or a deactivated subscription.

        Args:
            subscription_id: The ID of the subscription to resume.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/resume"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[ResumeSubscriptionRequest | ResumeSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ResumeSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_subscription(
        self, subscription_id: str, *, include: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveSubscriptionResponse, RawError]:
        """Retrieves a specific subscription.

        Args:
            subscription_id: The ID of the subscription to retrieve.
            include: A query parameter to specify related information to be included in the response. The supported
                query parameter values are: - ``actions``: to include scheduled actions on the targeted subscription.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            query_params=[param[str | None]("include", include)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_subscriptions(
        self,
        body: SearchSubscriptionsRequest | SearchSubscriptionsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchSubscriptionsResponse, RawError]:
        """Searches for subscriptions.

        Results are ordered chronologically by subscription creation date. If the request specifies more than one
        location ID, the endpoint orders the result by location ID, and then by creation date within each location. If
        no locations are given in the query, all locations are searched.

        You can also optionally specify ``customer_ids`` to search by customer. If left unset, all customers associated
        with the specified locations are returned. If the request specifies customer IDs, the endpoint orders results
        first by location, within location by customer ID, and within customer by subscription creation date.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/search"),
            body=json_body[SearchSubscriptionsRequest | SearchSubscriptionsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchSubscriptionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def swap_plan(
        self,
        subscription_id: str,
        body: SwapPlanRequest | SwapPlanRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SwapPlanResponse, RawError]:
        """Schedules a ``SWAP_PLAN`` action to swap a subscription plan variation in an existing subscription. For more
        information, see `Swap Subscription Plan Variations
        <https://developer.squareup.com/docs/subscriptions-api/swap-plan-variations>`__.

        Args:
            subscription_id: The ID of the subscription to swap the subscription plan for.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}/swap-plan"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[SwapPlanRequest | SwapPlanRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SwapPlanResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_subscription(
        self,
        subscription_id: str,
        body: UpdateSubscriptionRequest | UpdateSubscriptionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateSubscriptionResponse, RawError]:
        """Updates a subscription by modifying or clearing ``subscription`` field values. To clear a field, set its
        value to ``null``.

        Args:
            subscription_id: The ID of the subscription to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/subscriptions/{subscription_id}"),
            path_params=[param[str]("subscription_id", subscription_id)],
            body=json_body[UpdateSubscriptionRequest | UpdateSubscriptionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateSubscriptionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
