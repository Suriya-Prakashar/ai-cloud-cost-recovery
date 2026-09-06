class CostAnalyzer:

    def analyze(self, cost_data: dict) -> dict:
        yesterday = cost_data["yesterday"]
        today = cost_data["today"]

        increase = today - yesterday

        if yesterday > 0:
            increase_percentage = (increase / yesterday) * 100
        else:
            increase_percentage = 0

        return {
            "yesterday_cost": yesterday,
            "today_cost": today,
            "cost_increase": round(increase, 2),
            "increase_percentage": round(increase_percentage, 2)
        }