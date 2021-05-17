from flask import Flask, request
from flask_restful import Resource, Api, abort, reqparse
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

channels = {}
videos = {}

def abort_if_channel_does_not_exist(channel_id):
    if channel_id not in channels:
        abort(404, message="Channel does not exist")

def abort_if_video_does_not_exist(video_id):
    if video_id not in videos:
        abort(404, message="Video does not exist")

def abort_if_channel_exists(channel_id):
    if channel_id in channels:
        abort(409, message="A channel with this ID already exists")

def abort_if_video_exists(video_id):
    if video_id in videos:
        abort(409, message="A video with this ID already exists")

    
video_create_args = reqparse.RequestParser()
video_create_args.add_argument("name", type="str", help="Name of video")
video_create_args.add_argument("views", type="int", help="Number of views on video")
video_create_args.add_argument("likes", type="int", help="Number of likes on video")

class VideoModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    views = db.Column(db.Integer, nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Video(name={name}, views={views}, likes={likes}''


class Channel(Resource):
    def get(self, channel_id):
        abort_if_channel_does_not_exist(channel_id)
        return channels[channel_id]

class Video(Resource):
    def get(self, video_id):
        abort_if_video_does_not_exist(video_id)
        return videos[video_id]

    def put(self, video_id):
        abort_if_video_exists(video_id)
        args = video_create_args.parse_args()
        videos[video_id] = args
        return videos[video_id], 201


    def delete(self, video_id):
        abort_if_video_does_not_exist(video_id)
        del videos[video_id]
        return '', 204

api.add_resource(Channel, "/channel/<int:channel_id>")
api.add_resource(Video, "/video/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True)


