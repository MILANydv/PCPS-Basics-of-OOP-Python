# OOP Example in Python

This repository contains a clean, robust, and DRY example of Object-Oriented Programming (OOP) in Python. The example models a simple property management system inspired by platforms like Airbnb, with a focus on professional design, maintainability, and extensibility.

## Features

- **Abstract Base Classes**: Demonstrates the use of Python's `abc` module for abstraction.
- **Inheritance & Polymorphism**: Shows how to extend base classes and override methods.
- **Encapsulation**: Uses class attributes and methods to encapsulate data and behavior.
- **Theme Compatibility**: Includes a `Theme` class to demonstrate how objects can be styled or themed.
- **DRY Principle**: Code is organized to avoid repetition and maximize reusability.
- **Professional Design**: Follows clean code and design principles for readability and maintainability.

## File Structure

- `oop_example.py` — Main Python file containing all classes and example usage.
- `README.md` — This file.

## Classes Overview

- **Theme**: Represents a UI theme with primary and accent colors.
- **Property (Abstract Base Class)**: Base class for all property types.
- **Apartment**: Inherits from `Property`, adds a `floor` attribute.
- **House**: Inherits from `Property`, adds a `garden` attribute.
- **PropertyManager**: Manages a collection of properties.

## Example Usage

The `main()` function in `oop_example.py` demonstrates how to:

- Create themes
- Instantiate different property types
- Add properties to a manager
- Display all property information

### Run the Example

Make sure you have Python 3.7 or higher installed.

```bash
python oop_example.py
```

You should see output similar to:

```
Added Apartment: City View Loft
Added House: Sunny Villa

All Properties:
Apartment - City View Loft
Location: New York
Price per night: $150.0
Theme: Theme(Modern, Primary: #222831, Accent: #FFD369)

Floor: 12

House - Sunny Villa
Location: California
Price per night: $300.0
Theme: Theme(Classic, Primary: #F5F5DC, Accent: #8B4513)

Garden: Yes
```

## Customization

- You can add more property types by extending the `Property` class.
- Themes can be expanded for more complex UI or styling needs.
- The system is designed to be easily extensible and maintainable.

## License

This project is open source and available under the [MIT License](LICENSE).
