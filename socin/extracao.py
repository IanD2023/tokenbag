
from  selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--user-data-dir=~/.config/google-chrome/TokenBag")
chrome_options.add_argument('--disable-dev-shm-usage')


def SenhaToken(usuariosocin):
  
  browser = Chrome(chrome_options=chrome_options)
  url="http://tokenbag.novaeranet.com.br/"
  url2="http://tokenbag.novaeranet.com.br/Token/Pesquisar?dataInicial=25%2F12%2F2022&dataFinal=25%2F12%2F2022&filialId=&funcionarioId="
  #url2="http://tokenbag.novaeranet.com.br/Token"

  browser.get(url)

  username = browser.find_element(By.ID, "Email")
  password = browser.find_element(By.ID, "Senha")
  username.send_keys("ti.ian@novaeranet.com.br")
  password.send_keys("123456")
  login_attempt = browser.find_element(By.XPATH, "//*[@type='submit']")
  login_attempt.submit()

  browser.get(url2)
  sleep(2)
  pesquisar = browser.find_element(By.XPATH, "//*[@type='submit']")
  pesquisar.submit()
  sleep(3)

  browser.find_element(By.XPATH, "//*[@type='search']").send_keys(usuariosocin)

  a = browser.find_elements(By.TAG_NAME, "td")
  
  senha=a[4].text
  
  browser.quit()
  
  return senha
  



