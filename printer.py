from typing import Dict

def print_energy_resource(resource):
    print("=== Energy Resource Information ===")
    print(f"Resource Name: {resource.get_name()}")
    print(f"Tax Exempt: {resource.is_tax_exempt()}")
    print(f"Carbon Emission: {resource.get_carbon_emission():.2f}")
    print(f"Fuel Cost per Unit: {resource.get_fuel_cost_per_unit():.2f}")
    print(f"Energy Type: {resource.get_energy_type().value}")
    print()

def print_power_plant_info(plant):
    print("=== Power Plant Information ===")
    print(f"Power Plant Name: {plant.get_name()}")
    print(f"Capacity: {plant.get_capacity()}")
    print(f"Total Cost: {plant.calculate_total_cost():.2f}")
    print(f"Annual Cost: {plant.calculate_annual_cost():.2f}")
    print(f"Total Emissions: {plant.calculate_emissions():.2f}")
    print(f"Resource Information:")
    print_energy_resource(plant.get_resource())

def print_portfolio_info(portfolio):
    print("=== Portfolio Information ===")
    print(f"Portfolio ID: {portfolio.get_id()}")
    print(f"Portfolio Name: {portfolio.get_name()}")
    print("Power Plants in the Portfolio:")
    for plant in portfolio.get_power_plants():
        print_power_plant_info(plant)
    print(f"Total Portfolio Capacity: {portfolio.calculate_total_capacity()}")
    print("Energy Resource Ratios:")
    resource_ratios: Dict[str, float] = portfolio.calculate_resource_ratios()
    for resource, ratio in resource_ratios.items():
        print(f"{resource}: {ratio:.2%}")
    print("Energy Type Ratios:")
    energy_type_ratios = portfolio.calculate_energy_type_ratios()
    for energy_type, ratio in energy_type_ratios.items():
        print(f"{energy_type}: {ratio:.2%}")
