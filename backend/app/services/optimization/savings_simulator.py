class SavingsSimulator:

    def simulate(
        self,
        strategies: list
    ) -> dict:

        if not strategies:
            return {
                "recommended_strategy": None,
                "estimated_monthly_saving": 0,
                "estimated_yearly_saving": 0,
                "strategies": []
            }

        ranked_strategies = sorted(
            strategies,
            key=lambda strategy: strategy[
                "estimated_monthly_saving"
            ],
            reverse=True
        )

        recommended_strategy = ranked_strategies[0]

        monthly_saving = recommended_strategy[
            "estimated_monthly_saving"
        ]

        yearly_saving = monthly_saving * 12

        return {
            "recommended_strategy": recommended_strategy,
            "estimated_monthly_saving": round(
                monthly_saving,
                2
            ),
            "estimated_yearly_saving": round(
                yearly_saving,
                2
            ),
            "strategies": ranked_strategies
        }