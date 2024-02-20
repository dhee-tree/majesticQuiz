# Majestic Quiz

## By: Ighomena Odebala

This is the django web application for [visualisng_data_task](https://github.com/dhee-tree/majesticQuiz/tree/main/visualising_data_task) on the main branch of this repository.
Welcome to my Majestic Quiz repository, django-visualisation branch. 

This branch contains the code for the django web application that visualises the data from test C.

The application is built using the django framework and the data is visualised using the plotly library.

## Approach
- I stored the data in a csv file and used management commands to load the data into the database.
- I used the django ORM to query the data and used the plotly library to visualise the data.
- The database is a postgres database hosted on my private server.

## Technologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Plotly](https://plotly.com/python/)
- [Heroku](https://www.heroku.com/)
- [Cloudflare](https://www.cloudflare.com/)

## Running the application locally

Assuming you have python installed on your machine and have setup the environment variables for the application, you can run the application locally using the following steps:
- Clone the repository
- Create or activate a virtual environment (optional).
- Install the requirements using the command `pip install -r requirements.txt`
- Run the migrations using the command `python manage.py migrate`
- Load data into the database using the command `python manage.py load_drink` and `python manage.py load_sweet`
- Run the application using the command `python manage.py runserver`

## Accessing the application

The application is hosted on heroku and can be accessed via the link below:
[https://vis.ighomena.me/](https://vis.ighomena.me/)