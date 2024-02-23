from flask import *
import json, time, urllib.parse
from flask_cors import CORS, cross_origin
from api import *


app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/', methods=['GET'])
@cross_origin()
def home_page():
    objected = {"page": "Page is succesfully loaded", "time": time.time()}
    
    return objected

@app.route('/artist')
@cross_origin()
def request_artist():
    search_query = str(request.args.get('name'))

    return artist(search_query)


if __name__ == '__main__':
    app.run(port=4040)