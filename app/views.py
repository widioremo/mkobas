from flask import render_template, redirect, flash

from app import model
from app import app

@app.route('/')
@app.route('/index')
def index():
    items = model.get_categories()
    length = items.__len__()

    if items.__len__() < 1:
        items = model.get_all_files()
        return render_template('site/index.html',
                               template='files',
                               items=items,
                               length=length)
    else:
        return render_template('site/index.html',
                               template='categories',
                               items=items,
                               length=length)

@app.route('/categories/<category_name>')
def category(category_name):
    files = model.get_by_category(category_name)
    return render_template('site/category_index.html',
                           page_header=category_name,
                           files=files)


@app.route('/video/<path:file_path>')
def video(file_path):
    return render_template('/site/video_template.html',
                           file_path=file_path)

@app.route('/pdf/<file_path>')
def pdf(file_path):
    filename = 'web/viewer.html?file=../' + file_path
    url = url_for('static',
                  filename=filename)
    redirect(url)



@app.route('/admin')
def admin():
    return render_template('/dash/dash.html')

@app.route('/admin/files')
def files():
    #render datatable with all files in db, might want to add pagination
    files = model.get_all_files()
    return render_template('/dash/files.html', files=files)

@app.route('/admin/categories')
def categories():
    cat = model.get_categories()
    return render_template('/dash/categories.html', cat=cat)




