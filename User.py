class User:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_email(self):
        return self.email

    def set_name(self, name):
        self.name = name
    
    def set_age(self, age):
        self.age = age
    
    def set_email(self, email):
        self.email = email

