# AL ADL WEBSITE SETUP:

###### Written By:

###### Nauman Arif, NullStack Technologies

###### May, 2023

### SETUP DJANGO:

###### Make Sure you have Python 3 installed:

###### https://www.w3schools.com/django/django_create_virtual_environment.php

###### Then Go inside project and Activate Virtualenv

###### [Watch a Tutorial] or

`virtualenv -p /usr/bin/python3 venv`<br>
`pip install -r requirements.txt` <br>

###### Create a File secret.py inside al_adl_website <br>

##### Run Migrations:

`python manage.py migrate` <br>

##### RUN Server:

`python manage.py runserver 0.0.0.0:8000` <br>
<br>

### SETUP TAILWIND:

`npm install` <br>

### SETUP JS LIBRARIES:

`npm run build` <br>

`npm run build2` <br>

##### Start NPM Watch Server

`npx tailwindcss -i ./static/css/tailwind/tailwind-input.css -o ./static/css/tailwind/tailwind.css --watch` <br>

`npx tailwindcss -i ./static/css/tailwind/tailwind-develawp.css -o ./static/css/tailwind/develawp.css --watch` <br>

##### BUILD TAILWIND

`npx tailwindcss -i ./static/css/tailwind/tailwind-input.css -o ./static/css/tailwind/tailwind.css --minify` <br>

##### ------------------------------------
