import json
from core.globalvaris import *
from flask import url_for


def rander(keyword=None):
    """
    Rander the website with Flask Format
    input: None
    output: dict
    """
    with open(WEBSITE_CONFIG_DIR, "r") as f:
        content = json.load(f)
        content["pic"] = rander_pic_website(DB_DIR, keyword)
        content["keywords"] = rander_keywords(DB_DIR)
    return content


def rander_pic_website(input_picture_database: str, keyword=None) -> str:
    """
    Rander the picture into website with Flask Format
    input: input_picture_database: str
    output: str
    """
    with open(input_picture_database, "r") as f:
        content = ""
        pic_db = json.load(f)
        idxs = pic_db["idxs"]
        for i in reversed(idxs):
            index = str(i)
            preview_img = pic_db[index]["preview_img"]
            img = pic_db[index]["img"]
            title = pic_db[index]["title"]
            description = pic_db[index]["description"]
            if keyword is not None:
                if keyword not in title.lower() or keyword not in description.lower():
                    continue
            content_block = f"""
            <article class="thumb">
                <a href="{url_for('static', filename=img)}" class="image"><img src="{url_for('static', filename=preview_img)}" alt="preview image"/></a>
                <h2>{title}</h2>
                <p>{description}</p>
            </article>
            """
            content += content_block
    return content


def rander_keywords(input_picture_database: str):
    with open(input_picture_database, "r") as f:
        content = ""
        pic_db = json.load(f)
        keywords = pic_db["keywords"]
        content = ""
        for k in keywords:
            block = f"""
            <a href="/filter/{k}">{k}</a>, 
            """
            content += block
        return content[:-1]
