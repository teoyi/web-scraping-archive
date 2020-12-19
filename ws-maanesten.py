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

#print(driver.page_source)
while (driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")):
    try:
        WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='product-load']/div" )))
        # do your other actions within the Viewport
    except TimeoutException:
        break
print("Reached to the bottom of the page")

uls = driver.find_element_by_xpath("//*[@id='content']/ul")
items = uls.find_elements_by_tag_name("li")
for item in items: 
    print(item.text)
print(len(items))

driver.quit()