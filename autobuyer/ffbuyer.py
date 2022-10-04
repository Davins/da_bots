import time
import random
from selenium.webdriver.firefox.service import Service
from selenium import webdriver

service = Service(executable_path="G:\exam\webdriver\geckodriver.exe")
driver = webdriver.Firefox(service=service)
url = "https://www.komplett.dk/product/1182163/hardware/pc-komponenter/grafikkort/sapphire-radeon-rx-6700-xt-nitro"
driver.get(url) 
###sold out alternative https://www.komplett.dk/product/1111557/gaming/playstation/playstation-5-ps5?q=playstation%205

foundButton = False

while not foundButton:
    clickBuyButton = BuyButton = driver.find_element_by_class_name("buy-button")
    if("button-disabled" in clickBuyButton.get_attribute("class)")):
        time.sleep(5)

        driver.refresh()

        clickBuyButton = BuyButton = driver.find_element_by_class_name("buy-button")
    else:
        foundButton = True

BuyButton.click()

"""
random_wait_time = random.randrange(7.0,16.0)
time.sleep(random_wait_time)

add_to_cart_button = driver.find_element_by_class_name("buy-button")
add_to_cart_button.click()
"""