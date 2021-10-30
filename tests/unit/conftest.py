import pytest

from brickabode_ci.app import create_app

@pytest.fixture(scope="function")
def app ():
    """Instance of Main flask app"""
    return create_app()
