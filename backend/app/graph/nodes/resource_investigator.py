from app.mock.mock_aws import MockAWSService

from app.services.investigation.resource_investigator import (
    ResourceInvestigator
)


aws = MockAWSService()

investigator = ResourceInvestigator()


def resource_investigator_node(state):

    service_analysis = state.get(
        "service_analysis",
        {}
    )

    top_service = service_analysis.get(
        "top_service"
    )

    if not top_service:

        return {
            "resources": [],
            "investigated_resources": []
        }

    target_service = top_service.get(
        "service"
    )

    resources = aws.get_resources()

    investigated_resources = investigator.investigate(
        resources,
        target_service
    )

    return {
        "resources": resources,
        "investigated_resources": investigated_resources
    }