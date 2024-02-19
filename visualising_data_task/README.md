# Majestic Quiz (Test C - Visualising Data)

## By: Ighomena Odebala

### Task
Create a visualisation of each set of fictitious data.

#### Approach
- I used matplotlib library to visualise the data.
- The program uses three python files: `main.py`, `visualisation.py` and `data.py`.
- The `data.py` file contains the data for the visualisation.
- The `visualisation.py` file contains the class that takes in the data, labels and title as parameters.
- The `main.py` file contains the main program that runs the visualisation.

#### Resources
- [Matplotlib](https://matplotlib.org/stable/tutorials/lifecycle.html#sphx-glr-tutorials-lifecycle-py)

## Language and Libraries Used
- [Python](https://www.python.org/)
- [Matplotlib](https://matplotlib.org/)

## Installation
- Run `pip install -r requirements.txt` to install the required libraries

## Usage
1. Run `python main.py` to start the program.
2. The program would ask which data you want to visualise i.e 1 for sweet data, 2 for drink data.
3. Enter the number of the data you want to visualise and press enter.
4. The visualisation of the data would be displayed.
5. Close the visualisation to see the next visualisation.
6. Repeat steps 3 and 4 to see the visualisation of the other data

## More on visualising data task:
I created a django web application for the visualising data task. The code for the Django web application can be found in the  [django-visualisation](https://github.com/dhee-tree/majesticQuiz/tree/django-visualisation) branch of this repository.

It is deployed on Heroku and can be accessed [here](https://vis.ighomena.me/)