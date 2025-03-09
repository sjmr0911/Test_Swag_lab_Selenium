from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class LoginSuccessfulTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.wait = WebDriverWait(self.driver, 10)
    
    def test_login_successful(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")
        
        # Ingresar credenciales válidas
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        
        # Hacer clic en el botón de login
        driver.find_element(By.ID, "login-button").click()
        
        # Verificar que el usuario ha iniciado sesión correctamente
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_container")))
        self.assertTrue(driver.find_element(By.CLASS_NAME, "inventory_container").is_displayed(), "El usuario no fue redirigido a la página de productos.")
    
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
