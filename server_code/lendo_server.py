import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_lendor_frist_form(name,gender,city,user_id):
  app_tables.user_profile.add_row(name=name,gender=gender,city=city, coustmer_id=user_id )
