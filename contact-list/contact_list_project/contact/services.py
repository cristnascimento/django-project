from .mock_data import Contact, mock_contacts, nextId
import copy 

class ContactService:

  def __init__(self):
    self.contacts = mock_contacts
    self.nextId = nextId

  def getContacts(self):
    return copy.deepcopy(self.contacts)

  def getContact(self, id):
    return next(contact for contact in self.contacts if contact.id == id).copy()

  def createContact(self, contact):
    contact.id = self.nextId
    self.nextId += 1
    self.contacts.append(contact)

  def updateContact(self, contact):
    index = next(i for i, contactOld in enumerate(self.contacts) if contactOld.id == contact.id)
    self.contacts[index] = contact

  def deleteContact(self, id):
    index = next(i for i, contact in enumerate(self.contacts) if contact.id == id)
    contact = self.contacts.pop(index)