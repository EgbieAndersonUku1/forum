

# The Forum 
The url for the app is  https://theforum.pythonanywhere.com/

Because I am using Pythonanywhere the database resets after a certain amount of time inactive which
causes the connection to be lost which results with a 500 error. If that happens just refresh the page and 
everything should be normal again. I fixed the problem so it should not happen but if it does then you know the solution

## Project description
This is website allows the user to create a single thread or multiple threads along with a title (maximum 80 characters long)
and a description (maximum length 255 characters long) where anyone
who has account can post replies to that thread. If the user does not have account the user cannot
post a reply but can view the replies.



## Technologies used
1. Python 3.6
1. Flask
1. HTML
1. JavaScript
1. Bootstrap
1. Sqlite3
1. SQLAlchemy
1. Flask-Login
1. Flask-Security
1. Bootstrap
1. CSS

## How to run this in your local system
1. Create a virtual environment optional
1. Create a **name** for your directory
1. Go into your new directory
1. Clone the repository by using the command git clone https://github.com/EgbieAndersonUku1/<repository name here> **.** The full stop at end copies all the folder and directories and sub-directories into the your chosen directory without creating the based folder.
1. Type the command "**pip install -r requirements.txt**" (making sure you are in the root directory) this will install all the dependencies on your virtual environment

1. (First time use only) Open a command terminal make sure you are in the forum root folder and type the command: 
    1. flask db init
    1. flask db migrate
    1. flask db upgrade
    1. Next open a python terminal and type the following command
        1. from create_app import db
        1. db.create_all()
  
1. Next run the command ** flask run** If you get an error type in the command
    1. set FLASK_APP=app.py
    1. ** flask run **
1. Open a browser of your choice and type in **http://127.0.0.1:5000** and watch app go



