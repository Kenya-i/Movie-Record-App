from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError

class SearchForm(FlaskForm):
    title = StringField("映画名", validators=[DataRequired()])
    submit = SubmitField("検索")

