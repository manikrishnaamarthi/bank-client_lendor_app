from ._anvil_designer import Lender_reg_Institutional_form_1Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_Institutional_form_1(Lender_reg_Institutional_form_1Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    business_name = self.text_box_1.text
    business_loc = self.text_box_2.text
    business_add = self.text_box_3.text
    branch_name = self.text_box_4.text
    user_id = self.userId
    if not business_name or not business_loc or not business_add or not branch_name:
      Notification("Please fill all the fields")
    else:
     anvil.server.call('add_institutional_bank_first_form',business_name,business_loc,business_add,branch_name,user_id)
     open_form('lendor_registration_form.Lender_reg_Institutional_form_2',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_form_8',user_id=user_id)
    """This method is called when the button is clicked"""
    
