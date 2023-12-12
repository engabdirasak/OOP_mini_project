from enums import EnergyType

class EnergyResource:
    def __init__(self, name: str, tax_exempt: bool,  carbon_emission: float, fuel_cost_per_unit: float, energy_type: EnergyType):
        """
        Initialize an EnergyResource object.

        Parameters:
        - name: Name of the energy resource.
        - tax_exempt: A boolean indicating whether the resource is tax-exempt.
        - fuel_cost_per_unit: Fuel cost per unit of the resource (non-negative float).
        - energy_type: Enum representing the energy type (from enums.EnergyType).
        - carbon_emission: Carbon emission of the resource (default is 0 for renewable sources).
        """
        self.__name = name
        self.__tax_exempt = bool(tax_exempt)
        self.__fuel_cost_per_unit = max(0, float(fuel_cost_per_unit))
        self.__energy_type = energy_type
        self.__carbon_emission = carbon_emission if energy_type != EnergyType.RENEWABLE else 0

    # Getter methods for encapsulation

    def get_name(self) -> str:
        """Get the name of the energy resource."""
        return self.__name

    def is_tax_exempt(self) -> bool:
        """Check if the energy resource is tax-exempt."""
        return self.__tax_exempt

    def get_carbon_emission(self) -> float:
        """Get the carbon emission of the energy resource."""
        return self.__carbon_emission

    def get_fuel_cost_per_unit(self) -> float:
        """Get the fuel cost per unit of the energy resource."""
        return self.__fuel_cost_per_unit

    def get_energy_type(self) -> EnergyType:
        """Get the energy type of the resource (from enums.EnergyType)."""
        return self.__energy_type
