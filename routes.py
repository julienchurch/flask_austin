from imports import *
from controllers.auth import Login, Logout 
from controllers.page import Home, SecretPage


app.add_url_rule('/', view_func=Home.as_view('home'))
app.add_url_rule('/login', view_func=Login.as_view('login'))
app.add_url_rule('/logout', view_func=Logout.as_view('logout'))
app.add_url_rule('/secret_page', view_func=SecretPage.as_view('secret_page'))


