# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/me")
def home():

    name = "abc" # write your name
    age = "99" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage

app = Flask(__name__)


@app.route("/father")
def home():

    name = "xyz" # write your name
    age = "999" # write your age

    return render_template('father.html' , name = name , age = age)

# define the route to mother webpage

app = Flask(__name__)


@app.route("/mother")
def home():

    name = "pqr" # write your name
    age = "888" # write your age

    return render_template('mother.html' , name = name , age = age)


# define the route to friends webpage

app = Flask(__name__)


@app.route("/friend")
def home():

    name = "stu" # write your name
    age = "99" # write your age

    return render_template('friend.html' , name = name , age = age)


# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
