from selenium import webdriver  # 瀏覽器驅動模組
from webdriver_manager.chrome import ChromeDriverManager  # Chrome瀏覽器驅動模組
from selenium.webdriver.chrome.options import Options  # 瀏覽器選項設定模組
from selenium.webdriver.common.by import By  # 定位元素模組
import time  # 時間模組
driver = webdriver.Chrome()  # 這會打開 Chrome 瀏覽器
driver.get('https://www.roblox.com/Login')
email = driver.find_element(By.ID, "login-username")
password = driver.find_element(By.ID, "login-password")
# 輸入帳號欄位資料
email.send_keys("leemonron")
 
# 輸入密碼欄位資料
password.send_keys("lmr0811lmr0811")
password.submit()
button = driver.find_element(By.ID, "login-button")
button.click()
'''
element = driver.find_element(By.CLASS_NAME, "login-form-error")
if element.is_displayed():
    print("元素可見！")
else:
    print("元素不可見！")

'''
