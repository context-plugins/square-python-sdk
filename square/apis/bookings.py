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
from ..models.bulk_retrieve_bookings_request import BulkRetrieveBookingsRequest, BulkRetrieveBookingsRequestDict
from ..models.bulk_retrieve_bookings_response import BulkRetrieveBookingsResponse
from ..models.bulk_retrieve_team_member_booking_profiles_request import (
    BulkRetrieveTeamMemberBookingProfilesRequest,
    BulkRetrieveTeamMemberBookingProfilesRequestDict,
)
from ..models.bulk_retrieve_team_member_booking_profiles_response import BulkRetrieveTeamMemberBookingProfilesResponse
from ..models.cancel_booking_request import CancelBookingRequest, CancelBookingRequestDict
from ..models.cancel_booking_response import CancelBookingResponse
from ..models.create_booking_request import CreateBookingRequest, CreateBookingRequestDict
from ..models.create_booking_response import CreateBookingResponse
from ..models.list_bookings_response import ListBookingsResponse
from ..models.list_location_booking_profiles_response import ListLocationBookingProfilesResponse
from ..models.list_team_member_booking_profiles_response import ListTeamMemberBookingProfilesResponse
from ..models.retrieve_booking_response import RetrieveBookingResponse
from ..models.retrieve_business_booking_profile_response import RetrieveBusinessBookingProfileResponse
from ..models.retrieve_location_booking_profile_response import RetrieveLocationBookingProfileResponse
from ..models.retrieve_team_member_booking_profile_response import RetrieveTeamMemberBookingProfileResponse
from ..models.search_availability_request import SearchAvailabilityRequest, SearchAvailabilityRequestDict
from ..models.search_availability_response import SearchAvailabilityResponse
from ..models.update_booking_request import UpdateBookingRequest, UpdateBookingRequestDict
from ..models.update_booking_response import UpdateBookingResponse
from ..server.server import Server


