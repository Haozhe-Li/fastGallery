import json
import os
import sys
import string
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag

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


def init_project():
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
    "website_name": "Website Name",
    "website_title": "Website Title",
    "website_about": "Website About Info",
    "author_name": "Author Name",
    "author_url": "https://authoururl.com",
    "enable_search_bar": true
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
    """
    Generate keywords from the title and description of the images in the database
    input: input_picture_database: str
    output: None
    """
    with open(input_picture_database, "r") as f:
        pic_db = json.load(f)
        idxs = pic_db["idxs"]
        word_count = {}
        for i in idxs:
            index = str(i)
            title = pic_db[index]["title"]
            description = pic_db[index]["description"]
            tagged_words = pos_tag(word_tokenize(title + " " + description))
            nnp_words = [word for word, tag in tagged_words if tag == 'NNP']
            for word in nnp_words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1
        sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
        if len(sorted_words) < 10:
            keywords = [word.upper() for word, _ in sorted_words if word != ""]
        keywords = [word.upper() for word, _ in sorted_words[:10] if word != ""]
        pic_db["keywords"] = keywords
    with open(input_picture_database, "w") as f:
        json.dump(pic_db, f, indent=4)
