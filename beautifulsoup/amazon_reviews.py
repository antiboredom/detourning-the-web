import time
import requests
from bs4 import BeautifulSoup


def get_total_pages(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    total_pages = soup.select('.page-button')[-1].text
    total_pages = total_pages.replace(',', '')
    total_pages = int(total_pages)
    return total_pages



def get_reviews(url, pagenumber=1):
    html = requests.get(url + str(pagenumber)).text
    soup = BeautifulSoup(html, 'html.parser')

    reviews = soup.select('span.review-text')

    for review in reviews:
        print review.text


def get_title_and_stars(url, pagenumber=1):
    html = requests.get(url + str(pagenumber)).text
    soup = BeautifulSoup(html, 'html.parser')
    reviews = soup.select('.review')

    for review in reviews:
        title = review.select('.review-title')[0].text
        body = review.select('.review-text')[0].text
        stars = review.select('.review-rating')[0].text
        print title, stars


base_url = 'https://www.amazon.com/Amazon-Echo-Bluetooth-Speaker-with-WiFi-Alexa/product-reviews/B00X4WHP5E/ref=cm_cr_arp_d_paging_btm_2?ie=UTF8&reviewerType=all_reviews&pageNumber='

total_pages = get_total_pages(base_url + '1')

for pagenumber in range(1, total_pages):
    get_title_and_stars(base_url, pagenumber)
    time.sleep(0.2)
