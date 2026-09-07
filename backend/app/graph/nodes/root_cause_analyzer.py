from app.services.forensics.root_cause_analyzer import (
    RootCauseAnalyzer
)


analyzer = RootCauseAnalyzer()


def root_cause_analyzer_node(state):

    investigated_resources = state.get(
        "investigated_resources",
        []
    )

    evidence = state.get(
        "evidence",
        []
    )

    root_cause = analyzer.analyze(
        investigated_resources,
        evidence
    )

    return {
        "root_cause": root_cause
    }