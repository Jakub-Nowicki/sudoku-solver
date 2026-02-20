from flask import Flask, render_template, redirect, url_for, request, jsonify
import copy


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            if solve(bo):
                return True
            bo[row][col] = 0
    return False


def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j)
    return None


def valid(bo, num, pos):
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    row = pos[0] // 3
    column = pos[1] // 3
    for i in range(row * 3, row * 3 + 3):
        for j in range(column * 3, column * 3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True


def solve_with_steps(bo):
    steps = []
    _solve_steps(bo, steps)
    return steps


def _solve_steps(bo, steps):
    find = find_empty(bo)
    if not find:
        return True
    row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            steps.append((row, col, i))
            if _solve_steps(bo, steps):
                return True
            bo[row][col] = 0
    return False


app = Flask(__name__)

grid = [[0 for _ in range(9)] for _ in range(9)]


@app.route('/')
def home():
    g = [[0 for _ in range(9)] for _ in range(9)]
    return render_template('index.html', grid=g)


@app.route('/solve', methods=['POST'])
def solve_route():
    data = request.get_json()
    cells = data.get('grid', [])
    g = [[0] * 9 for _ in range(9)]
    given = []
    for item in cells:
        r, c, v = item['r'], item['c'], item['v']
        if v != 0:
            g[r][c] = v
            given.append([r, c])

    board = copy.deepcopy(g)
    steps = solve_with_steps(board)

    solved = []
    for r, c, v in steps:
        if [r, c] not in given:
            solved.append({'r': r, 'c': c, 'v': v})

    return jsonify({'solved': solved, 'success': len(solved) > 0})


if __name__ == '__main__':
    app.run(debug=True)
