from enums import EnergyType
from energy_resources import EnergyResource
from power_plants import PowerPlant
from portfolio import Portfolio
from printer import print_portfolio_info

# Creating energy resources
coal = EnergyResource("Coal", False, 543, 43, EnergyType.FOSSIL)
solar = EnergyResource("Solar", False, 0, 43, EnergyType.RENEWABLE)

# Creating power plants
powerplant1 = PowerPlant("P1", coal, 234, 343, 21, 432)
powerplant2 = PowerPlant("P2", coal, 121, 144, 30, 432)
powerplant3 = PowerPlant("P3", solar, 200, 200, 25, 300)
powerplant4 = PowerPlant("P4", solar, 150, 180, 20, 250)
powerplant5 = PowerPlant("P5", solar, 100, 120, 15, 150)

# Creating a portfolio
portfolio = Portfolio(1, "MyPortfolio", [powerplant1, powerplant2, powerplant3, powerplant4, powerplant5])

# Printing portfolio information using the printer module
print_portfolio_info(portfolio)
