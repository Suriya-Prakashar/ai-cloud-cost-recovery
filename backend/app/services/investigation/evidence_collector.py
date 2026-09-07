class EvidenceCollector:

    def collect(self, resources: list) -> list:

        evidence = []

        for resource in resources:

            resource_id = resource.get("resource_id")

            evidence.append({
                "resource_id": resource_id,
                "source": "EC2",
                "metric": "Instance type",
                "value": resource.get("instance_type")
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "EC2",
                "metric": "Cost",
                "value": resource.get("cost"),
                "unit": "USD/month"
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "CloudWatch",
                "metric": "CPU utilization",
                "value": resource.get("cpu"),
                "unit": "percent"
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "CloudWatch",
                "metric": "Memory utilization",
                "value": resource.get("memory"),
                "unit": "percent"
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "CloudWatch",
                "metric": "Network utilization",
                "value": resource.get("network"),
                "unit": "percent"
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "EC2",
                "metric": "Environment",
                "value": resource.get("environment")
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "EC2",
                "metric": "Owner",
                "value": resource.get("owner")
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "EC2",
                "metric": "Running days",
                "value": resource.get("running_days"),
                "unit": "days"
            })

            evidence.append({
                "resource_id": resource_id,
                "source": "CloudTrail",
                "metric": "Recent deployment",
                "value": resource.get(
                    "recent_deployment"
                )
            })

        return evidence