
import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class BaseClass():

#DropDown
    # Locator = Element identification
    # Locator Type = ID, Name, CSS, Xpath.....

    def selectOptionbyText(self, locator, text):
        element = Select(locator)
        element.select_by_visible_text(text)

    def selectOptionbyIndex(self, locator, text):
        element = Select(locator)
        element.select_by_index(text)

