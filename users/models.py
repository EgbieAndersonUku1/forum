from datetime import datetime
from flask_security import RoleMixin, UserMixin

from create_app import db


roles_users = db.Table('roles_user',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))

)


class Role(db.Model, RoleMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(250))


class User(db.Model, UserMixin):
    """The user model database"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    username = db.Column(db.String(255), unique=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime(), default=datetime.utcnow)
    roles = db.relationship("Role", secondary=roles_users, backref=db.backref('users', lazy='dynamic'))
    replies = db.relationship("Reply", backref="user", lazy="dynamic")

