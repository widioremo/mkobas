pogba: the best no.6 in the world
        also a micro cms using blitzdb to organise files
        
# Mkobas

Is a mini cms that uses a flat-file database to create a website from static files (pdf, video or images) developed for BRCK(http://education.brck.com/)

## Getting Started

###Motivation
The motivation for this project was to have a way in which the static files used for the education package can be tracked on git on a user friendly interface and to have to ability to generate a static website based on the static files available.



### Prerequisities and Installations

-Python (if using ubuntu python is already installed)
-Pip instructions here -> https://pip.pypa.io/en/stable/installing/
-virtualenv (Optional , but recommended), create a virtual environment for running the app

```
#run this in the cmd/terminal
$ sudo pip install virtualenv

#create the environment with
$sudo virtualenv venv

#venv is the name of the folder that will have your python interpreter

#activate the environment with 
$ sudo source venv/bin/activate


#to deactivate it later on when done use
$ deactivate

```

In the virtual environment install all dependancies with :

```

#run this in the cmd/terminal

$ pip install -r requirements.txt

```

## Deployment

###Static Files

####Step 1: Adding Files
Place the static files in their respective folders under the app/static/files directory
Every subfolder under files is considered a category 
Blitz-DB will save each folder as a category object and each file as a file object

```
#in pogba.py:
class File(Document):
    pass

class Category(Document):
    pass
```
####Step 2: Generating the DB
Check if a directory called file_db exists, this is is the file based database.
If it does NOT exist run the command below to generate it

```
(venv)$ python ./filedb.py

```
######NOTE for now there is no auto mated way of updating the db after adding static files to the appstatic/files dir, the best solution is to delete the file_db directory and regenerate it by running the command above


####Step 3 testing
To test start the server by running and the navigate to localhost:5000 on your browser

```
(venv)$ python ./run.py
```
To view the available files and their info go to localhost:5000/admin/files
localhost:5000/admin is the dashboard
localhost:5000/admin/settings - incomplete - meant to contain 
        - configuration settings
        - function to generate/regenerate the db
        - function to start the server 
        -function to generate a static website 

####Step 4: Generate Static Website aka Freeze
To get the static website run 
```
(venv)$ python ./freeze.py
```

The static site is generated under app/build directory,move it to host or zip it for future use.

## Built With

* Flask
* Blitz DB


## Authors

* **Widi Oremo** - *Initial work* - [widioremo](https://github.com/widioremo)


