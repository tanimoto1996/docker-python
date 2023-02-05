from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import chromedriver_binary
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/lib/python3.10/site-packages/chromedriver_binary/chromedriver',options=chrome_options)

driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S419790722%3A1675580575528918&continue=https%3A%2F%2Fanalytics.google.com%2Fanalytics%2Fweb%2F%3Fauthuser%3D5%23%2Freport%2Fvisitors-overview%2Fa232476265w320180923p269594273%2F_u.date00%3D20230101%26_u.date01%3D20230204&followup=https%3A%2F%2Fanalytics.google.com%2Fanalytics%2Fweb%2F%3Fauthuser%3D5&passive=1209600&service=analytics&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHexwPhkGxFKp_scu-l0tLFlSbRo7M5oCrC1UGeMfeW4YXrdkhepwmxU62IHsoy31TWAn-QNdQ')
print(driver.title)

# メールアドレス入力画面
mail = driver.find_element_by_name('identifier')
mail.clear()
mail.send_keys("k-tanimoto@mamiya-its.co.jp")
mail_button = driver.find_element_by_id('identifierNext')
mail_button.click()
time.sleep(2)

# CloudGate UNO画面
rawUsername = driver.find_element_by_id('rawUsername')
rawUsername.clear()
rawUsername.send_keys("k-tanimoto")

realm = driver.find_element_by_id('realm')
realm.click()

realmOption = driver.find_element_by_id('realm-option-1')
realmOption.click()

realmButton = driver.find_element_by_id('username-realm-form')
realmButton.submit()
time.sleep(2)

rawPassword = driver.find_element_by_id('password')
rawPassword.clear()
rawPassword.send_keys("N7vkGAV6")

passwordButton = driver.find_element_by_xpath('//*[@id="password-form"]/button[1]')
passwordButton.click()
time.sleep(30)

# ここからアナリティクス画面開始

driver.save_screenshot('search_results2.png')
driver.quit()
