"""Greeting Flask app."""

from random import choice

from flask import Flask, request

# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible',
    'wonderful', 'smashing', 'lovely']

DISSES = ["I can't see you behind all that plaid!", "Get your geek outta here!",
            "I'd rate you C++"]


@app.route("/")
def start_here():
    """Home page."""

    return """
    <!doctype html>
    <html>
      <head>
      Hi! This is the home page.
      </head>
      <body>
        <a href="http://localhost:5000/hello">Hello Page</a>
        <a href="http://localhost:5000/diss">Diss Page</a>
      </body>
    </html>
    """


@app.route("/hello")
def say_hello():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/greet">
          What's your name? <input type="text" name="person">
          Choose a compliment:
            <select name="compliment">
                <option value="awesome">Awesome</option>
                <option value="terrific">Terrific</option>
                <option value="fantastic">Fantastic</option>
                <option value="neato">Neato</option>
                <option value="fantabulous">Fantabulous!!</option>
                <option value="wowza">WOWZA!!</option>
                <option value="oh-so-not-meh">oh-so-not-meh ;)</option>
                <option value="brilliant">Brilliant</option>
                <option value="ducky">Ducky</option>
                <option value='coolio'>Coolio</option>
                <option value="incredible">Incredible</option>
                <option value="wonderful">WONDERFUL~ <3</option>
                <option value="smashing">Smashing!</option>
                <option value="lovely">Lovely <3</option>
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
    """


@app.route("/diss")
def say_diss():
    """Say hello and prompt for user's name."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Hi There!</title>
      </head>
      <body>
        <h1>Hi There!</h1>
        <form action="/diss_greet">
          What's your name? <input type="text" name="person">
          <input type="submit" value="Submit">
        </form>
      </body>
    </html>
   """


@app.route("/greet")
def greet_person():
    """Get user by name."""

    player = request.args.get("person")
    compliment = request.args.get("compliment")

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Compliment</title>
      </head>
      <body>
        Hi, {}! I think you're {}!
      </body>
    </html>
    """.format(player, compliment)


@app.route("/diss_greet")
def diss_greet():
    """Get user by name."""

    player = request.args.get("person")
    diss = choice(DISSES)

    return """
    <!doctype html>
    <html>
      <head>
        <title>A Diss</title>
      </head>
      <body>
        Hi, {}! {}!
      </body>
    </html>
    """.format(player, diss)


if __name__ == "__main__":
    # debug=True gives us error messages in the browser and also "reloads"
    # our web app if we change the code.
    app.run(debug=True, host="0.0.0.0")
