import allure
from allure_commons.types import Severity

from data import product_data
from pages.product_page import ProductPage


product_page = ProductPage()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Check description of \"Backpack\" item")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_item_backpack():
    product = product_data.backpack
    with allure.step(f"Check item {product.name}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Check description of \"Light\" item")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_item_light():
    product = product_data.light
    with allure.step(f"Check item {product.name}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Check description of \"Black T-shirt\" item")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_item_t_shirt_1():
    product = product_data.t_shirt_black
    with allure.step(f"Check item {product.name}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Check description of \"Jacket\" item")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_jacket():
    product = product_data.jacket
    with allure.step(f"Check item {product.name}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Check description of \"Onesie\" item")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_onesie():
    product = product_data.onesie
    with allure.step(f"Check item {product.name}"):
        product_page.check_item(product)


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Check description of \"Red T-shirt\" item")
@allure.feature("Product description")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_check_t_shirt_2():
    product = product_data.t_shirt_red
    with allure.step(f"Check item {product.name}"):
        product_page.check_item(product)
