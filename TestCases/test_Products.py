from PageObject.HomePage import HomePage
from PageObject.ProductsPage import ProductsPage
from Utilities.BaseClass import BaseClass

class Test_Product(BaseClass):

    def test_002_Products(self):
        hp = HomePage(self.driver)
        hp.click_Shop()

        Cart = ProductsPage(self.driver)
        Cart.Product_Title()

        i = -1
        for item in Cart.Product_Title():

            i = i+1
            item_Name = item.text
            # print(item_Name)

            if item_Name == "Nokia Edge":
                Cart.Product_Add()[i].click()

        Cart.Click_CheckOut()




