from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner

class NavigationTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 30)

    def test_navigate_products_page(self):  # Caso 1: Acceder a la página de productos
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Iniciar sesión
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()

        # Verificar que la lista de productos está visible
        product_list = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_list")))
        self.assertTrue(product_list.is_displayed(), "La lista de productos no está visible.")

    def test_navigate_cart_and_store(self):  # Caso 2: Navegar entre el carrito y la tienda
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
    try:
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name="Navigation_Test_Report", report_title="Resultados de Pruebas de Navegación"))
    except Exception as e:
        print(f"Error durante la ejecución de las pruebas: {e}")