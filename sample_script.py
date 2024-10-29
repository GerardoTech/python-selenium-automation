from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()
#  driver.implicitly.wait(4)
wait = WebDriverWait(driver, timeout=10)

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Shoes')

# wait for 4 sec
# sleep(4)
search_btn = (By.NAME, 'btnK')

# click search button
wait.until(EC.element_to_be_clickable(search_btn), message='Search button not clickable').click()
# => (By.smth, "value")
driver.find_element(*search_btn).click() # => 2: By..smth / "value"


# verify search results
assert 'shoes' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
