import unittest
from selenium import webdriver

class RegisterNewUser(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = self.driver
        driver.implicitly_wait(15) # Espera 15 seg ante de ejecutar la prueba
        driver.maximize_window() # Evitar que elementos responsivos cambien su ubicacion o orden
        driver.get("http://demo-store.seleniumacademy.com/")

    def test_new_user(self):
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div/div[2]/header/div/div[2]/div/a/span[2]').click()
        #el driver va a buscar el enlace por su texto y haga click
        driver.find_element_by_link_text('Log In').click()

    # Cerrar ventanas y todas las pestañas
    def tearDown(self):
        self.driver.quit()