from typing import TypedDict


class CostRecoveryState(TypedDict, total=False):
    account_id: str
    billing_data: dict
    cost_analysis: dict
    anomaly: dict
    services: list
    service_analysis: dict
    resources: list
    investigated_resources: list
    evidence: list
    root_cause: dict
    strategies: list
    savings: dict