from bs4 import BeautifulSoup
import requests
import urllib

start_url = 'https://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=riot+gear'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_results(url):

    html = requests.get(start_url, headers=headers).text

    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select('.s-result-item')

    for item in items:
        try:
            title = item.select('h2')[0]
            print title.text.encode('utf8')

            img = item.select('img')[0].get('src')

            print img
            img_filename = img.split('/')[-1]
            urllib.urlretrieve(img, 'images/' + img_filename)

        except Exception as e:
            print e
            continue

    next_button = soup.select('#pagnNextLink')
    if len(next_button) > 0:
        next_url = next_button[0].get('href')
        get_results(next_url)


get_results(start_url)
