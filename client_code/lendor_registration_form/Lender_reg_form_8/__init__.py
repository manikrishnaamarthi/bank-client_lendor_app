from ._anvil_designer import Lender_reg_form_8Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_8(Lender_reg_form_8Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_7')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    lending_type = self.radio_button_1.selected
    investment = self.text_box_1.text
    lending_period = self.text_box_2.text
    user_id = self.userId
    anvil.server.call('add_lendor_eight_form',lending_type,lending_period,investment,user_id)
    if self.radio_button_1.selected:
      open_form('lendor_registration_form.Lender_reg_individual_form_1')
    elif self.radio_button_2.selected:
      open_form('lendor_registration_form.Lender_reg_Institutional_form_1')
    """This method is called when the button is clicked"""
    
    
