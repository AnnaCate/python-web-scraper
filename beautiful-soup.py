# to run this script, pass the url you want to scrape as an argument:
# python beautiful-soup.py "https://www.example.com"

from bs4 import BeautifulSoup
import requests
import sys

url_link = sys.argv[1]

result = requests.get(url_link).text
doc = BeautifulSoup(result, "html.parser")

print(doc.main.get_text(" ", strip=True).replace("\n", ""))