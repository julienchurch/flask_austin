from mock_db import user_credentials as creds 
from passlib.apps import custom_app_context as ctx

class User(object):

  def __init__(self, id):
    self.id              = id
    self.email           = creds[id]['email']
    self.hashed_password = creds[id]['password']

  def verify_password(self, cleartext):
    return ctx.verify(cleartext, self.hashed_password)

  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return false

  def get_id(self):
    return self.id

  def __repr__(self):
    return 'Hi. My name is {0}'.format(self.name)

def query_user(email):
  for uid, cred in creds.items():
    if cred.get('email', '') == email:
      return User(uid)
  return None

