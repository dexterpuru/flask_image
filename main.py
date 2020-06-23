from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from helper import download_image, get_hex, get_img
from db import setup_db, Images
import json

app = Flask(__name__)
db = setup_db(app)


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to Flask API'


@app.route('/add_image', methods=['POST'])
def add_image():
    if request.data:
        data = json.loads(request.data.decode('utf-8'))
        if data['url'] and data['name'] and data['type']:
            image_loc = download_image(data['url'], data['name'], data['type'])
            image_hex = get_hex(image_loc)

            new_image = Images(
                image_url=data['url'],
                image_hex=image_hex,
                image_name=data['name'],
                image_type=data['type']
            )

            Images.insert(new_image)
            return jsonify({
                'success': True,
                'added': new_image.info()
            })
        abort(404)
    abort(422)


@app.route('/searchbyid/<id>', methods=['GET'])
def getById(id):
    img = Images.query.get(id)
    if img:
        return img.info()
    abort(404)


@app.route('/searchbyname/<name>', methods=['GET'])
def getByName(name):
    img = Images.query.filter_by(image_name=name).one_or_none()
    if img:
        return img.info()
    abort(404)


@app.route('/downloadbyid/<id>', methods=['GET'])
def downloadById(id):
    img = Images.query.get(id)
    if img:
        img = img.info()
        get_img(img['image_hex'], img['image_name'],
                img['image_type'].split('/')[1])
        return 'Downloaded in images folder'
    abort(404)


@app.route('/downloadbyname/<name>', methods=['GET'])
def downloadByName(name):
    img = Images.query.filter_by(image_name=name).one_or_none()
    if img:
        img = img.info()
        get_img(img['image_hex'], img['image_name'],
                img['image_type'].split('/')[1])
        return 'Downloaded in images folder'
    abort(404)


if __name__ == '__main__':
    app.run(debug=True)
