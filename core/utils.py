import json
import os
import json
import os
import sys
import string

from core.globalvaris import *


def delete_content_within_folder(folder_path: str) -> None:
    """
    Delete all files within a folder
    input: folder_path: str
    output: None
    """
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            os.remove(file_path)


def clear_all_data():
    """
    Clear all data in the database and image folders
    input: None
    output: None
    """
    with open(DB_DIR, "w") as f:
        f.write("""{"len": 0, "idxs": [], "keywords": []}""")

    with open(WEBSITE_CONFIG_DIR, "w") as f:
        content = """
{
    "website_name": "fastGallery",
    "website_title": "fastGallery",
    "website_about": "Hi there! This is a demo page for fastGallery - A simple and elegant photo gallery / portfolio website built with Flask.",
    "author_name": "Haozhe Li",
    "author_url": "https://www.haozhe.li"
}

"""
        f.write(content)

    image_folder = IMAGE_DIR
    preview_folder = PREVIEW_DIR
    if os.path.exists(image_folder):
        delete_content_within_folder(image_folder)
    if os.path.exists(preview_folder):
        delete_content_within_folder(preview_folder)
    if not os.path.exists(os.path.join(ROOT_DIR, "tests", "images_folder")):
        os.makedirs(os.path.join(ROOT_DIR, "tests", "images_folder"))


def compact_idxs(db_filepath: str) -> None:
    """
    Compact the idxs in the database to be continuous integers starting from 0
    input: db_filepath: str
    output: None
    """
    with open(db_filepath, "r") as file:
        data = json.load(file)

    new_len = len(data["idxs"])
    new_data = {"len": new_len, "idxs": list(range(new_len))}

    for new_idx, old_idx in enumerate(data["idxs"]):
        new_data[str(new_idx)] = data[str(old_idx)]

    with open(db_filepath, "w") as file:
        json.dump(new_data, file, indent=4)


def generate_keywords(input_picture_database: str) -> None:
    # load the input_picture_database json into a dict
    # go through the [title] and [description] of each picture
    # and find out the 5 most common words except 'the', 'a' and punctuation
    # save the 5 most common words into the output_website_config under the key "keywords" as a list.
    with open(input_picture_database, "r") as f:
        pic_db = json.load(f)
        idxs = pic_db["idxs"]
        word_count = {}
        for i in idxs:
            index = str(i)
            title = pic_db[index]["title"]
            description = pic_db[index]["description"]
            for word in title.split() + description.split():
                word = word.lower()
                if word in {"the", "a", "", " "}:
                    continue
                if word[-1] in string.punctuation:
                    word = word[:-1]
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_words) < 6:
            keywords = [word.upper() for word, _ in sorted_words if word != ""]
        else:
            keywords = [word.upper() for word, _ in sorted_words[:6] if word != ""]
        with open(input_picture_database, "r") as f:
            content = json.load(f)
            content["keywords"] = keywords
        with open(input_picture_database, "w") as f:
            json.dump(content, f, indent=4)
