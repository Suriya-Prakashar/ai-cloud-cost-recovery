from app.graph import graph
from langgraph.graph import StateGraph, START, END

from app.graph.state import CostRecoveryState


from app.graph.nodes.cost_analyzer import (
    cost_analyzer_node
)

from app.graph.nodes.anomaly_detector import (
    anomaly_detector_node
)

from app.graph.nodes.service_analyzer import (
    service_analyzer_node
)

from app.graph.nodes.resource_investigator import (
    resource_investigator_node
)

from app.graph.nodes.evidence_collector import (
    evidence_collector_node
)

from app.graph.nodes.root_cause_analyzer import (
    root_cause_analyzer_node
)


def build_cost_recovery_graph():

    graph = StateGraph(
        CostRecoveryState
    )

    # -------------------------
    # Nodes
    # -------------------------

    graph.add_node(
        "cost_analyzer",
        cost_analyzer_node
    )

    graph.add_node(
        "anomaly_detector",
        anomaly_detector_node
    )

    graph.add_node(
        "service_analyzer",
        service_analyzer_node
    )

    graph.add_node(
        "resource_investigator",
        resource_investigator_node
    )

    graph.add_node(
        "evidence_collector",
        evidence_collector_node
    )

    graph.add_node(
        "root_cause_analyzer",
        root_cause_analyzer_node
)

    # -------------------------
    # Edges
    # -------------------------

    graph.add_edge(
        START,
        "cost_analyzer"
    )

    graph.add_edge(
        "cost_analyzer",
        "anomaly_detector"
    )

    graph.add_edge(
        "anomaly_detector",
        "service_analyzer"
    )

    graph.add_edge(
        "service_analyzer",
        "resource_investigator"
    )

    graph.add_edge(
        "resource_investigator",
        "evidence_collector"
    )

    graph.add_edge(
        "evidence_collector",
        "root_cause_analyzer"
    )

    graph.add_edge(
        "root_cause_analyzer",
        END
    )

    return graph.compile()


cost_recovery_graph = (
    build_cost_recovery_graph()
)