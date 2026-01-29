"""Demo of https://github.com/sgraaf/cookiecutter-python-package."""


def add_one(x: int) -> int:
    """Add one to the input.

    Args:
        x: The input.

    Returns:
        The input plus one.

    Example:
        >>> from cookiecutter_python_package_demo import add_one
        >>> add_one(1)
        2
    """
    return x + 1
