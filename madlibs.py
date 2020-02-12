"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return """
    <!doctype html>
    <html>
      <head>
        <title>Homepage</title>
      </head>
      <body>
        Hi! This is the home page.
        <a href="http://localhost:5000/hello">Link Text</a>
      </body>  
    </html>
    """


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)

@app.route('/game')
def show_madlib_form():
    """ Ask if user wants to play a game."""

    play_game = request.args.get("choice")

    if play_game == 'yes':
        return render_template("game.html")

    else:
        return render_template("goodbye.html")


@app.route('/madlib')
def show_madlib():

    python_person = request.args.get("person_input")

    python_color = request.args.get("color_input")

    python_noun = request.args.get("noun_input")

    python_adjective = request.args.get("adjective_input")

    return render_template("madlibs.html",
                                python_person=html_person,
                                python_colort=html_color,
                                python_noun =html_noun,
                                python_adjective=html_adjective)





if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
