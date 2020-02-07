from datetime import datetime

from create_app import db
from reply.model import Reply # import reply is needed because it calls the Reply model in line 13


class Thread(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    created_by = db.Column(db.String(80))
    date_created = db.Column(db.DateTime(), default=datetime.utcnow)
    replies = db.relationship("Reply", backref='thread', lazy='dynamic')
