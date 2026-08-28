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
from ..models.bulk_publish_scheduled_shifts_request import (
    BulkPublishScheduledShiftsRequest,
    BulkPublishScheduledShiftsRequestDict,
)
from ..models.bulk_publish_scheduled_shifts_response import BulkPublishScheduledShiftsResponse
from ..models.create_break_type_request import CreateBreakTypeRequest, CreateBreakTypeRequestDict
from ..models.create_break_type_response import CreateBreakTypeResponse
from ..models.create_scheduled_shift_request import CreateScheduledShiftRequest, CreateScheduledShiftRequestDict
from ..models.create_scheduled_shift_response import CreateScheduledShiftResponse
from ..models.create_shift_request import CreateShiftRequest, CreateShiftRequestDict
from ..models.create_shift_response import CreateShiftResponse
from ..models.create_timecard_request import CreateTimecardRequest, CreateTimecardRequestDict
from ..models.create_timecard_response import CreateTimecardResponse
from ..models.delete_break_type_response import DeleteBreakTypeResponse
from ..models.delete_shift_response import DeleteShiftResponse
from ..models.delete_timecard_response import DeleteTimecardResponse
from ..models.get_break_type_response import GetBreakTypeResponse
from ..models.get_employee_wage_response import GetEmployeeWageResponse
from ..models.get_shift_response import GetShiftResponse
from ..models.get_team_member_wage_response import GetTeamMemberWageResponse
from ..models.list_break_types_response import ListBreakTypesResponse
from ..models.list_employee_wages_response import ListEmployeeWagesResponse
from ..models.list_team_member_wages_response import ListTeamMemberWagesResponse
from ..models.list_workweek_configs_response import ListWorkweekConfigsResponse
from ..models.publish_scheduled_shift_request import PublishScheduledShiftRequest, PublishScheduledShiftRequestDict
from ..models.publish_scheduled_shift_response import PublishScheduledShiftResponse
from ..models.retrieve_scheduled_shift_response import RetrieveScheduledShiftResponse
from ..models.retrieve_timecard_response import RetrieveTimecardResponse
from ..models.search_scheduled_shifts_request import SearchScheduledShiftsRequest, SearchScheduledShiftsRequestDict
from ..models.search_scheduled_shifts_response import SearchScheduledShiftsResponse
from ..models.search_shifts_request import SearchShiftsRequest, SearchShiftsRequestDict
from ..models.search_shifts_response import SearchShiftsResponse
from ..models.search_timecards_request import SearchTimecardsRequest, SearchTimecardsRequestDict
from ..models.search_timecards_response import SearchTimecardsResponse
from ..models.update_break_type_request import UpdateBreakTypeRequest, UpdateBreakTypeRequestDict
from ..models.update_break_type_response import UpdateBreakTypeResponse
from ..models.update_scheduled_shift_request import UpdateScheduledShiftRequest, UpdateScheduledShiftRequestDict
from ..models.update_scheduled_shift_response import UpdateScheduledShiftResponse
from ..models.update_shift_request import UpdateShiftRequest, UpdateShiftRequestDict
from ..models.update_shift_response import UpdateShiftResponse
from ..models.update_timecard_request import UpdateTimecardRequest, UpdateTimecardRequestDict
from ..models.update_timecard_response import UpdateTimecardResponse
from ..models.update_workweek_config_request import UpdateWorkweekConfigRequest, UpdateWorkweekConfigRequestDict
from ..models.update_workweek_config_response import UpdateWorkweekConfigResponse
from ..server.server import Server


