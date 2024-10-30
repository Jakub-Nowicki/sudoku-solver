# Sudoku Solver

## Overview
**This Sudoku Solver** is a Python-based web application that leverages **Flask** to provide a user-friendly interface for solving Sudoku puzzles. The solver utilizes backtracking to efficiently find solutions, displaying them in real-time on the web page.

## Features
- **Dynamic Web Interface**: Utilizes Flask to serve HTML pages that allow for interactive Sudoku puzzle input and visualization.
- **Real-time Solution Display**: Solves puzzles in real-time, showing the steps involved in solving the Sudoku on the web interface.
- **Input Validation**: Ensures that only valid numbers can be entered into the puzzle grid, providing immediate feedback on incorrect inputs.

## Technologies Used
- **Flask**: A lightweight WSGI web application framework used to create the web server.
- **HTML/CSS**: Used for creating and styling the web interface.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Jakub-Nowicki/sudoku-solver.git
   cd sudoku-solver
   
2. **Install dependencies**
   ```bash
   pip install Flask
   
3. **Run the application**
   ```bash
   python app.py
   
This will start the Flask server on `localhost:5000`. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000) to use the application.
   
## Usage

- **Navigate to the home page** and enter numbers into the Sudoku grid.
- **Click the "Solve" button** to see the solver in action. The solution, if available, will be displayed in the grid.
- **Use the "Reset" button** to clear the grid and enter a new puzzle.

## Website:
<img width="300" alt="Screenshot 2024-10-30 at 11 23 41" src="https://github.com/user-attachments/assets/e2f6d157-e33f-4ab3-bba2-04d9f6b9b003">
<img width="300" alt="Screenshot 2024-10-30 at 11 29 04" src="https://github.com/user-attachments/assets/fab7a3c5-9d3f-4af0-91e1-aafb30bf6db5">
<img width="300" alt="Screenshot 2024-10-30 at 11 29 08" src="https://github.com/user-attachments/assets/ad2ec2bf-42a9-4cd7-b8b2-a29df1954168">


## Contributing

Contributions to this project are welcome! Here are a few ways you can help:
- **Report bugs**: If you find a bug, please report it by opening an issue.
- **Add new features**: Have an idea for a new feature? Contribute your ideas through pull requests.
- **Improve the documentation**: Good documentation makes any project easier to understand and use. Enhance the documentation to help newcomers.
