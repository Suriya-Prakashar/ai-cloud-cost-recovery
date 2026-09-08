from app.services.optimization.strategy_generator import (
    StrategyGenerator
)

generator = StrategyGenerator()


def optimization_planner_node(state):

    investigated_resources = state.get(
        "investigated_resources",
        []
    )

    root_cause = state.get(
        "root_cause",
        {}
    )

    if not investigated_resources:
        return {
            "strategies": []
        }

    resource = investigated_resources[0]

    strategies = generator.generate(
        resource,
        root_cause
    )

    return {
        "strategies": strategies
    }