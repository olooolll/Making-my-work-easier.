from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
from time import sleep
import selenium.common.exceptions
import os

os.system('clear')

def dados_cooler_lista(dados_os):
    dados_os = dados_os[16]
    
    options = Options()
    options.headless = True
    options.add_argument("--headless")


    # Inicializar o driver do Firefox com as opções configuradas
    navegador = webdriver.Firefox(options=options)


    url = navegador.get('https://www.sistema.com')

    def funcao_xpath(X, SK=None, E=None, C=None, S=None):
        if E == 'E':
            xpath = navegador.find_element(By.XPATH, X).send_keys(SK, Keys.ENTER)
        elif C == 'C':
            xpath = navegador.find_element(By.XPATH, X).click()
        elif S == 'S':
            xpath = navegador.find_element(By.XPATH, X).send_keys(SK, Keys.ARROW_DOWN, Keys.ENTER)
        else:
            xpath = navegador.find_element(By.XPATH, X).send_keys(SK)    
        return xpath

    funcao_xpath('//*[@id=":r0:"]', SK='')
    funcao_xpath('//*[@id=":r1:"]', SK='', E='E')

    sleep(2)

    navegador.get('https://www.sistema.takeandgoapp.com/refrigerator/list?page=0')

    funcao_xpath('/html/body/div[1]/div[2]/div[2]/div[1]/div[2]/button[2]', C='C')
    
    sleep(0.5)

    funcao_xpath('//*[@id=":ra:"]', SK=dados_os, E='E')

    sleep(5)

    funcao_xpath('/html/body/div[1]/div[2]/div[2]/main/div[2]/div[2]/div/table/tbody/tr[1]/td[11]/div/div[1]/button', C='C')

    sleep(5)

    dados_cooler = []

    data_cooler = navegador.find_elements(By.TAG_NAME, 'input')

    for div in data_cooler:
        data_cooler = []
        data = div.get_attribute('value')
        dados_cooler.append(data)
    
    navegador.quit()

    return dados_cooler
