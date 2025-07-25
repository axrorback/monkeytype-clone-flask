from . import db
from datetime import datetime

class TypingTest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    wpm = db.Column(db.Integer)
    accuracy = db.Column(db.Float)
    time_taken = db.Column(db.Integer)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
