from dataclasses import replace

from state import State


class Simulator:

    def __init__(self, initial_state: State, n_simulations: int, n_years: int) -> None:
        self.initial_state = initial_state
        self.n_simulations = n_simulations
        self.n_years = n_years

    def run_simulations(self):
        outcomes = []
        for _ in range(self.n_simulations):
            current_state = replace(self.initial_state)
            for _ in range(self.n_years):
                current_state = self.simulate_year(current_state)
            outcomes.append(current_state)
        return outcomes
    
    def simulate_year(self, state: State) -> State:
       
       
       
       
       
       state.year += 1
       return state

initial_state = State(
    year=2024,
    equity=300000,
    wealth=0,
    debt=200000,
    home_market_value=2100000,
    effective_mortgage_rate=0.052,
    property_tax_rate=0.00265,
    property_tax_exemption=550000
)
simulator = Simulator(
    initial_state=initial_state,
    n_simulations=1,
    n_years=5
)
outcomes = simulator.run_simulations()
print(outcomes)
