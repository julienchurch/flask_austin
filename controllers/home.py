from imports import *
from flask.views import MethodView

class Home(MethodView):

  def get(self):
    title="Welcome home"
    return render_template('page/home.html',title=title)
