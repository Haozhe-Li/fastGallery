import os
import sys

import uuid
from PIL import Image
import json
from core.globalvaris import *

def convert_to_webp(input_file: str, output_file: str, quality: int, max_size: int) -> None:
    if not input_file.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
        print(f'''{input_file} is not a valid image file''')
        return
    try:
        with Image.open(input_file) as im:
            if max_size != None:
                ratio = max_size / max(im.width, im.height)
                new_size = (int(im.width * ratio), int(im.height * ratio))
                im.thumbnail(new_size)
            im.save(output_file, "webp", quality=quality)
    except Exception as e:
        print(str(e))
    
def update_db(args: dict) -> str:
    input_file = args['img_url']
    title = args['title']

    pic_id = str(uuid.uuid4())

    output_preview_img_path = f'''{PREVIEW_DIR}/{pic_id}.webp'''
    output_img_path = f'''{IMAGE_DIR}/{pic_id}.webp'''
    
    if not os.path.exists(PREVIEW_DIR):
        os.makedirs(PREVIEW_DIR)
    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)

    convert_to_webp(input_file=input_file, output_file=output_preview_img_path, quality=PREVIEW_QUALITY, max_size=PREVIEW_SIZE)
    convert_to_webp(input_file=input_file, output_file=output_img_path, quality=IMAGE_QUALITY, max_size=None)

    # save to json
    with open(DB_DIR, 'r') as f:
        db = json.load(f)
        index = db['len']
        db[index] = {
            'preview_img': f'''preview/{pic_id}.webp''',
            'img': f'''images/{pic_id}.webp''',
            'title': title,
            'description': args['description']
        }
        db['len'] += 1
    with open(DB_DIR, 'w') as f:
        json.dump(db, f)

def update_db_from_folder(folder_path: str) -> None:
    filenames = sorted(os.listdir(folder_path))
    for filename in filenames:
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            update_db({
                'img_url': file_path,
                'title': filename,
                'description': ''
            })


