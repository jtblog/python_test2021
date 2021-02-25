from flask import Flask, request
from flask_mongoengine import MongoEngine
#from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db' : 'db_name',
    'host' : 'localhost',
    'db' : '27017'
}
#app.config['MONGODB_SETTINGS'] = {
#    'host' : 'mongodb://localhost/db_name'
#}

db = MongoEngine()
db.init_app(app)


#class audio(db.Document):

#songs
# id
# Name of Song
# Duration in number of seconds
# Uploaded time

#podcast
# id
# Name of Song
# Duration in number of seconds
# Uploaded time
# host
# participants -optional - list of strings

#audiobook
# id
# title of audiobook
# author
# narrator
# Duration
# uploaded time

@app.route('/')
def index():
    return '<h1>Hello!</h1>'

#create audioFileType audioFileMetadata
#delete audioFileType/audioFileID
#update audioFileType/audioFileID
#get audioFileType/audioFileID
#get audioFileType

#200 Ok
#400 bad request
#500 internal server error

#app.config["MONGO_URI"]= ""
#mongo = PyMongo(app)
#client = pymongo.MongoClient("mongodb+srv://joetfx:<password>@cluster0.nxrlt.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
#db = client.test

#@app.route('/<name>')
#def index(name):
#    return '<h1>Hello {} !</h1>'.format(name)