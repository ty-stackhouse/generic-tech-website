import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture(scope="function")
def client():
    with TestClient(app) as c:
        yield c

import pytest


def test_homepage(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'TechConsult Group' in response.data
    assert b'Enterprise Solutions for Modern Challenges' in response.data


def test_services_page(client):
    response = client.get('/services')
    assert response.status_code == 200
    assert b'Cloud Migration' in response.data
    assert b'Security Audit' in response.data
    assert b'DevOps Optimization' in response.data


def test_service_detail_page(client):
    response = client.get('/services/cloud-migration')
    assert response.status_code == 200
    assert b'Cloud Migration' in response.data

    response = client.get('/services/security-audit')
    assert response.status_code == 200
    assert b'Security Audit' in response.data

    response = client.get('/services/devops-optimization')
    assert response.status_code == 200
    assert b'DevOps Optimization' in response.data
