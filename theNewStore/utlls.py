from bs4 import BeautifulSoup
import requests


def get_link_from_url(url):
    print(url)
    page = requests.get(url, headers={
    "User-Agent" : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
    })


    html_bytes = page.content
    html = html_bytes.decode("utf-8")

    # start soup
    soup = BeautifulSoup(html, "html.parser")

    divs = soup.find_all('div', class_='sound')[1]

    audio_link = divs.attrs.get('data-src-mp3')

    return audio_link


print('Hello Abdullah, \nWe Happy to see back')


