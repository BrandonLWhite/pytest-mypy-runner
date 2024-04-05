from pathlib import Path
import mypy.api
from pytest import FixtureRequest


def test_mypy(request: FixtureRequest) -> None:
    """
    Execute mypy using the pyproject.toml file as the reference point and config.  This avoids problems pertaining
    to the current working directory, which can affect some IDEs
    """
    def find_pyproject() -> Path:
        for folder in Path(request.path).parents:
            pyproject_path = folder / "pyproject.toml"
            if pyproject_path.exists():
                return pyproject_path
        raise Exception('Could not find pyproject.toml in any parent directories')

    pyproject_path = find_pyproject()
    stdout, stderr, exitcode = mypy.api.run([
        str(pyproject_path.parent),
        "--config-file", str(pyproject_path)
    ])
    print(stdout)
    assert exitcode == 0
