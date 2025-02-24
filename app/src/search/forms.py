from flask_wtf import FlaskForm
from wtforms.fields import StringField, SubmitField
from wtforms.validators import DataRequired

class SearchForm(FlaskForm):
    title = StringField("映画名", validators=[DataRequired()])
    submit = SubmitField("検索")

