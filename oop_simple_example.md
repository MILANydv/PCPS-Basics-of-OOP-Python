# Simple OOP Car Example in Python

This example provides a very simple and beginner-friendly introduction to Object-Oriented Programming (OOP) in Python. It models a basic `Car` class and demonstrates how to create objects, use attributes, and call methods.

## Features

- **Class Definition**: Shows how to define a class in Python.
- **Instance Attributes**: Demonstrates storing data in objects.
- **Methods**: Shows how to define and use methods (functions inside classes).
- **Object Creation**: Demonstrates how to create and use objects.
- **Clear Comments**: Every part of the code is commented for easy understanding.

## File Structure

- `oop_simple_example.py` — Main Python file containing the simple Car class and example usage.
- `oop_simple_example.md` — This file.

## How It Works

- The `Car` class has attributes for brand, model, year, and running state.
- Methods allow you to start, stop, and display information about the car.
- The example creates two car objects and demonstrates their behavior.

## Example Usage

The following code is in `oop_simple_example.py`:

```python
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2018)

car1.display_info()
car2.display_info()

car1.start()      # Start car1
car1.start()      # Try to start again (shows already running)
car1.display_info()

car2.start()      # Start car2
car2.stop()       # Stop car2
car2.stop()       # Try to stop again (shows already stopped)
car2.display_info()
```

### Run the Example

Make sure you have Python 3.x installed.

```bash
python oop_simple_example.py
```

You should see output similar to:

```
Car: Toyota Corolla (2020)
Running: No

Car: Honda Civic (2018)
Running: No

Toyota Corolla started.
Toyota Corolla is already running.
Car: Toyota Corolla (2020)
Running: Yes

Honda Civic started.
Honda Civic stopped.
Honda Civic is already stopped.
Car: Honda Civic (2018)
Running: No
```

## Customization

- Try creating more car objects with different brands, models, and years.
- Add new methods (like `honk`) to the `Car` class for more practice.

## License

This project is open source and available under the [MIT License](LICENSE).
