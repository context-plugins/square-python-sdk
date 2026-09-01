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
from ..models.add_group_to_customer_response import AddGroupToCustomerResponse
from ..models.bulk_create_customers_request import BulkCreateCustomersRequest, BulkCreateCustomersRequestDict
from ..models.bulk_create_customers_response import BulkCreateCustomersResponse
from ..models.bulk_delete_customers_request import BulkDeleteCustomersRequest, BulkDeleteCustomersRequestDict
from ..models.bulk_delete_customers_response import BulkDeleteCustomersResponse
from ..models.bulk_retrieve_customers_request import BulkRetrieveCustomersRequest, BulkRetrieveCustomersRequestDict
from ..models.bulk_retrieve_customers_response import BulkRetrieveCustomersResponse
from ..models.bulk_update_customers_request import BulkUpdateCustomersRequest, BulkUpdateCustomersRequestDict
from ..models.bulk_update_customers_response import BulkUpdateCustomersResponse
from ..models.create_customer_card_request import CreateCustomerCardRequest, CreateCustomerCardRequestDict
from ..models.create_customer_card_response import CreateCustomerCardResponse
from ..models.create_customer_request import CreateCustomerRequest, CreateCustomerRequestDict
from ..models.create_customer_response import CreateCustomerResponse
from ..models.delete_customer_card_response import DeleteCustomerCardResponse
from ..models.delete_customer_response import DeleteCustomerResponse
from ..models.enums.customer_sort_field import CustomerSortFieldOrStr
from ..models.enums.sort_order import SortOrderOrStr
from ..models.list_customers_response import ListCustomersResponse
from ..models.remove_group_from_customer_response import RemoveGroupFromCustomerResponse
from ..models.retrieve_customer_response import RetrieveCustomerResponse
from ..models.search_customers_request import SearchCustomersRequest, SearchCustomersRequestDict
from ..models.search_customers_response import SearchCustomersResponse
from ..models.update_customer_request import UpdateCustomerRequest, UpdateCustomerRequestDict
from ..models.update_customer_response import UpdateCustomerResponse
from ..server.server import Server


