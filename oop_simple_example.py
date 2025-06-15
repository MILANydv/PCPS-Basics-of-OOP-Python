# oop_simple_example.py
"""
A very simple and beginner-friendly example of Object-Oriented Programming (OOP) in Python.
This example models a basic Car class and demonstrates object creation, attributes, and methods.
"""

# Define a simple Car class
class Car:
    def __init__(self, brand, model, year):
        # Instance attributes
        self.brand = brand  # Brand of the car (e.g., 'Toyota')
        self.model = model  # Model of the car (e.g., 'Corolla')
        self.year = year    # Year of manufacture (e.g., 2020)
        self.is_running = False  # State: is the car running?

    def start(self):
        """Start the car."""
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        """Stop the car."""
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} stopped.")
        else:
            print(f"{self.brand} {self.model} is already stopped.")

    def display_info(self):
        """Display information about the car."""
        print(f"Car: {self.brand} {self.model} ({self.year})")
        print(f"Running: {'Yes' if self.is_running else 'No'}\n")

# Example usage
if __name__ == "__main__":
    # Create two car objects
    car1 = Car("Toyota", "Corolla", 2020)
    car2 = Car("Honda", "Civic", 2018)

    # Display their info
    car1.display_info()
    car2.display_info()

    # Start and stop the cars
    car1.start()      # Start car1
    car1.start()      # Try to start again (shows already running)
    car1.display_info()

    car2.start()      # Start car2
    car2.stop()       # Stop car2
    car2.stop()       # Try to stop again (shows already stopped)
    car2.display_info() 