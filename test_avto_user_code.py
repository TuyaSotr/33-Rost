import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages33.auth_key import AuthKey
import time


@pytest.fixture(autouse=True)
def code():
    code = webdriver.Chrome()
    code.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=lk_b2c&redirect_uri=https%3A%2F%2Flk-api.rt.ru%2Fsso-auth%2F%3Fredirect%3Dhttps%253A%252F%252Fstart.rt.ru%252F&response_type=code&scope=openid')
    time.sleep(5)

    yield code
    code.quit()


'''Авторизация по временному коду'''


# Авторизация по номеру
def test_auth_code_number(code):
    assert code.find_element(By.ID, "card-title").text == "Авторизация по коду"
    code.find_element(By.ID, "address").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(20)
    code.find_element(By.ID, "otp_get_code").click()
    time.sleep(7)
    assert code.find_element(By.ID, "card-title").text == 'Код подтверждения отправлен'
    # Для ввода кода подтверждения из сообщения
    time.sleep(20)

# Авторизация по почте
def test_auth_code_mail(code):
    assert code.find_element(By.ID, "card-title").text == "Авторизация по коду"
    code.find_element(By.ID, "address").send_keys(f'{AuthKey.mail_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(20)
    code.find_element(By.ID, "otp_get_code").click()
    time.sleep(7)
    assert code.find_element(By.ID, "card-title").text == 'Код подтверждения отправлен'
    # Для ввода кода подтверждения из сообщения
    time.sleep(20)

# Ограничение на ввод 12 цифр и подсказка под полем ввода примерный вид номера телефона и почты
def test_requirement_auth_code(code):
    assert code.find_element(By.ID, "card-title").text == "Авторизация по коду"
    code.find_element(By.ID, "address").send_keys('891400000123')
    code.find_element(By.ID, "card-title").click()
    assert code.find_element(By.ID, 'address-meta').text == "Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru"
    time.sleep(3)

