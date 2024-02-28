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
    RedFlagsAvgTable = worldCup.RedFlagsAvg()["data"].to_html( index=False, classes="table center", table_id="data_table", header="true")
    RedFlagsAvgCode = worldCup.RedFlagsAvg()["code"]
    ComeBackTable = worldCup.ComeBack()["data"].to_html( index=False, classes="table center", table_id="data_table", header="true")
    ComeBackCode = worldCup.ComeBack()["code"]
    champCurseTable = worldCup.champCurse()["data"].to_html( index=False, classes="table center", table_id="data_table", header="true")
    champCurseCode = worldCup.champCurse()["code"] 
    underDogTable = worldCup.underDog()["data"].to_html( index=False, classes="table center", table_id="data_table", header="true") 
    underDogCode = worldCup.underDog()["code"] 
    return render_template("analytics.html", title="Home/Analytics", 
                            RedFlagsAvgTable = RedFlagsAvgTable, 
                            RedFlagsAvgCode=RedFlagsAvgCode,
                            ComeBackTable=ComeBackTable,
                            ComeBackCode=ComeBackCode,
                            champCurseTable = champCurseTable,
                            champCurseCode = champCurseCode,
                            underDogTable = underDogTable,
                            underDogCode = underDogCode                           
                           )

@app.route("/players")
def players():
    return render_template("table_view.html", title="Players", table=worldCup.Players().to_html( index=False, classes="table", table_id="data_table", header="true"))

@app.route("/matches")
def matches():
    return render_template("table_view.html", title="Matches", table=worldCup.Matches().to_html( index=False, classes="table", table_id="data_table", header="true"))

@app.route("/cups")
def cups():
    return render_template("table_view.html", title="Cups", table=worldCup.Cups().to_html( index=False, classes="table", table_id="data_table", header="true"))
