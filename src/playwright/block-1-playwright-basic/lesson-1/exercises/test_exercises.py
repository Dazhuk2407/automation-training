# Exercises for Playwright Basics

import pytest
from playwright.sync_api import sync_playwright


class TestPlaywrightBasics:
    """Basic Playwright exercises"""

    @pytest.fixture
    def browser_context(self):
        """Fixture to create browser and page"""
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            yield page
            browser.close()

    def test_navigate_to_example_com(self, browser_context):
        """TODO: Navigate to https://example.com and verify page title"""
        page = browser_context
        # TODO: Navigate to https://example.com
        # TODO: Assert that page title contains "Example"
        pass

    def test_find_heading(self, browser_context):
        """TODO: Find h1 element on example.com"""
        page = browser_context
        # TODO: Navigate to https://example.com
        # TODO: Find h1 element
        # TODO: Assert that h1 exists
        pass

    def test_get_page_url(self, browser_context):
        """TODO: Get current page URL"""
        page = browser_context
        # TODO: Navigate to https://example.com
        # TODO: Get page URL
        # TODO: Assert URL is correct
        pass

