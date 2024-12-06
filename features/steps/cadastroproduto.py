

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import requests
import os
from behave import given, when, then


def setup_driver():
    """Configura o WebDriver do Chrome e maximiza a janela."""
    options = webdriver.ChromeOptions()
    options.add_argument("--log-level=3")  # Reduz o nível de log para warnings e erros
    options.add_experimental_option("excludeSwitches", ["enable-logging"])  # Oculta mensagens do DevTools
    driver = webdriver.Chrome(service=webdriver.chrome.service.Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    return driver


def login(driver):
    """Realiza login no sistema."""
    driver.get("https://projetofinal.jogajuntoinstituto.org/")
    WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "email"))).send_keys('testejogajunto1945@gmail.com')
    driver.find_element(By.NAME, "password").send_keys('teste123123123teste')
    WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Iniciar sessão')]"))).click()


def baixar_imagem():
    """Baixa uma imagem e retorna seu caminho."""
    url = "https://acdn-us.mitiendanube.com/stores/005/398/145/products/2k7a7769-copy-74129712f5ea9719a117325594835804-1024-1024.webp"
    caminho = os.path.abspath("imagem_produto.jpg")
    with open(caminho, 'wb') as file:
        file.write(requests.get(url).content)
    return caminho


@given(u'que estou na página do Instituto Joga Junto')
def step_impl(context):
    context.driver = setup_driver()
    login(context.driver)


@when(u'apertar o botão para adicionar produto')
def step_impl(context):
    try:
        botao_adicionar = WebDriverWait(context.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Adicionar')]"))
        )
        botao_adicionar.click()
        print("Botão 'Adicionar' clicado com sucesso.")
    except Exception as e:
        print("Erro ao localizar ou clicar no botão 'Adicionar':", e)
        botoes = context.driver.find_elements(By.TAG_NAME, "button")
        print("Botões disponíveis na página:")
        for botao in botoes:
            print(botao.text)
        raise e


@when(u'inserir as informações e clicar no botão de enviar novo produto')
def step_impl(context):
    imagem_path = baixar_imagem()
    WebDriverWait(context.driver, 30).until(EC.presence_of_element_located((By.NAME, "name"))).send_keys("Produto Simples")
    context.driver.find_element(By.NAME, "description").send_keys("Descrição do produto simples.")
    context.driver.find_element(By.XPATH, "//label[span[text()='Roupas']]").click()
    context.driver.find_element(By.NAME, "price").send_keys("50,00")
    context.driver.find_element(By.NAME, "image").send_keys(imagem_path)
    context.driver.find_element(By.NAME, "shipment").send_keys("Frete grátis")
    context.driver.find_element(By.XPATH, "//button[contains(text(), 'ENVIAR NOVO PRODUTO')]").click()


@then(u'o produto é cadastrado com sucesso')
def step_impl(context):
    try:
        WebDriverWait(context.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(text(), 'Produto adicionado com sucesso')]"))
        )
        print("Produto cadastrado com sucesso!")
    except Exception as e:
        print("Erro durante a validação do cadastro:", e)
    finally:
        context.driver.quit()
        if os.path.exists("imagem_produto.jpg"):
            os.remove("imagem_produto.jpg")
            print("Imagem temporária removida.")
