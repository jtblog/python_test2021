from flask import Flask, request, Response, jsonify
from flask_mongoengine import MongoEngine
import datetime
import json
#from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'db' : 'audio',
    'host' : 'localhost',
    'port' : 27017
}
#app.config['MONGODB_SETTINGS'] = {
#    'host' : 'mongodb://localhost/audio'
#}

db = MongoEngine()
db.init_app(app)

class cDateTimeField(db.DateTimeField):
    def validate(self, value):
        super(cDateTimeField, self).validate(value)
        if(value < datetime.datetime.utcnow()):
            self.error('DateTime cannot be in the past')

class audioMetaData(db.DynamicEmbeddedDocument):
    id = db.IntField(required = True, unique = True)
    name = db.StringField(required = True, max_length = 100)
    duration = db.IntField(required = True, min_value = 1)
    upload_time = cDateTimeField(required = True, default = datetime.datetime.utcnow())
    participants = db.ListField(db.StringField(max_length = 100) default = [])
        
class Audio(db.DynamicDocument):
    audioFileType = db.StringField(required = True, max_length = 100)
    audioFileMetadata = db.DynamicField(audioMetaData)

'''
@app.route('/')
def index():
    return '<h1>Hello! It is {}</h1>'.format(datetime.datetime.utcnow())
'''

def _ctask1(args1, args2):
    args2.save()
    if('host' not in args1):
        args2.update(unset__audioFileMetadata__participants=1)
    pass

def _ctask2(args1, args2, args3, args4):
    args4.update(audioFileType = args1, audioFileMetadata = args3)
    if('host' not in args2):
        args4.update(unset__audioFileMetadata__participants=1)
    pass

def _ctask(args1, args2):
    return args2, 200

def _metadatachk(value):
    if('host' in value):
        if not bool(value['host'].strip()):
            return jsonify({"message": "Host cannot be empty", "code": "host_value_empty"}), 400
        if(len(value['host']) > 100):
            return jsonify({"message": "Host cannot be larger than 100 characters", "code": "host_value_greater_than_100"}), 400
    pass
    if('author' in value or 'narrator' in value):
        if not bool(value['author'].strip()):
            return jsonify({"message": "Author cannot be empty", "code": "author_value_empty"}), 400
        if(len(value['author']) > 100):
            return jsonify({"message": "Author cannot be larger than 100 characters", "code": "author_value_greater_than_100"}), 400
        if not bool(value['narrator'].strip()):
            return jsonify({"message": "Narrator cannot be empty", "code": "narrator_value_empty"}), 400
        if(len(value['narrator']) > 100):
            return jsonify({"message": "Narrator cannot be larger than 100 characters", "code": "narrator_value_greater_than_100"}), 400
    pass


@app.route('/api/create', methods = ['POST'])
def create():
    body = request.get_json(force=True)
    ft = None
    fmd = None
    if('audioFileType' not in body or 'audioFileMetadata' not in body):
        if('audioFileType' not in body):
            return jsonify({"message": "Audio Filetype is required", "code": "audioFileType_missing"}), 400
        else:
            return jsonify({"message": "Audio Metadata is required", "code": "audioFileMetadata_missing"}), 400
    else:
        ft = body['audioFileType']
        fmd = body['audioFileMetadata']

        _audiometadata = audioMetaData(**fmd)
        chk = None
        chk = _metadatachk(fmd)
        
        audio = Audio( audioFileType = ft)
        audio.audioFileMetadata = _audiometadata

        return chk if chk!= None else _ctask(_ctask1(fmd, audio), jsonify(str(ft)))

@app.route('/api/delete/<audioFileType>/<audioFileID>', methods =['DELETE'])
def delete(audioFileType, audioFileID):
    audio = Audio.objects.filter(audioFileMetadata__id = audioFileID).first()
    audio.delete()
    return jsonify(str(audioFileID)), 200

@app.route('/api/update/<audioFileType>/<audioFileID>', methods =['PUT'])
def update(audioFileType, audioFileID):
    body = request.get_json(force=True)
    ft = None
    fmd = None

    if('audioFileType' not in body or 'audioFileMetadata' not in body):
        if('audioFileType' not in body):
            return jsonify({"message": "Audio Filetype is required", "code": "audioFileType_missing"}), 400
        else:
            return jsonify({"message": "Audio Metadata is required", "code": "audioFileMetadata_missing"}), 400
    else:
        fmd = body['audioFileMetadata']

        audio = Audio.objects.filter(audioFileMetadata__id = audioFileID).first()
        ft = audio.audioFileType
        _audiometadata = audioMetaData(**fmd)
        chk = None
        chk = _metadatachk(fmd)
        return chk if chk! = None else _ctask(_ctask2(ft, fmd, _audiometadata, audio), jsonify(audio))
    
@app.route('/api/get/<audioFileType>', methods =['GET'])
def get(audioFileType):
    audio = Audio.objects.filter(audioFileType = audioFileType)
    return jsonify(audio), 200

@app.route('/api/get/<audioFileType>/<audioFileID>', methods =['GET'])
def _get(audioFileType, audioFileID):
    audio = Audio.objects.filter(audioFileMetadata__id = audioFileID).first()
    return jsonify(audio), 200
