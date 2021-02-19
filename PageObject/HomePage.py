from selenium import webdriver
from selenium.webdriver.common.by import By

class HomePage():

    Name = (By.NAME,"name")
    Email = (By.NAME,"email")
    Password = (By.ID,"exampleInputPassword1")
    CheckBox = (By.ID,"exampleCheck1")
    Dropdown = (By.ID,"exampleFormControlSelect1")
    Submit = (By.CSS_SELECTOR,".btn-success")
    SuccessMsg = (By.CSS_SELECTOR,".alert-success")
    Shop =(By.LINK_TEXT, "Shop")


    def __init__(self,driver):
        self.driver = driver

    def set_Name(self,Name):
        self.driver.find_element(*HomePage.Name).send_keys(Name)

    def set_Email(self,Email):
        self.driver.find_element(*HomePage.Email).send_keys(Email)

    def set_Password(self,Password):
        self.driver.find_element(*HomePage.Password).send_keys(Password)

    def click_Checkbox(self):
        self.driver.find_element(*HomePage.CheckBox).click()

    def set_gender(self):
        return self.driver.find_element(*HomePage.Dropdown)

    def click_Submit(self):
        self.driver.find_element(*HomePage.Submit).click()

    def get_Alert_Msg(self):
        return self.driver.find_element(*HomePage.SuccessMsg)

    def click_Shop(self):
        self.driver.find_element(*HomePage.Shop).click()


