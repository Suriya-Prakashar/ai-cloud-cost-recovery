from app.services.cost.anomaly_detector import AnomalyDetector


detector = AnomalyDetector()


def anomaly_detector_node(state):
    cost_analysis = state["cost_analysis"]

    anomaly = detector.detect(cost_analysis)

    return {
        "anomaly": anomaly
    }