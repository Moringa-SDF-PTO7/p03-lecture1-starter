# Python Fundamentals Starter Project

This repository contains starter Python code for explaining essential programming concepts. The code is organized into three files, each focusing on different areas of Python fundamentals. This project is designed to help beginners understand key concepts, experiment with the code, and complete the included "TODO" tasks as practice exercises.

## Table of Contents

- [Project Structure](#project-structure)
- [Concepts Covered](#concepts-covered)
- [Getting Started](#getting-started)
- [How to Use](#how-to-use)
- [TODO Items](#todo-items)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
project/
│
├── fundamentals.py   # Data types, Error handling
├── basics.py         # Debugging, Testing, Indentation, Variable scope
└── control.py        # Conditional statements, Loops, Decorators
```

Each file is self-contained and includes Python code for explaining the concepts mentioned in the file names. The comments and "TODO" items provide additional context and learning opportunities.

## Concepts Covered

1. **`fundamentals.py`:**  
   - Basic data types: integers, floats, strings, booleans, lists, tuples, dictionaries.
   - Error handling: try-except blocks, ZeroDivisionError, IndexError.

2. **`basics.py`:**  
   - Debugging: How to use `ipdb` to set breakpoints and inspect variables.
   - Testing: Introduction to `pytest` for writing unit tests.
   - Indentation: Importance of indentation in Python.
   - Variable scope: Local, global, and nonlocal variables.

3. **`control.py`:**  
   - Conditional statements: `if`, `elif`, `else`.
   - Loops: `for` loops, `while` loops.
   - Decorators: How to create and use simple decorators in Python.

## Getting Started

To get started with this project:

1. Clone the repository:

   ```bash
   git clone git@github.com:Moringa-SDF-PTO7/p03-lecture1-starter.git
   cd p03-lecture1-starter
   ```

2. Install the necessary dependencies. (For debugging and testing):

   ```bash
   pip install ipdb pytest
   ```

3. Explore the code inside each file to understand the concepts and try out the examples.

## How to Use

### Running the Code

Each Python file can be run independently. To run a file, use:

```bash
python fundamentals.py
python basics.py
python control.py
```

### Testing

If you wish to test the functions in `basics.py`, run `pytest`:

```bash
pytest basics.py
```

### Debugging

To try out the debugger `ipdb`, uncomment the lines in `buggy_function` inside `basics.py`, then run:

```bash
python basics.py
```

This will allow you to step through the code interactively and inspect variables.

## TODO Items

Each file contains "TODO" comments to encourage further learning. These are tasks designed for you to complete on your own. Examples include:

- Expanding the code with additional data types in `fundamentals.py`.
- Writing new test cases using `pytest` in `basics.py`.
- Implementing more complex loops and decorators in `control.py`.

Feel free to experiment and enhance the code as you learn these concepts!

## Contributing

Contributions to this project are welcome! If you find any issues or want to improve the examples, feel free to create a pull request.

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
