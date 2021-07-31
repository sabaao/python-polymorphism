from polymorphism import facebook_login, google_login, twitter_login

facebook_user_login = facebook_login.FacebookLogin()
facebook_user_login.login() # FacebookLogin login implementation.

google_user_login = google_login.GoogleLogin()
google_user_login.login() # GoogleLogin login implementation.

twitter_user_login = twitter_login.TwitterLogin()
twitter_user_login.login() # TwitterLogin login implementation.

