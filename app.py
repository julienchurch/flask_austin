import config
from flask       import Flask, g, render_template
from flask_login import LoginManager, current_user

app = Flask(__name__.split('.')[0])
app.config.from_object('config')
login_manager = LoginManager()
login_manager.init_app(app)

import routes, controllers, models

@app.before_request
def before_request():
  g.config = config
  g.user   = current_user

@login_manager.user_loader
def load_user(id):
  return models.user.User(id)

# Just to show you what error handling looks like
@app.errorhandler(404)
def page_not_found(e):
  return render_template('error/404.html'), 404
