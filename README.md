# Campus Companion

This is a Django project that allows users to add journeys to an SQLite Database, view the database, and find information from the database using OpenAI GPT 4o-mini and RAG.

The purpose of the Campus Companion is to allow students walking alone to be accompanied by their peers as they can add information about their journeys, while others can look through the different journeys in order to find a buddy. The current project simply proves the concept but does not have the security features added.

The steps in this document assume that you have access to an OpenShift deployment that you can deploy applications on.

## How to Use it

Follow the steps below (for Mac users):

1. Install python and PIP if you do not have either 
2. Create a virtual environment using python -m venv myenv (You can use any name)
3. This sets up a virtual environment and creates a folder myenv
4. Activate the environment with source myenv/bin/activate
5. Install Django with python -m pip install Django
6. In the folder envname, run django-admin startproject buddy_system (any name is fine)
7. In the buddy_system folder, create an app with run python manage.py startapp journeys
8. In settings.py, look up the INSTALLED_APPS[] list and add journeys like this: 'journeys',
9. In the given code, go to journeys folder and copy paste models.py into your own models.py.
10. Run python manage.py makemigrations journeys and then python manage.py migrate
11. You now have a file 0001_initial.py in the migrations folder
12. Finally, copy over every other file and create new files for the ones not copied
13. In the virtual environment, pip install openai
14. Using OpenAI, get your own API key and in views.py, paste it in

If you want an introduction to [Django](https://www.w3schools.com/django/index.php), follow the tutorial linked.
