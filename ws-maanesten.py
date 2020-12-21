import requests
import numpy as np
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# DRIVER_PATH = '/Users/luke/Downloads/chromedriver'
# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

# driver = webdriver.Chrome(options=options, executable_path=DRIVER_PATH)
# driver.get("https://maanesten.com/product-category/accessories-2/hair-claws/")

# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# elements = WebDriverWait(driver,30).until(EC.visibility_of_all_elements_located((By.XPATH, "//*[@id='content']")))
# for element in elements: 
#     print(element.text)

gen_url = 'https://maanesten.com/product-category/accessories-2/hair-claws/?metaltype[]=accessories&ajaxcall=1&page='
pNames = []
for n in np.arange(1, 7, 1):
    #print(gen_url+str(n))
    r = requests.get(gen_url+str(n), headers= {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36',
        'Content-Type': 'text/html'})
    c = r.content 
    soup = BeautifulSoup(c, 'html.parser')
    uls = soup.find('ul', {'class' : 'products'})
    ils = uls.find_all('li')
    for il in ils: 
        pNames.append(il.find('h3').text)

for n in np.arange(0, len(pNames)):
    pNames[n] =  pNames[n].replace(' ', '-')
print(pNames)





# driver.quit()