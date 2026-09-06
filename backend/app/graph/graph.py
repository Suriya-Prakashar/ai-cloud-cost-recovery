from langgraph.graph import StateGraph, START, END

from app.graph.state import CostRecoveryState

from app.graph.nodes.cost_analyzer import cost_analyzer_node
from app.graph.nodes.anomaly_detector import anomaly_detector_node
from app.graph.nodes.service_analyzer import service_analyzer_node


def build_cost_recovery_graph():

    graph = StateGraph(CostRecoveryState)

    graph.add_node("cost_analyzer", cost_analyzer_node)
    graph.add_node("anomaly_detector", anomaly_detector_node)
    graph.add_node("service_analyzer", service_analyzer_node)

    graph.add_edge(START, "cost_analyzer")
    graph.add_edge("cost_analyzer", "anomaly_detector")
    graph.add_edge("anomaly_detector", "service_analyzer")
    graph.add_edge("service_analyzer", END)

    return graph.compile()


cost_recovery_graph = build_cost_recovery_graph()