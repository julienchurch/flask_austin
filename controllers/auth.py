from imports import *
from flask.views import MethodView
from models.user import User, query_user
from flask.ext.login import login_user, \
                            logout_user, \
                            current_user, \
                            login_required

def load_user(email):
  return query_user(email)

class Login(MethodView):

  def get(self):
    title = 'Log in.'
    return render_template('auth/login.html',title=title)

  def post(self):
    email    = request.form.get('email', '')
    password = request.form.get('password', '')
    user     = query_user(email) 
    if user:
      if user.verify_password(password):
        login_user(user)
        return redirect(url_for('home')) 
      else:
        return 'Bad password'
    return 'That user doesn\'t exist.'


class Logout(MethodView):

  def get(self):
    logout_user()
    return redirect(url_for('home'))

  def post(self):
    pass
