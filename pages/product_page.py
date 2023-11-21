from selene import be, have
from selene.support.shared import browser
from products.products import Product


class ProductPage:

    def open_main_page(self):
        browser.open('/inventory.html')

    def add_to_cart(self):
        browser.element('#add-to-cart-sauce-labs-bike-light').click()

    def add_to_cart_check(self):
        browser.element('#remove-sauce-labs-bike-light').should(be.visible)

    def remove_from_cart(self):
        browser.element('#remove-sauce-labs-bike-light').click()

    def remove_from_cart_check(self):
        browser.element('#add-to-cart-sauce-labs-bike-light').should(be.visible)

    def check_item(self, product: Product):
        browser.element(product.selector).click()
        browser.element('//div[@class="inventory_details_name large_size"]').should(have.exact_text(product.name))
        browser.element('//div[@class="inventory_details_desc large_size"]').should(
            have.exact_text(product.description))
        browser.element('//div[@class="inventory_details_price"]').should(have.exact_text(product.price))
