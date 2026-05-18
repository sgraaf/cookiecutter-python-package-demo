"""Smoke tests for the cookiecutter-python-package-demo package.

These tests verify that the most critical functionality of the package works.
They are designed to catch major breakage and ensure basic operations succeed.
"""


def test_import() -> None:
    """Test importing the package."""
    import cookiecutter_python_package_demo  # noqa: F401, PLC0415
