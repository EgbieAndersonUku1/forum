from flask_wtf import FlaskForm
from wtforms import StringField, validators


class NewThreadForm(FlaskForm):
    title = StringField('Thread title', validators=[validators.DataRequired(), validators.Length(min=10, max=80)])
    description = StringField('Thread description', validators=[validators.DataRequired(),
                                                                validators.Length(min=20, max=255)])




