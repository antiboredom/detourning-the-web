from selenium import webdriver
import time


#driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()

url = 'https://skymall.com/collections/health-beauty'


driver.get(url)

products = driver.find_elements_by_css_selector('.product')

for product in products:
    title = product.find_element_by_css_selector('.product_title').text
    price = product.find_element_by_css_selector('.price-box').text

    print title, price
