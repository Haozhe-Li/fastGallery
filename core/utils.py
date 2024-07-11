import json
import os
import json
import os
import sys

from core.globalvaris import *


def delete_content_within_folder(folder_path: str) -> None:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def clear_all_data():
    with open(DB_DIR, "w") as f:
        f.write("""{"len": 0}""")

    with open(WEBSITE_CONFIG_DIR, "w") as f:
        content = """
{
    "website_name": "Photo Portfolio",
    "website_title": "Photo Portfolio",
    "website_about": "Hi there! This is a demo page for Photo Portfolio - A simple and elegant photo gallery / portfolio website built with Flask.",
    "author_name": "Haozhe Li",
    "author_url": "https://www.haozhe.li"
}

"""
        f.write(content)

    image_folder = IMAGE_DIR
    for filename in os.listdir(image_folder):
        file_path = os.path.join(image_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)
    preview_folder = PREVIEW_DIR
    for filename in os.listdir(preview_folder):
        file_path = os.path.join(preview_folder, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


if __name__ == "__main__":
    clear_all_data()
