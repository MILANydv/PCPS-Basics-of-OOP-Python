# oop_example.py
"""
A clean, robust, and DRY example of Object-Oriented Programming (OOP) in Python.
This example models a simple system for managing properties (like Airbnb),
with a focus on professional design, maintainability, and extensibility.
"""

from abc import ABC, abstractmethod
from typing import List


class Theme:
    """A simple theme class to demonstrate theme compatibility."""
    def __init__(self, name: str, primary_color: str, accent_color: str):
        self.name = name
        self.primary_color = primary_color
        self.accent_color = accent_color

    def __str__(self):
        return f"Theme({self.name}, Primary: {self.primary_color}, Accent: {self.accent_color})"

class Property(ABC):
    """Abstract base class for all properties."""
    def __init__(self, name: str, location: str, price_per_night: float, theme: Theme):
        self.name = name
        self.location = location
        self.price_per_night = price_per_night
        self.theme = theme

    @abstractmethod
    def property_type(self) -> str:
        pass

    def display_info(self):
        print(f"{self.property_type()} - {self.name}")
        print(f"Location: {self.location}")
        print(f"Price per night: ${self.price_per_night}")
        print(f"Theme: {self.theme}\n")

class Apartment(Property):
    def __init__(self, name: str, location: str, price_per_night: float, theme: Theme, floor: int):
        super().__init__(name, location, price_per_night, theme)
        self.floor = floor

    def property_type(self) -> str:
        return "Apartment"

    def display_info(self):
        super().display_info()
        print(f"Floor: {self.floor}\n")

class House(Property):
    def __init__(self, name: str, location: str, price_per_night: float, theme: Theme, garden: bool):
        super().__init__(name, location, price_per_night, theme)
        self.garden = garden

    def property_type(self) -> str:
        return "House"

    def display_info(self):
        super().display_info()
        print(f"Garden: {'Yes' if self.garden else 'No'}\n")

class PropertyManager:
    """Manages a collection of properties."""
    def __init__(self):
        self.properties: List[Property] = []

    def add_property(self, property: Property):
        self.properties.append(property)
        print(f"Added {property.property_type()}: {property.name}")

    def show_all_properties(self):
        print("\nAll Properties:")
        for prop in self.properties:
            prop.display_info()

# Example usage
def main():
    modern_theme = Theme("Modern", "#222831", "#FFD369")
    classic_theme = Theme("Classic", "#F5F5DC", "#8B4513")

    apt1 = Apartment("City View Loft", "New York", 150.0, modern_theme, floor=12)
    house1 = House("Sunny Villa", "California", 300.0, classic_theme, garden=True)

    manager = PropertyManager()
    manager.add_property(apt1)
    manager.add_property(house1)
    manager.show_all_properties()

if __name__ == "__main__":
    main() 