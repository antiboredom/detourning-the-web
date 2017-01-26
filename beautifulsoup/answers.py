from bs4 import BeautifulSoup
import urllib

start_url = 'https://answers.search.yahoo.com/search;_ylt=AwrC2Q4kKxRYHgcAi3ZPmolQ;_ylc=X1MDMTM1MTE5NTIxNQRfcgMyBGZyA3VoM19hbnN3ZXJzX3ZlcnRfZ3MEZ3ByaWQDVG5YWlRfZjNRUWFLeWV5dE11MTVSQQRuX3JzbHQDMARuX3N1Z2cDNwRvcmlnaW4DYW5zd2Vycy5zZWFyY2gueWFob28uY29tBHBvcwMwBHBxc3RyAwRwcXN0cmwDBHFzdHJsAzMEcXVlcnkDbG9sBHRfc3RtcAMxNDc3NzE3MTc1?p=lol&fr2=sb-top-answers.search&fr=uh3_answers_vert_gs&type=2button'

def get_results(url):

    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html, 'html.parser')

    titles = soup.select('.lh-17')

    for title in titles:
        print title.text.encode('utf8')

    next_button = soup.select('a.next')
    if len(next_button) > 0:
        next_url = next_button[0].get('href')
        get_results(next_url)


get_results(start_url)
