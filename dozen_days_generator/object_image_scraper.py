import os
import time
from pathlib import Path
from PIL import Image
from io import BytesIO

import requests
from tqdm import tqdm


_ROOT = Path(__file__).parent.absolute()


def get_data(path):
    return _ROOT / 'data' / path


def load_object_list():
    with open(get_data('object-list.txt')) as file:
        return file.read().splitlines()


def download_search_result(search_term: str, download_directory: Path):
    if not download_directory.exists():
        download_directory.mkdir(parents=True)

    subscription_key = os.environ.get("BING_SUBSCRIPTION_KEY")

    search_url = "https://api.cognitive.microsoft.com/bing/v7.0/images/search"

    headers = {"Ocp-Apim-Subscription-Key": subscription_key}
    params = {"q": search_term, "license": "public", "imageType": "photo"}
    response = requests.get(search_url, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()

    thumbnail_urls = [img["thumbnailUrl"] for img in search_results["value"][:10]]

    for i, url in enumerate(thumbnail_urls):
        image_data = requests.get(url)
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))
        filename = f'{search_term}{i:02d}.png'
        print(filename)
        image.save(download_directory / filename)


def scrape_images():
    object_list = load_object_list()
    for search_term in tqdm(object_list):
        download_search_result(search_term, _ROOT / 'data' / 'object-images')
        time.sleep(1)


if __name__ == '__main__':
    scrape_images()
