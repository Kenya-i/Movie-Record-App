from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, HiddenField, TextAreaField, DateField
from wtforms.validators import DataRequired

class MovieForm(FlaskForm):
    title = HiddenField("タイトル")
    overview = HiddenField("あらすじ")
    comment = TextAreaField('コメント：', validators=[DataRequired()])
    date = DateField('鑑賞日付:', validators=[DataRequired()])
    poster_path = HiddenField("", validators=[DataRequired()])
    submit = SubmitField("登録")