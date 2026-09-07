from app.services.investigation.evidence_collector import (
    EvidenceCollector
)


collector = EvidenceCollector()


def evidence_collector_node(state):

    investigated_resources = state.get(
        "investigated_resources",
        []
    )

    evidence = collector.collect(
        investigated_resources
    )

    return {
        "evidence": evidence
    }