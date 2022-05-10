from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
from typing import Dict, Any, List


def format_listings(coin_data: List[Dict]) -> List[Dict[str, Any]]:
    """
    As of 7th May, the data is formatted such that the first item in the list of data, is the header columns
    The subsequent rows are a list, in the same order as the header columns

    This function formats them, such that each row of data is now a dictionary, key is column, and value is the column value
    :param data: data from https://coinmarketcap.com
    :return:
    """
    listings = coin_data["props"]["initialState"]["cryptocurrency"]["listingLatest"][
        "data"
    ]
    all_listings: List[Dict[Any, Any]] = []
    index_to_header: Dict[str, int] = {}

    for index, header in enumerate(listings[0]["keysArr"]):
        index_to_header[index] = header

    for data_row in listings[1:]:
        current_row: Dict[str, Any] = {}
        for current_index, current_item in enumerate(data_row[:-1]):
            current_header: str = index_to_header[current_index]
            current_row[current_header] = current_item
        all_listings.append(current_row)

    return all_listings