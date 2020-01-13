from flask import Flask, jsonify
from flask_restful import Resource, Api
from igql import InstagramGraphQL


app = Flask(__name__)
api = Api(app)

class Index(Resource):
    def get(self):
        return {'Instructions': 'Collect media from instagram. Endpoints: /string:hashtag, /string:hashtag/int:count'}


class Hashtag(Resource):
    def get(self, hashtag):
        session = InstagramGraphQL()
        htag = session.get_hashtag(hashtag)
        for media in htag.recent_media():
            return jsonify(media)


class HashtagCount(Resource):
    def get(self, hashtag, count):
        session = InstagramGraphQL()
        htag = session.get_hashtag(hashtag)
        media_collection = []
        for media in htag.recent_media():
            if len(media_collection) > count:
                return jsonify(media_collection)
            media_collection.extend(media)

api.add_resource(Index, '/')
api.add_resource(Hashtag, '/<string:hashtag>')
api.add_resource(HashtagCount, '/<string:hashtag>/<int:count>')


if __name__ == '__main__':
    app.run(debug=True)