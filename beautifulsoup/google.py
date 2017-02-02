# import urllib
# from bs4 import BeautifulSoup
#
# start_url = 'https://www.google.com/search?q="donald+trump+is"'
# html = urllib.urlopen(start_url).read()
#
# print html
#
# soup = BeautifulSoup(html, 'html.parser')
#
# titles = soup.select('.g')
#
# for title in titles:
#     print title.text
#

import requests
import time
import json
import csv
from bs4 import BeautifulSoup


def search_google(q, start=0):
    url = 'https://www.google.com/search'
    params = {'q': q, 'start': start}
    r = requests.get(url, params=params)
    print r.text
    soup = BeautifulSoup(r.text, 'html.parser')

    results = []
    elements = soup.select('.g')
    for el in elements:
        try:
            item = {}
            item['link'] = el.select('a')[0].get('href').encode('utf8')
            item['link_text'] = el.select('a')[0].text.encode('utf8')
            item['snippet'] = el.select('.st')[0].text.encode('utf8')

            results.append(item)
        except Exception as e:
            print e
            continue

    return results


def print_snippets():
    start = 0
    while start < 100:
        results = search_google('"donald+trump+is"', start)
        start += 10
        for r in results:
            print r['snippet'].encode('utf8')


def save_as_json():
    results = []
    start = 0
    while start < 100:
        results += search_google('"donald+trump+is"', start)
        start += 10

    with open('results.json', 'w') as outfile:
        json.dump(results, outfile) 


def save_as_csv():
    results = []
    start = 0
    while start < 100:
        results += search_google('"donald+trump+is"', start)
        start += 10

    with open('results.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['link', 'link_text', 'snippet'])
        for row in results:
            writer.writerow([row['link'], row['link_text'], row['snippet']])


print_snippets()
