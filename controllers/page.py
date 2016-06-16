from imports import *
from flask.views import MethodView

class Home(MethodView):

  def get(self):
    title="Welcome home"
    return render_template('page/home.html',title=title)

class SecretPage(MethodView):

  @login_required
  def get(self):
    return render_template('page/secret_page.html')
