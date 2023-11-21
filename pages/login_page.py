from users.users import User
from selene import be, have
from selene.support.shared import browser


class LoginPage:

    def open_page(self):
        browser.open('/')
        return self
    def submit_login_page(self, user: User):
        browser.element('#user-name').click().type(user.username)
        browser.element('#password').click().type(user.password)
        browser.element('#login-button').click()

    def login_result_standard_user(self):
        browser.element('#shopping_cart_container').should(be.visible)