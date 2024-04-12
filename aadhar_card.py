# Copyright (c) 2024, bhumika and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document
# class Aadharcard(Document):
#     pass
# class Aadharcard(Document):
#     def validate(self):
#         if self.aadhar_card and not self.aadhar_card.startswith("$AES$:"):
#             self.aadhar_card = frappe.utils.password.encrypt(self.aadhar_card)
# def setup():
#     Aadharcard.validate = validate_aadhar
# def validate_aadhar(self):
#     if self.aadhar_card and not self.aadhar_card.startswith("$AES$:"):
#         self.aadhar_card = frappe.utils.password.encrypt(self.aadhar_card)
# setup()


# import frappe
# from frappe.model.document import Document

# class Aadharcard(Document):
#     def validate(self):
#         if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
#             self.aadhar_card = frappe.utils.password.encrypt(self.aadhar_card)

# def setup():
#     Aadharcard.validate = validate_aadhar

# def validate_aadhar(self):
#     if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
#         self.aadhar_card = frappe.utils.password.encrypt(self.aadhar_card)

# setup()


# import frappe
# from frappe.model.document import Document
# import base64

# class Aadharcard(Document):
#     def validate(self):
#         if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
#             self.aadhar_card = base64.b64encode(self.aadhar_card.encode())

# def setup():
#     Aadharcard.validate = validate_aadhar

# def validate_aadhar(self):
#     if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
#         self.aadhar_card = base64.b64encode(self.aadhar_card.encode())

# setup()

# import frappe
# from frappe.model.document import Document
# import base64

# class Aadharcard(Document):
#     def validate(self):
#         if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
#             self.aadhar_card = base64.b64encode(self.aadhar_card.encode()).decode()

# def setup():
#     Aadharcard.validate = validate_aadhar

# def validate_aadhar(self):
#     if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
#         self.aadhar_card = base64.b64encode(self.aadhar_card.encode()).decode()

# setup()

import frappe
from frappe.model.document import Document
import base64

class Aadharcard(Document):
    def validate(self):
        if self.aadhar_card and not self.aadhar_card.startswith("#ENC#"):
            self.encrypt_aadhar()

    def encrypt_aadhar(self):
        self.aadhar_card = "#ENC#" + base64.b64encode(self.aadhar_card.encode()).decode()

def setup():
    pass

setup()













