from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
    page.locator("#login_id").fill("1234")
    page.locator("#login_id").press("Enter")

    assert page.inner_text('#error_login_id') == "identyfikator ma min. 8 znaków", f"Actual value: {page.inner_text('#error_login_id')}"

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
