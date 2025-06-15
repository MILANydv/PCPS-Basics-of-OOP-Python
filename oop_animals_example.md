# OOP Animal Hierarchy Example in Python

This repository contains a clean, robust, and DRY example of Object-Oriented Programming (OOP) in Python. The example models an animal hierarchy, demonstrating inheritance, abstraction, and polymorphism with a focus on professional design and maintainability.

## Features

- **Abstract Base Classes**: Uses Python's `abc` module for abstraction.
- **Inheritance & Polymorphism**: Demonstrates extending base classes and overriding methods.
- **Encapsulation**: Encapsulates animal data and behavior in classes.
- **Theme Compatibility**: Includes a `Theme` class to show how objects can be themed.
- **DRY Principle**: Code is organized to avoid repetition and maximize reusability.
- **Professional Design**: Follows clean code and design principles for readability and maintainability.

## File Structure

- `oop_animals_example.py` — Main Python file containing all classes and example usage.
- `oop_animals_example.md` — This file.

## Classes Overview

- **Theme**: Represents a theme for animals (e.g., playful, calm).
- **Animal (Abstract Base Class)**: Base class for all animal types.
- **Dog**: Inherits from `Animal`, adds a `breed` attribute.
- **Cat**: Inherits from `Animal`, adds a `color` attribute.
- **AnimalShelter**: Manages a collection of animals.

## Example Usage

The `main()` function in `oop_animals_example.py` demonstrates how to:

- Create themes
- Instantiate different animal types
- Add animals to a shelter
- Display all animal information

### Run the Example

Make sure you have Python 3.7 or higher installed.

```bash
python oop_animals_example.py
```

You should see output similar to:

```
Added Dog (Golden Retriever): Buddy
Added Cat (Gray): Whiskers

All Animals:
Dog (Golden Retriever) - Buddy
Age: 3
Theme: Theme(Playful, Primary: #FFB347, Accent: #FFD700)
Says: Woof!

Cat (Gray) - Whiskers
Age: 2
Theme: Theme(Calm, Primary: #B0E0E6, Accent: #4682B4)
Says: Meow!
```

## Customization

- You can add more animal types by extending the `Animal` class.
- Themes can be expanded for more complex styling needs.
- The system is designed to be easily extensible and maintainable.

## License

This project is open source and available under the [MIT License](LICENSE).
