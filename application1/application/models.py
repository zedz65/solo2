from application import db

class prize(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), nullable=False)
    prize = db.Column(db.String(5), nullable=False)
