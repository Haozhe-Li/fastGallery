import json
from core.globalvaris import *
from flask import url_for

def rander():
    with open(WEBSITE_CONFIG_DIR, 'r') as f:
        content = json.load(f)
        content['pic'] =  rander_pic_website(DB_DIR)
    return content

def rander_pic_website(input_picture_database: str) -> str:
    with open(input_picture_database, 'r') as f:
        content = ""
        pic_db = json.load(f)
        db_length = pic_db['len']
        for i in range(db_length):
            index = str(i)
            preview_img = pic_db[index]['preview_img']
            img = pic_db[index]['img']
            title = pic_db[index]['title']
            description = pic_db[index]['description']
            content_block = f'''
            <article class="thumb">
                <a href="{url_for('static', filename=img)}" class="image"><img src="{url_for('static', filename=preview_img)}" alt="preview image"/></a>
                <h2>{title}</h2>
                <p>{description}</p>
            </article>
            '''
            content += content_block
    return content
        
