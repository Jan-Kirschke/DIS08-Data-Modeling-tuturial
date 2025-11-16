from email.mime import base
import requests
import pandas as pd
from bs4 import BeautifulSoup
import random
import time

def scrape():
    base_url: str = "https://www.presseportal.de/blaulicht/nr/4971/"
    data: list[dict]  = []
    seite: int = 0
    counter: int = 0

    print("Starte Scraping")
    while True:
        url: str = f"{base_url}{seite}"
        print("Scrape URL:", url)
        response = requests.get(url)

        if response.status_code != 200:
            print("Bad Status code. Code: ", response.status_code)
            break

        soup = BeautifulSoup(response.text, "html.parser")

        artikel_liste = soup.find_all("h3", class_="news-headline-clamp")

        if not artikel_liste:
            print("Letzte Seite erreicht. Beende das Scrapen")
            break

        for artikel in artikel_liste:
            title = artikel.find("a").text.strip()
            link = artikel.find("a")["href"]

            data.append({
                "title": title,
                "link": link
            })

            counter += 1
            print(f"Artikel Nummer {counter} wird grade gescraped")

        x = random.random()*8
        print(f"Pause für {x} Sekunden")
        time.sleep(x)
        seite += 30

    df = pd.DataFrame(data)

    df.to_csv("web_scraping/tutorial_3.csv", index=False, encoding="utf-8")


df = pd.read_csv("web_scraping/tutorial_3.csv")

print(df.loc[df["title"].str.contains("Drogen")])
