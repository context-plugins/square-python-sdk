from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .create_team_member_request import CreateTeamMemberRequest, CreateTeamMemberRequestDict


class BulkCreateTeamMembersRequest(SdkBaseModel):
    """Represents a bulk create request for ``TeamMember`` objects."""

    team_members: dict[str, CreateTeamMemberRequest]
    """The data used to create the ``TeamMember`` objects. Each key is the ``idempotency_key`` that maps to the
    ``CreateTeamMemberRequest``. The maximum number of create objects is 25.

    If you include a team member's ``wage_setting``, you must provide ``job_id`` for each job assignment. To get job
    IDs, call `ListJobs <api-endpoint:Team-ListJobs>`__."""


class BulkCreateTeamMembersRequestDict(TypedDict):
    team_members: dict[str, CreateTeamMemberRequestDict]
