from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

# route to handle the landing page of a website.
@app.route('/')
def start_here():
    return "Hi! This is the home page."

# route to display a simple web page
@app.route('/hello')
def say_hello():
    return render_template("hello.html")

@app.route('/greet')
def greet_person():
    player = request.args.get("person")

    AWESOMENESS = [
        'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
        'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route('/game')
def show_game_form():
    play_game = request.args.get("game")

    if play_game == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route("/madlib")
def show_madlib():
    person = request.args.get("person")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")

    list_of_madlibs = ["There once was a %s %s sitting in the Hackbright Lab. When %s went to pick it up, it burst into flames in a totally %s way.",
                        "My %s %s blew up the servers at Hackbright. %s tried to fix it, but the %s machine caught fire halfway through."]

    mystring = choice(list_of_madlibs)

    mystring = mystring %( color, noun, person, adjective)

    return render_template('madlib.html', text=mystring)
    # return render_template("madlib.html", person_output = person, 
            # color_output = color, noun_output = noun, adjective_output = adjective)

if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
