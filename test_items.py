import time

from selenium.webdriver.common.by import By

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


class TestProductPage:

    def test_button_add_to_basket_is_visible(self, browser):
        browser.get(link)

        # Задержка времени для проверки pytest --language=fr test_items.py - нужно лишь раскомментировать
        time.sleep(30)

        # Проверка наличия на странице товара кнопки добавления в корзину
        assert len(browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")) > 0, 'The button was not found'
