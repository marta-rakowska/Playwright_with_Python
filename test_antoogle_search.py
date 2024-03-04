from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://antoogle.testoneo.com/")
    page.get_by_placeholder("Search phrase").click()
    page.get_by_placeholder("Search phrase").fill("test")
    page.get_by_role("button", name="Search!").click()
    page.get_by_role("cell", name="test").click()

    assert page.inner_text('#item0') == 'test', f"Actual value: {page.inner_text('#item0')}"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
