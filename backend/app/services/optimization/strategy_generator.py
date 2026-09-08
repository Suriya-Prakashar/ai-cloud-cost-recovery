class StrategyGenerator:

    def generate(
        self,
        resource: dict,
        root_cause: dict
    ) -> list:

        strategies = []

        if not resource:
            return strategies

        cost = resource.get("cost", 0)

        cpu = resource.get("cpu")
        memory = resource.get("memory")
        network = resource.get("network")

        environment = resource.get("environment")

        # Strategy 1: STOP
        if environment == "development":
            strategies.append({
                "strategy": "STOP",
                "description": (
                    "Stop the development resource "
                    "when it is not required."
                ),
                "current_monthly_cost": cost,
                "estimated_monthly_saving": round(cost, 2),
                "risk": "HIGH"
            })

        # Strategy 2: DOWNSIZE
        if (
            cpu is not None
            and memory is not None
            and cpu < 10
            and memory < 10
        ):
            estimated_saving = cost * 0.70

            strategies.append({
                "strategy": "DOWNSIZE",
                "description": (
                    "Move the resource to a smaller "
                    "instance type based on low utilization."
                ),
                "current_monthly_cost": cost,
                "estimated_monthly_saving": round(
                    estimated_saving,
                    2
                ),
                "risk": "MEDIUM"
            })

        # Strategy 3: SCHEDULE
        if environment == "development":
            estimated_saving = cost * 0.60

            strategies.append({
                "strategy": "SCHEDULE",
                "description": (
                    "Run the development resource only "
                    "during required working hours."
                ),
                "current_monthly_cost": cost,
                "estimated_monthly_saving": round(
                    estimated_saving,
                    2
                ),
                "risk": "LOW"
            })

        return strategies