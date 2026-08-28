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
    multipart_body,
    param,
    raw_error_response,
)
from ..models.accept_dispute_response import AcceptDisputeResponse
from ..models.create_dispute_evidence_file_request import (
    CreateDisputeEvidenceFileRequest,
    CreateDisputeEvidenceFileRequestDict,
)
from ..models.create_dispute_evidence_file_response import CreateDisputeEvidenceFileResponse
from ..models.create_dispute_evidence_text_request import (
    CreateDisputeEvidenceTextRequest,
    CreateDisputeEvidenceTextRequestDict,
)
from ..models.create_dispute_evidence_text_response import CreateDisputeEvidenceTextResponse
from ..models.delete_dispute_evidence_response import DeleteDisputeEvidenceResponse
from ..models.enums.dispute_state import DisputeStateOrStr
from ..models.list_dispute_evidence_response import ListDisputeEvidenceResponse
from ..models.list_disputes_response import ListDisputesResponse
from ..models.retrieve_dispute_evidence_response import RetrieveDisputeEvidenceResponse
from ..models.retrieve_dispute_response import RetrieveDisputeResponse
from ..models.submit_evidence_response import SubmitEvidenceResponse
from ..server.server import Server


class Disputes:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DisputesWithRawResponse(client, server, auth)

    def accept_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AcceptDisputeResponse:
        """Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute
        state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account does not have
        sufficient funds, Square debits the associated bank account.

        Args:
            dispute_id: The ID of the dispute you want to accept.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.accept_dispute(dispute_id, request_options=request_options).unwrap()

    def create_dispute_evidence_file(
        self,
        dispute_id: str,
        *,
        request: CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateDisputeEvidenceFileResponse:
        """Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP multipart/form-data file
        uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            request: Defines the parameters for a ``CreateDisputeEvidenceFile`` request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_dispute_evidence_file(
            dispute_id, request=request, image_file=image_file, request_options=request_options
        ).unwrap()

    def create_dispute_evidence_text(
        self,
        dispute_id: str,
        body: CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateDisputeEvidenceTextResponse:
        """Uploads text to use as evidence for a dispute challenge.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.create_dispute_evidence_text(
            dispute_id, body, request_options=request_options
        ).unwrap()

    def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteDisputeEvidenceResponse:
        """Removes specified evidence from a dispute. Square does not send the bank any evidence that is removed.

        Args:
            dispute_id: The ID of the dispute from which you want to remove evidence.
            evidence_id: The ID of the evidence you want to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_dispute_evidence(
            dispute_id, evidence_id, request_options=request_options
        ).unwrap()

    def list_dispute_evidence(
        self, dispute_id: str, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListDisputeEvidenceResponse:
        """Returns a list of evidence associated with a dispute.

        Args:
            dispute_id: The ID of the dispute.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_dispute_evidence(
            dispute_id, cursor=cursor, request_options=request_options
        ).unwrap()

    def list_disputes(
        self,
        *,
        cursor: str | None = None,
        states: DisputeStateOrStr | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDisputesResponse:
        """Returns a list of disputes associated with a particular account.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            states: The dispute states used to filter the result. If not specified, the endpoint returns all disputes.
            location_id: The ID of the location for which to return a list of disputes. If not specified, the endpoint
                returns disputes associated with all locations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.list_disputes(
            cursor=cursor, states=states, location_id=location_id, request_options=request_options
        ).unwrap()

    def retrieve_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveDisputeResponse:
        """Returns details about a specific dispute.

        Args:
            dispute_id: The ID of the dispute you want more details about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_dispute(dispute_id, request_options=request_options).unwrap()

    def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveDisputeEvidenceResponse:
        """Returns the metadata for the evidence specified in the request URL path.

        You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be
        downloaded after you upload it.

        Args:
            dispute_id: The ID of the dispute from which you want to retrieve evidence metadata.
            evidence_id: The ID of the evidence to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.retrieve_dispute_evidence(
            dispute_id, evidence_id, request_options=request_options
        ).unwrap()

    def submit_evidence(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubmitEvidenceResponse:
        """Submits evidence to the cardholder's bank.

        The evidence submitted by this endpoint includes evidence uploaded using the `CreateDisputeEvidenceFile
        <api-endpoint:Disputes-CreateDisputeEvidenceFile>`__ and `CreateDisputeEvidenceText
        <api-endpoint:Disputes-CreateDisputeEvidenceText>`__ endpoints and evidence automatically provided by Square,
        when available. Evidence cannot be removed from a dispute after submission.

        Args:
            dispute_id: The ID of the dispute for which you want to submit evidence.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.submit_evidence(dispute_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> DisputesWithRawResponse:
        return self._with_raw_response


class AsyncDisputes:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDisputesWithRawResponse(client, server, auth)

    async def accept_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AcceptDisputeResponse:
        """Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute
        state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account does not have
        sufficient funds, Square debits the associated bank account.

        Args:
            dispute_id: The ID of the dispute you want to accept.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.accept_dispute(dispute_id, request_options=request_options)).unwrap()

    async def create_dispute_evidence_file(
        self,
        dispute_id: str,
        *,
        request: CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateDisputeEvidenceFileResponse:
        """Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP multipart/form-data file
        uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            request: Defines the parameters for a ``CreateDisputeEvidenceFile`` request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_dispute_evidence_file(
                dispute_id, request=request, image_file=image_file, request_options=request_options
            )
        ).unwrap()

    async def create_dispute_evidence_text(
        self,
        dispute_id: str,
        body: CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CreateDisputeEvidenceTextResponse:
        """Uploads text to use as evidence for a dispute challenge.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.create_dispute_evidence_text(
                dispute_id, body, request_options=request_options
            )
        ).unwrap()

    async def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> DeleteDisputeEvidenceResponse:
        """Removes specified evidence from a dispute. Square does not send the bank any evidence that is removed.

        Args:
            dispute_id: The ID of the dispute from which you want to remove evidence.
            evidence_id: The ID of the evidence you want to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_dispute_evidence(
                dispute_id, evidence_id, request_options=request_options
            )
        ).unwrap()

    async def list_dispute_evidence(
        self, dispute_id: str, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ListDisputeEvidenceResponse:
        """Returns a list of evidence associated with a dispute.

        Args:
            dispute_id: The ID of the dispute.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_dispute_evidence(
                dispute_id, cursor=cursor, request_options=request_options
            )
        ).unwrap()

    async def list_disputes(
        self,
        *,
        cursor: str | None = None,
        states: DisputeStateOrStr | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDisputesResponse:
        """Returns a list of disputes associated with a particular account.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            states: The dispute states used to filter the result. If not specified, the endpoint returns all disputes.
            location_id: The ID of the location for which to return a list of disputes. If not specified, the endpoint
                returns disputes associated with all locations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.list_disputes(
                cursor=cursor, states=states, location_id=location_id, request_options=request_options
            )
        ).unwrap()

    async def retrieve_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveDisputeResponse:
        """Returns details about a specific dispute.

        Args:
            dispute_id: The ID of the dispute you want more details about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.retrieve_dispute(dispute_id, request_options=request_options)).unwrap()

    async def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> RetrieveDisputeEvidenceResponse:
        """Returns the metadata for the evidence specified in the request URL path.

        You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be
        downloaded after you upload it.

        Args:
            dispute_id: The ID of the dispute from which you want to retrieve evidence metadata.
            evidence_id: The ID of the evidence to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.retrieve_dispute_evidence(
                dispute_id, evidence_id, request_options=request_options
            )
        ).unwrap()

    async def submit_evidence(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> SubmitEvidenceResponse:
        """Submits evidence to the cardholder's bank.

        The evidence submitted by this endpoint includes evidence uploaded using the `CreateDisputeEvidenceFile
        <api-endpoint:Disputes-CreateDisputeEvidenceFile>`__ and `CreateDisputeEvidenceText
        <api-endpoint:Disputes-CreateDisputeEvidenceText>`__ endpoints and evidence automatically provided by Square,
        when available. Evidence cannot be removed from a dispute after submission.

        Args:
            dispute_id: The ID of the dispute for which you want to submit evidence.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Success

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (await self._with_raw_response.submit_evidence(dispute_id, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncDisputesWithRawResponse:
        return self._with_raw_response


class DisputesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def accept_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AcceptDisputeResponse, RawError]:
        """Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute
        state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account does not have
        sufficient funds, Square debits the associated bank account.

        Args:
            dispute_id: The ID of the dispute you want to accept.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/accept"),
            path_params=[param[str]("dispute_id", dispute_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[AcceptDisputeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_dispute_evidence_file(
        self,
        dispute_id: str,
        *,
        request: CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateDisputeEvidenceFileResponse, RawError]:
        """Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP multipart/form-data file
        uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            request: Defines the parameters for a ``CreateDisputeEvidenceFile`` request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence-files"),
            path_params=[param[str]("dispute_id", dispute_id)],
            body=multipart_body(
                [
                    param[CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None](
                        "request", request
                    ),
                ],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateDisputeEvidenceFileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def create_dispute_evidence_text(
        self,
        dispute_id: str,
        body: CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateDisputeEvidenceTextResponse, RawError]:
        """Uploads text to use as evidence for a dispute challenge.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence-text"),
            path_params=[param[str]("dispute_id", dispute_id)],
            body=json_body[CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateDisputeEvidenceTextResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteDisputeEvidenceResponse, RawError]:
        """Removes specified evidence from a dispute. Square does not send the bank any evidence that is removed.

        Args:
            dispute_id: The ID of the dispute from which you want to remove evidence.
            evidence_id: The ID of the evidence you want to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence/{evidence_id}"),
            path_params=[param[str]("dispute_id", dispute_id), param[str]("evidence_id", evidence_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteDisputeEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_dispute_evidence(
        self, dispute_id: str, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListDisputeEvidenceResponse, RawError]:
        """Returns a list of evidence associated with a dispute.

        Args:
            dispute_id: The ID of the dispute.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence"),
            path_params=[param[str]("dispute_id", dispute_id)],
            query_params=[param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListDisputeEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def list_disputes(
        self,
        *,
        cursor: str | None = None,
        states: DisputeStateOrStr | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDisputesResponse, RawError]:
        """Returns a list of disputes associated with a particular account.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            states: The dispute states used to filter the result. If not specified, the endpoint returns all disputes.
            location_id: The ID of the location for which to return a list of disputes. If not specified, the endpoint
                returns disputes associated with all locations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[DisputeStateOrStr | None]("states", states),
                param[str | None]("location_id", location_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListDisputesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveDisputeResponse, RawError]:
        """Returns details about a specific dispute.

        Args:
            dispute_id: The ID of the dispute you want more details about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes/{dispute_id}"),
            path_params=[param[str]("dispute_id", dispute_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveDisputeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveDisputeEvidenceResponse, RawError]:
        """Returns the metadata for the evidence specified in the request URL path.

        You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be
        downloaded after you upload it.

        Args:
            dispute_id: The ID of the dispute from which you want to retrieve evidence metadata.
            evidence_id: The ID of the evidence to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence/{evidence_id}"),
            path_params=[param[str]("dispute_id", dispute_id), param[str]("evidence_id", evidence_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveDisputeEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def submit_evidence(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubmitEvidenceResponse, RawError]:
        """Submits evidence to the cardholder's bank.

        The evidence submitted by this endpoint includes evidence uploaded using the `CreateDisputeEvidenceFile
        <api-endpoint:Disputes-CreateDisputeEvidenceFile>`__ and `CreateDisputeEvidenceText
        <api-endpoint:Disputes-CreateDisputeEvidenceText>`__ endpoints and evidence automatically provided by Square,
        when available. Evidence cannot be removed from a dispute after submission.

        Args:
            dispute_id: The ID of the dispute for which you want to submit evidence.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/submit-evidence"),
            path_params=[param[str]("dispute_id", dispute_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SubmitEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncDisputesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def accept_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AcceptDisputeResponse, RawError]:
        """Accepts the loss on a dispute. Square returns the disputed amount to the cardholder and updates the dispute
        state to ACCEPTED.

        Square debits the disputed amount from the seller’s Square account. If the Square account does not have
        sufficient funds, Square debits the associated bank account.

        Args:
            dispute_id: The ID of the dispute you want to accept.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/accept"),
            path_params=[param[str]("dispute_id", dispute_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[AcceptDisputeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_dispute_evidence_file(
        self,
        dispute_id: str,
        *,
        request: CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None = None,
        image_file: bytes | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateDisputeEvidenceFileResponse, RawError]:
        """Uploads a file to use as evidence in a dispute challenge. The endpoint accepts HTTP multipart/form-data file
        uploads in HEIC, HEIF, JPEG, PDF, PNG, and TIFF formats.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            request: Defines the parameters for a ``CreateDisputeEvidenceFile`` request.
            image_file: Value sent with the request.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence-files"),
            path_params=[param[str]("dispute_id", dispute_id)],
            body=multipart_body(
                [
                    param[CreateDisputeEvidenceFileRequest | CreateDisputeEvidenceFileRequestDict | None](
                        "request", request
                    ),
                ],
                {"image_file": image_file},
            ),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateDisputeEvidenceFileResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def create_dispute_evidence_text(
        self,
        dispute_id: str,
        body: CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CreateDisputeEvidenceTextResponse, RawError]:
        """Uploads text to use as evidence for a dispute challenge.

        Args:
            dispute_id: The ID of the dispute for which you want to upload evidence.
            body: An object containing the fields to POST for the request. See the corresponding object definition for
                field details.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence-text"),
            path_params=[param[str]("dispute_id", dispute_id)],
            body=json_body[CreateDisputeEvidenceTextRequest | CreateDisputeEvidenceTextRequestDict](body),
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[CreateDisputeEvidenceTextResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def delete_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[DeleteDisputeEvidenceResponse, RawError]:
        """Removes specified evidence from a dispute. Square does not send the bank any evidence that is removed.

        Args:
            dispute_id: The ID of the dispute from which you want to remove evidence.
            evidence_id: The ID of the evidence you want to remove.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence/{evidence_id}"),
            path_params=[param[str]("dispute_id", dispute_id), param[str]("evidence_id", evidence_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[DeleteDisputeEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_dispute_evidence(
        self, dispute_id: str, *, cursor: str | None = None, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListDisputeEvidenceResponse, RawError]:
        """Returns a list of evidence associated with a dispute.

        Args:
            dispute_id: The ID of the dispute.
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence"),
            path_params=[param[str]("dispute_id", dispute_id)],
            query_params=[param[str | None]("cursor", cursor)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListDisputeEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def list_disputes(
        self,
        *,
        cursor: str | None = None,
        states: DisputeStateOrStr | None = None,
        location_id: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListDisputesResponse, RawError]:
        """Returns a list of disputes associated with a particular account.

        Args:
            cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve
                the next set of results for the original query. For more information, see `Pagination
                <https://developer.squareup.com/docs/build-basics/common-api-patterns/pagination>`__.
            states: The dispute states used to filter the result. If not specified, the endpoint returns all disputes.
            location_id: The ID of the location for which to return a list of disputes. If not specified, the endpoint
                returns disputes associated with all locations.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes"),
            query_params=[
                param[str | None]("cursor", cursor),
                param[DisputeStateOrStr | None]("states", states),
                param[str | None]("location_id", location_id),
            ],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[ListDisputesResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_dispute(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveDisputeResponse, RawError]:
        """Returns details about a specific dispute.

        Args:
            dispute_id: The ID of the dispute you want more details about.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes/{dispute_id}"),
            path_params=[param[str]("dispute_id", dispute_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveDisputeResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def retrieve_dispute_evidence(
        self, dispute_id: str, evidence_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[RetrieveDisputeEvidenceResponse, RawError]:
        """Returns the metadata for the evidence specified in the request URL path.

        You must maintain a copy of any evidence uploaded if you want to reference it later. Evidence cannot be
        downloaded after you upload it.

        Args:
            dispute_id: The ID of the dispute from which you want to retrieve evidence metadata.
            evidence_id: The ID of the evidence to retrieve.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/v2/disputes/{dispute_id}/evidence/{evidence_id}"),
            path_params=[param[str]("dispute_id", dispute_id), param[str]("evidence_id", evidence_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[RetrieveDisputeEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def submit_evidence(
        self, dispute_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[SubmitEvidenceResponse, RawError]:
        """Submits evidence to the cardholder's bank.

        The evidence submitted by this endpoint includes evidence uploaded using the `CreateDisputeEvidenceFile
        <api-endpoint:Disputes-CreateDisputeEvidenceFile>`__ and `CreateDisputeEvidenceText
        <api-endpoint:Disputes-CreateDisputeEvidenceText>`__ endpoints and evidence automatically provided by Square,
        when available. Evidence cannot be removed from a dispute after submission.

        Args:
            dispute_id: The ID of the dispute for which you want to submit evidence.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/v2/disputes/{dispute_id}/submit-evidence"),
            path_params=[param[str]("dispute_id", dispute_id)],
            auth_scheme=self._auth.oauth2,
            decoder=json_decoder[SubmitEvidenceResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
