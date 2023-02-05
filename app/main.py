from selenium import webdriver
import time
import chromedriver_binary
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/lib/python3.10/site-packages/chromedriver_binary/chromedriver',options=chrome_options)

driver.get('https://accounts.google.com/v3/signin/identifier?dsh=S419790722%3A1675580575528918&continue=https%3A%2F%2Fanalytics.google.com%2Fanalytics%2Fweb%2F%3Fauthuser%3D5%23%2Freport%2Fvisitors-overview%2Fa232476265w320180923p269594273%2F_u.date00%3D20230101%26_u.date01%3D20230204&followup=https%3A%2F%2Fanalytics.google.com%2Fanalytics%2Fweb%2F%3Fauthuser%3D5&passive=1209600&service=analytics&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AWnogHexwPhkGxFKp_scu-l0tLFlSbRo7M5oCrC1UGeMfeW4YXrdkhepwmxU62IHsoy31TWAn-QNdQ')
print(driver.title)

mail = driver.find_element_by_name('identifier')
mail.clear()
mail.send_keys("k-tanimoto@mamiya-its.co.jp")
button = driver.find_element_by_id('identifierNext')
button.click()
time.sleep(7)
# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# print(driver.title)

driver.save_screenshot('search_results2.png')
driver.quit()
