from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home_page.html")


@app.route("/tutorial1")
def tutorial1():
    return render_template("tutorials/tutorial_page1.html")


@app.route("/tutorial2")
def tutorial2():
    return render_template("tutorials/tutorial_page2.html")


@app.route("/tutorial3")
def tutorial3():
    return render_template("tutorials/tutorial_page3.html")


@app.route("/phone tutorial1")
def phone_tutorial1():
    return render_template("tutorials/phone-tutorial_page1.html")


@app.route("/phone tutorial2")
def phone_tutorial2():
    return render_template("tutorials/phone-tutorial_page2.html")


@app.route("/phone tutorial3")
def phone_tutorial3():
    return render_template("tutorials/phone-tutorial_page3.html")


@app.route("/phone tutorial4")
def phone_tutorial4():
    return render_template("tutorials/phone-tutorial_page4.html")


@app.route("/main page")
def main():
    return render_template("main_page.html")


@app.route("/adventure game code")
def adventure():
    return render_template("downloads/adventure game.htm")


@app.route("/adventure page")
def adventure_page():
    return render_template("game_pages/adventure_page.html")


@app.route("/calculator code")
def calculator():
    return render_template("downloads/simple calculator.htm")


@app.route("/calculator page")
def calculator_page():
    return render_template("game_pages/calculator_page.html")


@app.route("/rps game  code")
def rps():
    return render_template("downloads/rps1.htm")


@app.route("/rps page")
def rps_page():
    return render_template("game_pages/rps_page.html")


@app.route("/snake code")
def snake():
    return render_template("downloads/snake gme.htm")


@app.route("/snake page")
def snake_page():
    return render_template("game_pages/snake_page.html")


@app.route("/pong code")
def pong():
    return render_template("downloads/pong.htm")


@app.route("/pong page")
def pong_page():
    return render_template("game_pages/pong_page.html")


@app.route("/meem shop code")
def meem():
    return render_template("downloads/meem shop.htm")


@app.route("/meem page")
def meem_page():
    return render_template("game_pages/meem_page.html")


@app.route("/guessing code")
def guess():
    return render_template("downloads/Guessing_game.htm")


@app.route("/guessing page")
def guess_page():
    return render_template("game_pages/guessing_page.html")


@app.route("/password code")
def password():
    return render_template("downloads/password_generator.htm")


@app.route("/quiz code")
def quiz():
    return render_template("downloads/quiz.htm")


@app.route("/tic tac toe code")
def tic_tac_toe():
    return render_template("downloads/tic_tac_toe.htm")


@app.route("/contact")
def contact_us():
    return render_template("navbar/contact_us.html")


@app.route("/what_new")
def what_new():
    return render_template("navbar/what_new.html")


@app.route("/new_games")
def new_game():
    return render_template("navbar/new_games.html")


if __name__ == "__main__":
    app.run(debug=True)
