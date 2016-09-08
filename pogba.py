import os
from blitzdb import Document
from blitzdb import FileBackend

backend = FileBackend('./file_db')


class File(Document):
    pass

class Category(Document):
    pass

class CategoryItem():
    def __init__(self):
        self.cat_name = ''
        self.cat_screen_name = ''
        self.cat_path = ''

    def save_cat(self):
        catinfo = {}

        catinfo['cat_name'] = self.cat_name
        catinfo['cat_screen_name'] = self.cat_screen_name
        catinfo['cat_slug'] = self.cat_name.replace(' ', '-')
        catinfo['cat_path'] = self.cat_path

        cat = Category(catinfo)
        backend.save(cat)
        backend.commit()


class FileItem:
    '''
    each document represented as an instance of FileItem class with its attributes

    '''

    def __init__(self):
        self.name = ''
        self.category = ''
        self.path_to_file = ''
        self.type = ''
        self.slug = ''
        self.screen_name = ''

    def save_file(self):

        fileInfo = {}
        print("SAVING")
        fileInfo['file_name'] = self.name
        fileInfo['file_path'] = self.path
        fileInfo['file_category'] = self.category
        fileInfo['file_screen_name'] = self.screen_name
        fileInfo['slug'] = self.name.replace(' ', '-')
        fileInfo['file_type'] = self.type

        # saves to blitzdb
        file = File(fileInfo)
        backend.save(file)
        backend.commit()



class Folder:
    def __init__(self, name):
        self.name = name



class DirBrowser():
    '''
    lists all files of specified type in the directory and sub directories
    and saves each file as an instance of the class 'file'
    saves each folder as an instance of folder
    '''

    # filter document types
    # filter = ['.pdf', '.jpg', '.png', '.mp3', '.mp4']

    # get root:  current working directory (cwd)

    def __init__(self, files_dir):
        print("INIT")
        self.files_dir = files_dir
        self.filter = ['.pdf','.mp3', '.mp4']
        print(self.files_dir)
        self.list(self.files_dir)





    def list(self,path):
        print("LISTING")
        dirItems = os.listdir(path)
        print(dirItems)

        for item in dirItems:
            itemPath = os.path.join(path,item)
            if os.path.isdir(itemPath):

                print("Dir Found")
                category = CategoryItem()
                category.cat_name = item
                category.cat_path = itemPath
                category.cat_screen_name = item

                category.save_cat()

                print(itemPath)
                self.list(itemPath)

            # otherwise it is a file: check filter
            else:

                print("FILE FOUND")
                (filepath, filename) = os.path.split(itemPath)
                print(itemPath)
                print(filename)
                (fileshortname, filetype) = os.path.splitext(filename)

                print(filetype)

                split_path = filepath.split('/')
                fileParentFolder = split_path[-1]

                if filetype in self.filter:
                    print("TO SAVE")
                    # file is instance of file
                    file = FileItem()
                    file.name = filename
                    file.path = filepath + '/'+ filename
                    file.path = file.path.replace(self.files_dir,'')
                    file.type = filetype
                    file.category = fileParentFolder
                    file.screen_name = filename

                    file.save_file()
                else:
                    pass


