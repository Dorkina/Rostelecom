Проект "Ростелеком"

Объект тестирования: https://b2c.passport.rt.ru

Протестированы требования
Разработаны тест-кейсы (по требованиям - не менее 15). Применено несколько техник тест-дизайна.
Проведено автоматизированное тестирование продукта (не менее 20 автотестов).
Оформлено описание обнаруженных дефектов.
Протестированы требования заказчика. Найдены ошибки.
Для тестирования интерфейса авторизации в личном кабинете от заказчика Ростелеком Информационные Технологии мной были
применены несколько техник тест-дизайна. Техника предугадывания ошибок - наиболее вероятные типы дефектов, допускаемых
при разработке, так как это достаточно популярная техника, используемая тестировщиками
Кроме того, в тест-кейсах была применена техника тест-диайна 'граничные значения', где на странице регистрации я
проверяю граничные значения поля "Имя", "Пароль". Необходимость заложена из предпосылок, что при написании кода, разработчик
может ошибиться при указании границ и/или логики

Тестирование требований,тест-кейсы по ручному и автоматизированному тестированию, баг-репорты:
https://docs.google.com/spreadsheets/d/1EecNaRw2hYcD0xRoz3okbm02GaaQB4xSSUf3w1FG7pM/edit?usp=sharing

Для тестирования сайта был использован инструмент Selenium. Для определения локаторов использовались следующие
инструменты: DevTools. Дополнительно установлены библиотеки: selenium, pytest, pytest-selenium.
Для того, чтобы запустить автоматизированные тесты, загрузите Selenium WebDriver с
https://chromedriver.chromium.org/downloads (выбрать ту версию,что совместима с браузером)
Для того, чтобы запустить тесты, ввести в терминале: python -m pytest -m

Содержание файлов:
- tests/test_auth_form - тестирование формы авторизации
- test/test_authorization - тестирование авторизации пользователя
- test/test_fogot_password - тестирование страницы восстановления пароля
- test/test_user_registration - тестирование регистрации нового пользователя
- test/test_other  - прочие тесты
- calculated - вычисляемые параметры
- setting - Данные для заполнения полей
