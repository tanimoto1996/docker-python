from selenium import webdriver
import time
import chromedriver_binary
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('/usr/local/lib/python3.10/site-packages/chromedriver_binary/chromedriver',options=chrome_options)

driver.get('https://www.google.com/')
print(driver.title)

# search_box = driver.find_element_by_name("q")
# search_box.send_keys('ChromeDriver')
# search_box.submit()
# print(driver.title)

driver.save_screenshot('search_results2.png')
driver.quit()
