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
# while (driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")):
#     try:
#         WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='product-load']/div" )))
#         # do your other actions within the Viewport
#     except TimeoutException:
#         break
# print("Reached to the bottom of the page")

# uls = driver.find_element_by_xpath("//*[@id='content']/ul")
# items = uls.find_elements_by_tag_name("li")
# for item in items: 
#     print(item.text)
# print(len(items))
#print([element.text for element in WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='content']")))])

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
elements = WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='content']")))
for element in elements: 
    print(element.text)
# names = []
# products = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='content']//ul/li/a/h3")))
# for product in products: 
#     names.append(product.text)
# try: 
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     products = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='content']//ul/li/a/h3")))
#     print(products)
#     for product in products: 
#         names.append(product.text)
# except:
#     pass 
# for name in names:
#     print(name)



# titles = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='productDescriptionAndPrice']//h4/a")))
# for title in titles:
#     item_names.append(title.text)
# try:
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     titles = WebDriverWait(driver, 5).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='productDescriptionAndPrice']//h4/a")))
#     for title in titles:
#     item_names.append(title.text)
# except:
#     pass
# for item_name in item_names:
#     print(item_name)

driver.quit()