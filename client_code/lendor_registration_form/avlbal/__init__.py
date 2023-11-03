from ._anvil_designer import avlbalTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class avlbal(avlbalTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

      
        #self.repeating_panel_1.items = app_tables.view_bor_loan_requests.search(self.user_id)

        # Define the user ID for the specific user you want to retrieve the available balance for
        self.user_id = '9502'

        # Fetch the data for the specific user from your table
        user_request = app_tables.view_bor_loan_requests.get(user_id=self.user_id)

        if user_request:
            initial_commitment = user_request['initial_commitment']
            top_up = user_request['top_up']
            total_loan_disbursed = user_request['total_loan_disbursed']
            available_balance = int(initial_commitment) + int(top_up) - int(total_loan_disbursed)
            self.output_lbl.text = f" {available_balance}"
        else:
            self.label1.text = f"User {self.user_id} not found or data not available."
        user_requests = app_tables.view_bor_loan_requests.search(user_id=self.user_id)
        self.repeating_panel_1.items = user_requests
