class AnomalyDetector:

    def detect(self, cost_analysis: dict) -> dict:
        increase_percentage = cost_analysis["increase_percentage"]

        if increase_percentage >= 100:
            severity = "HIGH"
            is_anomaly = True

        elif increase_percentage >= 30:
            severity = "MEDIUM"
            is_anomaly = True

        else:
            severity = "LOW"
            is_anomaly = False

        return {
            "is_anomaly": is_anomaly,
            "severity": severity,
            "increase_percentage": increase_percentage
        }