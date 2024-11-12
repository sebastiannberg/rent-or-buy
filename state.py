from dataclasses import dataclass


@dataclass
class State:
    year: int
    equity: float # Egenkapital
    wealth: float # Formue
    debt: float # Gjeld
    home_market_value: float # Markedsverdi bolig
    effective_mortgage_rate: float # Effektive rente boliglån
    property_tax_rate: float # Sats for eiendomsskatt
    property_tax_exemption: float # Bunnfradrag eiendomsskatt