import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module
from src.app import app

BASELINE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    app_module.activities = copy.deepcopy(BASELINE_ACTIVITIES)
    yield


@pytest.fixture
def client():
    with TestClient(app) as test_client:
        yield test_client
