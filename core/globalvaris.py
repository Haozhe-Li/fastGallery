# store the global variables for the project
import os

PREVIEW_QUALITY = 10
PREVIEW_SIZE = 1600
IMAGE_QUALITY = 100
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREVIEW_DIR = os.path.join(ROOT_DIR, "static", "preview")
IMAGE_DIR = os.path.join(ROOT_DIR, "static", "images")
DB_DIR = os.path.join(ROOT_DIR, "data", "image_db.json")
WEBSITE_CONFIG_DIR = os.path.join(ROOT_DIR, "data", "website_config.json")
