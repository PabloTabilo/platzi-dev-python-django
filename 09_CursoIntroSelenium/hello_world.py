import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    # Con el decorador classmethod hace que se quede en una ventana
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome(executable_path="./chromedriver")
        driver = cls.driver
        driver.implicitly_wait(10)

    def test_hello_world(self):
        driver = self.driver
        driver.get("https://www.platzi.com")

    def test_visit_wikipedia(self):
        self.driver.get("https://www.wikipedia.org")

    # Cerrar ventanas y todas las pestañas
    @classmethod
    def tearDown(cls):
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2, testRunner=HTMLTestRunner(output="reportes", report_name="hello-world-report"))