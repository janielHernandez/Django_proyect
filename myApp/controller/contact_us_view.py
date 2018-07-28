from ..models import Contacter


class ContactView:
    name = ''
    email = ''
    subject = ''

    def __init__(self, name, email, subject):
        self.name = name
        self.email = email
        self.subject = subject

    def create(self):
        ob = Contacter()
        ob.email = self.email
        ob.name = self.name
        ob.subject = self.subject
        ob.save()
        print(self.name)
        print(self.email)
        print(self.subject)


