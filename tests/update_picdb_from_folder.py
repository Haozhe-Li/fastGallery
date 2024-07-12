import sys


from core.update_db import update_db_from_folder
from core.globalvaris import *
from core.utils import *

folder = os.path.join(ROOT_DIR, "tests", "images_folder")# load all photos from this folder
update_db_from_folder(folder)
delete_content_within_folder(folder)


