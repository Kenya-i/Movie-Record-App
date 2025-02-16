from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

class SignupForm(FlaskForm):
    username = StringField("名前", validators=[DataRequired()])
    email = StringField("メールアドレス", validators=[DataRequired(), Email("メールアドレスを設定してください")])
    password = PasswordField("パスワード", validators=[DataRequired(), EqualTo("password_confirm", message="パスワードが一致しません")])
    password_confirm = PasswordField("パスワード確認", validators=[DataRequired()])
    submit = SubmitField("登録")

class LoginForm(FlaskForm):
    email = StringField("メールアドレス", validators=[DataRequired(), Email("メールアドレスの形式が正しくありません")])
    password = PasswordField("パスワード", validators=[DataRequired()])
    submit = SubmitField("ログイン")