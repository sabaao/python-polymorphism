from polymorphism import login

class FacebookLogin(login.Login):
    def login(self):
        print('FacebookLogin login implementation.')