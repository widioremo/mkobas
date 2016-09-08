from blitzdb import FileBackend
import os
from pogba import DirBrowser
from pogba import File, Category

files_dir = os.getcwd()+'/app/static/files/'
DirBrowser(files_dir)


backend = FileBackend('./file_db')

print("RETRIEVING")
file_res = backend.filter(File,{})
cat = backend.filter(Category, {})

for f in cat:
    print(f.cat_name)

for f in file_res:
    print(f.file_path)