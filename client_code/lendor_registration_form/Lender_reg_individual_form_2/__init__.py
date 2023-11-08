from ._anvil_designer import Lender_reg_individual_form_2Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_individual_form_2(Lender_reg_individual_form_2Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    company_add = self.text_box_1.text
    company_landmark = self.text_box_2.text
    business_no = self.text_box_3.text
    user_id = self.userId
    anvil.server.call('add_individual_second_form',company_add,company_landmark,business_no,user_id)
    
    open_form('lendor_registration_form.Lender_reg_individual_form_3',user_id = user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_individual_form_1',user_id=user_id)
    """This method is called when the button is clicked"""
    
