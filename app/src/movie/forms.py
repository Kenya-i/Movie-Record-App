from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, HiddenField, TextAreaField, DateField
from wtforms.validators import DataRequired, Email, EqualTo
from .models import User

class MovieForm(FlaskForm):
    title = HiddenField("タイトル")
    overview = HiddenField("あらすじ")
    comment = TextAreaField('コメント：', validators=[DataRequired()])
    date = DateField('鑑賞日付:', validators=[DataRequired()])
    poster_path = HiddenField("", validators=[DataRequired()])
    submit = SubmitField("登録")

#class ForgotPasswordForm(FlaskForm):
#    email = StringField("メール", validators=[DataRequired(), Email()])
#    submit = SubmitField("パスワードを再設定する")

#    def validate_email(self, field):
#        if not User.select_by_email(field.data):
#            raise ValidationError("そのメールアドレスは存在しません")