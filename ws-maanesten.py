from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

DRIVER_PATH = '/Users/luke/Downloads/chromedriver'
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
driver.get("https://maanesten.com/product-category/accessories-2/hair-claws/")

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
elements = WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='content']")))
for element in elements: 
    print(element.text)


driver.quit()