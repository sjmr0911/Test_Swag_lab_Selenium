import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAddToCart(unittest.TestCase):

    def setUp(self):
        # Inicializar el WebDriver antes de cada prueba
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
    
    def tearDown(self):
        # Cerrar el WebDriver después de cada prueba
        self.driver.quit()
    
    # Función para iniciar sesión
    def login(self):
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

    # Caso 1: Agregar un producto al carrito
    def test_add_to_cart(self):
        self.login()

        # Espera explícita para que el botón "Add to Cart" esté visible y sea clickeable
        add_to_cart_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_button.click()

        # Acceder al carrito
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Verificar que el producto esté en el carrito
        product_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertEqual(product_name, "Sauce Labs Backpack", "El producto no se agregó correctamente al carrito.")

        # Verificar el contador del carrito
        cart_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        self.assertEqual(cart_count, "1", f"Se esperaba un contador de 1, pero se obtuvo {cart_count}.")

if __name__ == "__main__":
    unittest.main()