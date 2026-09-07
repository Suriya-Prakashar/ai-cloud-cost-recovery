class RootCauseAnalyzer:

    def analyze(
        self,
        investigated_resources: list,
        evidence: list
    ) -> dict:

        if not investigated_resources:
            return {
                "root_cause": "No resource identified",
                "confidence": 0,
                "explanation": "No resource evidence was available.",
                "supporting_evidence": []
            }

        resource = investigated_resources[0]

        supporting_evidence = []

        cpu = resource.get("cpu")
        memory = resource.get("memory")
        network = resource.get("network")
        environment = resource.get("environment")
        owner = resource.get("owner")
        running_days = resource.get("running_days")
        recent_deployment = resource.get(
            "recent_deployment"
        )

        confidence = 0

        if cpu is not None and cpu < 10:
            confidence += 20
            supporting_evidence.append(
                "CPU utilization is below 10%"
            )

        if memory is not None and memory < 10:
            confidence += 15
            supporting_evidence.append(
                "Memory utilization is below 10%"
            )

        if network is not None and network < 10:
            confidence += 10
            supporting_evidence.append(
                "Network utilization is below 10%"
            )

        if environment == "development":
            confidence += 15
            supporting_evidence.append(
                "Resource belongs to development environment"
            )

        if owner is None:
            confidence += 15
            supporting_evidence.append(
                "Resource has no identified owner"
            )

        if running_days is not None and running_days >= 14:
            confidence += 10
            supporting_evidence.append(
                "Resource has been running for an extended period"
            )

        if recent_deployment is False:
            confidence += 10
            supporting_evidence.append(
                "No recent deployment was detected"
            )

        confidence = min(confidence, 100)

        root_cause = (
            "Probable underutilized development "
            "resource"
        )

        explanation = (
            "The resource shows very low utilization, "
            "belongs to a development environment, "
            "has no identified owner, has been running "
            "for an extended period, and has no recent "
            "deployment activity."
        )

        return {
            "root_cause": root_cause,
            "confidence": confidence,
            "explanation": explanation,
            "supporting_evidence": supporting_evidence
        }