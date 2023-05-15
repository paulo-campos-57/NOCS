from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

class TestHome(LiveServerTestCase):
    driver = webdriver.Chrome()
    
    def test_title(self):    
        self.driver.get('http://127.0.0.1:8000/')
        assert "NOCS" in self.driver.title

    def test_cadastro_login(self):
        driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")

        #preenche os campos de login com informações erradas
        username = driver.find_element_by_name("username")
        username.send_keys("usuario_inexistente")
        password = driver.find_element_by_name("password")
        password.send_keys("senha_errada")
        password.send_keys(Keys.RETURN)

        time.sleep(2)
        
        assert "Login incorreto" in driver.title
        #clica no link para realizar o cadastro
        link_cadastro = driver.find_element_by_link_text('Cadastre-se')
        link_cadastro.click()

        #preenche os campos do formulário de cadastro
        username = driver.find_element_by_name("username")
        username.send_keys("meu_usuario")
        email = driver.find_element_by_name("email")
        email.send_keys("meu_email@example.com")
        password1 = driver.find_element_by_name("password1")
        password1.send_keys("minha_senha")
        password2 = driver.find_element_by_name("password2")
        password2.send_keys("minha_senha")
        bairro = driver.find_element_by_name("bairro")
        bairro.send_keys("Meu bairro")
        rua = driver.find_element_by_name("rua")
        rua.send_keys("Minha rua")
        numero = driver.find_element_by_name("numero")
        numero.send_keys("123")
        complemento = driver.find_element_by_name("complemento")
        complemento.send_keys("Meu complemento")
        cadastro = driver.find_element_by_css_selector("button[type='submit']")
        cadastro.click()
        
        time.sleep(2)

        assert "Cadastro bem sucedido" in driver.title
        
        driver.close()

# Rodar teste: diretório onde está o manage.py e dá um python manage.py test
