class EnergyResource:
    def __init__(self, name, tax_exempt, carbon_emission, fuel_cost_per_unit):
        self._name = name  # Private attribute
        self._tax_exempt = tax_exempt  # Private attribute
        self._carbon_emission = carbon_emission  # Private attribute
        self._fuel_cost_per_unit = fuel_cost_per_unit  # Private attribute

    def get_name(self):
        return self._name

class PowerPlant(EnergyResource):
    def __init__(self, name, construction_cost, maintenance_cost, operating_cost, lifetime, energy_type, capacity):
        super().__init__(name, False, 0, 0)  # Inherit and set tax_exempt, carbon_emission, and fuel_cost_per_unit
        self._construction_cost = construction_cost  # Private attribute
        self._maintenance_cost = maintenance_cost  # Private attribute
        self._operating_cost = operating_cost  # Private attribute
        self._lifetime = lifetime  # Private attribute
        self._energy_type = energy_type  # Private attribute
        self._capacity = capacity  # Private attribute

    def calculate_total_cost(self):
        return self._construction_cost + (self._lifetime * self._maintenance_cost)

    def calculate_annual_cost(self):
        return self.calculate_total_cost() / self._lifetime

    def calculate_emissions(self):
        if self._energy_type == "fossil":
            emissions_per_unit = self.resource._carbon_emission  # Carbon emission per unit of energy
            energy_produced = self._lifetime * self._capacity  # Total energy produced during the lifetime
            return emissions_per_unit * energy_produced
        else:
            return 0

    def get_capacity(self):
        return self._capacity  # Implement get_capacity method

    def get_energy_type(self):  # Add get_energy_type method
        return self._energy_type

class Portfolio:
    def __init__(self, id, name):
        self._id = id  # Private attribute
        self._name = name  # Private attribute
        self._power_plants = []  # Private attribute
        self._total_capacity = 0  # Private attribute

    def add_power_plant(self, power_plant):
        self._power_plants.append(power_plant)

    def remove_power_plant(self, power_plant):
        self._power_plants.remove(power_plant)

    def calculate_total_capacity(self):
        self._total_capacity = sum(plant.get_capacity() for plant in self._power_plants)

    def get_name(self):
        return self._name

    def get_total_capacity(self):
        return self._total_capacity

    def calculate_resource_ratios(self):
        resource_ratios = {}
        for plant in self._power_plants:
            resource_name = plant.get_name()
            if resource_name not in resource_ratios:
                resource_ratios[resource_name] = 0
            resource_ratios[resource_name] += plant.get_capacity() / self._total_capacity
        return resource_ratios

    def calculate_energy_type_ratios(self):
        energy_type_ratios = {"renewable": 0, "fossil": 0}
        for plant in self._power_plants:
            if plant.get_energy_type() == "renewable":
                energy_type_ratios["renewable"] += plant.get_capacity() / self._total_capacity
            else:
                energy_type_ratios["fossil"] += plant.get_capacity() / self._total_capacity
        return energy_type_ratios

coal = EnergyResource("Coal", False, 5, 2)
solar = EnergyResource("Solar", True, 0, 1)

plant1 = PowerPlant("Plant 1", 1000000, 50000, 20000, 20, "fossil", 500)
plant1.resource = coal

plant2 = PowerPlant("Plant 2", 800000, 60000, 18000, 25, "renewable", 300)
plant2.resource = solar

portfolio = Portfolio(1, "My Portfolio")
portfolio.add_power_plant(plant1)
portfolio.add_power_plant(plant2)

portfolio.calculate_total_capacity()
resource_ratios = portfolio.calculate_resource_ratios()
energy_type_ratios = portfolio.calculate_energy_type_ratios()

# Print information about individual power plants and their associated energy resources
print("---------------------------------------Power Plants-------------------------------------")
for plant in portfolio._power_plants:
    print(f"Power Plant Name: {plant.get_name()}")
    print(f"Capacity: {plant.get_capacity()}")
    print(f"Energy Type: {plant.get_energy_type()}")
    print(f"Total Cost: {plant.calculate_total_cost()}")
    print(f"Annual Cost: {plant.calculate_annual_cost()}")
    print(f"Total Emissions: {plant.calculate_emissions()}")
    # Print information about the associated energy resource
    resource = plant.resource
    print(f"Resource Name: {resource.get_name()}")
    print(f"Tax Exempt: {resource._tax_exempt}")
    print(f"Carbon Emission: {resource._carbon_emission}")
    print(f"Fuel Cost per Unit: {resource._fuel_cost_per_unit}")
    print()

print("---------------------------------------Portfolios-------------------------------------")
# Print portfolio-level information
print(f"Total Portfolio Capacity: {portfolio.get_total_capacity()}")
print(f"Energy Resource Ratios: {resource_ratios}")
print(f"Energy Type Ratios: {energy_type_ratios}")
