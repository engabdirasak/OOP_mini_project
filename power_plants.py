from energy_resources import EnergyResource
from typing import Optional
from enums import  EnergyType

class PowerPlant:
    def __init__(self, name: str, resource: EnergyResource, construction_cost: float,
                 maintenance_cost: float, lifetime: int, capacity: float):
        """
        Initialize a PowerPlant object.

        Parameters:
        - name: Name of the power plant.
        - resource: Associated energy resource (instance of EnergyResource).
        - construction_cost: Cost of constructing the power plant.
        - maintenance_cost: Annual maintenance cost of the power plant.
        - lifetime: Expected lifetime of the power plant.
        - capacity: Capacity of the power plant.
        """
        self.__name = name
        self.__resource = resource
        self.__construction_cost = construction_cost
        self.__maintenance_cost = maintenance_cost
        self.__lifetime = lifetime
        self.__capacity = capacity

    def get_name(self) -> str:
        """Get the name of the power plant."""
        return self.__name

    def get_resource(self) -> EnergyResource:
        """Get the associated energy resource."""
        return self.__resource

    def get_capacity(self) -> float:
        """Get the capacity of the power plant."""
        return self.__capacity

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of the power plant over its lifetime."""
        return self.__construction_cost + (self.__lifetime * self.__maintenance_cost)

    def calculate_annual_cost(self) -> float:
        """Calculate the annual cost of the power plant."""
        return self.calculate_total_cost() / self.__lifetime

    def calculate_emissions(self) -> float:
        """Calculate the emissions produced by the power plant."""
        if self.__resource.get_energy_type() == EnergyType.FOSSIL:
            emissions_per_unit = self.__resource.get_carbon_emission()
            energy_produced = self.__lifetime * self.__capacity
            return emissions_per_unit * energy_produced
        else:
            return 0
