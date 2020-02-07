from flask_wtf import FlaskForm
from wtforms import StringField, validators

from wtforms.widgets import TextArea


class ReplyForm(FlaskForm):
    message = StringField("Reply", widget=TextArea(), validators=[validators.DataRequired()])