class Labor:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = LaborWithRawResponse(client, server, auth)

    def bulk_publish_scheduled_shifts(
        self,
        body: BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkPublishScheduledShiftsResponse:
        """Publishes 1 - 100 scheduled shifts. This endpoint takes a map of individual publish requests and returns a
        map of responses. When a scheduled shift is published, Square keeps the ``draft_shift_details`` field as is and
        copies it to the ``published_shift_details`` field.

        The minimum ``start_at`` and maximum ``end_at`` timestamps of all shifts in a ``BulkPublishScheduledShifts``
        request must fall within a two-week period.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_publish_scheduled_shifts(body, request_options=request_options).unwrap()

    def create_break_type(
        self,
        body: CreateBreakTypeRequest | CreateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBreakTypeResponse:
        """Creates a new ``BreakType``.

        A ``BreakType`` is a template for creating ``Break`` objects. You must provide the following values in your
        request to this endpoint:

        - ``location_id``
        - ``break_name``
        - ``expected_duration``
        - ``is_paid``

        You can only have three ``BreakType`` instances per location. If you attempt to add a fourth ``BreakType`` for a
        location, an ``INVALID_REQUEST_ERROR`` "Exceeded limit of 3 breaks per location." is returned.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_break_type(body, request_options=request_options).unwrap()

    def create_scheduled_shift(
        self,
        body: CreateScheduledShiftRequest | CreateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateScheduledShiftResponse:
        """Creates a scheduled shift by providing draft shift details such as job ID, team member assignment, and start
        and end times.

        The following ``draft_shift_details`` fields are required:
        - ``location_id``
        - ``job_id``
        - ``start_at``
        - ``end_at``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_scheduled_shift(body, request_options=request_options).unwrap()

    def create_shift(
        self, body: CreateShiftRequest | CreateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateShiftResponse:
        """Creates a new ``Shift``.

        A ``Shift`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Shift`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Shift`` is ``OPEN`` and the team member has another
        shift with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another shift for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Shift.start_at``, a break ``end_at`` is after the ``Shift.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_shift(body, request_options=request_options).unwrap()

    def create_timecard(
        self,
        body: CreateTimecardRequest | CreateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTimecardResponse:
        """Creates a new ``Timecard``.

        A ``Timecard`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Timecard`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Timecard`` is ``OPEN`` and the team member has another
        timecard with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another timecard for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Timecard.start_at``, a break ``end_at`` is after the ``Timecard.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_timecard(body, request_options=request_options).unwrap()

    def delete_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteBreakTypeResponse:
        """Deletes an existing ``BreakType``.

        A ``BreakType`` can be deleted even if it is referenced from a ``Shift``.

        Args:
            id: The UUID for the ``BreakType`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_break_type(id, request_options=request_options).unwrap()

    def delete_shift(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> DeleteShiftResponse:
        """Deletes a ``Shift``.

        Args:
            id: The UUID for the ``Shift`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_shift(id, request_options=request_options).unwrap()

    def delete_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteTimecardResponse:
        """Deletes a ``Timecard``.

        Args:
            id: The UUID for the ``Timecard`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_timecard(id, request_options=request_options).unwrap()

    def get_break_type(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetBreakTypeResponse:
        """Returns a single ``BreakType`` specified by ``id``.

        Args:
            id: The UUID for the ``BreakType`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_break_type(id, request_options=request_options).unwrap()

    def get_employee_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetEmployeeWageResponse:
        """Returns a single ``EmployeeWage`` specified by ``id``.

        Args:
            id: The UUID for the ``EmployeeWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_employee_wage(id, request_options=request_options).unwrap()

    def get_shift(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetShiftResponse:
        """Returns a single ``Shift`` specified by ``id``.

        Args:
            id: The UUID for the ``Shift`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_shift(id, request_options=request_options).unwrap()

    def get_team_member_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTeamMemberWageResponse:
        """Returns a single ``TeamMemberWage`` specified by ``id``.

        Args:
            id: The UUID for the ``TeamMemberWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_team_member_wage(id, request_options=request_options).unwrap()

    def list_break_types(
        self,
        *,
        location_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBreakTypesResponse:
        """Returns a paginated list of ``BreakType`` instances for a business.

        Args:
            location_id: Filter the returned ``BreakType`` results to only those that are associated with the specified
                location.
            limit: The maximum number of ``BreakType`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``BreakType`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_break_types(
            location_id=location_id, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_employee_wages(
        self,
        *,
        employee_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEmployeeWagesResponse:
        """Returns a paginated list of ``EmployeeWage`` instances for a business.

        Args:
            employee_id: Filter the returned wages to only those that are associated with the specified employee.
            limit: The maximum number of ``EmployeeWage`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_employee_wages(
            employee_id=employee_id, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_team_member_wages(
        self,
        *,
        team_member_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTeamMemberWagesResponse:
        """Returns a paginated list of ``TeamMemberWage`` instances for a business.

        Args:
            team_member_id: Filter the returned wages to only those that are associated with the specified team member.
            limit: The maximum number of ``TeamMemberWage`` results to return per page. The number can range between 1
                and 200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_team_member_wages(
            team_member_id=team_member_id, limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_workweek_configs(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkweekConfigsResponse:
        """Returns a list of ``WorkweekConfig`` instances for a business.

        Args:
            limit: The maximum number of ``WorkweekConfigs`` results to return per page.
            cursor: A pointer to the next page of ``WorkweekConfig`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_workweek_configs(
            limit=limit, cursor=cursor, request_options=request_options
        ).unwrap()

    def publish_scheduled_shift(
        self,
        id: str,
        body: PublishScheduledShiftRequest | PublishScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublishScheduledShiftResponse:
        """Publishes a scheduled shift. When a scheduled shift is published, Square keeps the ``draft_shift_details``
        field as is and copies it to the ``published_shift_details`` field.

        Args:
            id: The ID of the scheduled shift to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.publish_scheduled_shift(id, body, request_options=request_options).unwrap()

    def retrieve_scheduled_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveScheduledShiftResponse:
        """Retrieves a scheduled shift by ID.

        Args:
            id: The ID of the scheduled shift to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_scheduled_shift(id, request_options=request_options).unwrap()

    def retrieve_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTimecardResponse:
        """Returns a single ``Timecard`` specified by ``id``.

        Args:
            id: The UUID for the ``Timecard`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_timecard(id, request_options=request_options).unwrap()

    def search_scheduled_shifts(
        self,
        body: SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchScheduledShiftsResponse:
        """Returns a paginated list of scheduled shifts, with optional filter and sort settings. By default, results are
        sorted by ``start_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_scheduled_shifts(body, request_options=request_options).unwrap()

    def search_shifts(
        self,
        body: SearchShiftsRequest | SearchShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchShiftsResponse:
        """Returns a paginated list of ``Shift`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Shift status (``OPEN`` or ``CLOSED``)
        - Shift start
        - Shift end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_shifts(body, request_options=request_options).unwrap()

    def search_timecards(
        self,
        body: SearchTimecardsRequest | SearchTimecardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTimecardsResponse:
        """Returns a paginated list of ``Timecard`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Timecard status (``OPEN`` or ``CLOSED``)
        - Timecard start
        - Timecard end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_timecards(body, request_options=request_options).unwrap()

    def update_break_type(
        self,
        id: str,
        body: UpdateBreakTypeRequest | UpdateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateBreakTypeResponse:
        """Updates an existing ``BreakType``.

        Args:
            id: The UUID for the ``BreakType`` being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_break_type(id, body, request_options=request_options).unwrap()

    def update_scheduled_shift(
        self,
        id: str,
        body: UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateScheduledShiftResponse:
        """Updates the draft shift details for a scheduled shift. This endpoint supports sparse updates, so only new,
        changed, or removed fields are required in the request. You must publish the shift to make updates public.

        You can make the following updates to ``draft_shift_details``:
        - Change the ``location_id``, ``job_id``, ``start_at``, and ``end_at`` fields.
        - Add, change, or clear the ``team_member_id`` and ``notes`` fields. To clear these fields,
        set the value to null.
        - Change the ``is_deleted`` field. To delete a scheduled shift, set ``is_deleted`` to true
        and then publish the shift.

        Args:
            id: The ID of the scheduled shift to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_scheduled_shift(id, body, request_options=request_options).unwrap()

    def update_shift(
        self,
        id: str,
        body: UpdateShiftRequest | UpdateShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShiftResponse:
        """Updates an existing ``Shift``.

        When adding a ``Break`` to a ``Shift``, any earlier ``Break`` instances in the ``Shift`` have the ``end_at``
        property set to a valid RFC-3339 datetime string.

        When closing a ``Shift``, all ``Break`` instances in the ``Shift`` must be complete with ``end_at`` set on each
        ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_shift(id, body, request_options=request_options).unwrap()

    def update_timecard(
        self,
        id: str,
        body: UpdateTimecardRequest | UpdateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateTimecardResponse:
        """Updates an existing ``Timecard``.

        When adding a ``Break`` to a ``Timecard``, any earlier ``Break`` instances in the ``Timecard`` have the
        ``end_at`` property set to a valid RFC-3339 datetime string.

        When closing a ``Timecard``, all ``Break`` instances in the ``Timecard`` must be complete with ``end_at`` set on
        each ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_timecard(id, body, request_options=request_options).unwrap()

    def update_workweek_config(
        self,
        id: str,
        body: UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWorkweekConfigResponse:
        """Updates a ``WorkweekConfig``.

        Args:
            id: The UUID for the ``WorkweekConfig`` object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_workweek_config(id, body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> LaborWithRawResponse:
        return self._with_raw_response


class AsyncLabor:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncLaborWithRawResponse(client, server, auth)

    async def bulk_publish_scheduled_shifts(
        self,
        body: BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkPublishScheduledShiftsResponse:
        """Publishes 1 - 100 scheduled shifts. This endpoint takes a map of individual publish requests and returns a
        map of responses. When a scheduled shift is published, Square keeps the ``draft_shift_details`` field as is and
        copies it to the ``published_shift_details`` field.

        The minimum ``start_at`` and maximum ``end_at`` timestamps of all shifts in a ``BulkPublishScheduledShifts``
        request must fall within a two-week period.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.bulk_publish_scheduled_shifts(body, request_options=request_options)
        ).unwrap()

    async def create_break_type(
        self,
        body: CreateBreakTypeRequest | CreateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateBreakTypeResponse:
        """Creates a new ``BreakType``.

        A ``BreakType`` is a template for creating ``Break`` objects. You must provide the following values in your
        request to this endpoint:

        - ``location_id``
        - ``break_name``
        - ``expected_duration``
        - ``is_paid``

        You can only have three ``BreakType`` instances per location. If you attempt to add a fourth ``BreakType`` for a
        location, an ``INVALID_REQUEST_ERROR`` "Exceeded limit of 3 breaks per location." is returned.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_break_type(body, request_options=request_options)).unwrap()

    async def create_scheduled_shift(
        self,
        body: CreateScheduledShiftRequest | CreateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateScheduledShiftResponse:
        """Creates a scheduled shift by providing draft shift details such as job ID, team member assignment, and start
        and end times.

        The following ``draft_shift_details`` fields are required:
        - ``location_id``
        - ``job_id``
        - ``start_at``
        - ``end_at``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_scheduled_shift(body, request_options=request_options)).unwrap()

    async def create_shift(
        self, body: CreateShiftRequest | CreateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateShiftResponse:
        """Creates a new ``Shift``.

        A ``Shift`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Shift`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Shift`` is ``OPEN`` and the team member has another
        shift with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another shift for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Shift.start_at``, a break ``end_at`` is after the ``Shift.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_shift(body, request_options=request_options)).unwrap()

    async def create_timecard(
        self,
        body: CreateTimecardRequest | CreateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTimecardResponse:
        """Creates a new ``Timecard``.

        A ``Timecard`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Timecard`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Timecard`` is ``OPEN`` and the team member has another
        timecard with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another timecard for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Timecard.start_at``, a break ``end_at`` is after the ``Timecard.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_timecard(body, request_options=request_options)).unwrap()

    async def delete_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteBreakTypeResponse:
        """Deletes an existing ``BreakType``.

        A ``BreakType`` can be deleted even if it is referenced from a ``Shift``.

        Args:
            id: The UUID for the ``BreakType`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_break_type(id, request_options=request_options)).unwrap()

    async def delete_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteShiftResponse:
        """Deletes a ``Shift``.

        Args:
            id: The UUID for the ``Shift`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_shift(id, request_options=request_options)).unwrap()

    async def delete_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteTimecardResponse:
        """Deletes a ``Timecard``.

        Args:
            id: The UUID for the ``Timecard`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.delete_timecard(id, request_options=request_options)).unwrap()

    async def get_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetBreakTypeResponse:
        """Returns a single ``BreakType`` specified by ``id``.

        Args:
            id: The UUID for the ``BreakType`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_break_type(id, request_options=request_options)).unwrap()

    async def get_employee_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetEmployeeWageResponse:
        """Returns a single ``EmployeeWage`` specified by ``id``.

        Args:
            id: The UUID for the ``EmployeeWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_employee_wage(id, request_options=request_options)).unwrap()

    async def get_shift(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> GetShiftResponse:
        """Returns a single ``Shift`` specified by ``id``.

        Args:
            id: The UUID for the ``Shift`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_shift(id, request_options=request_options)).unwrap()

    async def get_team_member_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GetTeamMemberWageResponse:
        """Returns a single ``TeamMemberWage`` specified by ``id``.

        Args:
            id: The UUID for the ``TeamMemberWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.get_team_member_wage(id, request_options=request_options)).unwrap()

    async def list_break_types(
        self,
        *,
        location_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListBreakTypesResponse:
        """Returns a paginated list of ``BreakType`` instances for a business.

        Args:
            location_id: Filter the returned ``BreakType`` results to only those that are associated with the specified
                location.
            limit: The maximum number of ``BreakType`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``BreakType`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_break_types(
                location_id=location_id, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_employee_wages(
        self,
        *,
        employee_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListEmployeeWagesResponse:
        """Returns a paginated list of ``EmployeeWage`` instances for a business.

        Args:
            employee_id: Filter the returned wages to only those that are associated with the specified employee.
            limit: The maximum number of ``EmployeeWage`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_employee_wages(
                employee_id=employee_id, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_team_member_wages(
        self,
        *,
        team_member_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTeamMemberWagesResponse:
        """Returns a paginated list of ``TeamMemberWage`` instances for a business.

        Args:
            team_member_id: Filter the returned wages to only those that are associated with the specified team member.
            limit: The maximum number of ``TeamMemberWage`` results to return per page. The number can range between 1
                and 200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_team_member_wages(
                team_member_id=team_member_id, limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_workweek_configs(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListWorkweekConfigsResponse:
        """Returns a list of ``WorkweekConfig`` instances for a business.

        Args:
            limit: The maximum number of ``WorkweekConfigs`` results to return per page.
            cursor: A pointer to the next page of ``WorkweekConfig`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_workweek_configs(
                limit=limit, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def publish_scheduled_shift(
        self,
        id: str,
        body: PublishScheduledShiftRequest | PublishScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublishScheduledShiftResponse:
        """Publishes a scheduled shift. When a scheduled shift is published, Square keeps the ``draft_shift_details``
        field as is and copies it to the ``published_shift_details`` field.

        Args:
            id: The ID of the scheduled shift to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.publish_scheduled_shift(id, body, request_options=request_options)
        ).unwrap()

    async def retrieve_scheduled_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveScheduledShiftResponse:
        """Retrieves a scheduled shift by ID.

        Args:
            id: The ID of the scheduled shift to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_scheduled_shift(id, request_options=request_options)).unwrap()

    async def retrieve_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTimecardResponse:
        """Returns a single ``Timecard`` specified by ``id``.

        Args:
            id: The UUID for the ``Timecard`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_timecard(id, request_options=request_options)).unwrap()

    async def search_scheduled_shifts(
        self,
        body: SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchScheduledShiftsResponse:
        """Returns a paginated list of scheduled shifts, with optional filter and sort settings. By default, results are
        sorted by ``start_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_scheduled_shifts(body, request_options=request_options)).unwrap()

    async def search_shifts(
        self,
        body: SearchShiftsRequest | SearchShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchShiftsResponse:
        """Returns a paginated list of ``Shift`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Shift status (``OPEN`` or ``CLOSED``)
        - Shift start
        - Shift end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_shifts(body, request_options=request_options)).unwrap()

    async def search_timecards(
        self,
        body: SearchTimecardsRequest | SearchTimecardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTimecardsResponse:
        """Returns a paginated list of ``Timecard`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Timecard status (``OPEN`` or ``CLOSED``)
        - Timecard start
        - Timecard end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_timecards(body, request_options=request_options)).unwrap()

    async def update_break_type(
        self,
        id: str,
        body: UpdateBreakTypeRequest | UpdateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateBreakTypeResponse:
        """Updates an existing ``BreakType``.

        Args:
            id: The UUID for the ``BreakType`` being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_break_type(id, body, request_options=request_options)).unwrap()

    async def update_scheduled_shift(
        self,
        id: str,
        body: UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateScheduledShiftResponse:
        """Updates the draft shift details for a scheduled shift. This endpoint supports sparse updates, so only new,
        changed, or removed fields are required in the request. You must publish the shift to make updates public.

        You can make the following updates to ``draft_shift_details``:
        - Change the ``location_id``, ``job_id``, ``start_at``, and ``end_at`` fields.
        - Add, change, or clear the ``team_member_id`` and ``notes`` fields. To clear these fields,
        set the value to null.
        - Change the ``is_deleted`` field. To delete a scheduled shift, set ``is_deleted`` to true
        and then publish the shift.

        Args:
            id: The ID of the scheduled shift to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_scheduled_shift(id, body, request_options=request_options)
        ).unwrap()

    async def update_shift(
        self,
        id: str,
        body: UpdateShiftRequest | UpdateShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateShiftResponse:
        """Updates an existing ``Shift``.

        When adding a ``Break`` to a ``Shift``, any earlier ``Break`` instances in the ``Shift`` have the ``end_at``
        property set to a valid RFC-3339 datetime string.

        When closing a ``Shift``, all ``Break`` instances in the ``Shift`` must be complete with ``end_at`` set on each
        ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_shift(id, body, request_options=request_options)).unwrap()

    async def update_timecard(
        self,
        id: str,
        body: UpdateTimecardRequest | UpdateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateTimecardResponse:
        """Updates an existing ``Timecard``.

        When adding a ``Break`` to a ``Timecard``, any earlier ``Break`` instances in the ``Timecard`` have the
        ``end_at`` property set to a valid RFC-3339 datetime string.

        When closing a ``Timecard``, all ``Break`` instances in the ``Timecard`` must be complete with ``end_at`` set on
        each ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_timecard(id, body, request_options=request_options)).unwrap()

    async def update_workweek_config(
        self,
        id: str,
        body: UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWorkweekConfigResponse:
        """Updates a ``WorkweekConfig``.

        Args:
            id: The UUID for the ``WorkweekConfig`` object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_workweek_config(id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncLaborWithRawResponse:
        return self._with_raw_response


class LaborWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_publish_scheduled_shifts(
        self,
        body: BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkPublishScheduledShiftsResponse, RawError]:
        """Publishes 1 - 100 scheduled shifts. This endpoint takes a map of individual publish requests and returns a
        map of responses. When a scheduled shift is published, Square keeps the ``draft_shift_details`` field as is and
        copies it to the ``published_shift_details`` field.

        The minimum ``start_at`` and maximum ``end_at`` timestamps of all shifts in a ``BulkPublishScheduledShifts``
        request must fall within a two-week period.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts/bulk-publish"),
            body=json_body[BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkPublishScheduledShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_break_type(
        self,
        body: CreateBreakTypeRequest | CreateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBreakTypeResponse, RawError]:
        """Creates a new ``BreakType``.

        A ``BreakType`` is a template for creating ``Break`` objects. You must provide the following values in your
        request to this endpoint:

        - ``location_id``
        - ``break_name``
        - ``expected_duration``
        - ``is_paid``

        You can only have three ``BreakType`` instances per location. If you attempt to add a fourth ``BreakType`` for a
        location, an ``INVALID_REQUEST_ERROR`` "Exceeded limit of 3 breaks per location." is returned.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/break-types"),
            body=json_body[CreateBreakTypeRequest | CreateBreakTypeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_scheduled_shift(
        self,
        body: CreateScheduledShiftRequest | CreateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateScheduledShiftResponse, RawError]:
        """Creates a scheduled shift by providing draft shift details such as job ID, team member assignment, and start
        and end times.

        The following ``draft_shift_details`` fields are required:
        - ``location_id``
        - ``job_id``
        - ``start_at``
        - ``end_at``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts"),
            body=json_body[CreateScheduledShiftRequest | CreateScheduledShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_shift(
        self, body: CreateShiftRequest | CreateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateShiftResponse, RawError]:
        """Creates a new ``Shift``.

        A ``Shift`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Shift`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Shift`` is ``OPEN`` and the team member has another
        shift with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another shift for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Shift.start_at``, a break ``end_at`` is after the ``Shift.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/shifts"),
            body=json_body[CreateShiftRequest | CreateShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_timecard(
        self,
        body: CreateTimecardRequest | CreateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTimecardResponse, RawError]:
        """Creates a new ``Timecard``.

        A ``Timecard`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Timecard`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Timecard`` is ``OPEN`` and the team member has another
        timecard with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another timecard for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Timecard.start_at``, a break ``end_at`` is after the ``Timecard.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/timecards"),
            body=json_body[CreateTimecardRequest | CreateTimecardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteBreakTypeResponse, RawError]:
        """Deletes an existing ``BreakType``.

        A ``BreakType`` can be deleted even if it is referenced from a ``Shift``.

        Args:
            id: The UUID for the ``BreakType`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/labor/break-types/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteShiftResponse, RawError]:
        """Deletes a ``Shift``.

        Args:
            id: The UUID for the ``Shift`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/labor/shifts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteTimecardResponse, RawError]:
        """Deletes a ``Timecard``.

        Args:
            id: The UUID for the ``Timecard`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/labor/timecards/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBreakTypeResponse, RawError]:
        """Returns a single ``BreakType`` specified by ``id``.

        Args:
            id: The UUID for the ``BreakType`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/break-types/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_employee_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetEmployeeWageResponse, RawError]:
        """Returns a single ``EmployeeWage`` specified by ``id``.

        Args:
            id: The UUID for the ``EmployeeWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/employee-wages/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetEmployeeWageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetShiftResponse, RawError]:
        """Returns a single ``Shift`` specified by ``id``.

        Args:
            id: The UUID for the ``Shift`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/shifts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_team_member_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTeamMemberWageResponse, RawError]:
        """Returns a single ``TeamMemberWage`` specified by ``id``.

        Args:
            id: The UUID for the ``TeamMemberWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/team-member-wages/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTeamMemberWageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_break_types(
        self,
        *,
        location_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBreakTypesResponse, RawError]:
        """Returns a paginated list of ``BreakType`` instances for a business.

        Args:
            location_id: Filter the returned ``BreakType`` results to only those that are associated with the specified
                location.
            limit: The maximum number of ``BreakType`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``BreakType`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/break-types"),
            query_params=[
                param[str | None]("location_id", location_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBreakTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_employee_wages(
        self,
        *,
        employee_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEmployeeWagesResponse, RawError]:
        """Returns a paginated list of ``EmployeeWage`` instances for a business.

        Args:
            employee_id: Filter the returned wages to only those that are associated with the specified employee.
            limit: The maximum number of ``EmployeeWage`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/employee-wages"),
            query_params=[
                param[str | None]("employee_id", employee_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListEmployeeWagesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_team_member_wages(
        self,
        *,
        team_member_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTeamMemberWagesResponse, RawError]:
        """Returns a paginated list of ``TeamMemberWage`` instances for a business.

        Args:
            team_member_id: Filter the returned wages to only those that are associated with the specified team member.
            limit: The maximum number of ``TeamMemberWage`` results to return per page. The number can range between 1
                and 200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/team-member-wages"),
            query_params=[
                param[str | None]("team_member_id", team_member_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListTeamMemberWagesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_workweek_configs(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkweekConfigsResponse, RawError]:
        """Returns a list of ``WorkweekConfig`` instances for a business.

        Args:
            limit: The maximum number of ``WorkweekConfigs`` results to return per page.
            cursor: A pointer to the next page of ``WorkweekConfig`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/workweek-configs"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListWorkweekConfigsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def publish_scheduled_shift(
        self,
        id: str,
        body: PublishScheduledShiftRequest | PublishScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublishScheduledShiftResponse, RawError]:
        """Publishes a scheduled shift. When a scheduled shift is published, Square keeps the ``draft_shift_details``
        field as is and copies it to the ``published_shift_details`` field.

        Args:
            id: The ID of the scheduled shift to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts/{id}/publish"),
            path_params=[param[str]("id", id)],
            body=json_body[PublishScheduledShiftRequest | PublishScheduledShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PublishScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_scheduled_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveScheduledShiftResponse, RawError]:
        """Retrieves a scheduled shift by ID.

        Args:
            id: The ID of the scheduled shift to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/scheduled-shifts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTimecardResponse, RawError]:
        """Returns a single ``Timecard`` specified by ``id``.

        Args:
            id: The UUID for the ``Timecard`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/timecards/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_scheduled_shifts(
        self,
        body: SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchScheduledShiftsResponse, RawError]:
        """Returns a paginated list of scheduled shifts, with optional filter and sort settings. By default, results are
        sorted by ``start_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts/search"),
            body=json_body[SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchScheduledShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_shifts(
        self,
        body: SearchShiftsRequest | SearchShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchShiftsResponse, RawError]:
        """Returns a paginated list of ``Shift`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Shift status (``OPEN`` or ``CLOSED``)
        - Shift start
        - Shift end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/shifts/search"),
            body=json_body[SearchShiftsRequest | SearchShiftsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_timecards(
        self,
        body: SearchTimecardsRequest | SearchTimecardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTimecardsResponse, RawError]:
        """Returns a paginated list of ``Timecard`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Timecard status (``OPEN`` or ``CLOSED``)
        - Timecard start
        - Timecard end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/timecards/search"),
            body=json_body[SearchTimecardsRequest | SearchTimecardsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTimecardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_break_type(
        self,
        id: str,
        body: UpdateBreakTypeRequest | UpdateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateBreakTypeResponse, RawError]:
        """Updates an existing ``BreakType``.

        Args:
            id: The UUID for the ``BreakType`` being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/break-types/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateBreakTypeRequest | UpdateBreakTypeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_scheduled_shift(
        self,
        id: str,
        body: UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateScheduledShiftResponse, RawError]:
        """Updates the draft shift details for a scheduled shift. This endpoint supports sparse updates, so only new,
        changed, or removed fields are required in the request. You must publish the shift to make updates public.

        You can make the following updates to ``draft_shift_details``:
        - Change the ``location_id``, ``job_id``, ``start_at``, and ``end_at`` fields.
        - Add, change, or clear the ``team_member_id`` and ``notes`` fields. To clear these fields,
        set the value to null.
        - Change the ``is_deleted`` field. To delete a scheduled shift, set ``is_deleted`` to true
        and then publish the shift.

        Args:
            id: The ID of the scheduled shift to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/scheduled-shifts/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_shift(
        self,
        id: str,
        body: UpdateShiftRequest | UpdateShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShiftResponse, RawError]:
        """Updates an existing ``Shift``.

        When adding a ``Break`` to a ``Shift``, any earlier ``Break`` instances in the ``Shift`` have the ``end_at``
        property set to a valid RFC-3339 datetime string.

        When closing a ``Shift``, all ``Break`` instances in the ``Shift`` must be complete with ``end_at`` set on each
        ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/shifts/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateShiftRequest | UpdateShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_timecard(
        self,
        id: str,
        body: UpdateTimecardRequest | UpdateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateTimecardResponse, RawError]:
        """Updates an existing ``Timecard``.

        When adding a ``Break`` to a ``Timecard``, any earlier ``Break`` instances in the ``Timecard`` have the
        ``end_at`` property set to a valid RFC-3339 datetime string.

        When closing a ``Timecard``, all ``Break`` instances in the ``Timecard`` must be complete with ``end_at`` set on
        each ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/timecards/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateTimecardRequest | UpdateTimecardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_workweek_config(
        self,
        id: str,
        body: UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWorkweekConfigResponse, RawError]:
        """Updates a ``WorkweekConfig``.

        Args:
            id: The UUID for the ``WorkweekConfig`` object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/workweek-configs/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateWorkweekConfigResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncLaborWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_publish_scheduled_shifts(
        self,
        body: BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkPublishScheduledShiftsResponse, RawError]:
        """Publishes 1 - 100 scheduled shifts. This endpoint takes a map of individual publish requests and returns a
        map of responses. When a scheduled shift is published, Square keeps the ``draft_shift_details`` field as is and
        copies it to the ``published_shift_details`` field.

        The minimum ``start_at`` and maximum ``end_at`` timestamps of all shifts in a ``BulkPublishScheduledShifts``
        request must fall within a two-week period.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts/bulk-publish"),
            body=json_body[BulkPublishScheduledShiftsRequest | BulkPublishScheduledShiftsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkPublishScheduledShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_break_type(
        self,
        body: CreateBreakTypeRequest | CreateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateBreakTypeResponse, RawError]:
        """Creates a new ``BreakType``.

        A ``BreakType`` is a template for creating ``Break`` objects. You must provide the following values in your
        request to this endpoint:

        - ``location_id``
        - ``break_name``
        - ``expected_duration``
        - ``is_paid``

        You can only have three ``BreakType`` instances per location. If you attempt to add a fourth ``BreakType`` for a
        location, an ``INVALID_REQUEST_ERROR`` "Exceeded limit of 3 breaks per location." is returned.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/break-types"),
            body=json_body[CreateBreakTypeRequest | CreateBreakTypeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_scheduled_shift(
        self,
        body: CreateScheduledShiftRequest | CreateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateScheduledShiftResponse, RawError]:
        """Creates a scheduled shift by providing draft shift details such as job ID, team member assignment, and start
        and end times.

        The following ``draft_shift_details`` fields are required:
        - ``location_id``
        - ``job_id``
        - ``start_at``
        - ``end_at``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts"),
            body=json_body[CreateScheduledShiftRequest | CreateScheduledShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_shift(
        self, body: CreateShiftRequest | CreateShiftRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateShiftResponse, RawError]:
        """Creates a new ``Shift``.

        A ``Shift`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Shift`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Shift`` is ``OPEN`` and the team member has another
        shift with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another shift for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Shift.start_at``, a break ``end_at`` is after the ``Shift.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/shifts"),
            body=json_body[CreateShiftRequest | CreateShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_timecard(
        self,
        body: CreateTimecardRequest | CreateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTimecardResponse, RawError]:
        """Creates a new ``Timecard``.

        A ``Timecard`` represents a complete workday for a single team member. You must provide the following values in
        your request to this endpoint:

        - ``location_id``
        - ``team_member_id``
        - ``start_at``

        An attempt to create a new ``Timecard`` can result in a ``BAD_REQUEST`` error when:
        - The ``status`` of the new ``Timecard`` is ``OPEN`` and the team member has another
        timecard with an ``OPEN`` status.
        - The ``start_at`` date is in the future.
        - The ``start_at`` or ``end_at`` date overlaps another timecard for the same team member.
        - The ``Break`` instances are set in the request and a break ``start_at``
        is before the ``Timecard.start_at``, a break ``end_at`` is after the ``Timecard.end_at``, or both.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/timecards"),
            body=json_body[CreateTimecardRequest | CreateTimecardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteBreakTypeResponse, RawError]:
        """Deletes an existing ``BreakType``.

        A ``BreakType`` can be deleted even if it is referenced from a ``Shift``.

        Args:
            id: The UUID for the ``BreakType`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/labor/break-types/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteShiftResponse, RawError]:
        """Deletes a ``Shift``.

        Args:
            id: The UUID for the ``Shift`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/labor/shifts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteTimecardResponse, RawError]:
        """Deletes a ``Timecard``.

        Args:
            id: The UUID for the ``Timecard`` being deleted.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/labor/timecards/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_break_type(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetBreakTypeResponse, RawError]:
        """Returns a single ``BreakType`` specified by ``id``.

        Args:
            id: The UUID for the ``BreakType`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/break-types/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_employee_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetEmployeeWageResponse, RawError]:
        """Returns a single ``EmployeeWage`` specified by ``id``.

        Args:
            id: The UUID for the ``EmployeeWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/employee-wages/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetEmployeeWageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetShiftResponse, RawError]:
        """Returns a single ``Shift`` specified by ``id``.

        Args:
            id: The UUID for the ``Shift`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/shifts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_team_member_wage(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GetTeamMemberWageResponse, RawError]:
        """Returns a single ``TeamMemberWage`` specified by ``id``.

        Args:
            id: The UUID for the ``TeamMemberWage`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/team-member-wages/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[GetTeamMemberWageResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_break_types(
        self,
        *,
        location_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListBreakTypesResponse, RawError]:
        """Returns a paginated list of ``BreakType`` instances for a business.

        Args:
            location_id: Filter the returned ``BreakType`` results to only those that are associated with the specified
                location.
            limit: The maximum number of ``BreakType`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``BreakType`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/break-types"),
            query_params=[
                param[str | None]("location_id", location_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListBreakTypesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_employee_wages(
        self,
        *,
        employee_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListEmployeeWagesResponse, RawError]:
        """Returns a paginated list of ``EmployeeWage`` instances for a business.

        Args:
            employee_id: Filter the returned wages to only those that are associated with the specified employee.
            limit: The maximum number of ``EmployeeWage`` results to return per page. The number can range between 1 and
                200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/employee-wages"),
            query_params=[
                param[str | None]("employee_id", employee_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListEmployeeWagesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_team_member_wages(
        self,
        *,
        team_member_id: str | None = None,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTeamMemberWagesResponse, RawError]:
        """Returns a paginated list of ``TeamMemberWage`` instances for a business.

        Args:
            team_member_id: Filter the returned wages to only those that are associated with the specified team member.
            limit: The maximum number of ``TeamMemberWage`` results to return per page. The number can range between 1
                and 200. The default is 200.
            cursor: A pointer to the next page of ``EmployeeWage`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/team-member-wages"),
            query_params=[
                param[str | None]("team_member_id", team_member_id),
                param[int | None]("limit", limit),
                param[str | None]("cursor", cursor),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListTeamMemberWagesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_workweek_configs(
        self,
        *,
        limit: int | None = None,
        cursor: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListWorkweekConfigsResponse, RawError]:
        """Returns a list of ``WorkweekConfig`` instances for a business.

        Args:
            limit: The maximum number of ``WorkweekConfigs`` results to return per page.
            cursor: A pointer to the next page of ``WorkweekConfig`` results to fetch.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/workweek-configs"),
            query_params=[param[int | None]("limit", limit), param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListWorkweekConfigsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def publish_scheduled_shift(
        self,
        id: str,
        body: PublishScheduledShiftRequest | PublishScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublishScheduledShiftResponse, RawError]:
        """Publishes a scheduled shift. When a scheduled shift is published, Square keeps the ``draft_shift_details``
        field as is and copies it to the ``published_shift_details`` field.

        Args:
            id: The ID of the scheduled shift to publish.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts/{id}/publish"),
            path_params=[param[str]("id", id)],
            body=json_body[PublishScheduledShiftRequest | PublishScheduledShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[PublishScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_scheduled_shift(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveScheduledShiftResponse, RawError]:
        """Retrieves a scheduled shift by ID.

        Args:
            id: The ID of the scheduled shift to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/scheduled-shifts/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_timecard(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTimecardResponse, RawError]:
        """Returns a single ``Timecard`` specified by ``id``.

        Args:
            id: The UUID for the ``Timecard`` being retrieved.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/labor/timecards/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_scheduled_shifts(
        self,
        body: SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchScheduledShiftsResponse, RawError]:
        """Returns a paginated list of scheduled shifts, with optional filter and sort settings. By default, results are
        sorted by ``start_at`` in ascending order.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/scheduled-shifts/search"),
            body=json_body[SearchScheduledShiftsRequest | SearchScheduledShiftsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchScheduledShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_shifts(
        self,
        body: SearchShiftsRequest | SearchShiftsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchShiftsResponse, RawError]:
        """Returns a paginated list of ``Shift`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Shift status (``OPEN`` or ``CLOSED``)
        - Shift start
        - Shift end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/shifts/search"),
            body=json_body[SearchShiftsRequest | SearchShiftsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchShiftsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_timecards(
        self,
        body: SearchTimecardsRequest | SearchTimecardsRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTimecardsResponse, RawError]:
        """Returns a paginated list of ``Timecard`` records for a business. The list to be returned can be filtered by:
        - Location IDs
        - Team member IDs
        - Timecard status (``OPEN`` or ``CLOSED``)
        - Timecard start
        - Timecard end
        - Workday details

        The list can be sorted by:
        - ``START_AT``
        - ``END_AT``
        - ``CREATED_AT``
        - ``UPDATED_AT``

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/labor/timecards/search"),
            body=json_body[SearchTimecardsRequest | SearchTimecardsRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTimecardsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_break_type(
        self,
        id: str,
        body: UpdateBreakTypeRequest | UpdateBreakTypeRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateBreakTypeResponse, RawError]:
        """Updates an existing ``BreakType``.

        Args:
            id: The UUID for the ``BreakType`` being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/break-types/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateBreakTypeRequest | UpdateBreakTypeRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateBreakTypeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_scheduled_shift(
        self,
        id: str,
        body: UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateScheduledShiftResponse, RawError]:
        """Updates the draft shift details for a scheduled shift. This endpoint supports sparse updates, so only new,
        changed, or removed fields are required in the request. You must publish the shift to make updates public.

        You can make the following updates to ``draft_shift_details``:
        - Change the ``location_id``, ``job_id``, ``start_at``, and ``end_at`` fields.
        - Add, change, or clear the ``team_member_id`` and ``notes`` fields. To clear these fields,
        set the value to null.
        - Change the ``is_deleted`` field. To delete a scheduled shift, set ``is_deleted`` to true
        and then publish the shift.

        Args:
            id: The ID of the scheduled shift to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/scheduled-shifts/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateScheduledShiftRequest | UpdateScheduledShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateScheduledShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_shift(
        self,
        id: str,
        body: UpdateShiftRequest | UpdateShiftRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateShiftResponse, RawError]:
        """Updates an existing ``Shift``.

        When adding a ``Break`` to a ``Shift``, any earlier ``Break`` instances in the ``Shift`` have the ``end_at``
        property set to a valid RFC-3339 datetime string.

        When closing a ``Shift``, all ``Break`` instances in the ``Shift`` must be complete with ``end_at`` set on each
        ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/shifts/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateShiftRequest | UpdateShiftRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateShiftResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_timecard(
        self,
        id: str,
        body: UpdateTimecardRequest | UpdateTimecardRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateTimecardResponse, RawError]:
        """Updates an existing ``Timecard``.

        When adding a ``Break`` to a ``Timecard``, any earlier ``Break`` instances in the ``Timecard`` have the
        ``end_at`` property set to a valid RFC-3339 datetime string.

        When closing a ``Timecard``, all ``Break`` instances in the ``Timecard`` must be complete with ``end_at`` set on
        each ``Break``.

        Args:
            id: The ID of the object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/timecards/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateTimecardRequest | UpdateTimecardRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateTimecardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_workweek_config(
        self,
        id: str,
        body: UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWorkweekConfigResponse, RawError]:
        """Updates a ``WorkweekConfig``.

        Args:
            id: The UUID for the ``WorkweekConfig`` object being updated.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/labor/workweek-configs/{id}"),
            path_params=[param[str]("id", id)],
            body=json_body[UpdateWorkweekConfigRequest | UpdateWorkweekConfigRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateWorkweekConfigResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
