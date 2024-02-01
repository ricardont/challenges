from flask import Flask, render_template
from flask_bootstrap import Bootstrap
# import pandas
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
    return render_template("analytics.html", title="Home/Analytics" )

@app.route("/players")
def players():
    return render_template("table_view.html", title="Players", table=worldCup.Players().to_html(classes="table", table_id="data_table", header="true"))

@app.route("/matches")
def matches():
    return render_template("table_view.html", title="Matches", table=worldCup.Matches().to_html(classes="table", table_id="data_table", header="true"))

@app.route("/cups")
def cups():
    return render_template("table_view.html", title="Cups", table=worldCup.Cups().to_html(classes="table", table_id="data_table", header="true"))
