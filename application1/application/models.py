from application import db

class Prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False)
    prize = db.Column(db.String(500), nullable=False)
