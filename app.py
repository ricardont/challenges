from flask import Flask, render_template
import sudokuChecker
import worldCup
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/sudoku")
def sudoku():
    return render_template("sudoku.html", title="Home/Sudoku",  sudokuBoard=sudokuChecker.get_sudoku() )

@app.route("/analytics")
def analytics():
    return render_template("analytics.html", title="Home/Analytics", data=worldCup.Players() )