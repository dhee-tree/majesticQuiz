# Majestic Quiz

## By: Ighomena Odebala

### Task
Create a visualisation of each set of fictitious data.

## Approach
- I stored the data in a csv file and used management commands to load the data into the database. This ensures that the data from Majestic is always.
- I used the django ORM to query the data and used the plotly library to visualise the data.
- The database is a postgres database hosted on my private server.
- I also added an upload feature that allows users to upload their own data and visualise it.
- Users can download a sample csv file to see the format of the data that can be uploaded.
- The application would not accept any other file format other than csv, or a csv file that does not have exactly 2 columns.
- The application is hosted on heroku and the domain is managed by cloudflare.

## Technologies used

- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Plotly](https://plotly.com/python/)
- [Heroku](https://www.heroku.com/)
- [Cloudflare](https://www.cloudflare.com/)

## Resources
- [Plotly](https://plotly.com/python/plot-data-from-csv/)

## Running the application locally

Assuming you have python installed on your machine and have setup the environment variables for the application, you can run the application locally using the following steps:
- Clone the repository
- Create or activate a virtual environment (optional).
- Install the requirements using the command `pip install -r requirements.txt`
- Setup database using the command `python manage.py makemigrations`
- Run the migrations using the command `python manage.py migrate`
- Load data into the database using the command `python manage.py load_drink` and `python manage.py load_sweet`
- Run the application using the command `python manage.py runserver`

## Usage
- Navigate to the homepage and click any of the visualise button to visualise the data.
- On the homepage, click on the upload button to upload your own data and visualise it.
- On the upload page, clic on the download button to download a sample csv file to for upload (optional).
