from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from . import record_bp
from app.src import db

@record_bp.route("/record", methods=["GET", "POST"])
@login_required
def record():
    if request.method == "GET":
        return render_template("record/record.html")
    #elif request.method == "POST" and form.validate_on_submit():
        #user = User.add_user(form.username.data, form.email.data, form.password.data)
        #if user:
        #    login_user(user, remember=True, duration=timedelta(seconds=600))
        #    flash("登録しました")
        #    return redirect(url_for('user.user'))
        #else:
        #    flash("メールアドレスがすでに存在しています")
        #    print(user)
        #    return render_template("user_account/signup.html", form=form)