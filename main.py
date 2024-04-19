import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

def initialize_driver():
    chrome_options = Options()
    chrome_options.add_argument("--verbose")
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument("--window-size=1920, 1200")
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.5; Win64; x64; en-US) AppleWebKit/537.44 (KHTML, like Gecko) Chrome/52.0.2209.276 Safari/600")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

def create_pin(image_path, input_title, input_desclink, input_desc, tagged, board_name, section_name):
    try:
        ts1 = 2
        ts2 = 10
        url1 = 'https://id.pinterest.com/login/'
        driver = initialize_driver()
        driver.get(url1)
        wait = WebDriverWait(driver, 10)
        username = 'archivicore@gmail.com'
        password = 'vivian2552'
        
        print('Masuk ke halaman login')
        wait.until(EC.presence_of_element_located((By.ID, 'email'))).send_keys(username)
        print('Email berhasil dimasukkan')
        time.sleep(ts1)
        wait.until(EC.presence_of_element_located((By.ID, 'password'))).send_keys(password)
        print('Password berhasil dimasukkan')
        time.sleep(ts1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Log in"]'))).click()
        print('Login berhasil')
        time.sleep(ts1)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//div[text()="Continue in browser"]'))).click()
            print('Lewati halaman utama')
            time.sleep(ts1)
        except:
            pass
        url2 = 'https://id.pinterest.com/pin-creation-tool/'
        driver.get(url2)
        print('Masuk ke halaman pembuat pin')
        time.sleep(ts1)
        upload_button = wait.until(EC.presence_of_element_located((By.XPATH, '//input[@type="file"]')))
        ActionChains(driver).move_to_element(upload_button).click().perform()
        upload_button.send_keys(image_path)
        print('Unggah gambar berhasil')
        time.sleep(ts2)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Add a title")]'))).send_keys(input_title)
        # print('Judul berhasil dimasukkan')
        # time.sleep(ts1)
        # description_div = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[data-contents="true"]')))
        # description_div.send_keys(input_desc)
        # print('deskripsi berhasil masuk')
        # time.sleep(ts1)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Add a link")]'))).send_keys(input_desclink)
        # print('Link berhasil dimasukkan')
        # time.sleep(ts1)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//span[text()="Choose a board"]'))).click()
        # print('Klik pilih board')
        # time.sleep(ts1)
        # wait.until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{board_name}"]'))).click()
        # print(f'Pilih board "{board_name}"')
        # time.sleep(ts1)
        # wait.until(EC.presence_of_element_located((By.XPATH, f'//div[@title="{section_name}"]'))).click()
        # print(f'Pilih section "{section_name}"')
        # time.sleep(ts1)
        # wait.until(EC.presence_of_element_located((By.XPATH, '//input[contains(@placeholder, "Search for a tag")]'))).send_keys(tagged)
        # print(f'search tag: {tagged}')
        # time.sleep(ts1)
        # wait.until(EC.presence_of_element_located((By.XPATH, f'//div[text()="{tagged}"]'))).click()
        # print(f'Pilih tag "{tagged}"')
        # time.sleep(ts1)
        wait.until(EC.element_to_be_clickable((By.XPATH, '//div[text()="Publish"]'))).click()
        print('Klik Publish')
        time.sleep(ts2)
    except Exception as e:
        print('Terjadi kesalahan:', e)
    
    finally:
        driver.quit()

def main():

    # datapost = '/storage/emulated/0/Download/pint.csv'
    # with open(datapost, 'r') as file:
        # lines = file.readlines()
        # for line in lines:
            # # parts = line.strip().split(',')
            # # new_title = parts[0]
            # # file_code = parts[1]
            input_title = 'ini judul'
            input_desc = 'Here Description'
            input_desclink = 'https://t.me/'
            tagged = 'ootd'
            board_name = 'doodweeb'
            section_name = 'Female'
            image_path = './img.jpg'
            create_pin(image_path, input_title, input_desclink, input_desc, tagged, board_name, section_name)

if __name__ == "__main__":
    main()
