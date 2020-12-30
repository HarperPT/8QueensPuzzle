from flask import Flask, render_template, request
from EightQueensPuzzle import Puzzle

import json


app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
  if request.method =='POST':
    queens_count = request.form.get("SltQueens")
    queens_count = int(queens_count)
    if queens_count > 0:
      puzzle = Puzzle(queens_count)
      result = json.loads(puzzle.get_solutions())
      # print(result)
      return render_template("index.html", data = queens_count, result = result)
  
  return render_template("index.html", data=null)

if __name__ == '__main__':
  app.run(debug=True)