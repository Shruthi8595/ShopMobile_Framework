import time
import pytest
from Utilities.BaseClass import BaseClass
from PageObject.HomePage import HomePage
from TestData.homePageTestData import HomePageTestData

class Test_FillForm(BaseClass):

    def test_001_FillForm(self,getData):

        hp = HomePage(self.driver)
        hp.set_Name(getData["Name"])
        hp.set_Email(getData["Email"])
        hp.set_Password(getData["Password"])
        hp.click_Checkbox()
        self.selectOptionbyText(hp.set_gender(),getData["Gender"])
        hp.click_Submit()
    # Get alert msg and verify
        Msg = hp.get_Alert_Msg().text
        assert "Success!" in Msg

    # Click on Shop
        hp.click_Shop()



    @pytest.fixture(params=HomePageTestData.TestData_Home)
    def getData(self, request):
        return request.param
