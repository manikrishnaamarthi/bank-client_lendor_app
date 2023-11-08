from ._anvil_designer import Lender_reg_individual_form_3Template
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Lender_reg_individual_form_3(Lender_reg_individual_form_3Template):
  def __init__(self,user_id, **properties):
    self.userId = user_id
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_2_click(self, **event_args):
    annual_salary = self.text_box_1.text
    designation = self.text_box_2.text
    empolyee_id = self.file_loader_1.file
    bank_sts = self.file_loader_2.file
    user_id = self.userId
    if not annual_salary or not designation or not empolyee_id or not bank_sts:
      Notification("Please all the fields")
    else:
     anvil.server.call('add_individual_third_form',annual_salary,designation,empolyee_id,bank_sts,user_id)
  
     open_form('lendor_registration_form.Lender_reg_individual_bank_form_1',user_id=user_id)
    """This method is called when the button is clicked"""

  def button_1_click(self, **event_args):
    user_id = self.userId
    open_form('lendor_registration_form.Lender_reg_individual_form_2',user_id=user_id)
    """This method is called when the button is clicked"""
    
