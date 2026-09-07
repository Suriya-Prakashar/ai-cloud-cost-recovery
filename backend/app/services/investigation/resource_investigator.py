class ResourceInvestigator:

    def investigate(
        self,
        resources: list,
        target_service: str
    ) -> list:

        investigated_resources = []

        for resource in resources:

            resource_type = resource.get("type")

            if resource_type != target_service:
                continue

            investigated_resource = {
                "resource_id": resource.get("id"),
                "resource_type": resource.get("type"),
                "instance_type": resource.get("instance_type"),
                "cost": resource.get("cost"),
                "cpu": resource.get("cpu"),
                "memory": resource.get("memory"),
                "network": resource.get("network"),
                "environment": resource.get("environment"),
                "owner": resource.get("owner"),
                "running_days": resource.get("running_days"),
                "recent_deployment": resource.get(
                    "recent_deployment"
                )
            }

            investigated_resources.append(
                investigated_resource
            )

        return investigated_resources