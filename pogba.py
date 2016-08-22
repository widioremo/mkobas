import os
from blitzdb import Document
from blitzdb import FileBackend

backend = FileBackend('./file_db')

class File(Document):
    pass


class FileItem:
    '''
    each document represented as an instance of FileItem class with its attributes

    '''

    def __init__(self):
        self.name
        self.category
        self.path_to_file
        self.type
        self.slug

    def save_file(self):

        fileInfo = {}
        fileInfo['file_name'] = self.name
        fileInfo['file_path'] = self.path
        fileInfo['file_category'] = self.category
        fileInfo['slug'] = self.name.replace(' ', '-')

        # saves to blitzdb
        file = File(fileInfo)
        backend.save(file)
        backend.commit()


class Folder:
    def __init__(self, name, path):
        self.name = name
        self.path


class DirBrowser():
    '''
    lists all files of specified type in the directory and sub directories
    and saves each file as an instance of the class 'file'
    saves each folder as an instance of folder
    '''

    # filter document types
    filter = ['pdf', 'jpg', 'png', 'mp3', 'mp4']

    # get root:  current working directory (cwd)
    cwd = os.getcwd()
    pathLs = cwd.split('/')
    rootFolder = pathLs[-1]

    # save root folder
    root = Folder(rootFolder)

    # get list of items in the root directory
    # dirItems = os.listdir(cwd)

    # check for files or folders in cwd
    # if subfolder is found, check its contents with list()

    def __init__(self):
        pass


list(cwd)


def list(path):
    dirItems = os.listdir(path)

    for item in dirItems:
        path = os.path.join(cwd, item)
        # if its a dir check for contents
        if os.path.isdir(path):
            list(path)

        # otherwise it is a file: check filter
        elif os.path.isfile(path):
            (filepath, filename) = os.path.split(path)
            (fileshortname, filetype) = os.path.splitext(filename)

            split_path = filepath.split('/')
            fileParentFolder = split_path[-1]

            if filetype not in filter:
                pass
            else:
                # file is instance of file
                file = FileItem()
                file.name = filename
                file.path = filepath
                file.type = filetype
                file.category = fileParentFolder

                file.save_file();
