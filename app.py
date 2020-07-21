from flask import Flask

# import flask

# In order for us to use flask we need create a instance of our app
app = Flask(__name__)

# Syntax to create flask instance

# syntax for decorators to create a web route
# block of code for default page
@app.route("/")
# create a welcome method to display on home/default page
def index():
    return "<h1>Welcome to MVC with flask Project</h1>"
# end of block of code for default page

# exercise:- create a function called welcome_user
# create a decorator to link the page /user
# return "welcome to Python flask app dear {user}
# in the browser when we load the page from home page to user name i.e your name
# it should display your name in the browser with message from your methods

# index method will be called at the endpoint
# index method will display on our home page
# sytanx to run our app
if __name__ == "__main__":
    app.run(debug=True)
# debug=true ensure to update any changes without re-running the app
