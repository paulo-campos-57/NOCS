from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHome(LiveServerTestCase):
    browser = webdriver.Chrome()

    def test_title(self):
        self.browser.get('http://127.0.0.1:8000/')
        assert "NOCS" in self.browser.title # Vai rodar o teste

# Rodar teste: diretório onde está o requirements e dá um python manage.py test
