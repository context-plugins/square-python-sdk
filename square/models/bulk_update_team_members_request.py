from __future__ import annotations

from typing_extensions import TypedDict

from ..core import SdkBaseModel
from .update_team_member_request import UpdateTeamMemberRequest, UpdateTeamMemberRequestDict


class BulkUpdateTeamMembersRequest(SdkBaseModel):
    """Represents a bulk update request for ``TeamMember`` objects."""

    team_members: dict[str, UpdateTeamMemberRequest]
    """The data used to update the ``TeamMember`` objects. Each key is the ``team_member_id`` that maps to the
    ``UpdateTeamMemberRequest``. The maximum number of update objects is 25.

    For each team member, include the fields to add, change, or clear. Fields can be cleared using a null value. To
    update ``wage_setting.job_assignments``, you must provide the complete list of job assignments. If needed, call
    `ListJobs <api-endpoint:Team-ListJobs>`__ to get the required ``job_id`` values."""


class BulkUpdateTeamMembersRequestDict(TypedDict):
    team_members: dict[str, UpdateTeamMemberRequest | UpdateTeamMemberRequestDict]
