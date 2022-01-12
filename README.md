# Task
To run locally, do the usual:
1. Clone this repository: `git clone git@github.com:alaa-22/Task.git`.
2. cd into dir `cd Task`.
3. install virtualenv and activate
4. install depen by run `pip install -r requirements.txt`
5. configure database if you have postgresql user you can change 'USER':`root` to your username and 'PASSWORD':`root` to your user's password 
or
if you don't have user create postgresql user `root` with password `root` 
after that create database called `task` then run `python manage.py migrate`
6. run `python manage.py runserver` to run the project