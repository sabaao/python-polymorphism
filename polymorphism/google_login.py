from polymorphism import login

class GoogleLogin(login.Login):
    def login(self):
        print('GoogleLogin login implementation.')