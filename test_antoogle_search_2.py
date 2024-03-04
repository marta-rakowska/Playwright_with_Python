def test_antoogle_search(page):
    test_phrase = 'test'
    # Go to https://antoogle.testoneo.com/
    page.goto("https://antoogle.testoneo.com/")
    # Click [placeholder="Search phrase"]
    page.click("[placeholder=\"Search phrase\"]")
    # Fill [placeholder="Search phrase"]
    page.fill("[placeholder=\"Search phrase\"]", test_phrase)
    # Click text=Search!
    page.click("text=Search!")
    assert page.inner_text('#item0') == test_phrase, f"Actual value: {page.inner_text('#item0')} differ from expected: {test_phrase}"