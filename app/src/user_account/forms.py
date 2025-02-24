from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField, FileField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from .models import User

class SignupForm(FlaskForm):
    username = StringField("名前", validators=[DataRequired()])
    email = StringField("メールアドレス", validators=[DataRequired(), Email("メールアドレスの形式が正しくありません")])
    password = PasswordField("パスワード", validators=[DataRequired(), EqualTo("password_confirm", message="パスワードが一致しません")])
    password_confirm = PasswordField("パスワード確認", validators=[DataRequired()])
    submit = SubmitField("登録")

class LoginForm(FlaskForm):
    email = StringField("メールアドレス", validators=[DataRequired(), Email("メールアドレスの形式が正しくありません")])
    password = PasswordField("パスワード", validators=[DataRequired()])
    submit = SubmitField("ログイン")


class UserForm(FlaskForm):
    username = StringField("名前", validators=[DataRequired()])
    email = StringField("メール", validators=[DataRequired(), Email("メールアドレスの形式が正しくありません")])
    password = PasswordField("パスワード", validators=[DataRequired(), EqualTo("password_confirm", message="パスワードが一致しません")])
    password_confirm = PasswordField("パスワード確認", validators=[DataRequired()])
    submit = SubmitField("更新")

#class ForgotPasswordForm(FlaskForm):
#    email = StringField("メール", validators=[DataRequired(), Email()])
#    submit = SubmitField("パスワードを再設定する")

#    def validate_email(self, field):
#        if not User.select_by_email(field.data):
#            raise ValidationError("そのメールアドレスは存在しません")