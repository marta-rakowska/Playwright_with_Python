from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://playwright.dev/python/docs/codegen-intro")
    page.get_by_role("heading", name="IntroductionDirect link to").click()
    page.get_by_role("heading", name="Running CodegenDirect link to").click()
    page.get_by_label("Search").click()
    page.get_by_placeholder("Search docs").fill("docker")
    page.get_by_placeholder("Search docs").press("Enter")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)