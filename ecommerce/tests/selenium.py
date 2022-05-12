import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_browser_instance(request):
    """
    Предоставляет селениуму экземпляр драйвера хрома
    """
    options = Options()
    options.headless = False  # убирает или оставляет визуальный запуск хрома
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()
