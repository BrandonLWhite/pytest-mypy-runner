# pytest-mypy-runner
Run the [mypy](https://github.com/python/mypy) static type checker as a [pytest](https://github.com/pytest-dev/pytest) test case

## Usage
After adding this library to your dev/test dependencies and installing, add the following file to your test folder:

`test_mypy.py`
```test_mypy.py
from pytest_mypy_runner import test_mypy  # noqa
```

Pytest should then pick up the `test_mypy` test.

Note:  The `# noqa` is there to prevent formatters/linters like autoflake from removing what otherwise appears to be an
unused import.

## Configuration
The nearest `pyproject.toml` file will be used to configured mypy, traversing upward from the folder where test_mypy.py
resides.  Add any custom configuration to the `[tool.mypy]` section.