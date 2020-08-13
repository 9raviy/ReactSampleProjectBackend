# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 


## API DOCUMENTATION
# Getting Started
Base URL: Currently this application is only hosted locally. The backend is hosted at http://127.0.0.1:5000/
Authentication: This version does not require authentication or API keys.

# API Endpoints

ENDPOINT: GET /categories
OBJECTIVE: Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category.
ARGUMENTS: None
RETURNS: List of available categories.
SAMPLE: curl http://127.0.0.1:5000/categories

SAMPLE RESPONSE:  

 "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
}

ENDPOINT: GET /questions
OBJECTIVE: Returns a list of questions paginated.
ARGUMENTS: None
RETURNS:A list of questions, categories and total number of questions.
SAMPLE: curl http://127.0.0.1:5000/categories

SAMPLE RESPONSE:  

  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 19
}

ENDPOINT: GET /categories/<int:category_id>/questions
OBJECTIVE: To get questions based on category
ARGUMENTS: Category Id
RETURNS:List of questions, number of total questions, current category and categories.
SAMPLE: curl http://127.0.0.1:5000/categories/2/questions

SAMPLE RESPONSE:  

  "current_category": 2,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}

ENDPOINT: DELETE /questions/<question_id>
OBJECTIVE: Delete question from the list.
ARGUMENTS: Question id
RETURNS:  Question id of deleted question and True if deletion successful.
SAMPLE: curl http://127.0.0.1:5000/questions/4 -X DELETE

SAMPLE RESPONSE:  
{
   "deleted": "4",
  "success": true
}


ENDPOINT: POST /questions
OBJECTIVE: Stores the user entered question in the database.
ARGUMENTS: Question, Answer, Difficulty level and Category.
RETURNS: True if successfully added along with question id.
SAMPLE: curl  http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d ' { "question": "What is the capital of India?", "answer": "Delhi", "difficulty": 3, "category": "3" }'

SAMPLE RESPONSE:  
{
  "created": 26,
  "success": true
}


ENDPOINT: POST /questions/search
OBJECTIVE: Searches for the questions by the search term
ARGUMENTS: search term
RETURNS:List of questions, number of total questions and current category and related data.
SAMPLE: curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm": "Tom"}'

SAMPLE RESPONSE:  

 { "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }
  ],
  "success": true,
  "total_questions": 1
}


ENDPOINT: GET /categories/<int:category_id>/questions
OBJECTIVE: To get questions based on category.
ARGUMENTS: Category id
RETURNS: List of questions, number of total questions, current category and categories.
SAMPLE: curl http://127.0.0.1:5000/categories/2/questions

SAMPLE RESPONSE:  
{
  "current_category": 2,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}


ENDPOINT: POST /quizzes
OBJECTIVE: Allows users to play the quiz game by fetching the selected quiz by category
ARGUMENTS: Quiz category and previous questions
RETURNS: Random questions within the given category.
SAMPLE: curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [6, 7], "quiz_category": {"type": "Science", "id": "1"}}'

SAMPLE RESPONSE:  
{
  "question": {
    "answer": "The Liver",
    "category": 1,
    "difficulty": 4,
    "id": 20,
    "question": "What is the heaviest organ in the human body?"
  },
  "success": true
}


# Error Handling
Errors are returned as JSON in the following format:
```
{
    "success": False,
    "error": 404,
    "message": "resource not found"
}
```

The API will return four types of errors:
400 – bad request
404 – resource not found
422 – unprocessable
500 - Something went wrong:500



## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
## Author info
Ravi authored the API (__init__.py), test suite (test_flaskr.py), and this README.
All other project files, including the models and frontend, were created by Udacity as a project template for the Full Stack Web Developer Nanodegree.