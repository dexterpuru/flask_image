from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db_path = 'postgresql://root:puru2000@localhost/image_db'
db = SQLAlchemy()


def setup_db(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    # db.create_all()  # Only use if this is first time running this app
    return db

#-----------------Models------------------#


class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.String(), nullable=False)
    image_hex = db.Column(db.LargeBinary, nullable=False)
    image_name = db.Column(db.String(), nullable=False)
    image_type = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return'<Image %r>' % self.image_name

    def __init__(self, image_url, image_hex, image_name, image_type, image_size):
        self.image_url = image_url
        self.image_hex = image_hex
        self.image_name = image_name
        self.image_type = image_type

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def info(self):
        return {
            'id': self.id,
            'image_url': self.image_url,
            'image_hex': self.image_hex.decode('utf-8'),
            'image_name': self.image_name,
            'image_type': self.image_type
        }
