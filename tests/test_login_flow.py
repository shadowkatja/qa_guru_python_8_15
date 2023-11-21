from data import users_data
from pages.login_page import LoginPage
from pages.product_page import ProductPage

login_page = LoginPage()
product_page = ProductPage()
user = users_data.standard_user

def test_login_standard_user():
    login_page.open_page()
    login_page.submit_login_page(user)
    login_page.login_result_standard_user()



