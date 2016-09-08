import os
from app import db
from pogba import DirBrowser, File, Category, backend

cwd = os.getcwd()

def do_listing(cwd):
    DirBrowser(os.getcwd())


def get_by_category(category):
    result = backend.filter(File, {'file_category': category})
    return result

def get_all_files():
    result = backend.filter(File,{})
    return result

def get_by_name(name):
    result = backend.filter(File,{'file_name':name})

def get_categories():
    result = backend.filter(Category, {})
    return result