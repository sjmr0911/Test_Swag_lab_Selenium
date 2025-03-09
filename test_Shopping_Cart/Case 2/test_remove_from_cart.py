import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestRemoveFromCart(unittest.TestCase):

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

    # Caso 2: Eliminar un producto del carrito
    def test_remove_from_cart(self):
        self.login()

        # Paso 1: Agregar el producto al carrito
        add_to_cart_button = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack"))
        )
        add_to_cart_button.click()

        # Paso 2: Acceder al carrito
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Espera para asegurar que el producto esté en el carrito
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "cart_item")))

        # Verificar que el producto esté en el carrito antes de eliminarlo
        product_name = self.driver.find_element(By.CLASS_NAME, "inventory_item_name").text
        self.assertEqual(product_name, "Sauce Labs Backpack", "El producto no está en el carrito antes de eliminarlo.")

        # Paso 3: Eliminar el producto del carrito
        remove_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "cart_button"))
        )
        remove_button.click()

        # Verificar que el carrito esté vacío
        try:
            cart_count = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
            self.assertEqual(cart_count, "", f"Se esperaba que el carrito estuviera vacío, pero se encontró {cart_count}.")
        except:
            # Si no se encuentra el contador del carrito, verificar si no hay productos en el carrito
            cart_items = self.driver.find_elements(By.CLASS_NAME, "cart_item")
            self.assertEqual(len(cart_items), 0, "El carrito no está vacío.")

if __name__ == "__main__":
    unittest.main()