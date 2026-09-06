from fastapi import APIRouter

from app.mock.mock_aws import MockAWSService
from app.services.cost.analyzer import CostAnalyzer
from app.services.cost.anomaly_detector import AnomalyDetector
from app.services.cost.service_analyzer import ServiceAnalyzer


router = APIRouter(prefix="/cost", tags=["Cost Intelligence"])

aws = MockAWSService()

analyzer = CostAnalyzer()
detector = AnomalyDetector()
service_analyzer = ServiceAnalyzer()


@router.get("/analyze")
def analyze_cost():

    cost_data = aws.get_cost()

    analysis = analyzer.analyze(cost_data)

    anomaly = detector.detect(analysis)

    services = aws.get_services()

    service_analysis = service_analyzer.analyze(services)

    return {
        "cost_analysis": analysis,
        "anomaly": anomaly,
        "service_analysis": service_analysis
    }