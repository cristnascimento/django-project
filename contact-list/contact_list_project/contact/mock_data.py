import copy

class Contact:

  def __init__(self):
    self.id = 0
    self.firstName = ""
    self.lastName = ""
    self.email = ""
    self.phone = ""
    self.phoneCategory = "" 
    self.address = ""
    self.city = ""
    self.state = ""
    self.zip = ""
    self.closeFriend = ""

  def setFromForm(self, request):
    self.firstName = request.POST['firstName']
    self.lastName = request.POST['lastName']
    self.email = request.POST['email']
    self.phone = request.POST['phone']
    self.phoneCategory = request.POST['phoneCategory']
    self.address = request.POST['address']
    self.city = request.POST['city']
    self.state = request.POST['state']
    self.zip = request.POST['zip']
    self.closeFriend = request.POST['closeFriend'] if 'closeFriend' in request.POST else ""

  def copy(self):
    return copy.copy(self)

  def __repr__(self):
    return "Contact=[id: {0}, firstName: {1}]".format(self.id, self.firstName)

  def __str__(self):
    return "Contact=[id: {1}, firstName: {1}]".format(self.id, self.firstName)

mock_contacts = []

zapata = Contact()
zapata.id = 1
zapata.firstName = "Natasha"
zapata.lastName = "Zapata"
zapata.email = "zapata@blindspot.com"
zapata.phone = "+1 728 68768778"
zapata.phoneCategory = "Home"
zapata.address = "876 5th Av"
zapata.city = "New York"
zapata.state = "SP"
zapata.zip = "1323543"
zapata.closeFriend = "on"
mock_contacts.append(zapata)

reade = Contact()
reade.id = 2
reade.firstName = "Edgar"
reade.lastName = "Reade"
reade.email = "reade@blindspot.com"
reade.phone = "+1 102 8767878"
reade.phoneCategory = "Work"
reade.address = "156 Golden St"
reade.city = "New York"
reade.state = "RN"
reade.zip = "3452352"
reade.closeFriend = ""
mock_contacts.append(reade)

paty = Contact()
paty.id = 3
paty.firstName = "William"
paty.lastName = "Patterson"
paty.email = "patterson@blindspot.com"
paty.phone = "+1 304 9808151"
paty.phoneCategory = "Mobile"
paty.address = "74 Rich St"
paty.city = "New York"
paty.state = "MG"
paty.zip = "33252"
paty.closeFriend = "on"
mock_contacts.append(paty)

nextId = 4