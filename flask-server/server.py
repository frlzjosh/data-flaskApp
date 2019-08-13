# import the nessecary pieces from Flask
from flask import Flask,render_template, request,jsonify,Response
from flask_cors import CORS
import read_data as rd
import json
#Create the app object that will route our calls
app = Flask(__name__)
app.config.from_object(__name__)

#enable cors
CORS(app, resources={r'/*': {'origins': '*'}})


# VARIABLES
BOOKS = [
    {
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')
    
@app.route('/first-dataset', methods=['GET'])
def first_dataset():
    return rd.SimpleDF

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)

#When run from command line, start the server
if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 3030, debug = True)