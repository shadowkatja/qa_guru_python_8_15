import allure
from allure_commons.types import Severity

from data import users_data, product_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage


login_page = LoginPage()
product_page = ProductPage()
user = users_data.standard_user


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_item_backpack():
    with allure.step("Login"):
        login_page.login(user)
    product = product_data.backpack
    with allure.step(f"Check_item_{product}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_item_light():
    with allure.step("Login"):
        login_page.login(user)
    product = product_data.light
    with allure.step(f"Check_item_{product}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_ckeck_item_t_shirt_1():
    with allure.step("Login"):
        login_page.login(user)
    product = product_data.t_shirt_black
    with allure.step(f"Check_item_{product}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_jacket():
    with allure.step("Login"):
        login_page.login(user)
    product = product_data.jacket
    with allure.step(f"Check_item_{product}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_onesie():
    with allure.step("Login"):
        login_page.login(user)
    product = product_data.onesie
    with allure.step(f"Check_item_{product}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.description("Test with allure steps")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_t_shirt_2():
    with allure.step("Login"):
        login_page.login(user)
    product = product_data.t_shirt_red
    with allure.step(f"Check_item_{product}"):
        product_page.check_item(product)