import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages33.auth_key import AuthKey
import time

@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome()
    # Переходим на страницу авторизации
    driver.get('https://b2c.passport.rt.ru/auth/realms/b2c/protocol/openid-connect/auth?client_id=account_b2c&redirect_uri=https://b2c.passport.rt.ru/account_b2c/login&response_type=code&scope=openid&state=7ec0a16e-43a6-40ef-acd1-fd4d4021f340')
    time.sleep(5)

    yield driver
    driver.quit()


''''Регистрация'''''

def test_registration_login_profile(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"
    # Ввод имени
    driver.find_element(By.NAME, "firstName").send_keys("Туяра")
    # Ввод фамилии
    driver.find_element(By.NAME, "lastName").send_keys("Сотрудникова")
    # Для выбора/написания в ручную регион
    time.sleep(10)
    driver.find_element(By.ID, "address").send_keys(f'{AuthKey.mail_regis}')
    driver.find_element(By.ID, "password").send_keys(f'{AuthKey.password_regis}')
    driver.find_element(By.ID, "password-confirm").send_keys(f'{AuthKey.confir_pass_reg}')
    time.sleep(5)
    driver.find_element(By.NAME, "register").click()

def test_requirement_no_correct_name(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    # Ввод имени меньше трех символов и латиницей
    driver.find_element(By.NAME, "firstName").send_keys("Tj")
    driver.find_element(By.ID, "card-title").click()
    requirement_name = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text
    assert requirement_name == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(2)

def test_requirement_no_correct_name_symbols(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    # Ввод имени больше граничного значения
    driver.find_element(By.NAME, "firstName").send_keys("ТатьянаЛеройнаСеверинаКириллинна")
    driver.find_element(By.ID, "card-title").click()
    requirement_name_symbols = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/span[1]').text
    assert requirement_name_symbols == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(2)

def test_requirement_no_correct_surname_latin(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    # Ввод фамилии на латинице
    driver.find_element(By.NAME, "lastName").send_keys("Sivsev")
    driver.find_element(By.ID, "card-title").click()
    requirement_username = driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]').text
    assert requirement_username == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(2)

def test_requirement_no_correct_surname_symbols(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    # Ввод фамилии на кириллице меньше минимальной границы
    driver.find_element(By.NAME, "lastName").send_keys("П")
    driver.find_element(By.ID, "card-title").click()
    requirement_username_symbols = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[1]/div[2]/span[1]').text
    assert requirement_username_symbols == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    time.sleep(2)

def test_requirement_no_correct_mail(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    # Ввод почты и номера
    driver.find_element(By.ID, "address").send_keys('qwdefr.com')
    driver.find_element(By.ID, "card-title").click()
    requirement_mail = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]').text
    assert requirement_mail == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    time.sleep(2)

def test_requirement_no_correct_number(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    driver.find_element(By.ID, "address").send_keys('898976687')
    driver.find_element(By.ID, "card-title").click()
    requirement_number = driver.find_element(By.XPATH,'//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]').text
    assert requirement_number == 'Введите телефон в формате +7ХХХХХХХХХХ или +375XXXXXXXXX, или email в формате example@email.ru'
    time.sleep(2)

def test_requirement_no_correct_password_symbol(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    driver.find_element(By.ID, "password").send_keys('Qwerty1')
    driver.find_element(By.ID, "card-title").click()
    requirement_password_symbol = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]').text
    assert requirement_password_symbol == "Длина пароля должна быть не менее 8 символов"
    time.sleep(2)

def test_requirement_no_correct_password_latin(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    driver.find_element(By.ID, "password").send_keys('Пароль111')
    driver.find_element(By.ID, "card-title").click()
    requirement_password_symbol = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]').text
    assert requirement_password_symbol == "Пароль должен содержать только латинские буквы"
    time.sleep(2)

def test_requirement_no_correct_password_capital_letter(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    driver.find_element(By.ID, "password").send_keys('qwerrre2332')
    driver.find_element(By.ID, "card-title").click()
    requirement_password_symbol = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[1]/span[1]').text
    assert requirement_password_symbol == "Пароль должен содержать хотя бы одну заглавную букву"
    time.sleep(2)

def test_requirement_password_confirmation_not_identical_password(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    driver.find_element(By.NAME, "firstName").send_keys("Таша")
    # Ввод фамилии
    driver.find_element(By.NAME, "lastName").send_keys("Титова")
    # Для выбора/написания в ручную регион
    time.sleep(10)
    driver.find_element(By.ID, "address").send_keys('qwerty12@mail.ru')
    driver.find_element(By.ID, "password").send_keys('Qwerrre2332')
    driver.find_element(By.ID, 'password-confirm').send_keys('Qwerre2332')
    driver.find_element(By.NAME, "register").click()
    no_identical = driver.find_element(By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/div[2]/span[1]').text
    assert no_identical == "Пароли не совпадают"
    time.sleep(2)

def test_registration_not_possible_without_filling_the_form(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Клик "Зарегистрироваться"
    driver.find_element(By.ID, 'kc-register').click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице с регистрацией
    assert driver.find_element(By.ID, "card-title").text == "Регистрация"

    driver.find_element(By.NAME, "register").click()
    driver.save_screenshot('empty_fields_reg.png')
    time.sleep(2)


'''Стандартная авторизация по логину и паролю'''


def test_auth_correct_number_password(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # В документе закзачика в левой части блока: - Форма авторизации
    # В правой части блока: -  слоган ЛК "Ростелеком ID", информация для клиента
    driver.save_screenshot('test_caseEXP-002.png')
    # Вводим номер телефона и пароль
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    driver.find_element(By.ID, 'password').send_keys(f'{AuthKey.password_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    # Проверяем, что мы странице Вход и безопасность
    assert driver.find_element(By.CSS_SELECTOR, "h1[class='app-container__title']").text == "Вход и безопасность"

def test_auth_no_correct_number_and_correct_pass(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Вводим некорректный номер телефона и пароль
    driver.find_element(By.ID, "username").send_keys('79675768499')
    driver.find_element(By.ID, 'password').send_keys(f'{AuthKey.password_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(6)
    # Сравниваем сообщением при введении неправльного номера
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_auth_correct_email_pass(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем меню выбора ввода почты, через которую будем проходить авторизацию
    driver.find_element(By.ID, "t-btn-tab-mail").click()
    # Вводим корректную почту и пароль
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.mail_auth}')
    driver.find_element(By.ID, 'password').send_keys(f'{AuthKey.password_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    # Проверяем, что мы странице Вход и безопасность
    assert driver.find_element(By.CSS_SELECTOR, "h1[class='app-container__title']").text == "Вход и безопасность"

def test_auth_no_correct_email_and_correct_pass(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем меню выбора ввода почты, через которую будем проходить авторизацию
    driver.find_element(By.ID, "t-btn-tab-mail").click()
    # Вводим некорректную почту и пароль
    driver.find_element(By.ID, "username").send_keys('tQweet@mail.com')
    driver.find_element(By.ID, 'password').send_keys(f'{AuthKey.password_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(6)
    # Сравниваем сообщением ошибки при введении неправльной почты
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"

def test_auth_correct_login_pass(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем меню выбора ввода логина, через которую будем проходить авторизацию
    driver.find_element(By.ID, "t-btn-tab-login").click()
    # Вводим некорректную почту и пароль
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.login}')
    driver.find_element(By.ID, 'password').send_keys(f'{AuthKey.password_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(5)
    # Проверяем, что мы странице Вход и безопасность
    assert driver.find_element(By.CSS_SELECTOR, "h1[class='app-container__title']").text == "Вход и безопасность"

def test_auth_no_correct_login_and_correct_pass(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем меню выбора ввода логина, через которую будем проходить авторизацию
    driver.find_element(By.ID, "t-btn-tab-login").click()
    # Вводим некорректную почту и пароль
    driver.find_element(By.ID, "username").send_keys('rostel_1727009')
    driver.find_element(By.ID, 'password').send_keys(f'{AuthKey.password_auth}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Нажимаем на кнопку входа в аккаунт
    driver.find_element(By.ID, 'kc-login').click()
    time.sleep(6)
    # Сравниваем сообщением ошибки при введении неправльного логина
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный логин или пароль"


'''Восстановление пароля'''

def test_recovery_pass_choice_number_number(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По номеру телефона"
    driver.find_element(By.XPATH, '//*[@id="sms-reset-type"]/span[1]/span[3]/span[1]').click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения кода подтверждения из сообщения/почты
    time.sleep(20)
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Ввести поле "Пароль" новый пароль с латинским заглавным буквой от 8 до 20 знаков
    driver.find_element(By.ID, "password-new").send_keys(f'{AuthKey.new_password_recovery}')
    # Повторить введенный пароль "Пароль" на поле "Подтверждение пароля"
    driver.find_element(By.ID, "password-confirm").send_keys(f'{AuthKey.confir_pass_recovery}')
    #Клик "Сохранить"
    driver.find_element(By.ID, "t-btn-reset-pass").click()

def test_input_false_code_confirmations_and_ending_time_code(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По номеру телефона"
    driver.find_element(By.CSS_SELECTOR, "span[class='rt-radio__label']").click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения неверного кода подтверждения из сообщения/почты в ручную
    time.sleep(18)
    #Оранжевым цветом "Неверный код. Повторите попытку"
    assert driver.find_element(By.ID, "form-error-message").text == "Неверный код. Повторите попытку"
    # При истечении временного кода можно ввести неверный код подтверждения
    time.sleep(150)
    assert driver.find_element(By.ID, "form-error-message").text ==  "Срок действия кода истёк. Пожалуйста, запросите код снова"
    # При истечении временного кода можно отправить повторно
    time.sleep(30)
    driver.find_element(By.XPATH, "//*[@id='otp-resend-code']/svg[1]").click()

def test_recovery_requirement_no_correct_new_password_symbols(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По номеру телефона"
    driver.find_element(By.XPATH, '//*[@id="sms-reset-type"]/span[1]/span[3]/span[1]').click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения кода подтверждения из сообщения/почты
    time.sleep(20)
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Ввести поле "Пароль" новый пароль с длиной меньше 8 знаков
    driver.find_element(By.ID, "password-new").send_keys('Qwerty')
    driver.find_element(By.ID, "card-title").click()
    assert driver.find_element(By.XPATH, '//*[@id="password-new-meta"]').text == "Длина пароля должна быть не менее 8 символов"

def test_recovery_requirement_no_correct_new_password_capital_letter(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По номеру телефона"
    driver.find_element(By.XPATH, '//*[@id="sms-reset-type"]/span[1]/span[3]/span[1]').click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения кода подтверждения из сообщения/почты
    time.sleep(20)
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Ввести поле "Пароль" новый пароль без заглавных букв латиницей
    driver.find_element(By.ID, "password-new").send_keys('qwerty1234')
    driver.find_element(By.ID, "card-title").click()
    assert driver.find_element(By.XPATH, '//*[@id="password-new-meta"]').text == "Пароль должен содержать хотя бы одну заглавную букву"

def test_recovery_requirement_no_correct_new_password_latin(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По номеру телефона"
    driver.find_element(By.XPATH, '//*[@id="sms-reset-type"]/span[1]/span[3]/span[1]').click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения кода подтверждения из сообщения/почты
    time.sleep(20)
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Ввести поле "Пароль" новый пароль кириллицей
    driver.find_element(By.ID, "password-new").send_keys('Пароль222')
    driver.find_element(By.ID, "card-title").click()
    assert driver.find_element(By.XPATH,'//*[@id="password-new-meta"]').text == "Пароль должен содержать только латинские буквы"

def test_recovery_requirement_password_confirmation_not_identical_new_password(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По номеру телефона"
    driver.find_element(By.XPATH, '//*[@id="sms-reset-type"]/span[1]/span[3]/span[1]').click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения кода подтверждения из сообщения/почты
    time.sleep(20)
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Ввести поле "Пароль" новый пароль с латинским заглавным буквой от 8 до 20 знаков
    driver.find_element(By.ID, "password-new").send_keys('Qwerty1234')
    # Неверный пароль на поле "Подтверждение пароля"
    driver.find_element(By.ID, "password-confirm").send_keys('Qwerty129')
    driver.find_element(By.ID, "t-btn-reset-pass").click()
    assert driver.find_element(By.XPATH, '//*[@id="password-confirm-meta"]').text == "Пароли не совпадают"

def test_recovery_pass_choice_number_email(driver):
    # Проверяем, что мы на правильной странице с авторизацией
    assert driver.find_element(By.ID, "card-title").text == "Авторизация"
    # Кликаем текст "Забыль пароль"
    driver.find_element(By.ID, "forgot_password").click()
    time.sleep(5)
    # Проверяем, что мы на правильной странице
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Вводим номер телефона
    driver.find_element(By.ID, "username").send_keys(f'{AuthKey.number}')
    # Если есть Капча - Нужно ввести в ручную
    time.sleep(18)
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset").click()
    time.sleep(5)
    # Выбираем "По email"
    driver.find_element(By.XPATH, "//*[@id='email-reset-type']/span[1]/span[3]/span[1]").click()
    # Клик "Продолжить"
    driver.find_element(By.ID, "reset-form-submit").click()
    # Время для введения кода подтверждения из сообщения/почты
    time.sleep(20)
    assert driver.find_element(By.ID, "card-title").text == "Восстановление пароля"
    # Ввести поле "Пароль" новый пароль с латинским заглавным буквой от 8 до 20 знаков
    driver.find_element(By.ID, "password-new").send_keys(f'{AuthKey.new_password_recovery}')
    # Повторить введенный пароль "Пароль" на поле "Подтверждение пароля"
    driver.find_element(By.ID, "password-confirm").send_keys(f'{AuthKey.confir_pass_recovery}')
    # Клик "Сохранить"
    driver.find_element(By.ID, "t-btn-reset-pass").click()



