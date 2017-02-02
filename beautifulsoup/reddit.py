from bs4 import BeautifulSoup
import urllib
import time
import csv
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


def get_page(url, s):
    output = []

    html = s.get(url, headers=headers).text
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select('.entry')
    for item in items:
        link = item.select('.title a')[0]
        href = link.get('href').encode('utf8')
        title = link.text.strip().encode('utf8')

        author = item.select('.tagline .author')[0].text.strip().encode('utf8')
        date = item.select('.tagline time')[0].get('datetime').encode('utf8')

        result = {
            "href": href,
            "title": title,
            "author": author,
            "date": date
        }

        output.append(result)

        print title

    next_button = soup.select('.next-button a')

    if len(next_button) > 0:
        next_url = next_button[0].get('href')
    else:
        next_url = None
    return (next_url, output)



s = requests.Session()
next_url = 'https://www.reddit.com/r/The_Donald/'

csvfile = open('reddit.csv', 'w')
writer = csv.writer(csvfile)

while next_url is not None:
    next_url, items = get_page(next_url, s)
    for item in items:
        writer.writerow([item['href'], item['title'], item['author'], item['date']])
    time.sleep(.5)



