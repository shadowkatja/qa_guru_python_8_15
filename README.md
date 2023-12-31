## Проект по тестированию карточек товаров на тестовом магазине Swag Labs

> <a target="_blank" href="https://www.saucedemo.com">Swag Labs</a>

![This is an image](images/screenshots/main.png)

### Список проверок, реализованных в авто-тестах

- [x] Логин стандартного пользователя (Вынесен в фикстуру так как без логина невозможны любые действия на сайте)
- [x] Проверка заполнения карточек товара (7 штук)

### Проект реализован с использованием:

<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/pycharm.png"></code>
  <code><img width="5%" title="Python" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/python.png"></code>
  <code><img width="5%" title="Pytest" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/pytest.png"></code>
  <code><img width="5%" title="Selene" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/selene.png"></code>
  <code><img width="5%" title="Selenium" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/github.png"></code>
  <code><img width="5%" title="Jenkins" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/jenkins.png"></code>
  <code><img width="5%" title="Selenoid" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/allure.png"></code>
  <code><img width="5%" title="Allure TestOps" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/allure_testops.png"></code>
  <code><img width="5%" title="Telegram" src="https://github.com/shadowkatja/qa_guru_python_8_15/blob/master/images/icons/telegram.png"></code>
</p>

### Запуск автотестов выполняется на сервере Jenkins
> <a target="_blank" href="https://jenkins.autotests.cloud/job/goldinova_qa_guru_python_8_15/">Ссылка на проект в Jenkins</a>

### Параметры сборки

* `ENVIRONMENT` - определяет окружение для запуска тестов, по умолчанию STAGE
* `COMMENT` - комментарий к сборке
* `BROWSER_VERSION` - желаемая версия браузера Google Chrome, по умолчанию 100

### Для запуска автотестов в Jenkins

1. Открыть <a target="_blank" href="https://jenkins.autotests.cloud/job/goldinova_qa_guru_python_8_15/">проект</a>
2. Выбрать пункт `Build with Parameters`
3. Выбрать окружение в выпадающем списке ENVIRONMENT
4. Указать комментарий в поле COMMENT
5. Указать версию браузера в поле BROWSER_VERSION
6. Нажать кнопку `Build`

![This is an image](images/screenshots/build.png)

### Просмотр результатов в Allure results

#### Просмотр общих результатов тест-рана

![This is an image](images/screenshots/allure_main.png)

#### Просмотр тест-кейсов с отчетом о прохождении

![This is an image](images/screenshots/allure_suits.png)

### Интеграция с Allure TestOps

#### Хранение всех тест-кейсов

![This is an image](images/screenshots/testops_tests.png)

#### Дашборд с историей тест-ранов

![This is an image](images/screenshots/testops_dashboard.png)

### Интеграция с Telegram

#### Отправка отчетов о прохождении тест-рана в телеграм

![This is an image](images/screenshots/telegram.png)

### Видео-отчет о прохождении тестов

![report_gif](images/screenshots/report.gif)


