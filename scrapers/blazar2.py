from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import json

browser = webdriver.Chrome(ChromeDriverManager().install())
browser.get("https://www.asdc.asi.it/bzcat/")

page = browser.execute_script("setPageSizeValue(0); setHead(Head, 1, 0); writeBottom(); setHead(Head, 1, 2); writeBottom(); setHead(Head, 1, 2); writeBottom(); setHead(Head, 1, 3); writeBottom(); setHead(Head, 1, 6); writeBottom(); return document.body.innerHTML")

soup = bs(page, "html.parser")

bottom = soup.find("div", {"id": "bottom"})

lines = []

table = bottom.find("table", {"class":"table_catalog"})
tbody = table.find("tbody")

for tr in tbody.findAll("tr", {"id":lambda x: x == "second_line" or x == "first_line"}):
    lines.append([i.text.strip() for i in tr.findAll("td")][3:8])

f = open("../data2.json", "w")
final = [{"ra": ra, "de": de, "a": a, "z": z} for ra, de, a, z in lines]
f.write(json.dumps(final, sort_keys=True, indent=4, separators=(",", ": ")))
f.close()

print("finished")
