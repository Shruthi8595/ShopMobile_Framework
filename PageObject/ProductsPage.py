from selenium.webdriver.common.by import By


class ProductsPage():

    # Products_Body = (By.XPATH, "//div[@class='card h-100']") # all the products on the Page
    Product_title = (By.XPATH, "//div[@class='card-body']//h4")
    Product_Add_Button = (By.XPATH, "//button[@class='btn btn-info']")
    CheckOut = (By.CSS_SELECTOR, "a[class='nav-link btn btn-primary']")


    def __init__(self,driver):
        self.driver = driver

    def Product_Title(self):
        return self.driver.find_elements(*ProductsPage.Product_title)

    def Product_Add(self):
        return self.driver.find_elements(*ProductsPage.Product_Add_Button)

    def Click_CheckOut(self):
        return self.driver.find_element(*ProductsPage.CheckOut).click()




