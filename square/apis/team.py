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
from ..models.bulk_create_team_members_request import BulkCreateTeamMembersRequest, BulkCreateTeamMembersRequestDict
from ..models.bulk_create_team_members_response import BulkCreateTeamMembersResponse
from ..models.bulk_update_team_members_request import BulkUpdateTeamMembersRequest, BulkUpdateTeamMembersRequestDict
from ..models.bulk_update_team_members_response import BulkUpdateTeamMembersResponse
from ..models.create_job_request import CreateJobRequest, CreateJobRequestDict
from ..models.create_job_response import CreateJobResponse
from ..models.create_team_member_request import CreateTeamMemberRequest, CreateTeamMemberRequestDict
from ..models.create_team_member_response import CreateTeamMemberResponse
from ..models.list_jobs_response import ListJobsResponse
from ..models.retrieve_job_response import RetrieveJobResponse
from ..models.retrieve_team_member_response import RetrieveTeamMemberResponse
from ..models.retrieve_wage_setting_response import RetrieveWageSettingResponse
from ..models.search_team_members_request import SearchTeamMembersRequest, SearchTeamMembersRequestDict
from ..models.search_team_members_response import SearchTeamMembersResponse
from ..models.update_job_request import UpdateJobRequest, UpdateJobRequestDict
from ..models.update_job_response import UpdateJobResponse
from ..models.update_team_member_request import UpdateTeamMemberRequest, UpdateTeamMemberRequestDict
from ..models.update_team_member_response import UpdateTeamMemberResponse
from ..models.update_wage_setting_request import UpdateWageSettingRequest, UpdateWageSettingRequestDict
from ..models.update_wage_setting_response import UpdateWageSettingResponse
from ..server.server import Server


