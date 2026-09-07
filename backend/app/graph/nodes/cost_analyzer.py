from app.mock.mock_aws import MockAWSService
from app.services.cost.analyzer import CostAnalyzer


aws = MockAWSService()
analyzer = CostAnalyzer()


def cost_analyzer_node(state):
    cost_data = aws.get_cost()

    analysis = analyzer.analyze(cost_data)

    return {
        "billing_data": cost_data,
        "cost_analysis": analysis
    }