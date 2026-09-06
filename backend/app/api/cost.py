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
        "cost_analysis": result["cost_analysis"],
        "anomaly": result["anomaly"],
        "service_analysis": result["service_analysis"]
    }