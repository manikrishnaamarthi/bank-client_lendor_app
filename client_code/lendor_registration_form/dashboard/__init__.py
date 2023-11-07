from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.





  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.avlbal")

  def button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vblr")

  def button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.ld")

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.td")

  def outlined_button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlo")

  def outlined_button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vcl")

  def outlined_button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vler")

  def outlined_button_5_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vlfr")

  def outlined_button_6_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.rta")

  def outlined_button_7_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vdp")

  def outlined_button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vep")

  def outlined_button_9_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.vsn")

  def outlined_button_10_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.cp")

  def link_1_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("bank_users.user_form")

  def link_2_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form("bank_users.main_form")

  def radio_button_1_clicked(self, **event_args):
    """This method is called when this radio button is selected"""
    if self.radio_button.enabled:
      alert("online")
      
    

  