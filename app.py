from flask import Flask, request
from flask_cors import CORS

from sudoku_solver import *
from practice import *

app = Flask(__name__)
CORS(app) 


@app.route("/healthcheck")
def hello():
    return {'message':"Hello World!"}


@app.route("/solve", methods = ['POST'])
def solver():
    grid = request.get_json()['puzzle']
    answer = solve_puzzle(grid)

    return answer


@app.route("/generate", methods = ['GET'])
def generate():
    difficulty = request.args["difficulty"]
    answer = generate_puzzle(difficulty)

    return answer


@app.route("/candidates", methods = ['POST'])
def get_candidates():
    grid = request.get_json()['puzzle']
    candidates = get_all_cell_candidates(grid)

    return candidates


@app.route("/soleCandidates", methods = ['POST'])
def get_sole_candidates():
    grid = request.get_json()['puzzle']
    print(grid)
    candidates = get_cell_sole_candidates(grid)

    return candidates

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