class Bookings:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BookingsWithRawResponse(client, server, auth)

    def bulk_retrieve_bookings(
        self,
        body: BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveBookingsResponse:
        """Bulk-Retrieves a list of bookings by booking IDs.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_retrieve_bookings(body, request_options=request_options).unwrap()

    def bulk_retrieve_team_member_booking_profiles(
        self,
        body: BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveTeamMemberBookingProfilesResponse:
        """Retrieves one or more team members' booking profiles.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_retrieve_team_member_booking_profiles(
            body, request_options=request_options
        ).unwrap()

    def cancel_booking(
        self,
        booking_id: str,
        body: CancelBookingRequest | CancelBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelBookingResponse:
        """Cancels an existing booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-cancelled booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.cancel_booking(booking_id, body, request_options=request_options).unwrap()

    def create_booking(
        self,
        body: CreateBookingRequest | CreateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBookingResponse:
        """Creates a booking.

        The required input must include the following:
        - ``Booking.location_id``
        - ``Booking.start_at``
        - ``Booking.AppointmentSegment.team_member_id``
        - ``Booking.AppointmentSegment.service_variation_id``
        - ``Booking.AppointmentSegment.service_variation_version``

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_booking(body, request_options=request_options).unwrap()

    def list_bookings(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        team_member_id: str | None = None,
        location_id: str | None = None,
        start_at_min: str | None = None,
        start_at_max: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBookingsResponse:
        """Retrieve a collection of bookings.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results per page to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            customer_id: The `customer <entity:Customer>`__ for whom to retrieve bookings. If this is not set, bookings
                for all customers are retrieved.
            team_member_id: The team member for whom to retrieve bookings. If this is not set, bookings of all members
                are retrieved.
            location_id: The location for which to retrieve bookings. If this is not set, all locations' bookings are
                retrieved.
            start_at_min: The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the
                current time is used.
            start_at_max: The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time
                of 31 days after ``start_at_min`` is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_bookings(
            limit=limit,
            cursor=cursor,
            customer_id=customer_id,
            team_member_id=team_member_id,
            location_id=location_id,
            start_at_min=start_at_min,
            start_at_max=start_at_max,
            request_options=request_options,
        ).unwrap()

    def list_location_booking_profiles(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLocationBookingProfilesResponse:
        """Lists location booking profiles of a seller.

        Args:
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_location_booking_profiles(
            limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: bool | None = False,
        limit: int | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTeamMemberBookingProfilesResponse:
        """Lists booking profiles for team members.

        Args:
            bookable_only: Indicates whether to include only bookable team members in the returned result (``true``) or
                not (``false``).
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            location_id: Indicates whether to include only team members enabled at the given location in the returned
                result.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_team_member_booking_profiles(
            bookable_only=bookable_only,
            limit=limit,
            cursor=cursor,
            location_id=location_id,
            request_options=request_options,
        ).unwrap()

    def retrieve_booking(
        self, booking_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveBookingResponse:
        """Retrieves a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-retrieved booking.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_booking(booking_id, request_options=request_options).unwrap()

    def retrieve_business_booking_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveBusinessBookingProfileResponse:
        """Retrieves a seller's booking profile.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_business_booking_profile(request_options=request_options).unwrap()

    def retrieve_location_booking_profile(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationBookingProfileResponse:
        """Retrieves a seller's location booking profile.

        Args:
            location_id: The ID of the location to retrieve the booking profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_location_booking_profile(
            location_id, request_options=request_options
        ).unwrap()

    def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTeamMemberBookingProfileResponse:
        """Retrieves a team member's booking profile.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_team_member_booking_profile(
            team_member_id, request_options=request_options
        ).unwrap()

    def search_availability(
        self,
        body: SearchAvailabilityRequest | SearchAvailabilityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchAvailabilityResponse:
        """Searches for availabilities for booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_availability(body, request_options=request_options).unwrap()

    def update_booking(
        self,
        booking_id: str,
        body: UpdateBookingRequest | UpdateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateBookingResponse:
        """Updates a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-updated booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_booking(booking_id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> BookingsWithRawResponse:
        return self._with_raw_response


class AsyncBookings:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBookingsWithRawResponse(client, server, auth)

    async def bulk_retrieve_bookings(
        self,
        body: BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveBookingsResponse:
        """Bulk-Retrieves a list of bookings by booking IDs.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_retrieve_bookings(body, request_options=request_options)).unwrap()

    async def bulk_retrieve_team_member_booking_profiles(
        self,
        body: BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkRetrieveTeamMemberBookingProfilesResponse:
        """Retrieves one or more team members' booking profiles.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_retrieve_team_member_booking_profiles(
                body, request_options=request_options
            )
        ).unwrap()

    async def cancel_booking(
        self,
        booking_id: str,
        body: CancelBookingRequest | CancelBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CancelBookingResponse:
        """Cancels an existing booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-cancelled booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.cancel_booking(booking_id, body, request_options=request_options)
        ).unwrap()

    async def create_booking(
        self,
        body: CreateBookingRequest | CreateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBookingResponse:
        """Creates a booking.

        The required input must include the following:
        - ``Booking.location_id``
        - ``Booking.start_at``
        - ``Booking.AppointmentSegment.team_member_id``
        - ``Booking.AppointmentSegment.service_variation_id``
        - ``Booking.AppointmentSegment.service_variation_version``

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_booking(body, request_options=request_options)).unwrap()

    async def list_bookings(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        team_member_id: str | None = None,
        location_id: str | None = None,
        start_at_min: str | None = None,
        start_at_max: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBookingsResponse:
        """Retrieve a collection of bookings.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results per page to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            customer_id: The `customer <entity:Customer>`__ for whom to retrieve bookings. If this is not set, bookings
                for all customers are retrieved.
            team_member_id: The team member for whom to retrieve bookings. If this is not set, bookings of all members
                are retrieved.
            location_id: The location for which to retrieve bookings. If this is not set, all locations' bookings are
                retrieved.
            start_at_min: The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the
                current time is used.
            start_at_max: The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time
                of 31 days after ``start_at_min`` is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_bookings(
                limit=limit,
                cursor=cursor,
                customer_id=customer_id,
                team_member_id=team_member_id,
                location_id=location_id,
                start_at_min=start_at_min,
                start_at_max=start_at_max,
                request_options=request_options,
            )
        ).unwrap()

    async def list_location_booking_profiles(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListLocationBookingProfilesResponse:
        """Lists location booking profiles of a seller.

        Args:
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_location_booking_profiles(
                limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: bool | None = False,
        limit: int | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTeamMemberBookingProfilesResponse:
        """Lists booking profiles for team members.

        Args:
            bookable_only: Indicates whether to include only bookable team members in the returned result (``true``) or
                not (``false``).
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            location_id: Indicates whether to include only team members enabled at the given location in the returned
                result.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_team_member_booking_profiles(
                bookable_only=bookable_only,
                limit=limit,
                cursor=cursor,
                location_id=location_id,
                request_options=request_options,
            )
        ).unwrap()

    async def retrieve_booking(
        self, booking_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveBookingResponse:
        """Retrieves a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-retrieved booking.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_booking(booking_id, request_options=request_options)).unwrap()

    async def retrieve_business_booking_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveBusinessBookingProfileResponse:
        """Retrieves a seller's booking profile.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_business_booking_profile(request_options=request_options)
        ).unwrap()

    async def retrieve_location_booking_profile(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveLocationBookingProfileResponse:
        """Retrieves a seller's location booking profile.

        Args:
            location_id: The ID of the location to retrieve the booking profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_location_booking_profile(
                location_id, request_options=request_options
            )
        ).unwrap()

    async def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTeamMemberBookingProfileResponse:
        """Retrieves a team member's booking profile.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_team_member_booking_profile(
                team_member_id, request_options=request_options
            )
        ).unwrap()

    async def search_availability(
        self,
        body: SearchAvailabilityRequest | SearchAvailabilityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchAvailabilityResponse:
        """Searches for availabilities for booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_availability(body, request_options=request_options)).unwrap()

    async def update_booking(
        self,
        booking_id: str,
        body: UpdateBookingRequest | UpdateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateBookingResponse:
        """Updates a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-updated booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_booking(booking_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncBookingsWithRawResponse:
        return self._with_raw_response


class BookingsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_retrieve_bookings(
        self,
        body: BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveBookingsResponse, RawError]:
        """Bulk-Retrieves a list of bookings by booking IDs.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveBookingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_retrieve_team_member_booking_profiles(
        self,
        body: BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveTeamMemberBookingProfilesResponse, RawError]:
        """Retrieves one or more team members' booking profiles.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/team-member-booking-profiles/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveTeamMemberBookingProfilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def cancel_booking(
        self,
        booking_id: str,
        body: CancelBookingRequest | CancelBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelBookingResponse, RawError]:
        """Cancels an existing booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-cancelled booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/{booking_id}/cancel"),
            path_params=[param[str]("booking_id", booking_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelBookingRequest | CancelBookingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_booking(
        self,
        body: CreateBookingRequest | CreateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBookingResponse, RawError]:
        """Creates a booking.

        The required input must include the following:
        - ``Booking.location_id``
        - ``Booking.start_at``
        - ``Booking.AppointmentSegment.team_member_id``
        - ``Booking.AppointmentSegment.service_variation_id``
        - ``Booking.AppointmentSegment.service_variation_version``

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateBookingRequest | CreateBookingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_bookings(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        team_member_id: str | None = None,
        location_id: str | None = None,
        start_at_min: str | None = None,
        start_at_max: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBookingsResponse, RawError]:
        """Retrieve a collection of bookings.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results per page to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            customer_id: The `customer <entity:Customer>`__ for whom to retrieve bookings. If this is not set, bookings
                for all customers are retrieved.
            team_member_id: The team member for whom to retrieve bookings. If this is not set, bookings of all members
                are retrieved.
            location_id: The location for which to retrieve bookings. If this is not set, all locations' bookings are
                retrieved.
            start_at_min: The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the
                current time is used.
            start_at_max: The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time
                of 31 days after ``start_at_min`` is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("customer_id", customer_id),
                param[str | None]("team_member_id", team_member_id),
                param[str | None]("location_id", location_id),
                param[str | None]("start_at_min", start_at_min),
                param[str | None]("start_at_max", start_at_max),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBookingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_location_booking_profiles(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLocationBookingProfilesResponse, RawError]:
        """Lists location booking profiles of a seller.

        Args:
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/location-booking-profiles"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLocationBookingProfilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: bool | None = False,
        limit: int | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTeamMemberBookingProfilesResponse, RawError]:
        """Lists booking profiles for team members.

        Args:
            bookable_only: Indicates whether to include only bookable team members in the returned result (``true``) or
                not (``false``).
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            location_id: Indicates whether to include only team members enabled at the given location in the returned
                result.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/team-member-booking-profiles"),
            query_params=[
                param[bool | None]("bookable_only", bookable_only),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListTeamMemberBookingProfilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_booking(
        self, booking_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveBookingResponse, RawError]:
        """Retrieves a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-retrieved booking.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/{booking_id}"),
            path_params=[param[str]("booking_id", booking_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_business_booking_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveBusinessBookingProfileResponse, RawError]:
        """Retrieves a seller's booking profile.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/business-booking-profile"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBusinessBookingProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_location_booking_profile(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationBookingProfileResponse, RawError]:
        """Retrieves a seller's location booking profile.

        Args:
            location_id: The ID of the location to retrieve the booking profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/location-booking-profiles/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLocationBookingProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTeamMemberBookingProfileResponse, RawError]:
        """Retrieves a team member's booking profile.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/team-member-booking-profiles/{team_member_id}"),
            path_params=[param[str]("team_member_id", team_member_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTeamMemberBookingProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_availability(
        self,
        body: SearchAvailabilityRequest | SearchAvailabilityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchAvailabilityResponse, RawError]:
        """Searches for availabilities for booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/availability/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchAvailabilityRequest | SearchAvailabilityRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchAvailabilityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_booking(
        self,
        booking_id: str,
        body: UpdateBookingRequest | UpdateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateBookingResponse, RawError]:
        """Updates a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-updated booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/bookings/{booking_id}"),
            path_params=[param[str]("booking_id", booking_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateBookingRequest | UpdateBookingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncBookingsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_retrieve_bookings(
        self,
        body: BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveBookingsResponse, RawError]:
        """Bulk-Retrieves a list of bookings by booking IDs.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BulkRetrieveBookingsRequest | BulkRetrieveBookingsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveBookingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_retrieve_team_member_booking_profiles(
        self,
        body: BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkRetrieveTeamMemberBookingProfilesResponse, RawError]:
        """Retrieves one or more team members' booking profiles.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/team-member-booking-profiles/bulk-retrieve"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                BulkRetrieveTeamMemberBookingProfilesRequest | BulkRetrieveTeamMemberBookingProfilesRequestDict
            ](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkRetrieveTeamMemberBookingProfilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def cancel_booking(
        self,
        booking_id: str,
        body: CancelBookingRequest | CancelBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CancelBookingResponse, RawError]:
        """Cancels an existing booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-cancelled booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/{booking_id}/cancel"),
            path_params=[param[str]("booking_id", booking_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CancelBookingRequest | CancelBookingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CancelBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_booking(
        self,
        body: CreateBookingRequest | CreateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBookingResponse, RawError]:
        """Creates a booking.

        The required input must include the following:
        - ``Booking.location_id``
        - ``Booking.start_at``
        - ``Booking.AppointmentSegment.team_member_id``
        - ``Booking.AppointmentSegment.service_variation_id``
        - ``Booking.AppointmentSegment.service_variation_version``

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateBookingRequest | CreateBookingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_bookings(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        customer_id: str | None = None,
        team_member_id: str | None = None,
        location_id: str | None = None,
        start_at_min: str | None = None,
        start_at_max: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBookingsResponse, RawError]:
        """Retrieve a collection of bookings.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            limit: The maximum number of results per page to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            customer_id: The `customer <entity:Customer>`__ for whom to retrieve bookings. If this is not set, bookings
                for all customers are retrieved.
            team_member_id: The team member for whom to retrieve bookings. If this is not set, bookings of all members
                are retrieved.
            location_id: The location for which to retrieve bookings. If this is not set, all locations' bookings are
                retrieved.
            start_at_min: The RFC 3339 timestamp specifying the earliest of the start time. If this is not set, the
                current time is used.
            start_at_max: The RFC 3339 timestamp specifying the latest of the start time. If this is not set, the time
                of 31 days after ``start_at_min`` is used.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings"),
            query_params=[
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("customer_id", customer_id),
                param[str | None]("team_member_id", team_member_id),
                param[str | None]("location_id", location_id),
                param[str | None]("start_at_min", start_at_min),
                param[str | None]("start_at_max", start_at_max),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBookingsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_location_booking_profiles(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListLocationBookingProfilesResponse, RawError]:
        """Lists location booking profiles of a seller.

        Args:
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/location-booking-profiles"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListLocationBookingProfilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_team_member_booking_profiles(
        self,
        *,
        bookable_only: bool | None = False,
        limit: int | None = None,
        cursor: str | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTeamMemberBookingProfilesResponse, RawError]:
        """Lists booking profiles for team members.

        Args:
            bookable_only: Indicates whether to include only bookable team members in the returned result (``true``) or
                not (``false``).
            limit: The maximum number of results to return in a paged response.
            cursor: The pagination cursor from the preceding response to return the next page of the results. Do not set
                this when retrieving the first page of the results.
            location_id: Indicates whether to include only team members enabled at the given location in the returned
                result.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/team-member-booking-profiles"),
            query_params=[
                param[bool | None]("bookable_only", bookable_only),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
                param[str | None]("location_id", location_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListTeamMemberBookingProfilesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_booking(
        self, booking_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveBookingResponse, RawError]:
        """Retrieves a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-retrieved booking.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/{booking_id}"),
            path_params=[param[str]("booking_id", booking_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_business_booking_profile(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveBusinessBookingProfileResponse, RawError]:
        """Retrieves a seller's booking profile.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/business-booking-profile"),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveBusinessBookingProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_location_booking_profile(
        self, location_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveLocationBookingProfileResponse, RawError]:
        """Retrieves a seller's location booking profile.

        Args:
            location_id: The ID of the location to retrieve the booking profile.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/location-booking-profiles/{location_id}"),
            path_params=[param[str]("location_id", location_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveLocationBookingProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_team_member_booking_profile(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTeamMemberBookingProfileResponse, RawError]:
        """Retrieves a team member's booking profile.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/bookings/team-member-booking-profiles/{team_member_id}"),
            path_params=[param[str]("team_member_id", team_member_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTeamMemberBookingProfileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_availability(
        self,
        body: SearchAvailabilityRequest | SearchAvailabilityRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchAvailabilityResponse, RawError]:
        """Searches for availabilities for booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_READ`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_READ`` and ``APPOINTMENTS_READ`` for the OAuth
        scope.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/bookings/availability/search"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SearchAvailabilityRequest | SearchAvailabilityRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchAvailabilityResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_booking(
        self,
        booking_id: str,
        body: UpdateBookingRequest | UpdateBookingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateBookingResponse, RawError]:
        """Updates a booking.

        To call this endpoint with buyer-level permissions, set ``APPOINTMENTS_WRITE`` for the OAuth scope. To call this
        endpoint with seller-level permissions, set ``APPOINTMENTS_ALL_WRITE`` and ``APPOINTMENTS_WRITE`` for the OAuth
        scope.

        For calls to this endpoint with seller-level permissions to succeed, the seller must have subscribed to
        *Appointments Plus* or *Appointments Premium*.

        Args:
            booking_id: The ID of the `Booking <entity:Booking>`__ object representing the to-be-updated booking.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/bookings/{booking_id}"),
            path_params=[param[str]("booking_id", booking_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UpdateBookingRequest | UpdateBookingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateBookingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
