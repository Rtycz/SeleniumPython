import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="function")
def browser():
    options = Options()
    # options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    options.add_experimental_option('prefs', {'intl.accept_languages': 'en-US'})
    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()