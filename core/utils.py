import json
import os
import json
import os
import sys

from core.globalvaris import *

def clear_all_data():
    with open(DB_DIR, 'w') as f:
        f.write('''{"len": 0}''')
    
    with open(WEBSITE_CONFIG_DIR, 'w') as f:
        content = '''
{
    "website_name": "test",
    "website_title": "test",
    "website_about": "test",
    "author_name": "test",
    "author_url": "test"
}

'''
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

if __name__ == '__main__':
    clear_all_data()    
    
