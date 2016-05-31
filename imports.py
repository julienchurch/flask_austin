from app import app, login_manager
from flask import request, render_template, redirect, url_for
from flask.ext.login import login_user, logout_user, current_user, login_required

