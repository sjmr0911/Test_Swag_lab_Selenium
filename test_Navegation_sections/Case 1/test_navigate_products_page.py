from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NavigateProductsPageTest(unittest.TestCase):
    def setUp(self):
        # Inicializa el navegador
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 30)

    def test_navigate_products_page(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Iniciar sesión
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verificar que la lista de productos está visible
        product_list = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        self.assertTrue(product_list.is_displayed(), "La lista de productos no está visible.")

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
