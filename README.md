# Sudoku Solver

A Sudoku solver you can play with in the browser. Type in any puzzle, hit solve, and watch a backtracking algorithm fill in the rest cell by cell.

## What it does

You get a 9x9 grid you can type numbers into directly. As you type, the board checks for conflicts in real time (duplicate numbers in a row, column, or box get highlighted immediately). Once your puzzle looks right, you can:

* Hit **Solve** to watch the algorithm fill in the missing numbers with a short animation
* Hit **Instant** to skip the animation and see the finished puzzle right away
* Hit **Sample** to load a demo puzzle if you don't have one on hand
* Hit **Reset** to clear the board and start over

## How it works

The solving logic lives in `sudoku_solver.py` and uses classic backtracking: it finds the next empty cell, tries the numbers 1 through 9, checks whether each one is valid for that row, column, and 3x3 box, and recurses. If it hits a dead end it backtracks and tries the next number. Every step it takes is recorded so the frontend can animate the solution instead of just dumping the finished grid on screen.

The frontend is a single HTML page with vanilla JavaScript, no frameworks. It sends the grid to a `/solve` endpoint as JSON, gets back the list of solved cells, and animates them onto the board.

## Tech used

* Python and Flask for the backend and solving logic
* Vanilla HTML, CSS, and JavaScript for the frontend
* Deployed on Vercel as a serverless function (see `api/index.py` and `vercel.json`)

## Running it locally

Clone the repo and install Flask:

```bash
git clone https://github.com/Jakub-Nowicki/sudoku-solver.git
cd sudoku-solver
pip install -r requirements.txt
```

Then start the server:

```bash
python sudoku_solver.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser and you're good to go.

## Website

<p align="center">
  <img src="https://github.com/user-attachments/assets/e2f6d157-e33f-4ab3-bba2-04d9f6b9b003" alt="First Image" width="31%" style="margin-right: 10px;"/>
  <img src="https://github.com/user-attachments/assets/fab7a3c5-9d3f-4af0-91e1-aafb30bf6db5" alt="Second Image" width="31%" style="margin-right: 10px;"/>
  <img src="https://github.com/user-attachments/assets/ad2ec2bf-42a9-4cd7-b8b2-a29df1954168" alt="Third Image" width="31%"/>
</p>

## Contributing

Bug reports, feature ideas, and pull requests are all welcome. If something looks off or you have an idea for an improvement, feel free to open an issue.
