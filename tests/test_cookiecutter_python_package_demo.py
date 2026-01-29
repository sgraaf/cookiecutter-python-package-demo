from cookiecutter_python_package_demo import add_one


def test_add_one() -> None:
    assert add_one(1) == 2
