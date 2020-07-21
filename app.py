from flask import Flask, render_template, url_for, request

# import flask

# In order for us to use flask we need create a instance of our app
app = Flask(__name__)

# Syntax to create flask instance

# syntax for decorators to create a web route
# block of code for default page
# @app.route("/")
# # create a welcome method to display on home/default page
# def index():
#     return "<h1>Welcome to MVC with flask Project</h1>"
# end of block of code for default page

@app.route("/")
def welcome_user():
    return render_template("base.html")

@app.route("/loging/")
def welcome_user():
# login in functionality with GET,POST methods of HTTP
# import request to use the methods check status code
# add control flow to redirect the user accorinding to the status code received.

    return render_template("index.html")


# index method will be called at the endpoint
# index method will display on our home page
# sytanx to run our app
if __name__ == "__main__":
    app.run(debug=True)
# debug=true ensure to update any changes without re-running the app


# when you see an error/exception - look at the line number at the end of error and review your code first
# when you see an error/exception - look at the line number at the end of errors on the browser and review your code first