import pytest
from playwright.sync_api import Page, expect

@pytest.fixture(scope="function")
def page_fixture(page: Page):
    yield page


import pytest
from playwright.sync_api import Page


def test_homepage(page: Page):
    page.goto('/')
    assert page.title() == 'TechConsult Group'
    assert page.locator('text=Enterprise Solutions for Modern Challenges').count() > 0


def test_services_page(page: Page):
    page.goto('/services')
    assert page.title() == 'Services'
    assert page.locator('text=Cloud Migration').count() > 0
    assert page.locator('text=Security Audit').count() > 0
    assert page.locator('text=DevOps Optimization').count() > 0


def test_service_detail_page(page: Page):
    page.goto('/services/cloud-migration')
    assert page.title() == 'Cloud Migration'
    assert page.locator('text=Cloud Migration').count() > 0

    page.goto('/services/security-audit')
    assert page.title() == 'Security Audit'
    assert page.locator('text=Security Audit').count() > 0

    page.goto('/services/devops-optimization')
    assert page.title() == 'DevOps Optimization'
    assert page.locator('text=DevOps Optimization').count() > 0
