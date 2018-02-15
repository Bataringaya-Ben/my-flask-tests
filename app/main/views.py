from flask import render_template
from flask import redirect
from flask import url_for
from ..models import User
from .forms import NameForm
from . import main
from .. import db
from datetime import datetime
from flask_login import login_required


@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    current_time = datetime.utcnow()
    if form.validate_on_submit():
        if form.name.data != '':
            user = User(
                username=form.name.data,
                password=form.password.data,
                email=form.email.data)
            db.session.add(user)
            form.name.data = ''
            form.password.data = ''
            form.email.data = ''
            return redirect(url_for('.view_users'))
        else:
            return redirect(url_for('.index'))
    form.name.data = ''
    form.password.data = ''
    form.email.data = ''
    return render_template('index.html', form=form, current_time=current_time)


@main.route('/users')
def view_users():
    users = User.query.all()
    return render_template('users.html', users=users)


@main.route('/secret')
@login_required
def secret():
    return 'only authorized users have access'
