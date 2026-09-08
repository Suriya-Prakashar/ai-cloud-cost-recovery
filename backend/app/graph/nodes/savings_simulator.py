from app.services.optimization.savings_simulator import (
    SavingsSimulator
)

simulator = SavingsSimulator()


def savings_simulator_node(state):

    strategies = state.get(
        "strategies",
        []
    )

    savings = simulator.simulate(
        strategies
    )

    return {
        "savings": savings
    }