from bs4 import BeautifulSoup
import urllib

start_url = 'https://www.alibaba.com/Pharmaceuticals_pid100009383'
html = urllib.urlopen(start_url).read()

soup = BeautifulSoup(html, 'html.parser')

titles = soup.select('h2.title a')

for title in titles:
    print title.text
