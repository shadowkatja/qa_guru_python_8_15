from data import users_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage

login_page = LoginPage()
product_page = ProductPage()
user = users_data.standard_user

def test_cart_flow():
    login_page.open_page()
    login_page.submit_login_page(user)
    product_page.add_to_cart()
    product_page.add_to_cart_check()
    product_page.remove_from_cart()
    product_page.remove_from_cart_check()