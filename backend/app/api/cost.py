from fastapi import APIRouter

from app.graph.graph import cost_recovery_graph


router = APIRouter(
    prefix="/cost",
    tags=["Cost Intelligence"]
)


@router.get("/analyze")
def analyze_cost():

    result = cost_recovery_graph.invoke({})

    return {
        "cost_analysis": result.get(
            "cost_analysis"
        ),
        "anomaly": result.get(
            "anomaly"
        ),
        "service_analysis": result.get(
            "service_analysis"
        ),
        "investigated_resources": result.get(
            "investigated_resources",
            []
        ),
        "evidence": result.get(
            "evidence",
            []
        ),
        "root_cause": result.get(
            "root_cause",
            {}
        ),
    }