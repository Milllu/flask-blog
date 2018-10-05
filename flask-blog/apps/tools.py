import os
from datetime import datetime

def creat_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        os.chmod(folder, os.O_RDWR)
        

def secure_filename_with_timestamp(filename):
    filename = datetime.now().strftime('%Y%m%d%H%M%S') + '_' + filename
    return filename

