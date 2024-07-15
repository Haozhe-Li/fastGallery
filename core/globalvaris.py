import os
import json

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(ROOT_DIR, "data", "image_db.json")
WEBSITE_CONFIG_DIR = os.path.join(ROOT_DIR, "data", "website_config.json")
with open(WEBSITE_CONFIG_DIR, "r") as file:
    config = json.load(file)
PREVIEW_DIR = os.path.join(ROOT_DIR, "static", "preview")
IMAGE_DIR = os.path.join(ROOT_DIR, "static", "images")

ENABLE_SEARCH_BAR = config["enable_search_bar"]

PREVIEW_QUALITY = 10
PREVIEW_SIZE = 1600
IMAGE_QUALITY = 80
IMAGE_SIZE = 4000
