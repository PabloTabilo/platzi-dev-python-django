import unittest
from selenium import webdriver
from time import sleep

class AddRemoveElements(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Add/Remove Elements').click()

    def test_add_remove(self):
        driver = self.driver
        userAdd = int(input("How many elements will you add?: "))
        userRemove = int(input("How many elements will you remove?: "))
        remainderElements = userAdd - userRemove
        addButton = driver.find_element_by_css_selector("button")
        for i in range(userAdd):
            addButton.click()

        removeElements = driver.find_elements_by_css_selector(".added-manually")
        for i in range(userRemove):
            removeElements[i].click()

        print(f"Total elements on screen : {remainderElements}")

        sleep(4)


    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)