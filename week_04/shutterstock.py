import requests
import sys
from bs4 import BeautifulSoup
from subprocess import call


def download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter
    r = requests.get(url, stream=True)
    with open(local_filename, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024): 
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)
                #f.flush() commented by recommendation from J.F.Sebastian
    return local_filename

def search(q, page):
    url = 'https://www.shutterstock.com/search'

    querystring = {
        'language': 'en',
        'image_type': 'photo',
        'searchterm': q,
        'page': page 
    }

    html = requests.get(url, params=querystring).text
    soup = BeautifulSoup(html)

    images = soup.select('.img-wrap img')

    if len(images) == 0:
        exit()

    for image in images:
        src = 'http:' + image.get('src')
        descrip = image.get('alt')
        print src
        localname = download_file(src)
        call(['convert', localname, '-solarize', '50', localname + '.solarized.jpg'])
        call(['open', localname + '.solarized.jpg'])
        call(['say', descrip])

    search(q, page+1)


search(sys.argv[1], 1)

# call(['convert', 'cop.jpg', 'cop.png'])