class Customers:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = CustomersWithRawResponse(client, server, auth)

    def add_group_to_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AddGroupToCustomerResponse:
        """Adds a group membership to a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to add to a group.
            group_id: The ID of the customer group to add the customer to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.add_group_to_customer(
            customer_id, group_id, request_options=request_options
        ).unwrap()

    def bulk_create_customers(
        self,
        body: BulkCreateCustomersRequest | BulkCreateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateCustomersResponse:
        """Creates multiple `customer profiles <entity:Customer>`__ for a business.

        This endpoint takes a map of individual create requests and returns a map of responses.

        You must provide at least one of the following values in each create request:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_create_customers(body, request_options=request_options).unwrap()

    def bulk_delete_customers(
        self,
        body: BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteCustomersResponse:
        """Deletes multiple customer profiles.

        The endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_delete_customers(body, request_options=request_options).unwrap()

    def bulk_retrieve_customers(
        self,
        body: BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveCustomersResponse:
        """Retrieves multiple customer profiles.

        This endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_retrieve_customers(body, request_options=request_options).unwrap()

    def bulk_update_customers(
        self,
        body: BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateCustomersResponse:
        """Updates multiple customer profiles.

        This endpoint takes a map of individual update requests and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_update_customers(body, request_options=request_options).unwrap()

    def create_customer(
        self,
        body: CreateCustomerRequest | CreateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerResponse:
        """Creates a new customer for a business.

        You must provide at least one of the following values in your request to this endpoint:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer(body, request_options=request_options).unwrap()

    def create_customer_card(
        self,
        customer_id: str,
        body: CreateCustomerCardRequest | CreateCustomerCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerCardResponse:
        """Adds a card on file to an existing customer.

        As with charges, calls to ``CreateCustomerCard`` are idempotent. Multiple calls with the same card nonce return
        the same card record that was created with the provided nonce during the _first_ call.

        Args:
            customer_id: The Square ID of the customer profile the card is linked to.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_customer_card(customer_id, body, request_options=request_options).unwrap()

    def delete_customer(
        self, customer_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerResponse:
        """Deletes a customer profile from a business.

        To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to delete.
            version: The current version of the customer profile. As a best practice, you should include this parameter
                to enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control. For more information, see `Delete a customer profile
                <https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer(
            customer_id, version=version, request_options=request_options
        ).unwrap()

    def delete_customer_card(
        self, customer_id: str, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerCardResponse:
        """Removes a card on file from a customer.

        Args:
            customer_id: The ID of the customer that the card on file belongs to.
            card_id: The ID of the card on file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_customer_card(
            customer_id, card_id, request_options=request_options
        ).unwrap()

    def list_customers(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        sort_field: CustomerSortFieldOrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        count: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomersResponse:
        """Lists customer profiles associated with a Square account.

        Under normal operating conditions, newly created or updated customer profiles become available for the listing
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 100, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 100. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            sort_field: Indicates how customers should be sorted. The default value is ``DEFAULT``.
            sort_order: Indicates whether customers should be sorted in ascending (``ASC``) or descending (``DESC``)
                order. The default value is ``ASC``.
            count: Indicates whether to return the total count of customers in the ``count`` field of the response. The
                default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_customers(
            cursor=cursor,
            limit=limit,
            sort_field=sort_field,
            sort_order=sort_order,
            count=count,
            request_options=request_options,
        ).unwrap()

    def remove_group_from_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RemoveGroupFromCustomerResponse:
        """Removes a group membership from a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to remove from the group.
            group_id: The ID of the customer group to remove the customer from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.remove_group_from_customer(
            customer_id, group_id, request_options=request_options
        ).unwrap()

    def retrieve_customer(
        self, customer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerResponse:
        """Returns details for a single customer.

        Args:
            customer_id: The ID of the customer to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_customer(customer_id, request_options=request_options).unwrap()

    def search_customers(
        self,
        body: SearchCustomersRequest | SearchCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchCustomersResponse:
        """Searches the customer profiles associated with a Square account using one or more supported query filters.

        Calling ``SearchCustomers`` without any explicit query filter returns all customer profiles ordered
        alphabetically based on ``given_name`` and ``family_name``.

        Under normal operating conditions, newly created or updated customer profiles become available for the search
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_customers(body, request_options=request_options).unwrap()

    def update_customer(
        self,
        customer_id: str,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCustomerResponse:
        """Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required
        in the request. To add or update a field, specify the new value. To remove a field, specify ``null``.

        To update a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_customer(customer_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> CustomersWithRawResponse:
        return self._with_raw_response


class AsyncCustomers:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncCustomersWithRawResponse(client, server, auth)

    async def add_group_to_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AddGroupToCustomerResponse:
        """Adds a group membership to a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to add to a group.
            group_id: The ID of the customer group to add the customer to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.add_group_to_customer(customer_id, group_id, request_options=request_options)
        ).unwrap()

    async def bulk_create_customers(
        self,
        body: BulkCreateCustomersRequest | BulkCreateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateCustomersResponse:
        """Creates multiple `customer profiles <entity:Customer>`__ for a business.

        This endpoint takes a map of individual create requests and returns a map of responses.

        You must provide at least one of the following values in each create request:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_create_customers(body, request_options=request_options)).unwrap()

    async def bulk_delete_customers(
        self,
        body: BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkDeleteCustomersResponse:
        """Deletes multiple customer profiles.

        The endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_delete_customers(body, request_options=request_options)).unwrap()

    async def bulk_retrieve_customers(
        self,
        body: BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveCustomersResponse:
        """Retrieves multiple customer profiles.

        This endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_retrieve_customers(body, request_options=request_options)).unwrap()

    async def bulk_update_customers(
        self,
        body: BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateCustomersResponse:
        """Updates multiple customer profiles.

        This endpoint takes a map of individual update requests and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_update_customers(body, request_options=request_options)).unwrap()

    async def create_customer(
        self,
        body: CreateCustomerRequest | CreateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerResponse:
        """Creates a new customer for a business.

        You must provide at least one of the following values in your request to this endpoint:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_customer(body, request_options=request_options)).unwrap()

    async def create_customer_card(
        self,
        customer_id: str,
        body: CreateCustomerCardRequest | CreateCustomerCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateCustomerCardResponse:
        """Adds a card on file to an existing customer.

        As with charges, calls to ``CreateCustomerCard`` are idempotent. Multiple calls with the same card nonce return
        the same card record that was created with the provided nonce during the _first_ call.

        Args:
            customer_id: The Square ID of the customer profile the card is linked to.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_customer_card(customer_id, body, request_options=request_options)
        ).unwrap()

    async def delete_customer(
        self, customer_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerResponse:
        """Deletes a customer profile from a business.

        To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to delete.
            version: The current version of the customer profile. As a best practice, you should include this parameter
                to enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control. For more information, see `Delete a customer profile
                <https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_customer(customer_id, version=version, request_options=request_options)
        ).unwrap()

    async def delete_customer_card(
        self, customer_id: str, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteCustomerCardResponse:
        """Removes a card on file from a customer.

        Args:
            customer_id: The ID of the customer that the card on file belongs to.
            card_id: The ID of the card on file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_customer_card(customer_id, card_id, request_options=request_options)
        ).unwrap()

    async def list_customers(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        sort_field: CustomerSortFieldOrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        count: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListCustomersResponse:
        """Lists customer profiles associated with a Square account.

        Under normal operating conditions, newly created or updated customer profiles become available for the listing
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 100, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 100. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            sort_field: Indicates how customers should be sorted. The default value is ``DEFAULT``.
            sort_order: Indicates whether customers should be sorted in ascending (``ASC``) or descending (``DESC``)
                order. The default value is ``ASC``.
            count: Indicates whether to return the total count of customers in the ``count`` field of the response. The
                default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_customers(
                cursor=cursor,
                limit=limit,
                sort_field=sort_field,
                sort_order=sort_order,
                count=count,
                request_options=request_options,
            )
        ).unwrap()

    async def remove_group_from_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RemoveGroupFromCustomerResponse:
        """Removes a group membership from a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to remove from the group.
            group_id: The ID of the customer group to remove the customer from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.remove_group_from_customer(
                customer_id, group_id, request_options=request_options
            )
        ).unwrap()

    async def retrieve_customer(
        self, customer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveCustomerResponse:
        """Returns details for a single customer.

        Args:
            customer_id: The ID of the customer to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_customer(customer_id, request_options=request_options)).unwrap()

    async def search_customers(
        self,
        body: SearchCustomersRequest | SearchCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchCustomersResponse:
        """Searches the customer profiles associated with a Square account using one or more supported query filters.

        Calling ``SearchCustomers`` without any explicit query filter returns all customer profiles ordered
        alphabetically based on ``given_name`` and ``family_name``.

        Under normal operating conditions, newly created or updated customer profiles become available for the search
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_customers(body, request_options=request_options)).unwrap()

    async def update_customer(
        self,
        customer_id: str,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateCustomerResponse:
        """Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required
        in the request. To add or update a field, specify the new value. To remove a field, specify ``null``.

        To update a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_customer(customer_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncCustomersWithRawResponse:
        return self._with_raw_response


class CustomersWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def add_group_to_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AddGroupToCustomerResponse, RawError]:
        """Adds a group membership to a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to add to a group.
            group_id: The ID of the customer group to add the customer to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/customers/{customer_id}/groups/{group_id}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[AddGroupToCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_create_customers(
        self,
        body: BulkCreateCustomersRequest | BulkCreateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateCustomersResponse, RawError]:
        """Creates multiple `customer profiles <entity:Customer>`__ for a business.

        This endpoint takes a map of individual create requests and returns a map of responses.

        You must provide at least one of the following values in each create request:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateCustomersRequest | BulkCreateCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkCreateCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_delete_customers(
        self,
        body: BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteCustomersResponse, RawError]:
        """Deletes multiple customer profiles.

        The endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_retrieve_customers(
        self,
        body: BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveCustomersResponse, RawError]:
        """Retrieves multiple customer profiles.

        This endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_update_customers(
        self,
        body: BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateCustomersResponse, RawError]:
        """Updates multiple customer profiles.

        This endpoint takes a map of individual update requests and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpdateCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_customer(
        self,
        body: CreateCustomerRequest | CreateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerResponse, RawError]:
        """Creates a new customer for a business.

        You must provide at least one of the following values in your request to this endpoint:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerRequest | CreateCustomerRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_customer_card(
        self,
        customer_id: str,
        body: CreateCustomerCardRequest | CreateCustomerCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerCardResponse, RawError]:
        """Adds a card on file to an existing customer.

        As with charges, calls to ``CreateCustomerCard`` are idempotent. Multiple calls with the same card nonce return
        the same card record that was created with the provided nonce during the _first_ call.

        Args:
            customer_id: The Square ID of the customer profile the card is linked to.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/{customer_id}/cards"),
            path_params=[param[str]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerCardRequest | CreateCustomerCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer(
        self, customer_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerResponse, RawError]:
        """Deletes a customer profile from a business.

        To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to delete.
            version: The current version of the customer profile. As a best practice, you should include this parameter
                to enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control. For more information, see `Delete a customer profile
                <https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}"),
            path_params=[param[str]("customer_id", customer_id)],
            query_params=[param[int | None]("version", version)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_customer_card(
        self, customer_id: str, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerCardResponse, RawError]:
        """Removes a card on file from a customer.

        Args:
            customer_id: The ID of the customer that the card on file belongs to.
            card_id: The ID of the card on file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}/cards/{card_id}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("card_id", card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_customers(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        sort_field: CustomerSortFieldOrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        count: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomersResponse, RawError]:
        """Lists customer profiles associated with a Square account.

        Under normal operating conditions, newly created or updated customer profiles become available for the listing
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 100, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 100. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            sort_field: Indicates how customers should be sorted. The default value is ``DEFAULT``.
            sort_order: Indicates whether customers should be sorted in ascending (``ASC``) or descending (``DESC``)
                order. The default value is ``ASC``.
            count: Indicates whether to return the total count of customers in the ``count`` field of the response. The
                default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
                param[CustomerSortFieldOrStr | None]("sort_field", sort_field),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[bool | None]("count", count),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def remove_group_from_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RemoveGroupFromCustomerResponse, RawError]:
        """Removes a group membership from a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to remove from the group.
            group_id: The ID of the customer group to remove the customer from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}/groups/{group_id}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RemoveGroupFromCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_customer(
        self, customer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerResponse, RawError]:
        """Returns details for a single customer.

        Args:
            customer_id: The ID of the customer to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/{customer_id}"),
            path_params=[param[str]("customer_id", customer_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_customers(
        self,
        body: SearchCustomersRequest | SearchCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchCustomersResponse, RawError]:
        """Searches the customer profiles associated with a Square account using one or more supported query filters.

        Calling ``SearchCustomers`` without any explicit query filter returns all customer profiles ordered
        alphabetically based on ``given_name`` and ``family_name``.

        Under normal operating conditions, newly created or updated customer profiles become available for the search
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchCustomersRequest | SearchCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_customer(
        self,
        customer_id: str,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCustomerResponse, RawError]:
        """Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required
        in the request. To add or update a field, specify the new value. To remove a field, specify ``null``.

        To update a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/customers/{customer_id}"),
            path_params=[param[str]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerRequest | UpdateCustomerRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncCustomersWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def add_group_to_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AddGroupToCustomerResponse, RawError]:
        """Adds a group membership to a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to add to a group.
            group_id: The ID of the customer group to add the customer to.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/customers/{customer_id}/groups/{group_id}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[AddGroupToCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_create_customers(
        self,
        body: BulkCreateCustomersRequest | BulkCreateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateCustomersResponse, RawError]:
        """Creates multiple `customer profiles <entity:Customer>`__ for a business.

        This endpoint takes a map of individual create requests and returns a map of responses.

        You must provide at least one of the following values in each create request:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-create"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkCreateCustomersRequest | BulkCreateCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkCreateCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_delete_customers(
        self,
        body: BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkDeleteCustomersResponse, RawError]:
        """Deletes multiple customer profiles.

        The endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-delete"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkDeleteCustomersRequest | BulkDeleteCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkDeleteCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_retrieve_customers(
        self,
        body: BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveCustomersResponse, RawError]:
        """Retrieves multiple customer profiles.

        This endpoint takes a list of customer IDs and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveCustomersRequest | BulkRetrieveCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_update_customers(
        self,
        body: BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateCustomersResponse, RawError]:
        """Updates multiple customer profiles.

        This endpoint takes a map of individual update requests and returns a map of responses.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/bulk-update"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkUpdateCustomersRequest | BulkUpdateCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpdateCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_customer(
        self,
        body: CreateCustomerRequest | CreateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerResponse, RawError]:
        """Creates a new customer for a business.

        You must provide at least one of the following values in your request to this endpoint:

        - ``given_name``
        - ``family_name``
        - ``company_name``
        - ``email_address``
        - ``phone_number``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerRequest | CreateCustomerRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_customer_card(
        self,
        customer_id: str,
        body: CreateCustomerCardRequest | CreateCustomerCardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateCustomerCardResponse, RawError]:
        """Adds a card on file to an existing customer.

        As with charges, calls to ``CreateCustomerCard`` are idempotent. Multiple calls with the same card nonce return
        the same card record that was created with the provided nonce during the _first_ call.

        Args:
            customer_id: The Square ID of the customer profile the card is linked to.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/{customer_id}/cards"),
            path_params=[param[str]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateCustomerCardRequest | CreateCustomerCardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateCustomerCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer(
        self, customer_id: str, *, version: int | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerResponse, RawError]:
        """Deletes a customer profile from a business.

        To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to delete.
            version: The current version of the customer profile. As a best practice, you should include this parameter
                to enable `optimistic concurrency
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/optimistic-concurrency>`__
                control. For more information, see `Delete a customer profile
                <https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}"),
            path_params=[param[str]("customer_id", customer_id)],
            query_params=[param[int | None]("version", version)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_customer_card(
        self, customer_id: str, card_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteCustomerCardResponse, RawError]:
        """Removes a card on file from a customer.

        Args:
            customer_id: The ID of the customer that the card on file belongs to.
            card_id: The ID of the card on file to delete.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}/cards/{card_id}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("card_id", card_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteCustomerCardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_customers(
        self,
        *,
        cursor: str | None = None,
        limit: int | None = None,
        sort_field: CustomerSortFieldOrStr | None = None,
        sort_order: SortOrderOrStr | None = None,
        count: bool | None = False,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListCustomersResponse, RawError]:
        """Lists customer profiles associated with a Square account.

        Under normal operating conditions, newly created or updated customer profiles become available for the listing
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for your original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            limit: The maximum number of results to return in a single page. This limit is advisory. The response might
                contain more or fewer results. If the specified limit is less than 1 or greater than 100, Square returns
                a ``400 VALUE_TOO_LOW`` or ``400 VALUE_TOO_HIGH`` error. The default value is 100. For more information,
                see `Pagination <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            sort_field: Indicates how customers should be sorted. The default value is ``DEFAULT``.
            sort_order: Indicates whether customers should be sorted in ascending (``ASC``) or descending (``DESC``)
                order. The default value is ``ASC``.
            count: Indicates whether to return the total count of customers in the ``count`` field of the response. The
                default value is ``false``.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[int | None]("limit", limit),
                param[CustomerSortFieldOrStr | None]("sort_field", sort_field),
                param[SortOrderOrStr | None]("sort_order", sort_order),
                param[bool | None]("count", count),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def remove_group_from_customer(
        self, customer_id: str, group_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RemoveGroupFromCustomerResponse, RawError]:
        """Removes a group membership from a customer.

        The customer is identified by the ``customer_id`` value and the customer group is identified by the ``group_id``
        value.

        Args:
            customer_id: The ID of the customer to remove from the group.
            group_id: The ID of the customer group to remove the customer from.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/customers/{customer_id}/groups/{group_id}"),
            path_params=[param[str]("customer_id", customer_id), param[str]("group_id", group_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RemoveGroupFromCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_customer(
        self, customer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveCustomerResponse, RawError]:
        """Returns details for a single customer.

        Args:
            customer_id: The ID of the customer to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/customers/{customer_id}"),
            path_params=[param[str]("customer_id", customer_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_customers(
        self,
        body: SearchCustomersRequest | SearchCustomersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchCustomersResponse, RawError]:
        """Searches the customer profiles associated with a Square account using one or more supported query filters.

        Calling ``SearchCustomers`` without any explicit query filter returns all customer profiles ordered
        alphabetically based on ``given_name`` and ``family_name``.

        Under normal operating conditions, newly created or updated customer profiles become available for the search
        operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to
        one minute or longer, especially during network incidents and outages.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/customers/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchCustomersRequest | SearchCustomersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchCustomersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_customer(
        self,
        customer_id: str,
        body: UpdateCustomerRequest | UpdateCustomerRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateCustomerResponse, RawError]:
        """Updates a customer profile. This endpoint supports sparse updates, so only new or changed fields are required
        in the request. To add or update a field, specify the new value. To remove a field, specify ``null``.

        To update a customer profile that was created by merging existing profiles, you must use the ID of the newly
        created profile.

        Args:
            customer_id: The ID of the customer to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/customers/{customer_id}"),
            path_params=[param[str]("customer_id", customer_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateCustomerRequest | UpdateCustomerRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateCustomerResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
