from flask import Flask, request, response, jsonify
from flask_mongoengine import MongoEngine
import datetime
#from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db' : 'db_name',
    'host' : 'localhost',
    'db' : '27017'
}
#app.config['MONGODB_SETTINGS'] = {
#    'host' : 'mongodb://localhost/audio'
#}

db = MongoEngine()
db.init_app(app)

class cDateTimeField(db.DateTimeField):
    def validate(self, value):
        super(cDateTimeField, self).validate(value)
        #if(value < datetime.datetime.utcnow):
        #    self.error('DateTime cannot be in the past')

class Song(db.EmbeddedDocument):
    id = db.IntField(required = True, unique = True)
    name = db.StringField(required = True, max_length = 100)
    duration = db.IntField(required = True, min_value = 1)
    #upload_time = cDateTimeField(required = True, default = datetime.datetime.utcnow)

class Podcast(db.EmbeddedDocument):
    id = db.IntField(required = True, unique = True)
    name = db.StringField(required = True, max_length = 100)
    duration = db.IntField(required = True, min_value = 1)
    #upload_time = cDateTimeField(required = True, default = datetime.datetime.utcnow)
    host = db.StringField(required = True, max_length = 100)
    participant = db.ListField(db.StringField(max_length = 100), default = [])

class Audiobook(db.EmbeddedDocument):
    id = db.IntField(required = True, unique = True)
    name = db.StringField(required = True, max_length = 100)
    duration = db.IntField(required = True, min_value = 1)
    #upload_time = cDateTimeField(required = True, default = datetime.datetime.utcnow)
    author = db.StringField(required = True, max_length = 100)
    narrator = db.StringField(required = True, max_length = 100)

#class metaData(db.DynamicEmbeddedDocument):
#    pass

class Audio(db.Document):
    fileType = db.StringField(required = True, max_length = 100)
    #metadata = db.EmbeddedDocumentField(???)

def sortedAudio(mdata):
    if('host' in mdata or 'participant' in mdata):
        return Podcast(mdata)
    elif('author' in mdata or 'narrator' in mdata):
        return Audiobook(mdata)
    else:
        return Song(mdata)

@app.route('/')
def index():
    return '<h1>Hello!</h1>' + datetime.datetime.utcnow

@app.route('/api/create', method =['POST'])
def create():
    body = request.json
    ft = None
    fmd = None
    if('audioFileType' not in body or 'audioFileMetadata' not in body):
        return response("Bad Request", status = 400)
    else:
        ft = body['audioFileType']
        fmd = body['audioFileMetadata']
        dt = sortedAudio(fmd)
        audio = Audio( audioFileType = ft, audioFileMetadata = dt).save()
        return jsonify(audio), 200

@app.route('/api/delete/<audioFileType>/<audioFileID>', method =['DELETE'])
def delete(audioFileType, audioFileID):
    audio = Audio.objects.get_or_404(audioFileMetadata__id = audioFileID)
    audio.delete()
    return jsonify(str(audioFileID)), 200

@app.route('/api/update/<audioFileType>/<audioFileID>', method =['PUT'])
def update(audioFileType, audioFileID):
    body = request.json
    ft = None
    fmd = None

    if('audioFileType' not in body or 'audioFileMetadata' not in body):
        return response("Bad Request", status = 400)
    else:
        fmd = body['audioFileMetadata']

        audio = Audio.objects.get_or_404(audioFileMetadata__id = audioFileID)
        ft = audio.audioFileType
        dt = sortedAudio(fmd)
        audio.update(audioFileType = ft, audioFileMetadata = dt)
        return jsonify(audio), 200
    
@app.route('/api/get/<audioFileType>', method =['GET'])
def get(audioFileType):
    audio = Audio.objects.get_or_404(audioFileType = audioFileType)
    return audio.to_dict(), 200

@app.route('/api/get/<audioFileType>/<audioFileID>', method =['GET'])
def _get(audioFileType, audioFileID):
    audio = Audio.objects.get_or_404(audioFileMetadata__id = audioFileID)
    return jsonify(audio), 200

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