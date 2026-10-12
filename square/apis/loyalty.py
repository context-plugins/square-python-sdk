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
from ..models.accumulate_loyalty_points_request import (
    AccumulateLoyaltyPointsRequest,
    AccumulateLoyaltyPointsRequestDict,
)
from ..models.accumulate_loyalty_points_response import AccumulateLoyaltyPointsResponse
from ..models.adjust_loyalty_points_request import AdjustLoyaltyPointsRequest, AdjustLoyaltyPointsRequestDict
from ..models.adjust_loyalty_points_response import AdjustLoyaltyPointsResponse
from ..models.calculate_loyalty_points_request import CalculateLoyaltyPointsRequest, CalculateLoyaltyPointsRequestDict
from ..models.calculate_loyalty_points_response import CalculateLoyaltyPointsResponse
from ..models.cancel_loyalty_promotion_response import CancelLoyaltyPromotionResponse
from ..models.create_loyalty_account_request import CreateLoyaltyAccountRequest, CreateLoyaltyAccountRequestDict
from ..models.create_loyalty_account_response import CreateLoyaltyAccountResponse
from ..models.create_loyalty_promotion_request import CreateLoyaltyPromotionRequest, CreateLoyaltyPromotionRequestDict
from ..models.create_loyalty_promotion_response import CreateLoyaltyPromotionResponse
from ..models.create_loyalty_reward_request import CreateLoyaltyRewardRequest, CreateLoyaltyRewardRequestDict
from ..models.create_loyalty_reward_response import CreateLoyaltyRewardResponse
from ..models.delete_loyalty_reward_response import DeleteLoyaltyRewardResponse
from ..models.enums.loyalty_promotion_status import LoyaltyPromotionStatusOrStr
from ..models.list_loyalty_programs_response import ListLoyaltyProgramsResponse
from ..models.list_loyalty_promotions_response import ListLoyaltyPromotionsResponse
from ..models.redeem_loyalty_reward_request import RedeemLoyaltyRewardRequest, RedeemLoyaltyRewardRequestDict
from ..models.redeem_loyalty_reward_response import RedeemLoyaltyRewardResponse
from ..models.retrieve_loyalty_account_response import RetrieveLoyaltyAccountResponse
from ..models.retrieve_loyalty_program_response import RetrieveLoyaltyProgramResponse
from ..models.retrieve_loyalty_promotion_response import RetrieveLoyaltyPromotionResponse
from ..models.retrieve_loyalty_reward_response import RetrieveLoyaltyRewardResponse
from ..models.search_loyalty_accounts_request import SearchLoyaltyAccountsRequest, SearchLoyaltyAccountsRequestDict
from ..models.search_loyalty_accounts_response import SearchLoyaltyAccountsResponse
from ..models.search_loyalty_events_request import SearchLoyaltyEventsRequest, SearchLoyaltyEventsRequestDict
from ..models.search_loyalty_events_response import SearchLoyaltyEventsResponse
from ..models.search_loyalty_rewards_request import SearchLoyaltyRewardsRequest, SearchLoyaltyRewardsRequestDict
from ..models.search_loyalty_rewards_response import SearchLoyaltyRewardsResponse
from ..server.server import Server


