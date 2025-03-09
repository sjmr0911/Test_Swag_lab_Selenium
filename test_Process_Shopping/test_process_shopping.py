import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import HtmlTestRunner

class TestCheckoutSuccess(unittest.TestCase):

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

    # Caso 1: Completar una compra exitosamente
    def test_checkout_success(self):
        self.login()

        # Agregar productos al carrito
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bike-light").click()

        # Acceder al carrito
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

        # Hacer clic en "Checkout"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        ).click()

        # Ingresar los datos personales
        self.driver.find_element(By.ID, "first-name").send_keys("Juan")
        self.driver.find_element(By.ID, "last-name").send_keys("Pérez")
        self.driver.find_element(By.ID, "postal-code").send_keys("10101")

        # Hacer clic en "Continue"
        self.driver.find_element(By.ID, "continue").click()

        # Verificar los detalles de la compra
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "summary_info"))
        )

        # Hacer clic en "Finish" para confirmar la compra
        self.driver.find_element(By.ID, "finish").click()

        # Verificar mensaje de confirmación
        confirmation_message = self.driver.find_element(By.CLASS_NAME, "complete-header").text.strip()

        # Imprimir el mensaje obtenido para verificar qué se está obteniendo
        print(f"Mensaje de confirmación obtenido: '{confirmation_message}'")

        self.assertEqual(confirmation_message, "Thank you for your order!", 
                         f"Se esperaba el mensaje 'Thank you for your order!', pero se obtuvo '{confirmation_message}'.")

        # Verificar que el carrito esté vacío
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        
        # Comprobamos si el carrito muestra un número de artículos
        try:
            cart_badge = self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
        except:
            cart_badge = None  # Si no encuentra el elemento, significa que el carrito está vacío
        
        self.assertIsNone(cart_badge, "El carrito no se vació correctamente después de la compra.")

if __name__ == "__main__":
    # Ejecutar las pruebas y generar un reporte HTML
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name="Checkout_Success_Test_Report", report_title="Resultados de Pruebas de Checkout Exitoso"))

