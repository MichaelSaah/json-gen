from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    transactions = db.relationship('Transaction', backref='user',
                                lazy='dynamic')
    # api key

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.DateTime)
    request = db.Column(db.String(5000))
    cost = db.Column(db.Integer)
    # backref: user
