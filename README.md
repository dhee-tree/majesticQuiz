# Majestic Quiz

## By: Ighomena Odebala

Welcome to my Majestic Quiz repository, django-production branch. 

This is the django web application for [visualisng_data_task](https://github.com/dhee-tree/majesticQuiz/tree/main/visualising_data_task) on the main branch of this repository.

This branch contains the code for the django web application that deploys the application to heroku.

The application is built using the django framework and the data is visualised using the plotly library.

## Approach
- I stored the data in a csv file and used management commands to load the data into the database.
- I used the django ORM to query the data and used the plotly library to visualise the data.
- The database is a postgres database hosted on my private server.
- I also added an upload feature that allows users to upload their own data and visualise it.
- Users can download a sample csv file to see the format of the data that can be uploaded.
- The application does not accept any other file format other than csv, or a csv file that does not have exactly 2 columns.

## Technologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Plotly](https://plotly.com/python/)
- [Heroku](https://www.heroku.com/)
- [Cloudflare](https://www.cloudflare.com/)

## Resources
- [Plotly](https://plotly.com/python/plot-data-from-csv/)

## Running the application locally

To run the application locally, it is advisable you clone the [main branch](https://github.com/dhee-tree/majesticQuiz/tree/main/visualising_data_task) of this repository and follow the instructions in the README file in the `visualising_data_task` directory.

## Accessing the application

The application is hosted on heroku and can be accessed via the link below:
[https://vis.ighomena.me/](https://vis.ighomena.me/)

## Usage
- Navigate to the homepage and click any of the visualise button to visualise the data.
- On the homepage, click on the upload button to upload your own data and visualise it.
- On the upload page, click on the download button to download a sample csv file to for upload (optional).