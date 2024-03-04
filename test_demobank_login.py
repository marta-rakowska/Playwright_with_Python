def test_demobank_valid_login(page):
    # Go to https://demobank.jaktestowac.pl/logowanie_etap_1.html
    page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "12345678")
    # Press Enter
    # with page.expect_navigation(url="https://demobank.jaktestowac.pl/logowanie_etap_2.html?login=12345678"):
    with page.expect_navigation():
        page.press("input[type=\"text\"]", "Enter")
    # Click input[name="haslo"]
    page.click("input[name=\"haslo\"]")
    # Fill input[name="haslo"]
    page.fill("input[name=\"haslo\"]", "12345678")
    # Press Enter
    # with page.expect_navigation(url="https://demobank.jaktestowac.pl/pulpit.html"):
    with page.expect_navigation():
        page.press("input[name=\"haslo\"]", "Enter")
    # assert text=Jan Demobankowy
    assert page.inner_text('#user_name') == r'Jan Demobankowy'

def test_demobank_login_id_too_short(page):
    # Go to https://demobank.jaktestowac.pl/logowanie_etap_1.html
    page.goto("https://demobank.jaktestowac.pl/logowanie_etap_1.html")
    # Fill input[type="text"]
    page.fill("input[type=\"text\"]", "123")
    # Press Enter
    page.press("input[type=\"text\"]", "Enter")
    # assert error
    assert page.inner_text('#error_login_id') == r'identyfikator ma min. 8 znaków'
