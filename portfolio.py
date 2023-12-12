from power_plants import PowerPlant
from enums import EnergyType
from typing import List, Dict, Optional

class Portfolio:
    def __init__(self, id: int, name: str, power_plants: Optional[List[PowerPlant]] = None):
        """
        Initialize a Portfolio object.

        Parameters:
        - id: Identifier for the portfolio.
        - name: Name of the portfolio.
        - power_plants: List of power plants in the portfolio (optional).
        """
        self.__id = id
        self.__name = name
        self.__power_plants = power_plants or []

    def get_id(self)-> float:
        """Get the id of the portfolio."""
        return self.__id

    def get_name(self)-> str:
        """Get the name of the portfolio."""
        return self.__name

    def get_power_plants(self) -> List[PowerPlant]:
        """Get the list of power plants in the portfolio."""
        return self.__power_plants

    def add_power_plant(self, power_plant: PowerPlant) -> None:
        """Add a power plant to the portfolio."""
        self.__power_plants.append(power_plant)

    def remove_power_plant(self, power_plant: PowerPlant) -> None:
        """Remove a power plant from the portfolio."""
        self.__power_plants.remove(power_plant)

    def calculate_total_capacity(self) -> float:
        """Calculate the total capacity of all power plants in the portfolio."""
        total_capacity = sum(plant.get_capacity() for plant in self.__power_plants)
        return total_capacity if total_capacity != 0 else 0

    def calculate_resource_ratios(self) -> Dict[str, float]:
        """Calculate the ratios of different resources in the portfolio."""
        total_capacity = self.calculate_total_capacity()
        resource_ratios: Dict[str, float] = {}
        for plant in self.__power_plants:
            resource_name = plant.get_resource().get_name()
            if resource_name not in resource_ratios:
                resource_ratios[resource_name] = 0
            resource_ratios[resource_name] += plant.get_capacity() / total_capacity if total_capacity != 0 else 0
        return resource_ratios

    def calculate_energy_type_ratios(self) -> Dict[EnergyType, float]:
        """Calculate the ratios of renewable and fossil energy types in the portfolio."""
        total_capacity = self.calculate_total_capacity()
        energy_type_ratios: Dict[EnergyType, float] = {EnergyType.RENEWABLE: 0, EnergyType.FOSSIL: 0}
        for plant in self.__power_plants:
            if plant.get_resource().get_energy_type() == EnergyType.RENEWABLE:
                energy_type_ratios[EnergyType.RENEWABLE] += plant.get_capacity() / total_capacity if total_capacity != 0 else 0
            else:
                energy_type_ratios[EnergyType.FOSSIL] += plant.get_capacity() / total_capacity if total_capacity != 0 else 0
        return energy_type_ratios
