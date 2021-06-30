import unittest
from selenium import webdriver
from time import sleep

# Requerimientos
# Ir a mercado libre
# Filtrar por CL
# Buscar PS4
# Filtro RM, Nuevo
# Menor precio

class MercadoLibre(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./chromedriver")
        driver = self.driver
        driver.implicitly_wait(30)
        driver.maximize_window()
        driver.get("https://www.mercadolibre.com/")

    def clickMeWithJS(self, clickAble):
        self.driver.execute_script("arguments[0].click();", clickAble)

    def test_search_ps4(self):
        driver = self.driver
        country = driver.find_element_by_css_selector("#CL")
        country.click()

        search_field = driver.find_element_by_css_selector("body > header > div > form > input")
        search_field.click()
        search_field.clear()
        search_field.send_keys("ps4")
        search_field.submit()
        sleep(3)

        location = driver.find_element_by_partial_link_text('RM (Metropolitana)')
        #location.click()
        self.clickMeWithJS(location)
        sleep(3)

        condition = driver.find_element_by_partial_link_text('Nuevo')
        self.clickMeWithJS(condition)
        #condition.click()
        sleep(3)

        buttonDropDown = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > button')
        buttonDropDown.click()
        sleep(3)

        ascPrice = driver.find_element_by_css_selector('#root-app > div > div > section > div.ui-search-view-options__container > div > div > div > div.ui-search-sort-filter > div > div > div > ul > li:nth-child(2) > a')
        ascPrice.click()
        sleep(3)

        objectsNames = driver.find_elements_by_class_name('ui-search-item__title')
        #objectsPrices = driver.find_elements_by_class_name('price-tag-fraction')
        size = len(objectsNames)
        res = dict()
        for i in range(size):
            x = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[1]/a/h2')
            y = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div/section/ol/li[{i+1}]/div/div/div[2]/div[2]/div[1]/div/div/div/span[1]/span[2]/span[2]')
            res[i] = {"name": x.text, "price": y.text}

        print(res)

        sleep(3)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)