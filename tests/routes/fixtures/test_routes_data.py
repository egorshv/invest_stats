import pytest
from fastapi.testclient import TestClient

from app import app
from schemas.portfolio import PortfolioSchema


@pytest.fixture
def test_client():
    return TestClient(app)


@pytest.fixture
def test_portfolio_data():
    return 4, 'portfolio 1'


@pytest.fixture
def test_posting_portfolio():
    return PortfolioSchema(
        name='posting portfolio',
        user_id=254
    )


@pytest.fixture
def test_updating_portfolio_data():
    return PortfolioSchema(
        name='updating portfolio',
        user_id=932
    ), 'updated portfolio name'


@pytest.fixture
def test_deleting_portfolio():
    return PortfolioSchema(
        name='deleting portfolio',
        user_id=1024
    )