class Loyalty:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LoyaltyWithRawResponse(client, server, auth)

    def accumulate_loyalty_points(
        self,
        account_id: str,
        body: AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccumulateLoyaltyPointsResponse:
        """Adds points earned from a purchase to a `loyalty account <entity:LoyaltyAccount>`__.

        - If you are using the Orders API to manage orders, provide the ``order_id``. Square reads the order
        to compute the points earned from both the base loyalty program and an associated `loyalty promotion
        <entity:LoyaltyPromotion>`__. For purchases that qualify for multiple accrual rules, Square computes points
        based on the accrual rule that grants the most points. For purchases that qualify for multiple promotions,
        Square computes points based on the most recently created promotion. A purchase must first qualify for program
        points to be eligible for promotion points.

        - If you are not using the Orders API to manage orders, provide ``points`` with the number of points to add.
        You must first perform a client-side computation of the points earned from the loyalty program and loyalty
        promotion. For spend-based and visit-based programs, you can call `CalculateLoyaltyPoints
        <api-endpoint:Loyalty-CalculateLoyaltyPoints>`__ to compute the points earned from the base loyalty program. For
        information about computing points earned from a loyalty promotion, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.accumulate_loyalty_points(account_id, body, request_options=request_options)
        )

    def adjust_loyalty_points(
        self,
        account_id: str,
        body: AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdjustLoyaltyPointsResponse:
        """Adds points to or subtracts points from a buyer's account.

        Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
        `AccumulateLoyaltyPoints <api-endpoint:Loyalty-AccumulateLoyaltyPoints>`__ to add points when a buyer pays for
        the purchase.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.adjust_loyalty_points(account_id, body, request_options=request_options))

    def calculate_loyalty_points(
        self,
        program_id: str,
        body: CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculateLoyaltyPointsResponse:
        """Calculates the number of points a buyer can earn from a purchase. Applications might call this endpoint to
        display the points to the buyer.

        - If you are using the Orders API to manage orders, provide the ``order_id`` and (optional)
            ``loyalty_account_id``.
        Square reads the order to compute the points earned from the base loyalty program and an associated `loyalty
        promotion <entity:LoyaltyPromotion>`__.

        - If you are not using the Orders API to manage orders, provide ``transaction_amount_money`` with the
        purchase amount. Square uses this amount to calculate the points earned from the base loyalty program, but not
        points earned from a loyalty promotion. For spend-based and visit-based programs, the ``tax_mode`` setting of
        the accrual rule indicates how taxes should be treated for loyalty points accrual. If the purchase qualifies for
        program points, call `ListLoyaltyPromotions <api-endpoint:Loyalty-ListLoyaltyPromotions>`__ and perform a
        client-side computation to calculate whether the purchase also qualifies for promotion points. For more
        information, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__, which defines the rules for accruing
                points.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.calculate_loyalty_points(program_id, body, request_options=request_options)
        )

    def cancel_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelLoyaltyPromotionResponse:
        """Cancels a loyalty promotion. Use this endpoint to cancel an ``ACTIVE`` promotion earlier than the end date,
        cancel an ``ACTIVE`` promotion when an end date is not specified, or cancel a ``SCHEDULED`` promotion. Because
        updating a promotion is not supported, you can also use this endpoint to cancel a promotion before you create a
        new one.

        This endpoint sets the loyalty promotion to the ``CANCELED`` state

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to cancel. You can cancel a
                promotion that has an ``ACTIVE`` or ``SCHEDULED`` status.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.cancel_loyalty_promotion(promotion_id, program_id, request_options=request_options)
        )

    def create_loyalty_account(
        self,
        body: CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLoyaltyAccountResponse:
        """Creates a loyalty account. To create a loyalty account, you must provide the ``program_id`` and a ``mapping``
        with the ``phone_number`` of the buyer.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_loyalty_account(body, request_options=request_options))

    def create_loyalty_promotion(
        self,
        program_id: str,
        body: CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLoyaltyPromotionResponse:
        """Creates a loyalty promotion for a `loyalty program <entity:LoyaltyProgram>`__. A loyalty promotion enables
        buyers to earn points in addition to those earned from the base loyalty program.

        This endpoint sets the loyalty promotion to the ``ACTIVE`` or ``SCHEDULED`` status, depending on the
        ``available_time`` setting. A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or
        ``SCHEDULED`` status.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__ to associate with the promotion. To
                get the program ID, call `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using
                the ``main`` keyword.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.create_loyalty_promotion(program_id, body, request_options=request_options)
        )

    def create_loyalty_reward(
        self,
        body: CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLoyaltyRewardResponse:
        """Creates a loyalty reward. In the process, the endpoint does following:

        - Uses the ``reward_tier_id`` in the request to determine the number of points
        to lock for this reward.
        - If the request includes ``order_id``, it adds the reward and related discount to the order.

        After a reward is created, the points are locked and not available for the buyer to redeem another reward.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.create_loyalty_reward(body, request_options=request_options))

    def delete_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteLoyaltyRewardResponse:
        """Deletes a loyalty reward by doing the following:

        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created
        (see `CreateLoyaltyReward <api-endpoint:Loyalty-CreateLoyaltyReward>`__), it updates the order by removing the
        reward and related discounts.

        You cannot delete a reward that has reached the terminal state (REDEEMED).

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.delete_loyalty_reward(reward_id, request_options=request_options))

    def list_loyalty_programs(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListLoyaltyProgramsResponse:
        """Returns a list of loyalty programs in the seller's account. Loyalty programs define how buyers can earn
        points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and
        managed from the Seller Dashboard. For more information, see `Loyalty Program Overview
        <https://developer.squareup.com/docs/loyalty/overview>`__.

        Replaced with `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ when used with the
        keyword ``main``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.list_loyalty_programs(request_options=request_options))

    def list_loyalty_promotions(
        self,
        program_id: str,
        *,
        status: LoyaltyPromotionStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLoyaltyPromotionsResponse:
        """Lists the loyalty promotions associated with a `loyalty program <entity:LoyaltyProgram>`__. Results are
        sorted by the ``created_at`` date in descending order (newest to oldest).

        Args:
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            status: The status to filter the results by. If a status is provided, only loyalty promotions with the
                specified status are returned. Otherwise, all loyalty promotions associated with the loyalty program are
                returned.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single paged response. The minimum value is 1 and the
                maximum value is 30. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.list_loyalty_promotions(
                program_id, status=status, cursor=cursor, limit=limit, request_options=request_options
            ),
        )

    def redeem_loyalty_reward(
        self,
        reward_id: str,
        body: RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RedeemLoyaltyRewardResponse:
        """Redeems a loyalty reward.

        The endpoint sets the reward to the ``REDEEMED`` terminal state.

        If you are using your own order processing system (not using the Orders API), you call this endpoint after the
        buyer paid for the purchase.

        After the reward reaches the terminal state, it cannot be deleted. In other words, points used for the reward
        cannot be returned to the account.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to redeem.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.redeem_loyalty_reward(reward_id, body, request_options=request_options))

    def retrieve_loyalty_account(
        self, account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyAccountResponse:
        """Retrieves a loyalty account.

        Args:
            account_id: The ID of the `loyalty account <entity:LoyaltyAccount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_loyalty_account(account_id, request_options=request_options))

    def retrieve_loyalty_program(
        self, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyProgramResponse:
        """Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword ``main``.

        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only
        one loyalty program, which is created and managed from the Seller Dashboard. For more information, see `Loyalty
        Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__.

        Args:
            program_id: The ID of the loyalty program or the keyword ``main``. Either value can be used to retrieve the
                single loyalty program that belongs to the seller.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_loyalty_program(program_id, request_options=request_options))

    def retrieve_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyPromotionResponse:
        """Retrieves a loyalty promotion.

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to retrieve.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            self._with_raw_response.retrieve_loyalty_promotion(
                promotion_id, program_id, request_options=request_options
            ),
        )

    def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyRewardResponse:
        """Retrieves a loyalty reward.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.retrieve_loyalty_reward(reward_id, request_options=request_options))

    def search_loyalty_accounts(
        self,
        body: SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchLoyaltyAccountsResponse:
        """Searches for loyalty accounts in a loyalty program.

        You can search for a loyalty account using the phone number or customer ID associated with the account. To
        return all loyalty accounts, specify an empty ``query`` object or omit it entirely.

        Search results are sorted by ``created_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_loyalty_accounts(body, request_options=request_options))

    def search_loyalty_events(
        self,
        body: SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchLoyaltyEventsResponse:
        """Searches for loyalty events.

        A Square loyalty program maintains a ledger of events that occur during the lifetime of a buyer's loyalty
        account. Each change in the point balance (for example, points earned, points redeemed, and points expired) is
        recorded in the ledger. Using this endpoint, you can search the ledger for events.

        Search results are sorted by ``created_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_loyalty_events(body, request_options=request_options))

    def search_loyalty_rewards(
        self,
        body: SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchLoyaltyRewardsResponse:
        """Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for
        all loyalty accounts. If you include a ``query`` object, ``loyalty_account_id`` is required and ``status`` is
        optional.

        If you know a reward ID, use the `RetrieveLoyaltyReward <api-endpoint:Loyalty-RetrieveLoyaltyReward>`__
        endpoint.

        Search results are sorted by ``updated_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(self._with_raw_response.search_loyalty_rewards(body, request_options=request_options))

    @property
    def with_raw_response(self) -> LoyaltyWithRawResponse:
        return self._with_raw_response


class AsyncLoyalty:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLoyaltyWithRawResponse(client, server, auth)

    async def accumulate_loyalty_points(
        self,
        account_id: str,
        body: AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccumulateLoyaltyPointsResponse:
        """Adds points earned from a purchase to a `loyalty account <entity:LoyaltyAccount>`__.

        - If you are using the Orders API to manage orders, provide the ``order_id``. Square reads the order
        to compute the points earned from both the base loyalty program and an associated `loyalty promotion
        <entity:LoyaltyPromotion>`__. For purchases that qualify for multiple accrual rules, Square computes points
        based on the accrual rule that grants the most points. For purchases that qualify for multiple promotions,
        Square computes points based on the most recently created promotion. A purchase must first qualify for program
        points to be eligible for promotion points.

        - If you are not using the Orders API to manage orders, provide ``points`` with the number of points to add.
        You must first perform a client-side computation of the points earned from the loyalty program and loyalty
        promotion. For spend-based and visit-based programs, you can call `CalculateLoyaltyPoints
        <api-endpoint:Loyalty-CalculateLoyaltyPoints>`__ to compute the points earned from the base loyalty program. For
        information about computing points earned from a loyalty promotion, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.accumulate_loyalty_points(account_id, body, request_options=request_options)
        )

    async def adjust_loyalty_points(
        self,
        account_id: str,
        body: AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AdjustLoyaltyPointsResponse:
        """Adds points to or subtracts points from a buyer's account.

        Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
        `AccumulateLoyaltyPoints <api-endpoint:Loyalty-AccumulateLoyaltyPoints>`__ to add points when a buyer pays for
        the purchase.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.adjust_loyalty_points(account_id, body, request_options=request_options)
        )

    async def calculate_loyalty_points(
        self,
        program_id: str,
        body: CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculateLoyaltyPointsResponse:
        """Calculates the number of points a buyer can earn from a purchase. Applications might call this endpoint to
        display the points to the buyer.

        - If you are using the Orders API to manage orders, provide the ``order_id`` and (optional)
            ``loyalty_account_id``.
        Square reads the order to compute the points earned from the base loyalty program and an associated `loyalty
        promotion <entity:LoyaltyPromotion>`__.

        - If you are not using the Orders API to manage orders, provide ``transaction_amount_money`` with the
        purchase amount. Square uses this amount to calculate the points earned from the base loyalty program, but not
        points earned from a loyalty promotion. For spend-based and visit-based programs, the ``tax_mode`` setting of
        the accrual rule indicates how taxes should be treated for loyalty points accrual. If the purchase qualifies for
        program points, call `ListLoyaltyPromotions <api-endpoint:Loyalty-ListLoyaltyPromotions>`__ and perform a
        client-side computation to calculate whether the purchase also qualifies for promotion points. For more
        information, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__, which defines the rules for accruing
                points.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.calculate_loyalty_points(program_id, body, request_options=request_options)
        )

    async def cancel_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> CancelLoyaltyPromotionResponse:
        """Cancels a loyalty promotion. Use this endpoint to cancel an ``ACTIVE`` promotion earlier than the end date,
        cancel an ``ACTIVE`` promotion when an end date is not specified, or cancel a ``SCHEDULED`` promotion. Because
        updating a promotion is not supported, you can also use this endpoint to cancel a promotion before you create a
        new one.

        This endpoint sets the loyalty promotion to the ``CANCELED`` state

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to cancel. You can cancel a
                promotion that has an ``ACTIVE`` or ``SCHEDULED`` status.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.cancel_loyalty_promotion(
                promotion_id, program_id, request_options=request_options
            ),
        )

    async def create_loyalty_account(
        self,
        body: CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLoyaltyAccountResponse:
        """Creates a loyalty account. To create a loyalty account, you must provide the ``program_id`` and a ``mapping``
        with the ``phone_number`` of the buyer.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_loyalty_account(body, request_options=request_options))

    async def create_loyalty_promotion(
        self,
        program_id: str,
        body: CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLoyaltyPromotionResponse:
        """Creates a loyalty promotion for a `loyalty program <entity:LoyaltyProgram>`__. A loyalty promotion enables
        buyers to earn points in addition to those earned from the base loyalty program.

        This endpoint sets the loyalty promotion to the ``ACTIVE`` or ``SCHEDULED`` status, depending on the
        ``available_time`` setting. A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or
        ``SCHEDULED`` status.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__ to associate with the promotion. To
                get the program ID, call `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using
                the ``main`` keyword.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.create_loyalty_promotion(program_id, body, request_options=request_options)
        )

    async def create_loyalty_reward(
        self,
        body: CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateLoyaltyRewardResponse:
        """Creates a loyalty reward. In the process, the endpoint does following:

        - Uses the ``reward_tier_id`` in the request to determine the number of points
        to lock for this reward.
        - If the request includes ``order_id``, it adds the reward and related discount to the order.

        After a reward is created, the points are locked and not available for the buyer to redeem another reward.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.create_loyalty_reward(body, request_options=request_options))

    async def delete_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteLoyaltyRewardResponse:
        """Deletes a loyalty reward by doing the following:

        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created
        (see `CreateLoyaltyReward <api-endpoint:Loyalty-CreateLoyaltyReward>`__), it updates the order by removing the
        reward and related discounts.

        You cannot delete a reward that has reached the terminal state (REDEEMED).

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.delete_loyalty_reward(reward_id, request_options=request_options))

    async def list_loyalty_programs(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListLoyaltyProgramsResponse:
        """Returns a list of loyalty programs in the seller's account. Loyalty programs define how buyers can earn
        points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and
        managed from the Seller Dashboard. For more information, see `Loyalty Program Overview
        <https://developer.squareup.com/docs/loyalty/overview>`__.

        Replaced with `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ when used with the
        keyword ``main``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.list_loyalty_programs(request_options=request_options))

    async def list_loyalty_promotions(
        self,
        program_id: str,
        *,
        status: LoyaltyPromotionStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLoyaltyPromotionsResponse:
        """Lists the loyalty promotions associated with a `loyalty program <entity:LoyaltyProgram>`__. Results are
        sorted by the ``created_at`` date in descending order (newest to oldest).

        Args:
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            status: The status to filter the results by. If a status is provided, only loyalty promotions with the
                specified status are returned. Otherwise, all loyalty promotions associated with the loyalty program are
                returned.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single paged response. The minimum value is 1 and the
                maximum value is 30. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.list_loyalty_promotions(
                program_id, status=status, cursor=cursor, limit=limit, request_options=request_options
            ),
        )

    async def redeem_loyalty_reward(
        self,
        reward_id: str,
        body: RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RedeemLoyaltyRewardResponse:
        """Redeems a loyalty reward.

        The endpoint sets the reward to the ``REDEEMED`` terminal state.

        If you are using your own order processing system (not using the Orders API), you call this endpoint after the
        buyer paid for the purchase.

        After the reward reaches the terminal state, it cannot be deleted. In other words, points used for the reward
        cannot be returned to the account.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to redeem.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.redeem_loyalty_reward(reward_id, body, request_options=request_options)
        )

    async def retrieve_loyalty_account(
        self, account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyAccountResponse:
        """Retrieves a loyalty account.

        Args:
            account_id: The ID of the `loyalty account <entity:LoyaltyAccount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_loyalty_account(account_id, request_options=request_options)
        )

    async def retrieve_loyalty_program(
        self, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyProgramResponse:
        """Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword ``main``.

        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only
        one loyalty program, which is created and managed from the Seller Dashboard. For more information, see `Loyalty
        Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__.

        Args:
            program_id: The ID of the loyalty program or the keyword ``main``. Either value can be used to retrieve the
                single loyalty program that belongs to the seller.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_loyalty_program(program_id, request_options=request_options)
        )

    async def retrieve_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyPromotionResponse:
        """Retrieves a loyalty promotion.

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to retrieve.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(
            await self._with_raw_response.retrieve_loyalty_promotion(
                promotion_id, program_id, request_options=request_options
            ),
        )

    async def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLoyaltyRewardResponse:
        """Retrieves a loyalty reward.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.retrieve_loyalty_reward(reward_id, request_options=request_options))

    async def search_loyalty_accounts(
        self,
        body: SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchLoyaltyAccountsResponse:
        """Searches for loyalty accounts in a loyalty program.

        You can search for a loyalty account using the phone number or customer ID associated with the account. To
        return all loyalty accounts, specify an empty ``query`` object or omit it entirely.

        Search results are sorted by ``created_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_loyalty_accounts(body, request_options=request_options))

    async def search_loyalty_events(
        self,
        body: SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchLoyaltyEventsResponse:
        """Searches for loyalty events.

        A Square loyalty program maintains a ledger of events that occur during the lifetime of a buyer's loyalty
        account. Each change in the point balance (for example, points earned, points redeemed, and points expired) is
        recorded in the ledger. Using this endpoint, you can search the ledger for events.

        Search results are sorted by ``created_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_loyalty_events(body, request_options=request_options))

    async def search_loyalty_rewards(
        self,
        body: SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchLoyaltyRewardsResponse:
        """Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for
        all loyalty accounts. If you include a ``query`` object, ``loyalty_account_id`` is required and ``status`` is
        optional.

        If you know a reward ID, use the `RetrieveLoyaltyReward <api-endpoint:Loyalty-RetrieveLoyaltyReward>`__
        endpoint.

        Search results are sorted by ``updated_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return unwrap(await self._with_raw_response.search_loyalty_rewards(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncLoyaltyWithRawResponse:
        return self._with_raw_response


class LoyaltyWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def accumulate_loyalty_points(
        self,
        account_id: str,
        body: AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccumulateLoyaltyPointsResponse, RawError]:
        """Adds points earned from a purchase to a `loyalty account <entity:LoyaltyAccount>`__.

        - If you are using the Orders API to manage orders, provide the ``order_id``. Square reads the order
        to compute the points earned from both the base loyalty program and an associated `loyalty promotion
        <entity:LoyaltyPromotion>`__. For purchases that qualify for multiple accrual rules, Square computes points
        based on the accrual rule that grants the most points. For purchases that qualify for multiple promotions,
        Square computes points based on the most recently created promotion. A purchase must first qualify for program
        points to be eligible for promotion points.

        - If you are not using the Orders API to manage orders, provide ``points`` with the number of points to add.
        You must first perform a client-side computation of the points earned from the loyalty program and loyalty
        promotion. For spend-based and visit-based programs, you can call `CalculateLoyaltyPoints
        <api-endpoint:Loyalty-CalculateLoyaltyPoints>`__ to compute the points earned from the base loyalty program. For
        information about computing points earned from a loyalty promotion, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts/{account_id}/accumulate"),
            path_params=[param[str]("account_id", account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[AccumulateLoyaltyPointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def adjust_loyalty_points(
        self,
        account_id: str,
        body: AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdjustLoyaltyPointsResponse, RawError]:
        """Adds points to or subtracts points from a buyer's account.

        Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
        `AccumulateLoyaltyPoints <api-endpoint:Loyalty-AccumulateLoyaltyPoints>`__ to add points when a buyer pays for
        the purchase.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts/{account_id}/adjust"),
            path_params=[param[str]("account_id", account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[AdjustLoyaltyPointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def calculate_loyalty_points(
        self,
        program_id: str,
        body: CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculateLoyaltyPointsResponse, RawError]:
        """Calculates the number of points a buyer can earn from a purchase. Applications might call this endpoint to
        display the points to the buyer.

        - If you are using the Orders API to manage orders, provide the ``order_id`` and (optional)
            ``loyalty_account_id``.
        Square reads the order to compute the points earned from the base loyalty program and an associated `loyalty
        promotion <entity:LoyaltyPromotion>`__.

        - If you are not using the Orders API to manage orders, provide ``transaction_amount_money`` with the
        purchase amount. Square uses this amount to calculate the points earned from the base loyalty program, but not
        points earned from a loyalty promotion. For spend-based and visit-based programs, the ``tax_mode`` setting of
        the accrual rule indicates how taxes should be treated for loyalty points accrual. If the purchase qualifies for
        program points, call `ListLoyaltyPromotions <api-endpoint:Loyalty-ListLoyaltyPromotions>`__ and perform a
        client-side computation to calculate whether the purchase also qualifies for promotion points. For more
        information, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__, which defines the rules for accruing
                points.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/calculate"),
            path_params=[param[str]("program_id", program_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CalculateLoyaltyPointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancel_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelLoyaltyPromotionResponse, RawError]:
        """Cancels a loyalty promotion. Use this endpoint to cancel an ``ACTIVE`` promotion earlier than the end date,
        cancel an ``ACTIVE`` promotion when an end date is not specified, or cancel a ``SCHEDULED`` promotion. Because
        updating a promotion is not supported, you can also use this endpoint to cancel a promotion before you create a
        new one.

        This endpoint sets the loyalty promotion to the ``CANCELED`` state

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to cancel. You can cancel a
                promotion that has an ``ACTIVE`` or ``SCHEDULED`` status.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions/{promotion_id}/cancel"),
            path_params=[param[str]("promotion_id", promotion_id), param[str]("program_id", program_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelLoyaltyPromotionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_loyalty_account(
        self,
        body: CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLoyaltyAccountResponse, RawError]:
        """Creates a loyalty account. To create a loyalty account, you must provide the ``program_id`` and a ``mapping``
        with the ``phone_number`` of the buyer.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateLoyaltyAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_loyalty_promotion(
        self,
        program_id: str,
        body: CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLoyaltyPromotionResponse, RawError]:
        """Creates a loyalty promotion for a `loyalty program <entity:LoyaltyProgram>`__. A loyalty promotion enables
        buyers to earn points in addition to those earned from the base loyalty program.

        This endpoint sets the loyalty promotion to the ``ACTIVE`` or ``SCHEDULED`` status, depending on the
        ``available_time`` setting. A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or
        ``SCHEDULED`` status.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__ to associate with the promotion. To
                get the program ID, call `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using
                the ``main`` keyword.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions"),
            path_params=[param[str]("program_id", program_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateLoyaltyPromotionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_loyalty_reward(
        self,
        body: CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLoyaltyRewardResponse, RawError]:
        """Creates a loyalty reward. In the process, the endpoint does following:

        - Uses the ``reward_tier_id`` in the request to determine the number of points
        to lock for this reward.
        - If the request includes ``order_id``, it adds the reward and related discount to the order.

        After a reward is created, the points are locked and not available for the buyer to redeem another reward.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/rewards"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteLoyaltyRewardResponse, RawError]:
        """Deletes a loyalty reward by doing the following:

        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created
        (see `CreateLoyaltyReward <api-endpoint:Loyalty-CreateLoyaltyReward>`__), it updates the order by removing the
        reward and related discounts.

        You cannot delete a reward that has reached the terminal state (REDEEMED).

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/loyalty/rewards/{reward_id}"),
            path_params=[param[str]("reward_id", reward_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_loyalty_programs(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListLoyaltyProgramsResponse, RawError]:
        """Returns a list of loyalty programs in the seller's account. Loyalty programs define how buyers can earn
        points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and
        managed from the Seller Dashboard. For more information, see `Loyalty Program Overview
        <https://developer.squareup.com/docs/loyalty/overview>`__.

        Replaced with `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ when used with the
        keyword ``main``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLoyaltyProgramsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_loyalty_promotions(
        self,
        program_id: str,
        *,
        status: LoyaltyPromotionStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLoyaltyPromotionsResponse, RawError]:
        """Lists the loyalty promotions associated with a `loyalty program <entity:LoyaltyProgram>`__. Results are
        sorted by the ``created_at`` date in descending order (newest to oldest).

        Args:
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            status: The status to filter the results by. If a status is provided, only loyalty promotions with the
                specified status are returned. Otherwise, all loyalty promotions associated with the loyalty program are
                returned.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single paged response. The minimum value is 1 and the
                maximum value is 30. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions"),
            path_params=[param[str]("program_id", program_id)],
            query_params=[
                param[LoyaltyPromotionStatusOrStr | None]("status", status),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLoyaltyPromotionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def redeem_loyalty_reward(
        self,
        reward_id: str,
        body: RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RedeemLoyaltyRewardResponse, RawError]:
        """Redeems a loyalty reward.

        The endpoint sets the reward to the ``REDEEMED`` terminal state.

        If you are using your own order processing system (not using the Orders API), you call this endpoint after the
        buyer paid for the purchase.

        After the reward reaches the terminal state, it cannot be deleted. In other words, points used for the reward
        cannot be returned to the account.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to redeem.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/rewards/{reward_id}/redeem"),
            path_params=[param[str]("reward_id", reward_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RedeemLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_loyalty_account(
        self, account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyAccountResponse, RawError]:
        """Retrieves a loyalty account.

        Args:
            account_id: The ID of the `loyalty account <entity:LoyaltyAccount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/accounts/{account_id}"),
            path_params=[param[str]("account_id", account_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLoyaltyAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_loyalty_program(
        self, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyProgramResponse, RawError]:
        """Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword ``main``.

        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only
        one loyalty program, which is created and managed from the Seller Dashboard. For more information, see `Loyalty
        Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__.

        Args:
            program_id: The ID of the loyalty program or the keyword ``main``. Either value can be used to retrieve the
                single loyalty program that belongs to the seller.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}"),
            path_params=[param[str]("program_id", program_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLoyaltyProgramResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyPromotionResponse, RawError]:
        """Retrieves a loyalty promotion.

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to retrieve.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions/{promotion_id}"),
            path_params=[param[str]("promotion_id", promotion_id), param[str]("program_id", program_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLoyaltyPromotionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyRewardResponse, RawError]:
        """Retrieves a loyalty reward.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/rewards/{reward_id}"),
            path_params=[param[str]("reward_id", reward_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_loyalty_accounts(
        self,
        body: SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchLoyaltyAccountsResponse, RawError]:
        """Searches for loyalty accounts in a loyalty program.

        You can search for a loyalty account using the phone number or customer ID associated with the account. To
        return all loyalty accounts, specify an empty ``query`` object or omit it entirely.

        Search results are sorted by ``created_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchLoyaltyAccountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_loyalty_events(
        self,
        body: SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchLoyaltyEventsResponse, RawError]:
        """Searches for loyalty events.

        A Square loyalty program maintains a ledger of events that occur during the lifetime of a buyer's loyalty
        account. Each change in the point balance (for example, points earned, points redeemed, and points expired) is
        recorded in the ledger. Using this endpoint, you can search the ledger for events.

        Search results are sorted by ``created_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/events/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchLoyaltyEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_loyalty_rewards(
        self,
        body: SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchLoyaltyRewardsResponse, RawError]:
        """Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for
        all loyalty accounts. If you include a ``query`` object, ``loyalty_account_id`` is required and ``status`` is
        optional.

        If you know a reward ID, use the `RetrieveLoyaltyReward <api-endpoint:Loyalty-RetrieveLoyaltyReward>`__
        endpoint.

        Search results are sorted by ``updated_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/rewards/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchLoyaltyRewardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLoyaltyWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def accumulate_loyalty_points(
        self,
        account_id: str,
        body: AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccumulateLoyaltyPointsResponse, RawError]:
        """Adds points earned from a purchase to a `loyalty account <entity:LoyaltyAccount>`__.

        - If you are using the Orders API to manage orders, provide the ``order_id``. Square reads the order
        to compute the points earned from both the base loyalty program and an associated `loyalty promotion
        <entity:LoyaltyPromotion>`__. For purchases that qualify for multiple accrual rules, Square computes points
        based on the accrual rule that grants the most points. For purchases that qualify for multiple promotions,
        Square computes points based on the most recently created promotion. A purchase must first qualify for program
        points to be eligible for promotion points.

        - If you are not using the Orders API to manage orders, provide ``points`` with the number of points to add.
        You must first perform a client-side computation of the points earned from the loyalty program and loyalty
        promotion. For spend-based and visit-based programs, you can call `CalculateLoyaltyPoints
        <api-endpoint:Loyalty-CalculateLoyaltyPoints>`__ to compute the points earned from the base loyalty program. For
        information about computing points earned from a loyalty promotion, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts/{account_id}/accumulate"),
            path_params=[param[str]("account_id", account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccumulateLoyaltyPointsRequest | AccumulateLoyaltyPointsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[AccumulateLoyaltyPointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def adjust_loyalty_points(
        self,
        account_id: str,
        body: AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AdjustLoyaltyPointsResponse, RawError]:
        """Adds points to or subtracts points from a buyer's account.

        Use this endpoint only when you need to manually adjust points. Otherwise, in your application flow, you call
        `AccumulateLoyaltyPoints <api-endpoint:Loyalty-AccumulateLoyaltyPoints>`__ to add points when a buyer pays for
        the purchase.

        Args:
            account_id: The ID of the target `loyalty account <entity:LoyaltyAccount>`__.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts/{account_id}/adjust"),
            path_params=[param[str]("account_id", account_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AdjustLoyaltyPointsRequest | AdjustLoyaltyPointsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[AdjustLoyaltyPointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def calculate_loyalty_points(
        self,
        program_id: str,
        body: CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculateLoyaltyPointsResponse, RawError]:
        """Calculates the number of points a buyer can earn from a purchase. Applications might call this endpoint to
        display the points to the buyer.

        - If you are using the Orders API to manage orders, provide the ``order_id`` and (optional)
            ``loyalty_account_id``.
        Square reads the order to compute the points earned from the base loyalty program and an associated `loyalty
        promotion <entity:LoyaltyPromotion>`__.

        - If you are not using the Orders API to manage orders, provide ``transaction_amount_money`` with the
        purchase amount. Square uses this amount to calculate the points earned from the base loyalty program, but not
        points earned from a loyalty promotion. For spend-based and visit-based programs, the ``tax_mode`` setting of
        the accrual rule indicates how taxes should be treated for loyalty points accrual. If the purchase qualifies for
        program points, call `ListLoyaltyPromotions <api-endpoint:Loyalty-ListLoyaltyPromotions>`__ and perform a
        client-side computation to calculate whether the purchase also qualifies for promotion points. For more
        information, see `Calculating promotion points
        <https://developer.squareup.com/docs/loyalty-api/loyalty-promotions#calculate-promotion-points>`__.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__, which defines the rules for accruing
                points.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/calculate"),
            path_params=[param[str]("program_id", program_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateLoyaltyPointsRequest | CalculateLoyaltyPointsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CalculateLoyaltyPointsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancel_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CancelLoyaltyPromotionResponse, RawError]:
        """Cancels a loyalty promotion. Use this endpoint to cancel an ``ACTIVE`` promotion earlier than the end date,
        cancel an ``ACTIVE`` promotion when an end date is not specified, or cancel a ``SCHEDULED`` promotion. Because
        updating a promotion is not supported, you can also use this endpoint to cancel a promotion before you create a
        new one.

        This endpoint sets the loyalty promotion to the ``CANCELED`` state

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to cancel. You can cancel a
                promotion that has an ``ACTIVE`` or ``SCHEDULED`` status.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions/{promotion_id}/cancel"),
            path_params=[param[str]("promotion_id", promotion_id), param[str]("program_id", program_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CancelLoyaltyPromotionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_loyalty_account(
        self,
        body: CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLoyaltyAccountResponse, RawError]:
        """Creates a loyalty account. To create a loyalty account, you must provide the ``program_id`` and a ``mapping``
        with the ``phone_number`` of the buyer.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLoyaltyAccountRequest | CreateLoyaltyAccountRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateLoyaltyAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_loyalty_promotion(
        self,
        program_id: str,
        body: CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLoyaltyPromotionResponse, RawError]:
        """Creates a loyalty promotion for a `loyalty program <entity:LoyaltyProgram>`__. A loyalty promotion enables
        buyers to earn points in addition to those earned from the base loyalty program.

        This endpoint sets the loyalty promotion to the ``ACTIVE`` or ``SCHEDULED`` status, depending on the
        ``available_time`` setting. A loyalty program can have a maximum of 10 loyalty promotions with an ``ACTIVE`` or
        ``SCHEDULED`` status.

        Args:
            program_id: The ID of the `loyalty program <entity:LoyaltyProgram>`__ to associate with the promotion. To
                get the program ID, call `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using
                the ``main`` keyword.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions"),
            path_params=[param[str]("program_id", program_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLoyaltyPromotionRequest | CreateLoyaltyPromotionRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateLoyaltyPromotionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_loyalty_reward(
        self,
        body: CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateLoyaltyRewardResponse, RawError]:
        """Creates a loyalty reward. In the process, the endpoint does following:

        - Uses the ``reward_tier_id`` in the request to determine the number of points
        to lock for this reward.
        - If the request includes ``order_id``, it adds the reward and related discount to the order.

        After a reward is created, the points are locked and not available for the buyer to redeem another reward.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/rewards"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateLoyaltyRewardRequest | CreateLoyaltyRewardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[CreateLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteLoyaltyRewardResponse, RawError]:
        """Deletes a loyalty reward by doing the following:

        - Returns the loyalty points back to the loyalty account.
        - If an order ID was specified when the reward was created
        (see `CreateLoyaltyReward <api-endpoint:Loyalty-CreateLoyaltyReward>`__), it updates the order by removing the
        reward and related discounts.

        You cannot delete a reward that has reached the terminal state (REDEEMED).

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/loyalty/rewards/{reward_id}"),
            path_params=[param[str]("reward_id", reward_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[DeleteLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_loyalty_programs(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListLoyaltyProgramsResponse, RawError]:
        """Returns a list of loyalty programs in the seller's account. Loyalty programs define how buyers can earn
        points and redeem points for rewards. Square sellers can have only one loyalty program, which is created and
        managed from the Seller Dashboard. For more information, see `Loyalty Program Overview
        <https://developer.squareup.com/docs/loyalty/overview>`__.

        Replaced with `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ when used with the
        keyword ``main``.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs"),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListLoyaltyProgramsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_loyalty_promotions(
        self,
        program_id: str,
        *,
        status: LoyaltyPromotionStatusOrStr | None = None,
        cursor: str | None = None,
        limit: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLoyaltyPromotionsResponse, RawError]:
        """Lists the loyalty promotions associated with a `loyalty program <entity:LoyaltyProgram>`__. Results are
        sorted by the ``created_at`` date in descending order (newest to oldest).

        Args:
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            status: The status to filter the results by. If a status is provided, only loyalty promotions with the
                specified status are returned. Otherwise, all loyalty promotions associated with the loyalty program are
                returned.
            cursor: The cursor returned in the paged response from the previous call to this endpoint. Provide this
                cursor to retrieve the next page of results for your original request. For more information, see
                `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single paged response. The minimum value is 1 and the
                maximum value is 30. The default value is 30. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions"),
            path_params=[param[str]("program_id", program_id)],
            query_params=[
                param[LoyaltyPromotionStatusOrStr | None]("status", status),
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[ListLoyaltyPromotionsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def redeem_loyalty_reward(
        self,
        reward_id: str,
        body: RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RedeemLoyaltyRewardResponse, RawError]:
        """Redeems a loyalty reward.

        The endpoint sets the reward to the ``REDEEMED`` terminal state.

        If you are using your own order processing system (not using the Orders API), you call this endpoint after the
        buyer paid for the purchase.

        After the reward reaches the terminal state, it cannot be deleted. In other words, points used for the reward
        cannot be returned to the account.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to redeem.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/rewards/{reward_id}/redeem"),
            path_params=[param[str]("reward_id", reward_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RedeemLoyaltyRewardRequest | RedeemLoyaltyRewardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RedeemLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_loyalty_account(
        self, account_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyAccountResponse, RawError]:
        """Retrieves a loyalty account.

        Args:
            account_id: The ID of the `loyalty account <entity:LoyaltyAccount>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/accounts/{account_id}"),
            path_params=[param[str]("account_id", account_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLoyaltyAccountResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_loyalty_program(
        self, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyProgramResponse, RawError]:
        """Retrieves the loyalty program in a seller's account, specified by the program ID or the keyword ``main``.

        Loyalty programs define how buyers can earn points and redeem points for rewards. Square sellers can have only
        one loyalty program, which is created and managed from the Seller Dashboard. For more information, see `Loyalty
        Program Overview <https://developer.squareup.com/docs/loyalty/overview>`__.

        Args:
            program_id: The ID of the loyalty program or the keyword ``main``. Either value can be used to retrieve the
                single loyalty program that belongs to the seller.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}"),
            path_params=[param[str]("program_id", program_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLoyaltyProgramResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_loyalty_promotion(
        self, promotion_id: str, program_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyPromotionResponse, RawError]:
        """Retrieves a loyalty promotion.

        Args:
            promotion_id: The ID of the `loyalty promotion <entity:LoyaltyPromotion>`__ to retrieve.
            program_id: The ID of the base `loyalty program <entity:LoyaltyProgram>`__. To get the program ID, call
                `RetrieveLoyaltyProgram <api-endpoint:Loyalty-RetrieveLoyaltyProgram>`__ using the ``main`` keyword.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/programs/{program_id}/promotions/{promotion_id}"),
            path_params=[param[str]("promotion_id", promotion_id), param[str]("program_id", program_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLoyaltyPromotionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_loyalty_reward(
        self, reward_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLoyaltyRewardResponse, RawError]:
        """Retrieves a loyalty reward.

        Args:
            reward_id: The ID of the `loyalty reward <entity:LoyaltyReward>`__ to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/loyalty/rewards/{reward_id}"),
            path_params=[param[str]("reward_id", reward_id)],
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[RetrieveLoyaltyRewardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_loyalty_accounts(
        self,
        body: SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchLoyaltyAccountsResponse, RawError]:
        """Searches for loyalty accounts in a loyalty program.

        You can search for a loyalty account using the phone number or customer ID associated with the account. To
        return all loyalty accounts, specify an empty ``query`` object or omit it entirely.

        Search results are sorted by ``created_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/accounts/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchLoyaltyAccountsRequest | SearchLoyaltyAccountsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[SearchLoyaltyAccountsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_loyalty_events(
        self,
        body: SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchLoyaltyEventsResponse, RawError]:
        """Searches for loyalty events.

        A Square loyalty program maintains a ledger of events that occur during the lifetime of a buyer's loyalty
        account. Each change in the point balance (for example, points earned, points redeemed, and points expired) is
        recorded in the ledger. Using this endpoint, you can search the ledger for events.

        Search results are sorted by ``created_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/events/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchLoyaltyEventsRequest | SearchLoyaltyEventsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[SearchLoyaltyEventsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_loyalty_rewards(
        self,
        body: SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchLoyaltyRewardsResponse, RawError]:
        """Searches for loyalty rewards. This endpoint accepts a request with no query filters and returns results for
        all loyalty accounts. If you include a ``query`` object, ``loyalty_account_id`` is required and ``status`` is
        optional.

        If you know a reward ID, use the `RetrieveLoyaltyReward <api-endpoint:Loyalty-RetrieveLoyaltyReward>`__
        endpoint.

        Search results are sorted by ``updated_at`` in descending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/loyalty/rewards/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchLoyaltyRewardsRequest | SearchLoyaltyRewardsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=async_json_decoder[SearchLoyaltyRewardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