class Team:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TeamWithRawResponse(client, server, auth)

    def bulk_create_team_members(
        self,
        body: BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateTeamMembersResponse:
        """Creates multiple ``TeamMember`` objects. The created ``TeamMember`` objects are returned on successful
        creates. This process is non-transactional and processes as much of the request as possible. If one of the
        creates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed create.

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_create_team_members(body, request_options=request_options).unwrap()

    def bulk_update_team_members(
        self,
        body: BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateTeamMembersResponse:
        """Updates multiple ``TeamMember`` objects. The updated ``TeamMember`` objects are returned on successful
        updates. This process is non-transactional and processes as much of the request as possible. If one of the
        updates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed update. Learn about `Troubleshooting the Team
        API <https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.bulk_update_team_members(body, request_options=request_options).unwrap()

    def create_job(
        self, body: CreateJobRequest | CreateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateJobResponse:
        """Creates a job in a seller account. A job defines a title and tip eligibility. Note that compensation is
        defined in a `job assignment <entity:JobAssignment>`__ in a team member's wage setting.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_job(body, request_options=request_options).unwrap()

    def create_team_member(
        self,
        body: CreateTeamMemberRequest | CreateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTeamMemberResponse:
        """Creates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful creates. You must
        provide the following values in your request to this endpoint:
        - ``given_name``
        - ``family_name``

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#createteammember>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_team_member(body, request_options=request_options).unwrap()

    def list_jobs(
        self, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListJobsResponse:
        """Lists jobs in a seller account. Results are sorted by title in ascending order.

        Args:
            cursor: The pagination cursor returned by the previous call to this endpoint. Provide this cursor to
                retrieve the next page of results for your original request. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_jobs(cursor=cursor, request_options=request_options).unwrap()

    def retrieve_job(self, job_id: str, *, request_options: RequestOptionsOrDict | None = None) -> RetrieveJobResponse:
        """Retrieves a specified job.

        Args:
            job_id: The ID of the job to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_job(job_id, request_options=request_options).unwrap()

    def retrieve_team_member(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTeamMemberResponse:
        """Retrieves a ``TeamMember`` object for the given ``TeamMember.id``. Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_team_member(team_member_id, request_options=request_options).unwrap()

    def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveWageSettingResponse:
        """Retrieves a ``WageSetting`` object for a team member specified by ``TeamMember.id``. For more information,
        see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting>`__.

        Square recommends using `RetrieveTeamMember <api-endpoint:Team-RetrieveTeamMember>`__ or `SearchTeamMembers
        <api-endpoint:Team-SearchTeamMembers>`__ to get this information directly from the ``TeamMember.wage_setting``
        field.

        Args:
            team_member_id: The ID of the team member for which to retrieve the wage setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_wage_setting(team_member_id, request_options=request_options).unwrap()

    def search_team_members(
        self,
        body: SearchTeamMembersRequest | SearchTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTeamMembersResponse:
        """Returns a paginated list of ``TeamMember`` objects for a business. The list can be filtered by location IDs,
        ``ACTIVE`` or ``INACTIVE`` status, or whether the team member is the Square account owner.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.search_team_members(body, request_options=request_options).unwrap()

    def update_job(
        self,
        job_id: str,
        body: UpdateJobRequest | UpdateJobRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateJobResponse:
        """Updates the title or tip eligibility of a job. Changes to the title propagate to all ``JobAssignment``,
        ``Shift``, and ``TeamMemberWage`` objects that reference the job ID. Changes to tip eligibility propagate to all
        ``TeamMemberWage`` objects that reference the job ID.

        Args:
            job_id: The ID of the job to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_job(job_id, body, request_options=request_options).unwrap()

    def update_team_member(
        self,
        team_member_id: str,
        body: UpdateTeamMemberRequest | UpdateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateTeamMemberResponse:
        """Updates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful updates. Learn
        about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_team_member(
            team_member_id, body, request_options=request_options
        ).unwrap()

    def update_wage_setting(
        self,
        team_member_id: str,
        body: UpdateWageSettingRequest | UpdateWageSettingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWageSettingResponse:
        """Creates or updates a ``WageSetting`` object. The object is created if a ``WageSetting`` with the specified
        ``team_member_id`` doesn't exist. Otherwise, it fully replaces the ``WageSetting`` object for the team member.
        The ``WageSetting`` is returned on a successful update. For more information, see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting>`__.

        Square recommends using `CreateTeamMember <api-endpoint:Team-CreateTeamMember>`__ or `UpdateTeamMember
        <api-endpoint:Team-UpdateTeamMember>`__ to manage the ``TeamMember.wage_setting`` field directly.

        Args:
            team_member_id: The ID of the team member for which to update the ``WageSetting`` object.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.update_wage_setting(
            team_member_id, body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TeamWithRawResponse:
        return self._with_raw_response


class AsyncTeam:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTeamWithRawResponse(client, server, auth)

    async def bulk_create_team_members(
        self,
        body: BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkCreateTeamMembersResponse:
        """Creates multiple ``TeamMember`` objects. The created ``TeamMember`` objects are returned on successful
        creates. This process is non-transactional and processes as much of the request as possible. If one of the
        creates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed create.

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_create_team_members(body, request_options=request_options)).unwrap()

    async def bulk_update_team_members(
        self,
        body: BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BulkUpdateTeamMembersResponse:
        """Updates multiple ``TeamMember`` objects. The updated ``TeamMember`` objects are returned on successful
        updates. This process is non-transactional and processes as much of the request as possible. If one of the
        updates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed update. Learn about `Troubleshooting the Team
        API <https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.bulk_update_team_members(body, request_options=request_options)).unwrap()

    async def create_job(
        self, body: CreateJobRequest | CreateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> CreateJobResponse:
        """Creates a job in a seller account. A job defines a title and tip eligibility. Note that compensation is
        defined in a `job assignment <entity:JobAssignment>`__ in a team member's wage setting.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_job(body, request_options=request_options)).unwrap()

    async def create_team_member(
        self,
        body: CreateTeamMemberRequest | CreateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateTeamMemberResponse:
        """Creates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful creates. You must
        provide the following values in your request to this endpoint:
        - ``given_name``
        - ``family_name``

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#createteammember>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.create_team_member(body, request_options=request_options)).unwrap()

    async def list_jobs(
        self, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListJobsResponse:
        """Lists jobs in a seller account. Results are sorted by title in ascending order.

        Args:
            cursor: The pagination cursor returned by the previous call to this endpoint. Provide this cursor to
                retrieve the next page of results for your original request. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.list_jobs(cursor=cursor, request_options=request_options)).unwrap()

    async def retrieve_job(
        self, job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveJobResponse:
        """Retrieves a specified job.

        Args:
            job_id: The ID of the job to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_job(job_id, request_options=request_options)).unwrap()

    async def retrieve_team_member(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveTeamMemberResponse:
        """Retrieves a ``TeamMember`` object for the given ``TeamMember.id``. Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_team_member(team_member_id, request_options=request_options)
        ).unwrap()

    async def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveWageSettingResponse:
        """Retrieves a ``WageSetting`` object for a team member specified by ``TeamMember.id``. For more information,
        see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting>`__.

        Square recommends using `RetrieveTeamMember <api-endpoint:Team-RetrieveTeamMember>`__ or `SearchTeamMembers
        <api-endpoint:Team-SearchTeamMembers>`__ to get this information directly from the ``TeamMember.wage_setting``
        field.

        Args:
            team_member_id: The ID of the team member for which to retrieve the wage setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_wage_setting(team_member_id, request_options=request_options)
        ).unwrap()

    async def search_team_members(
        self,
        body: SearchTeamMembersRequest | SearchTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchTeamMembersResponse:
        """Returns a paginated list of ``TeamMember`` objects for a business. The list can be filtered by location IDs,
        ``ACTIVE`` or ``INACTIVE`` status, or whether the team member is the Square account owner.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.search_team_members(body, request_options=request_options)).unwrap()

    async def update_job(
        self,
        job_id: str,
        body: UpdateJobRequest | UpdateJobRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateJobResponse:
        """Updates the title or tip eligibility of a job. Changes to the title propagate to all ``JobAssignment``,
        ``Shift``, and ``TeamMemberWage`` objects that reference the job ID. Changes to tip eligibility propagate to all
        ``TeamMemberWage`` objects that reference the job ID.

        Args:
            job_id: The ID of the job to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.update_job(job_id, body, request_options=request_options)).unwrap()

    async def update_team_member(
        self,
        team_member_id: str,
        body: UpdateTeamMemberRequest | UpdateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateTeamMemberResponse:
        """Updates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful updates. Learn
        about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_team_member(team_member_id, body, request_options=request_options)
        ).unwrap()

    async def update_wage_setting(
        self,
        team_member_id: str,
        body: UpdateWageSettingRequest | UpdateWageSettingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateWageSettingResponse:
        """Creates or updates a ``WageSetting`` object. The object is created if a ``WageSetting`` with the specified
        ``team_member_id`` doesn't exist. Otherwise, it fully replaces the ``WageSetting`` object for the team member.
        The ``WageSetting`` is returned on a successful update. For more information, see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting>`__.

        Square recommends using `CreateTeamMember <api-endpoint:Team-CreateTeamMember>`__ or `UpdateTeamMember
        <api-endpoint:Team-UpdateTeamMember>`__ to manage the ``TeamMember.wage_setting`` field directly.

        Args:
            team_member_id: The ID of the team member for which to update the ``WageSetting`` object.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.update_wage_setting(team_member_id, body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTeamWithRawResponse:
        return self._with_raw_response


class TeamWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def bulk_create_team_members(
        self,
        body: BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateTeamMembersResponse, RawError]:
        """Creates multiple ``TeamMember`` objects. The created ``TeamMember`` objects are returned on successful
        creates. This process is non-transactional and processes as much of the request as possible. If one of the
        creates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed create.

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/bulk-create"),
            body=json_body[BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkCreateTeamMembersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def bulk_update_team_members(
        self,
        body: BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateTeamMembersResponse, RawError]:
        """Updates multiple ``TeamMember`` objects. The updated ``TeamMember`` objects are returned on successful
        updates. This process is non-transactional and processes as much of the request as possible. If one of the
        updates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed update. Learn about `Troubleshooting the Team
        API <https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/bulk-update"),
            body=json_body[BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpdateTeamMembersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_job(
        self, body: CreateJobRequest | CreateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateJobResponse, RawError]:
        """Creates a job in a seller account. A job defines a title and tip eligibility. Note that compensation is
        defined in a `job assignment <entity:JobAssignment>`__ in a team member's wage setting.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/jobs"),
            body=json_body[CreateJobRequest | CreateJobRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateJobResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_team_member(
        self,
        body: CreateTeamMemberRequest | CreateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTeamMemberResponse, RawError]:
        """Creates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful creates. You must
        provide the following values in your request to this endpoint:
        - ``given_name``
        - ``family_name``

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#createteammember>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members"),
            body=json_body[CreateTeamMemberRequest | CreateTeamMemberRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTeamMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_jobs(
        self, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListJobsResponse, RawError]:
        """Lists jobs in a seller account. Results are sorted by title in ascending order.

        Args:
            cursor: The pagination cursor returned by the previous call to this endpoint. Provide this cursor to
                retrieve the next page of results for your original request. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/jobs"),
            query_params=[param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListJobsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_job(
        self, job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveJobResponse, RawError]:
        """Retrieves a specified job.

        Args:
            job_id: The ID of the job to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/jobs/{job_id}"),
            path_params=[param[str]("job_id", job_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveJobResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_team_member(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTeamMemberResponse, RawError]:
        """Retrieves a ``TeamMember`` object for the given ``TeamMember.id``. Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/{team_member_id}"),
            path_params=[param[str]("team_member_id", team_member_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTeamMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveWageSettingResponse, RawError]:
        """Retrieves a ``WageSetting`` object for a team member specified by ``TeamMember.id``. For more information,
        see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting>`__.

        Square recommends using `RetrieveTeamMember <api-endpoint:Team-RetrieveTeamMember>`__ or `SearchTeamMembers
        <api-endpoint:Team-SearchTeamMembers>`__ to get this information directly from the ``TeamMember.wage_setting``
        field.

        Args:
            team_member_id: The ID of the team member for which to retrieve the wage setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/{team_member_id}/wage-setting"),
            path_params=[param[str]("team_member_id", team_member_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveWageSettingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def search_team_members(
        self,
        body: SearchTeamMembersRequest | SearchTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTeamMembersResponse, RawError]:
        """Returns a paginated list of ``TeamMember`` objects for a business. The list can be filtered by location IDs,
        ``ACTIVE`` or ``INACTIVE`` status, or whether the team member is the Square account owner.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/search"),
            body=json_body[SearchTeamMembersRequest | SearchTeamMembersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTeamMembersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_job(
        self,
        job_id: str,
        body: UpdateJobRequest | UpdateJobRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateJobResponse, RawError]:
        """Updates the title or tip eligibility of a job. Changes to the title propagate to all ``JobAssignment``,
        ``Shift``, and ``TeamMemberWage`` objects that reference the job ID. Changes to tip eligibility propagate to all
        ``TeamMemberWage`` objects that reference the job ID.

        Args:
            job_id: The ID of the job to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/team-members/jobs/{job_id}"),
            path_params=[param[str]("job_id", job_id)],
            body=json_body[UpdateJobRequest | UpdateJobRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateJobResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_team_member(
        self,
        team_member_id: str,
        body: UpdateTeamMemberRequest | UpdateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateTeamMemberResponse, RawError]:
        """Updates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful updates. Learn
        about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/team-members/{team_member_id}"),
            path_params=[param[str]("team_member_id", team_member_id)],
            body=json_body[UpdateTeamMemberRequest | UpdateTeamMemberRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateTeamMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def update_wage_setting(
        self,
        team_member_id: str,
        body: UpdateWageSettingRequest | UpdateWageSettingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWageSettingResponse, RawError]:
        """Creates or updates a ``WageSetting`` object. The object is created if a ``WageSetting`` with the specified
        ``team_member_id`` doesn't exist. Otherwise, it fully replaces the ``WageSetting`` object for the team member.
        The ``WageSetting`` is returned on a successful update. For more information, see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting>`__.

        Square recommends using `CreateTeamMember <api-endpoint:Team-CreateTeamMember>`__ or `UpdateTeamMember
        <api-endpoint:Team-UpdateTeamMember>`__ to manage the ``TeamMember.wage_setting`` field directly.

        Args:
            team_member_id: The ID of the team member for which to update the ``WageSetting`` object.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/team-members/{team_member_id}/wage-setting"),
            path_params=[param[str]("team_member_id", team_member_id)],
            body=json_body[UpdateWageSettingRequest | UpdateWageSettingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateWageSettingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncTeamWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def bulk_create_team_members(
        self,
        body: BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkCreateTeamMembersResponse, RawError]:
        """Creates multiple ``TeamMember`` objects. The created ``TeamMember`` objects are returned on successful
        creates. This process is non-transactional and processes as much of the request as possible. If one of the
        creates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed create.

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/bulk-create"),
            body=json_body[BulkCreateTeamMembersRequest | BulkCreateTeamMembersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkCreateTeamMembersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def bulk_update_team_members(
        self,
        body: BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BulkUpdateTeamMembersResponse, RawError]:
        """Updates multiple ``TeamMember`` objects. The updated ``TeamMember`` objects are returned on successful
        updates. This process is non-transactional and processes as much of the request as possible. If one of the
        updates in the request cannot be successfully processed, the request is not marked as failed, but the body of
        the response contains explicit error information for the failed update. Learn about `Troubleshooting the Team
        API <https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/bulk-update"),
            body=json_body[BulkUpdateTeamMembersRequest | BulkUpdateTeamMembersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[BulkUpdateTeamMembersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_job(
        self, body: CreateJobRequest | CreateJobRequestDict, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[CreateJobResponse, RawError]:
        """Creates a job in a seller account. A job defines a title and tip eligibility. Note that compensation is
        defined in a `job assignment <entity:JobAssignment>`__ in a team member's wage setting.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/jobs"),
            body=json_body[CreateJobRequest | CreateJobRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateJobResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_team_member(
        self,
        body: CreateTeamMemberRequest | CreateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateTeamMemberResponse, RawError]:
        """Creates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful creates. You must
        provide the following values in your request to this endpoint:
        - ``given_name``
        - ``family_name``

        Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#createteammember>`__.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members"),
            body=json_body[CreateTeamMemberRequest | CreateTeamMemberRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateTeamMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_jobs(
        self, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListJobsResponse, RawError]:
        """Lists jobs in a seller account. Results are sorted by title in ascending order.

        Args:
            cursor: The pagination cursor returned by the previous call to this endpoint. Provide this cursor to
                retrieve the next page of results for your original request. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/jobs"),
            query_params=[param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListJobsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_job(
        self, job_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveJobResponse, RawError]:
        """Retrieves a specified job.

        Args:
            job_id: The ID of the job to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/jobs/{job_id}"),
            path_params=[param[str]("job_id", job_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveJobResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_team_member(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveTeamMemberResponse, RawError]:
        """Retrieves a ``TeamMember`` object for the given ``TeamMember.id``. Learn about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/{team_member_id}"),
            path_params=[param[str]("team_member_id", team_member_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveTeamMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_wage_setting(
        self, team_member_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveWageSettingResponse, RawError]:
        """Retrieves a ``WageSetting`` object for a team member specified by ``TeamMember.id``. For more information,
        see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting>`__.

        Square recommends using `RetrieveTeamMember <api-endpoint:Team-RetrieveTeamMember>`__ or `SearchTeamMembers
        <api-endpoint:Team-SearchTeamMembers>`__ to get this information directly from the ``TeamMember.wage_setting``
        field.

        Args:
            team_member_id: The ID of the team member for which to retrieve the wage setting.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/team-members/{team_member_id}/wage-setting"),
            path_params=[param[str]("team_member_id", team_member_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveWageSettingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def search_team_members(
        self,
        body: SearchTeamMembersRequest | SearchTeamMembersRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchTeamMembersResponse, RawError]:
        """Returns a paginated list of ``TeamMember`` objects for a business. The list can be filtered by location IDs,
        ``ACTIVE`` or ``INACTIVE`` status, or whether the team member is the Square account owner.

        Args:
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/team-members/search"),
            body=json_body[SearchTeamMembersRequest | SearchTeamMembersRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SearchTeamMembersResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_job(
        self,
        job_id: str,
        body: UpdateJobRequest | UpdateJobRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateJobResponse, RawError]:
        """Updates the title or tip eligibility of a job. Changes to the title propagate to all ``JobAssignment``,
        ``Shift``, and ``TeamMemberWage`` objects that reference the job ID. Changes to tip eligibility propagate to all
        ``TeamMemberWage`` objects that reference the job ID.

        Args:
            job_id: The ID of the job to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/team-members/jobs/{job_id}"),
            path_params=[param[str]("job_id", job_id)],
            body=json_body[UpdateJobRequest | UpdateJobRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateJobResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_team_member(
        self,
        team_member_id: str,
        body: UpdateTeamMemberRequest | UpdateTeamMemberRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateTeamMemberResponse, RawError]:
        """Updates a single ``TeamMember`` object. The ``TeamMember`` object is returned on successful updates. Learn
        about `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member>`__.

        Args:
            team_member_id: The ID of the team member to update.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/team-members/{team_member_id}"),
            path_params=[param[str]("team_member_id", team_member_id)],
            body=json_body[UpdateTeamMemberRequest | UpdateTeamMemberRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateTeamMemberResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def update_wage_setting(
        self,
        team_member_id: str,
        body: UpdateWageSettingRequest | UpdateWageSettingRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateWageSettingResponse, RawError]:
        """Creates or updates a ``WageSetting`` object. The object is created if a ``WageSetting`` with the specified
        ``team_member_id`` doesn't exist. Otherwise, it fully replaces the ``WageSetting`` object for the team member.
        The ``WageSetting`` is returned on a successful update. For more information, see `Troubleshooting the Team API
        <https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting>`__.

        Square recommends using `CreateTeamMember <api-endpoint:Team-CreateTeamMember>`__ or `UpdateTeamMember
        <api-endpoint:Team-UpdateTeamMember>`__ to manage the ``TeamMember.wage_setting`` field directly.

        Args:
            team_member_id: The ID of the team member for which to update the ``WageSetting`` object.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PUT",
            url_template=self._server.default("/v2/team-members/{team_member_id}/wage-setting"),
            path_params=[param[str]("team_member_id", team_member_id)],
            body=json_body[UpdateWageSettingRequest | UpdateWageSettingRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[UpdateWageSettingResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
