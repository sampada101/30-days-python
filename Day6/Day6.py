import os
from zipfile import ZipFile

downloads_folder = os.path.expanduser("~")+"\Downloads"
desktop = os.path.expanduser("~")+"\Desktop"
with ZipFile(desktop+'\Downloads.zip', 'w') as f:
    for folderName, subfolders, filenames in os.walk(downloads_folder):
        for filename in filenames:
            file = os.path.join(folderName, filename)
            f.write(file, filename)
print('Success')
