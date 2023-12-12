from energy_resources import EnergyResource
from enums import EnergyType
from power_plants import PowerPlant
from portfolio import Portfolio
coal = EnergyResource("Coal", False, 543, 43,EnergyType.FOSSIL)
solar = EnergyResource("Solar", False, 0, 43,EnergyType.RENEWABLE)
print(coal.get_energy_type().value)
powerplant1 = PowerPlant("P1", coal, 234,343,21,432)
powerplant2 = PowerPlant("P2", solar, 121,144,30,432)
print(powerplant1.calculate_emissions())
portflolio1 = Portfolio(1,"port1")
portflolio1.add_power_plant(powerplant2)
portflolio1.add_power_plant(powerplant1)
print(portflolio1.calculate_energy_type_ratios())