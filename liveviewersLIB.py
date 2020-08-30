import requests
from html5print import HTMLBeautifier
import re


def liveviewers(video_tokenID):
    url = 'https://www.youtube.com/watch?v=' + video_tokenID

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'
    }

    scrape = requests.get(url, headers=headers, timeout=999)

    output = open('liveviewers.txt', 'w+', encoding="utf8")
    beautify = HTMLBeautifier.beautify(scrape.text, 4)
    output.write(beautify)
    output.close()

    with open('liveviewers.txt', 'r', encoding="utf8") as f:
        data = f.readlines()
        for views in data:
            if '"text": "Aktuell' in views:
                removeSpace = views.replace(' ', '')
                removeChars = re.sub('[^0-9]', '', removeSpace)
                output = open('liveviewers.txt', 'w+', encoding="utf8")
                output.write(removeChars)
                output.close()
