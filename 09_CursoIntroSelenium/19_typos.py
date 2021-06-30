import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Typos(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Typos').click()

    def test_find_typo(self):
        driver = self.driver
        # firstTime
        paragraph_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)")
        text_to_check = paragraph_to_check.text
        print(text_to_check)

        tries = 1
        correct_text = "Sometimes you'll see a typo, other times you won't."
        while text_to_check != correct_text:
            tries += 1
            text_to_check = driver.find_element_by_css_selector("#content > div > p:nth-child(3)").text
            driver.refresh()

        self.assertEqual(text_to_check == correct_text, True)
        print(f"It took {tries} tries to find the typo")

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)