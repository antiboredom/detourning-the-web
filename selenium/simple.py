from selenium import webdriver
import time
import csv

# driver = webdriver.Firefox()
# driver = webdriver.Chrome()
driver = webdriver.PhantomJS()

writer = csv.writer(open('output.csv', 'w'))


def get_page():
    time.sleep(1)
    items = driver.find_elements_by_css_selector('.m-product-item')
    for item in items:
        title = item.find_element_by_css_selector('h2.title').text
        if 'class="price"' in item.get_attribute('innerHTML'):
            price = item.find_element_by_css_selector('.price').text
        else:
            price = "UNKNOWN"
        print([title, price])
        writer.writerow([title, price])

    driver.find_element_by_css_selector('.ui2-pagination-pages a.next').click()
    get_page()

url = "http://www.alibaba.com/trade/search?fsb=y&IndexArea=product_en&CatId=&SearchText=surveillance"

driver.get(url)
get_page()

driver.quit()
