from ._anvil_designer import dashboardTemplate
from anvil import *
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users

class dashboard(dashboardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.user_form")

  def button_2_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("bank_users.main_form")

  def button_3_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("lendor_registration_form.dashboard.opbal")

  def button_4_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("")
    pass

  def outlined_button_8_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form("len")
