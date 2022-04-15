# VaporDB
This is the code needed to run a VaporDB API. This project was created for CPSC 471 at the University of Calgary.
This API was written in Python with Django over the course of the Winter semester of 2022.

Please note that this API in its current state is NOT secure, this is a development build. Attempting to deploy this API to a production enviroment without HTTPS or following the deployment checklist provided in app will inevitably result in a security breach.

# Operation
Requirements: Python 3.9.1 or newer, your database backend of choice.

To use this API:

1. Download the latest release and extract to a location of your choosing
2. In '/VaporAPI/settings.py' ensure that DATABASES has been configured for your database 
3. In a terminal window execute the command '.venv/scripts/activate'
4. Followed by the command 'python manage.py runserver'
5. (Optional) If you receive any warnings about migrations, your database does not include all tables necessary to run this django API. It is highly reccomended that you execute the migration command it provides before attempting to utilize this API.

Documentation on how to use this API can be found here: https://documenter.getpostman.com/view/20376836/UVyvvEZA#aaddd2c6-285a-4ab7-a692-e02696d90e46
