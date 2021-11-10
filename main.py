from datetime import datetime

import requests
import pandas as pd
from bs4 import BeautifulSoup, element


URL = "https://steamdb.info/sales/"

HEADERS = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
}

COOKIES = {
    # "cf_clearance": "",
    "__cf_bm": "",
}


def get_html_data() -> str:

    req = requests.get(URL, headers=HEADERS, cookies=COOKIES)

    if req.status_code == 200:
        return req.text

    else:
        msg = f"{req.status_code}: {req.reason}"
        raise ConnectionError(msg)


def extract_table_rows(html_data: str) -> element.ResultSet:

    soup = BeautifulSoup(html_data, "html.parser")
    items = soup.find_all("tr", {"class": "appimg"})
    return items


def extract_data_from_rows(items: element.ResultSet) -> list[dict]:

    items_data = []

    for item in items:
        tds = item.findAll("td")
        name = tds[2].text.strip("\n").split("\n\n")[0]
        other_fields = tds[3:]
        other_fields_values = [field["data-sort"] for field in other_fields]
        (
            discount_in_percent,
            price_in_brl,
            rating_in_percent,
            end_time_in_seconds,
            start_time_in_second,
            release_time_in_second,
        ) = other_fields_values

        discount_in_percent = int(discount_in_percent)
        price_in_brl = float(price_in_brl) / 100
        rating_in_percent = float(rating_in_percent)
        end_time_in_seconds = int(end_time_in_seconds)
        start_time_in_second = int(start_time_in_second)
        release_time_in_second = int(release_time_in_second)

        items_data.append(
            {
                "name": name,
                "discount_in_percent": discount_in_percent,
                "price_in_brl": price_in_brl,
                "rating_in_percent": rating_in_percent,
                "end_time_in_seconds": end_time_in_seconds,
                "start_time_in_second": start_time_in_second,
                "release_time_in_second": release_time_in_second,
            }
        )

    return items_data


def build_and_export_dataframe(items_data: list[dict]) -> None:

    df = pd.DataFrame(items_data)
    file_name = datetime.now().strftime("output-%Hh%Mmin-%d%m%Y.csv")
    df.to_csv(file_name, index=False)


if __name__ == "__main__":

    html_data = get_html_data()
    items = extract_table_rows(html_data)
    items_data = extract_data_from_rows(items)
    build_and_export_dataframe(items_data)
