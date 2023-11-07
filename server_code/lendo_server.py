import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_lendor_frist_form(name,gender,city,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['full_name'] = name
    row[0]['gender'] = gender
    row[0]['city'] = city
    
@anvil.server.callable
def add_lendor_second_form(investment,mobile,email,photo,user_id):
  row = app_tables.user_profile.search(coustmer_id=user_id)
  if row:
    row[0]['investment'] = investment
    row[0]['mobile'] = mobile
    row[0]['email_user'] = email
    row[0]['user_photo'] = photo
  
