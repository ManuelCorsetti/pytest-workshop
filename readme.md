# Pytest Workshop

## Table of Contents

1. [Why Unit Testing?](#why-unit-testing)
2. [Introduction to PyTest](#introduction-to-pytest)
3. [Structure Your Projects for PyTest](#structure-your-projects-for-pytest)
4. [Fixtures and conftest.py](#fixtures-and-conftestpy)
5. [Mocking Basics](#mocking-basics)
6. [Patching](#patching)

---

## Why Unit Testing?

### What is Unit Testing?

- **Unit testing** verifies the functionality of small, isolated pieces of code (e.g., functions or classes) to ensure they perform as expected.

### Benefits of Unit Testing

- **Early Bug Detection**: Catch bugs early in development.
- **Facilitates Refactoring**: Ensure your code remains stable after changes.
- **Supports Continuous Integration (CI)**: Integrates well with CI pipelines to ensure stable builds.
- **Improved Code Quality**: Writing tests forces better code structure and design.
- **Documentation**: Unit tests serve as a reference for how your code is intended to work.
- **Reduced Debugging Time**: Quickly pinpoint where issues arise.
- **Confidence in Code Changes**: Tests serve as a safety net when modifying the codebase.

---

## Introduction to PyTest

### Key Features

- **Simple and Intuitive Syntax**: No boilerplate code or special method names required.
- **Automatic Test Discovery**: PyTest discovers tests by looking for files starting with `test_` or ending in `_test.py`.
- **Powerful Fixtures**: Reusable setup logic that can be shared across tests.
- **Rich Plugin Architecture**: Extensible via plugins (e.g., `pytest-cov` for coverage, `pytest-mock` for mocking).
- **Detailed Reporting**: Provides detailed test failure output for debugging.

### Installing PyTest

```bash
pip install pytest
```

To verify the installation:

```bash
pytest --version
```

### Running Your First Test

Create a file `test_example.py`:

```python
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
```

Run the test:

```bash
pytest
```

---

## Structure Your Projects for PyTest

### Basic Project Layout

```plaintext
my_project/
├── src/
│   └── my_project/
│       ├── __init__.py
│       ├── module1.py
│       └── module2.py
├── tests/
│   ├── __init__.py
│   ├── test_module1.py
│   ├── test_module2.py
│   └── conftest.py
└── main.py
```

- **src/**: Contains source code.
- **tests/**: Contains test files, mirroring the structure of the `src` directory.

### Benefits of Using `src/` Folder

- Prevents accidental imports from the wrong directory.
- Organizes source code and tests for scalability and maintainability.

### Conventions for Python test discovery

- Tests are searched **recursively** starting from the current active folder in your command line
  - Test discovery is manually set up on VS Code - this is my preferred way of working
- In the active directory, search for `test_*.py` (our chosen approach) or `*_test.py` files

From those test files found, collect test items:

- `test` prefixed test functions or methods outside of class
- `test` prefixed test functions or methods inside `Test` prefixed test classes (without an `__init__` method)

#### In Summary

- Test files and functions should start with `test_` for automatic discovery by PyTest.
- It is not required for test discovery for the tests to exist within the `tests` folder, but it is best practice and will help you manage your project

---

## Fixtures and `conftest.py`

### What are Fixtures?

- **Fixtures** are reusable setup/teardown functions executed before/after test functions. They help avoid redundant setup code.

### Fixture Scope

- **Function**: (default) Fixture is executed for each test function.
- **Class**: Fixture is shared across all methods in a test class.
- **Module**: Fixture is shared across all tests in a module.
- **Session**: Fixture is shared across the entire test session.

### Example Fixture

```python
import pytest

@pytest.fixture
def sample_data():
    return {"name": "John", "age": 30}

def test_sample_data(sample_data):
    assert sample_data["name"] == "John"
```

### Sharing Fixtures Across Files

- Use `conftest.py` to share fixtures across multiple test files within the same directory.

---

## Mocking Basics

### What is Mocking?

- **Mocking** involves replacing parts of the system with mock objects to simulate dependencies such as databases or APIs, allowing isolated unit testing.

### Basic Mock Example

```python
from unittest.mock import Mock

mock_obj = Mock()
mock_obj.some_method.return_value = 42
assert mock_obj.some_method() == 42
```

## Patching

### What is Patching?

- **Patching** is temporarily replacing a real object (e.g., function, method, or class) with a mock for the duration of a test.

### Example Using `patch`

```python
from unittest.mock import patch

@patch('module.some_class')
def test_patch_example(mock_class):
    instance = mock_class.return_value
    instance.method.return_value = 'mocked!'
    assert instance.method() == 'mocked!'
```

### Using `patch` as a Context Manager

```python
with patch('module.some_class') as mock_class:
    instance = mock_class.return_value
    instance.method.return_value = 'mocked!'
    assert instance.method() == 'mocked!'
```

### Using patch with new_callable

When you use `new_callable`, you can define a custom class or factory to replace the original class. This is useful when you need to patch with a specific mock object or class rather than simply modifying return_value.

```python
from unittest.mock import patch, MagicMock

class CustomMock(MagicMock):
    def method(self):
        return 'mocked with new_callable!'

@patch('module.some_class', new_callable=CustomMock)
def test_patch_with_new_callable(mock_class):
    # Since new_callable is CustomMock, the method will return the value we defined
    assert mock_class.method() == 'mocked with new_callable!'
```

**Key Differences:**

- `return_value` is used to define the return of a method or object
- `new_callable` allows replacing the entire target with a custom class or callable, offering more control over the behavior of the patched object.

Both methods can be useful depending on the level of customization needed.

### Best Practices for Mocking and Patching

1. **Patch where it's used**: Always patch where the object is being looked up, not where it is defined.
2. **Keep mocks simple**: Focus on simulating specific behaviors and avoid unnecessary complexity.
3. **Verify mock usage**: Always assert that mocks were called as expected in tests.

---

## Conclusion

Mocking and patching are essential tools in unit testing. They allow you to isolate code, simulate dependencies, and write focused, maintainable, and reliable tests. Using `unittest.mock` and `pytest-mock`, you can effectively manage and control complex systems in your tests.
