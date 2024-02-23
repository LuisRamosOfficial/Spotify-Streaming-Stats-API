import requests, json5, json
from bs4 import BeautifulSoup


def artist(name):
    
    songs = []
    
    html = requests.get('https://kworb.net/spotify/artists.html').text
    soup = BeautifulSoup(html, "lxml")
    
    lowname = name.lower().replace(" ", "")
    nospace = str(soup).replace(" ", "")
    
    nameIndex = nospace.lower().index(lowname)
    cut1html = nospace[:nameIndex - 2]
    url = "https://kworb.net" + cut1html[nameIndex - 51:]
    html = requests.get(url).text
    soup = BeautifulSoup(html, "lxml")
    cutted = soup.find_all("tbody")[1].find_all('a')
    
    for n in cutted:
        songs.append({"name": n.text,
                      "streams": n.find_next("td").text,
                      "daily_streams": n.find_next("td").find_next("td").text
                      })
    
    return songs

artist("21 Savage")