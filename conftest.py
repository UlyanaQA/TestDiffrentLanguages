import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    """Добавление опции командной строки.
    В командную строку передается параметр '--language=es' / '--language=fr'
    По умолчанию английский язык интерфейса
    """
    parser.addoption('--language', action='store', default='en', help='Choose language')


@pytest.fixture(scope="function")
def browser(request):
    # Передача из командной строки параметра language в переменную browser_language
    browser_language = request.config.getoption('language')

    # Инициализация опции браузера
    options = Options()

    # Передача в опции webdriver параметра из командной строки
    options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    browser.quit()
