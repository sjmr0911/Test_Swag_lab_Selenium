from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner  

class LoginTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_login_successful(self):  # Caso 1: Inicio de sesión exitoso
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Ingresar credenciales válidas
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")

        # Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()

        # Verificar que el usuario ha iniciado sesión correctamente
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_container")))
        self.assertTrue(driver.find_element(By.CLASS_NAME, "inventory_container").is_displayed())

    def test_login_invalid_credentials(self):  # Caso 2: Credenciales incorrectas
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Ingresar credenciales incorrectas
        driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
        driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar que aparece un mensaje de error
        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error esperado.")

    def test_login_locked_user(self):  # Caso 3: Usuario bloqueado
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

        # Ingresar credenciales de usuario bloqueado
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar que aparece un mensaje de error
        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error esperado.")
        self.assertIn("Sorry, this user has been locked out.", error_message.text, "El mensaje de error no es el esperado.")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports', report_name="Login_Test_Report", report_title="Resultados de Pruebas de Login"))