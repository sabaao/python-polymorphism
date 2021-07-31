from polymorphism import login

class TwitterLogin(login.Login):
    def login(self):
        print('TwitterLogin login implementation.')