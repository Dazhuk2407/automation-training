# Example: Basic Playwright usage

from playwright.sync_api import sync_playwright


def example_launch_browser():
    """Example: Launch a browser and navigate to a website"""
    with sync_playwright() as p:
        # Launch browser
        browser = p.chromium.launch(headless=True)

        # Create a new page
        page = browser.new_page()

        # Navigate to website
        page.goto("https://example.com")

        # Get page title
        title = page.title()
        print(f"Page title: {title}")

        # Get page URL
        url = page.url
        print(f"Current URL: {url}")

        # Close browser
        browser.close()


def example_find_elements():
    """Example: Find and interact with elements"""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("https://example.com")

        # Find element by CSS selector
        heading = page.query_selector("h1")
        if heading:
            text = heading.text_content()
            print(f"Heading text: {text}")

        # Find multiple elements
        paragraphs = page.query_selector_all("p")
        print(f"Found {len(paragraphs)} paragraphs")

        # Using Locator API (newer approach)
        link = page.locator("a")
        if link.count() > 0:
            print(f"Found {link.count()} links")

        browser.close()


if __name__ == "__main__":
    print("=== Launch Browser ===")
    example_launch_browser()

    print("\n=== Find Elements ===")
    example_find_elements()

