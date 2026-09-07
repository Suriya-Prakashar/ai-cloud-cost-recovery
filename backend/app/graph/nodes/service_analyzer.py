from app.mock.mock_aws import MockAWSService
from app.services.cost.service_analyzer import ServiceAnalyzer


aws = MockAWSService()
service_analyzer = ServiceAnalyzer()


def service_analyzer_node(state):
    services = aws.get_services()

    analysis = service_analyzer.analyze(services)

    return {
        "services": services,
        "service_analysis": analysis
    }