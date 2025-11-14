from regex import P
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape():
    url = "https://www.scrapethissite.com/pages/simple/"
    data = []

    response = requests.get(url=url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features="html.parser")

        zeilen = soup.find_all("div", class_="col-md-4 country")

        for zeile in zeilen:
            country_name = zeile.find("h3", class_="country-name").text.strip()
            capital = zeile.find("span", class_="country-capital").text.strip()
            population = zeile.find("span", class_="country-population").text.strip()
            area = zeile.find("span", class_="country-area").text.strip()

            data.append({
                "country_name": country_name,
                "capital": capital,
                "population": population,
                "area": area
            })
    else:
        print("Url nicht erreichbar")
    return data

def to_csv(data):
    if data:
        filename = "web_scraping/tutrial_01.csv"
        df = pd.DataFrame(data=data)
        df.to_csv(filename, encoding="utf-8", index=False)


print("\nData:\n"+ str("_"*70))
df = pd.read_csv("web_scraping/tutrial_01.csv")
print(df.head(5))

