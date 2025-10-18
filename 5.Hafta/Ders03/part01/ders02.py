from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
# ChromeDriver yolunu belirt (kendi yolunuza göre güncelleyin)
#service = Service(executable_path="chromedriver.exe")
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")
print(driver)
print(driver.title)

time.sleep(10)
driver.fullscreen_window()
time.sleep(5)
driver.quit()