from ._anvil_designer import rtaTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class rta(rtaTemplate):
  def __init__(self,user_id, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.user_Id = user_id
    #self.user_id = '4891'
    
    
    #initial_commitment = user_request['initial_commitment']
    #self.output_lbl.text = f" {initial_commitment}"

    # Any code you write here will run before the form opens.
  def button_2_click(self, **event_args):
     user_request = app_tables.view_bor_loan_requests.get(customer_id=self.user_id)
     
     if user_request:
      
      initial_commitment = user_request['initial_commitment']
      total_rta = self.tp_tb.text
      user_request = app_tables.view_bor_loan_requests.get(initial_commitment = initial_commitment)
      fin_rta = int(initial_commitment) + int(total_rta)
      user_id = self.user_Idd
      Notification("Topup added successfully").show()

    # Call the server function with the correct name and parameter
     anvil.server.call('view_bor_loan_requests', fin_rta,user_id)
   

   

            

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.avlbal")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vblr")

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.ld")

  def link_4_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def link_5_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.td")

  def link_6_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vcl")

  def link_7_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def link_8_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def link_9_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def link_10_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def link_11_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def link_12_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def link_13_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("lendor_registration_form.dashboard.cp")

  
