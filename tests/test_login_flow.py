#import allure
#from allure_commons.types import Severity

#from data import users_data
#from pages.login_page import LoginPage
#from pages.product_page import ProductPage

#login_page = LoginPage()
#product_page = ProductPage()
#user = users_data.standard_user


#@allure.tag("web")
#@allure.severity(Severity.NORMAL)
#@allure.label("owner", "e.goldinova")
#@allure.title("Login with standard user")
#@allure.description("Flow for login with standard user")
#@allure.feature("Login flow")
#@allure.link('https://www.saucedemo.com', name='Testing')
#def test_login_standard_user():
#    with allure.step("Login"):
#        login_page.login(user)
#    with allure.step("Check the result of login"):
#        login_page.login_result_standard_user()

