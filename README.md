Модуль 33.1 Реальный опыт | Дипломный проект: реальный кейс компании «Ростелеком Информационные Технологии».
Бриф от заказчика - https://docs.google.com/document/d/1Onrxx9fWEwGHLuo39e53XVaECMUWGuRi/edit?usp=drive_link&ouid=113733934354208288906&rtpof=true&sd=true .
К работе прикреплены:
1)ТЕСТ-КЕЙС (ссылка на Google-таблицу "ЛИСТ 1").
2)Автотесты (ссылка автотестов на GitHub).
3)Баги (Google-таблице с тест-кейсами "ЛИСТ 2").
В Автотестах были применены:
1)Инструмент "Element Locator", для быстрого нахождения элементов DOM (скачанное из интернет-магазина Chrome).
2)Тест дизайн-техника пограничные границы полей.
Для работы тестов необходимы:
1)PyCharm - https://www.jetbrains.com/pycharm/download/?section=windows .
2)ChromeDriver (вашй версии Chrome) - https://developer.chrome.com/docs/chromedriver/downloads?hl=ru .
3)Библиотеки:
a)pip install pytest (терминал PyCharm).
b)pip install pytest-selenium  (терминал PyCharm).
ПРИ ТЕСТИРОВАНИИ "РЕГИСТАЦИЯ", создается УЧЕТНАЯ ЗАПИСЬ в "Ростелеком".
ДО тестирования, необходимо внести ВАШИ ДАННЫЕ в папке "pages33" -> файл "auth_key.py" .
Переносить и использовать в таком же виде как на GitHub на главную папку Pycharm.
Для запуска тестов необходимо в терминале PyCharm указать, какой именно браузер мы хотим использовать, и путь к его драйверу (не забываем заменить /path/to/ на свой путь):
pytest -v --driver Chrome --driver-path /path/to//chromedriver.exe название файл.py
К сожалению, имеется ограничение в сутки отправки кода подтверждения
