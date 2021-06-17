import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class AssertionsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.implicitly_wait(15) # Espera 15 seg ante de ejecutar la prueba
        driver.maximize_window() # Evitar que elementos responsivos cambien su ubicacion o orden
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_field(self):
        self.assertTrue(self.is_element_present(By.NAME, "q"))

    def test_language_option(self):
        self.assertTrue(self.is_element_present(By.ID, "select-language"))

    # Cerrar ventanas y todas las pestañas
    def tearDown(self):
        self.driver.quit()

    # how: tipo de selector
    # by : valor que tiene
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True