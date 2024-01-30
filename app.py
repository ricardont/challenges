from flask import Flask, render_template
import sudokuChecker

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home")

@app.route("/sudoku")
def sudoku():
   return render_template("sudoku.html", title="Home > Sudoku",  sudokuBoard=sudokuChecker.get_sudoku() )
    # return "sudoku template""board1"