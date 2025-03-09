from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginInvalidCredentialsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_login_invalid_credentials(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Ingresar credenciales incorrectas
        driver.find_element(By.ID, "user-name").send_keys("usuario_invalido")
        driver.find_element(By.ID, "password").send_keys("clave_incorrecta")
        
        # Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar que aparece un mensaje de error
        error_message = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "error-message-container")))
        self.assertTrue(error_message.is_displayed(), "No se mostró el mensaje de error esperado.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
