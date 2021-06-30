import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

class Tables(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver')
        driver = self.driver
        driver.get('https://the-internet.herokuapp.com/')
        driver.find_element_by_link_text('Sortable Data Tables').click()

    def test_sort_tables(self):
        driver = self.driver
        n, m = 5, 6
        myTable = [[0 for j in range(m)] for i in range(n)]
        # header
        headers = driver.find_elements_by_css_selector('#table1 > thead > tr > th > span')
        for i in range(len(headers)):
            myTable[0][i] = headers[i].text
        # data
        for i in range(1, n):
            for j in range(m):
                data_i = driver.find_element_by_css_selector(f"#table1 > tbody > tr:nth-child({i}) > td:nth-child({j+1})")
                myTable[i][j] = data_i.text
        print(myTable)
        sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main(verbosity=2)