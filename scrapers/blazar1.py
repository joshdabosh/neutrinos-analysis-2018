from bs4 import BeautifulSoup as bs
import requests
import json
import os

page = requests.get("http://www.physics.purdue.edu/astro/MOJAVE/blazarlist.html")

print("page retrieved")

if page:
    soup = bs(page.content, "html.parser")

    main = soup.find("div", {"class":"narrow-block wrapper"})

    content = main.find("table", {"id":"table2"})

    tbody = content.find("tbody")

    tw = []

    for blazar in tbody.findAll("tr"):
        inf = {
            "j": blazar.find("td", {"class":"J2000"}).text.strip(),
            "b": blazar.find("td", {"class":"B1950"}).text.strip(),
            "a": blazar.find("td", {"class":"alias"}).text.strip(),
            "ra": blazar.find("td", {"class":"RA"}).text.strip(),
            "de": blazar.find("td", {"class":"Dec"}).text.strip()
        }

        tw.append(inf)

    print(tw)
