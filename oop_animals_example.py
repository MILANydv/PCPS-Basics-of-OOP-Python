# oop_animals_example.py
"""
A clean, robust, and DRY example of Object-Oriented Programming (OOP) in Python.
This example models an animal hierarchy, demonstrating inheritance, abstraction, and polymorphism.
"""

from abc import ABC, abstractmethod
from typing import List


class Theme:
    """A simple theme class to demonstrate theme compatibility for animals."""
    def __init__(self, name: str, primary_color: str, accent_color: str):
        self.name = name
        self.primary_color = primary_color
        self.accent_color = accent_color

    def __str__(self):
        return f"Theme({self.name}, Primary: {self.primary_color}, Accent: {self.accent_color})"

class Animal(ABC):
    """Abstract base class for all animals."""
    def __init__(self, name: str, age: int, theme: Theme):
        self.name = name
        self.age = age
        self.theme = theme

    @abstractmethod
    def speak(self) -> str:
        pass

    @abstractmethod
    def species(self) -> str:
        pass

    def display_info(self):
        print(f"{self.species()} - {self.name}")
        print(f"Age: {self.age}")
        print(f"Theme: {self.theme}")
        print(f"Says: {self.speak()}\n")

class Dog(Animal):
    def __init__(self, name: str, age: int, theme: Theme, breed: str):
        super().__init__(name, age, theme)
        self.breed = breed

    def speak(self) -> str:
        return "Woof!"

    def species(self) -> str:
        return f"Dog ({self.breed})"

class Cat(Animal):
    def __init__(self, name: str, age: int, theme: Theme, color: str):
        super().__init__(name, age, theme)
        self.color = color

    def speak(self) -> str:
        return "Meow!"

    def species(self) -> str:
        return f"Cat ({self.color})"

class AnimalShelter:
    """Manages a collection of animals."""
    def __init__(self):
        self.animals: List[Animal] = []

    def add_animal(self, animal: Animal):
        self.animals.append(animal)
        print(f"Added {animal.species()}: {animal.name}")

    def show_all_animals(self):
        print("\nAll Animals:")
        for animal in self.animals:
            animal.display_info()

# Example usage
def main():
    playful_theme = Theme("Playful", "#FFB347", "#FFD700")
    calm_theme = Theme("Calm", "#B0E0E6", "#4682B4")

    dog1 = Dog("Buddy", 3, playful_theme, breed="Golden Retriever")
    cat1 = Cat("Whiskers", 2, calm_theme, color="Gray")

    shelter = AnimalShelter()
    shelter.add_animal(dog1)
    shelter.add_animal(cat1)
    shelter.show_all_animals()

if __name__ == "__main__":
    main() 