from flask_security.forms import RegisterForm
from wtforms import StringField, validators, ValidationError
import re

from users.models import User


_PATTERN_TO_MATCH = "^[a-zA-Z0-9_-]{4,80}$"


class RegistrationForm(RegisterForm):
    name = StringField('name', validators=[validators.DataRequired(), validators.Length(min=3, max=80)])
    username = StringField('username', validators=[validators.DataRequired(), validators.Length(min=3, max=20)
                                                 ])

    def validate_username(form, field):

        if User.query.filter_by(username=field.data).first():
            raise ValidationError("Username already exists")

        if not re.match(_PATTERN_TO_MATCH, field.data):
            raise ValidationError("Invalid username")
