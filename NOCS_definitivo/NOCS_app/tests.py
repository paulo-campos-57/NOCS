from django.test import LiveServerTestCase
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
driver = webdriver.Chrome(options=chrome_options)


class TestHome(LiveServerTestCase):
    driver = webdriver.Chrome()
    
    def test_title(self):
        # Verifica o título da página
        self.driver.get('http://127.0.0.1:8000/')
        assert "NOCS" in self.driver.title

    def test_cadastro_login(self):
        driver = webdriver.Chrome()
        self.driver.get("http://127.0.0.1:8000/")

        # Preenche os campos de login com informações erradas
        username = driver.find_element_by_name("username")
        username.send_keys("usuario_inexistente")
        password = driver.find_element_by_name("password")
        password.send_keys("senha_errada")
        password.send_keys(Keys.RETURN)

        time.sleep(2)
        
        assert "Login incorreto" in driver.title
        # Clica no link para realizar o cadastro
        link_cadastro = driver.find_element_by_link_text('Cadastre-se')
        link_cadastro.click()

        # Preenche os campos do formulário de cadastro
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
        
        continuar = driver.find_element_by_css_selector("button[type='submit']")
        continuar.click()

        time.sleep(2)

    def test_descarte_perigoso(self):
        driver = webdriver.Chrome()
        self.drive.get('http://127.0.0.1:8000/nocs/descarte_p')

        username = driver.find_element_by_name("username")
        username.sendkeys("meu_usuario")
        email = driver.find_element_by_name("email")
        email.sendkeys("meu_email@example.com")
        endereco = driver.find_element_by_name("endereco")
        endereco.sendkeys("meu_endereco")
        checkbox = driver.find_element_by_css_selector("input[type='checkbox']")
        checkbox.click()
        mensagem = driver.find_element_by_name("mensagem")
        mensagem.sendkeys("minha_mensagem")
        enviar = driver.find_element_by_css_selector("button1[type='submit']")
        enviar.click()

        time.sleep(0.5)

        voltar = driver.find_element_by_css_selector("button[type='submit']")
        voltar.click()

    def test_melhorar_descarte(self):
        driver = webdriver.Chrome()
        self.driver.get('http://127.0.0.1:8000/nocs/info/info_descarte')

        email = driver.find_element_by_name("email")
        email.sendkeys("meu_email@example.com")
        pergunta = driver.find_element_by_name("pergunta")
        pergunta.sendkeys("minha_pergunta")
        enviar = driver.find_element_by_css_selector("button1[type='submit']")
        enviar.click()

        time.sleep(0.5)

        voltar = driver.find_element_by_css_selector("button[type='submit']")
        voltar.click()

    

    driver.close()
