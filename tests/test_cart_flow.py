import allure
from allure_commons.types import Severity

from data import users_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage

login_page = LoginPage()
product_page = ProductPage()
user = users_data.standard_user


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "e.goldinova")
@allure.title("Add/remove items to/from cart")
@allure.description("Flow for adding and removing items to/from cart on catalog page")
@allure.feature("Cart flow")
@allure.link('https://www.saucedemo.com', name='Testing')
def test_cart_flow():
    with allure.step("Add item to cart from catalog"):
        product_page.add_to_cart()
    with allure.step("Check the result of adding"):
        product_page.add_to_cart_check()
    with allure.step("Remove item from cart from catalog"):
        product_page.remove_from_cart()
    with allure.step("Check the result of removing"):
        product_page.remove_from_cart_check()
