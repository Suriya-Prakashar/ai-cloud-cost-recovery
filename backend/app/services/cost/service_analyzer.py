class ServiceAnalyzer:

    def analyze(self, services: list) -> dict:

        if not services:
            return {
                "top_service": None,
                "services": []
            }

        sorted_services = sorted(
            services,
            key=lambda service: service["cost"],
            reverse=True
        )

        top_service = sorted_services[0]

        total_cost = sum(
            service["cost"]
            for service in services
        )

        if total_cost > 0:
            contribution_percentage = (
                top_service["cost"] / total_cost
            ) * 100
        else:
            contribution_percentage = 0

        return {
            "top_service": top_service,
            "contribution_percentage": round(
                contribution_percentage,
                2
            ),
            "services": sorted_services
        }