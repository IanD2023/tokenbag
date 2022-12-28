
from  selenium.webdriver import Chrome
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument("--user-data-dir=~/.config/google-chrome/TokenBag")
chrome_options.add_argument('--disable-dev-shm-usage')

def ConvertMD5(md5):

        browser = Chrome(chrome_options=chrome_options)
        url="https://md5.gromweb.com/"
        browser.get(url)
        browser.find_element(By.ID, "form_hash_to_string_hash").send_keys(md5)
        browser.find_element(By.ID, "form_hash_to_string_submit").send_keys(Keys.ENTER)
        convertmd5=browser.find_element(By.CSS_SELECTOR, '[class="long-content string"]')

        senha=convertmd5.text

        browser.quit()

        return senha