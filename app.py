import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
from werkzeug.exceptions import HTTPException
from flask_migrate import Migrate

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    db = SQLAlchemy()
    migrate = Migrate(app, db)
  
    '''
    @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
    '''
    CORS(app, resources={'/': {'origins': '*'}})

    '''
    @TODO: Use the after_request decorator to set Access-Control-Allow
    
    '''
    # Define access control
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
        response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
        return response

    '''
    @TODO: 
    Create an endpoint to handle GET requests 
    for all available categories.
    '''
    # Query the quiz categories and return the info
    @app.route('/categories')
    def get_categories():
        categories = Category.query.order_by(Category.type).all()
        if len(categories) == 0:
            abort(404)
        return jsonify({
            'success': True,
            'categories': {category.id: category.type for category in categories}
        })


    '''
    @TODO: 
    Create an endpoint to handle GET requests for questions, 
    including pagination (every 10 questions). 
    This endpoint should return a list of questions, 
    number of total questions, current category, categories. 



    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions. 
    '''
    # Function to paginate the questions as per the QUESTIONS_PER_PAGE parameter above
    def paginate_questions(request, selection):
        page = request.args.get('page', 1, type=int)
        start = (page - 1) * QUESTIONS_PER_PAGE
        end = start + QUESTIONS_PER_PAGE

        questions = [question.format() for question in selection]
        current_questions = questions[start:end]

        return current_questions

    @app.route('/questions')
    def get_current_questions():

        questions=Question.query.order_by(Question.id).all()
        total_questions=len(questions)
        questions_selection=paginate_questions(request,questions)

        if len(questions_selection) == 0:
            abort(404)

        categories = Category.query.order_by(Category.type).all()

        return jsonify({
            'success': True,
            'questions':questions_selection,
            'total_questions':total_questions,
            'categories':{category.id: category.type for category in categories},
            'current_category':None
        })


    '''
    @TODO: 
    Create an endpoint to DELETE question using a question ID. 
    
    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page. 
    '''
    # Query the questions in database as per the input data of question id and delete it from database.
    @app.route('/questions/<question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            deleted=Question.query.get(question_id).delete()
            return jsonify({
            'success': True,
            'deleted': question_id
            })
        except:
            abort(422)

    '''
    @TODO: 
    Create an endpoint to POST a new question, 
    which will require the question and answer text, 
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab, 
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.  
    '''
    # Save the user entered question in the database along with other details and return success info
    @app.route('/questions',methods=['POST'])
    def save_question():    
        body = request.get_json()

        if not ('question' in body and 'answer' in body and 'difficulty' in body and 'category' in body):
            abort(422)

        question = body.get('question')
        answer = body.get('answer')
        difficulty = body.get('difficulty')
        category = body.get('category')

        try:
            question = Question(question=question, answer=answer,
                                difficulty=difficulty, category=category)
            question.insert()

            return jsonify({
                'success': True,
                'created': question.id,
            })

        except:
            abort(422)           


    '''
    @TODO: 
    Create a POST endpoint to get questions based on a search term. 
    It should return any questions for whom the search term 
    is a substring of the question. 

    TEST: Search by any phrase. The questions list will update to include 
    only question that include that string within their question. 
    Try using the word "title" to start. 
    '''
    # Search the database for questions having the input searchTerm and return the results
    @app.route('/questions/search',methods=['POST'])
    def search_question():
        body = request.get_json()
        search_term = body.get('searchTerm', None)

        if search_term:
            search_results = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()

            return jsonify({
                'success': True,
                'questions': [question.format() for question in search_results],
                'total_questions': len(search_results),
                'current_category': None
            })
        abort(404)

    
    '''
    @TODO: 
    Create a GET endpoint to get questions based on category. 

    TEST: In the "List" tab / main screen, clicking on one of the 
    categories in the left column will cause only questions of that 
    category to be shown. 
    '''
    # Query the database for questions in a particular category id received as input
    @app.route('/categories/<int:category_id>/questions', methods=['GET'])
    def get_questions(category_id):
        if not category_id:
            return abort(404, 'Invalid category id')
        questions = [question.format() for question in Question.query.filter(Question.category == category_id)]
        return jsonify({
            'success':True,
            'questions': questions,
            'total_questions': len(questions),
            'current_category': category_id
        })


    '''
    @TODO: 
    Create a POST endpoint to get questions to play the quiz. 
    This endpoint should take category and previous question parameters 
    and return a random questions within the given category, 
    if provided, and that is not one of the previous questions. 

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not. 
    '''
    # Search for quiz questions which have not been displayed earlier using random function and queries
    @app.route('/quizzes', methods=['POST'])
    def get_quiz_questions():
        try:

            body = request.get_json()

            if not ('quiz_category' in body and 'previous_questions' in body):
                abort(422)

            category = body.get('quiz_category')
            previous_questions = body.get('previous_questions')

            if category['type'] == 'click':
                unused_questions = Question.query.filter(Question.id.notin_((previous_questions))).all()
            else:
                unused_questions = Question.query.filter_by(category=category['id']).filter(Question.id.notin_((previous_questions))).all()

            new_question = unused_questions[random.randrange(0, len(unused_questions))].format() if len(unused_questions) > 0 else None

            return jsonify({
                'success': True,
                'question': new_question
            })
        except:
            abort(422)


    '''
    @TODO: 
    Create error handlers for all expected errors 
    including 404 and 422. 
    '''
    #Return error info 
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    #Return error info 
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    #Return error info 
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "bad request"
        }), 400

    #Return error info 
    @app.errorhandler(Exception)
    def exception_handler(error):
        return jsonify({
            'success': False,
            'error': 500,
            'message': f'Something went wrong: {error}'
        }), 500

    return app

    