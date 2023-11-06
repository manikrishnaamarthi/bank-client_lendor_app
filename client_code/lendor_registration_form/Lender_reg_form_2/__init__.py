from ._anvil_designer import Lender_reg_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_form_2(Lender_reg_form_2Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  

  def button_1_click(self, **event_args):
    open_form('lendor_registration_form.Lender_reg_form_1')
    """This method is called when the button is clicked"""

  def button_2_click(self, **event_args):
    investment=self.drop_down_1.selected_value
    mobile = self.text_box_1.text
    email = self.text_box_2.text
    if not investment or not mobile or not email :
      Notification("Please fill all the fields").show()
    else:
     open_form('lendor_registration_form.Lender_reg_form_3')
    """This method is called when the button is clicked"""
    
    
