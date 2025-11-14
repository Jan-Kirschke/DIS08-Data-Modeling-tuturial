from jwt import encode
import requests
import pandas as pd
import random


def scrape_javascript():
    base_url: str = "https://www.scrapethissite.com/pages/ajax-javascript/"

    data: list[dict] = []
    df = pd.DataFrame()

    years = [2010, 2011, 2012, 2013, 2014, 2015]
    for year in years:
        params: dict[bool, int] = {
            'ajax': 'true',
            'year': year
        }

        try:
            response = requests.get(url=base_url, params=params)
            response.raise_for_status()

            response_json = response.json()

            for film in response_json:

                data.append(film)

        except Exception as e:
            print(e)
    print(data)
    data = pd.DataFrame(data)
    data.to_csv("web_scraping/tutorial_2.csv", encoding="utf-8", index=False)

scrape_javascript()