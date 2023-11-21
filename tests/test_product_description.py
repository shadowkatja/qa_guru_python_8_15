from data import users_data, product_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage


login_page = LoginPage()
product_page = ProductPage()
user = users_data.standard_user


def test_check_item_backpack():
    login_page.open_page()
    login_page.submit_login_page(user)
    product = product_data.backpack
    product_page.check_item(product)

def test_ckeck_item_light():
    login_page.open_page()
    login_page.submit_login_page(user)
    product = product_data.light
    product_page.check_item(product)

def test_ckeck_item_t_shirt_1():
    login_page.open_page()
    login_page.submit_login_page(user)
    product = product_data.t_shirt_black
    product_page.check_item(product)

def test_check_jacket():
    login_page.open_page()
    login_page.submit_login_page(user)
    product = product_data.jacket
    product_page.check_item(product)

def test_check_onesie():
    login_page.open_page()
    login_page.submit_login_page(user)
    product = product_data.onesie
    product_page.check_item(product)

def test_check_t_shirt_2():
    login_page.open_page()
    login_page.submit_login_page(user)
    product = product_data.t_shirt_red
    product_page.check_item(product)