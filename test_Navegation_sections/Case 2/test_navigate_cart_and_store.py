from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class NavigateCartAndStoreTest(unittest.TestCase):
    def setUp(self):
        # Inicializa el navegador
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 30)

    def test_navigate_cart_and_store(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Iniciar sesión
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Agregar un producto al carrito
        driver.find_element(By.CLASS_NAME, "inventory_item").click()
        driver.find_element(By.CLASS_NAME, "btn_inventory").click()

        # Verificar que el producto se haya agregado al carrito
        driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        cart_item = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "cart_item")))
        self.assertTrue(cart_item.is_displayed(), "El producto no se encuentra en el carrito.")

        # Regresar a la tienda
        driver.find_element(By.CSS_SELECTOR, "button#continue-shopping").click()
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_container")))
        self.assertTrue(driver.find_element(By.CLASS_NAME, "inventory_container").is_displayed(), "No se regresó a la tienda.")

    def tearDown(self):
        # Cierra el navegador después de cada prueba
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
