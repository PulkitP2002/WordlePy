# Wordle Game in Python with Flask

This project is a web-based implementation of the popular word puzzle game, Wordle, developed using Python and Flask. The game challenges players to guess a secret 5-letter word within six attempts. After each guess, players receive feedback indicating which letters are correctly placed, present in the word but in the wrong position, or not in the word at all.

## Key Features

- **Interactive Gameplay**: Users can input their guesses through a web interface.
- **Dynamic Feedback**: Each guess is evaluated and displayed with color-coded feedback using Tailwind CSS:
  - Green for correct letters in the correct position.
  - Yellow for correct letters in the wrong position.
  - Gray for incorrect letters.
- **Game Management**: The game ends when the player either guesses the word correctly or exhausts all six attempts. The game state resets automatically or can be reset manually.
- **Responsive Design**: The user interface is built with Tailwind CSS, ensuring a clean and responsive experience across devices.

## How to Start

Follow these steps to get the project running on your local machine:

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system.
- **Flask**: Install Flask if it's not already installed.

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/wordle-flask.git
    ```
2. Navigate to the project directory:
    ```bash
    cd wordle-flask
    ```
3. Install the required Python packages:
    ```bash
    pip install Flask
    ```

### Running the Application

1. Start the Flask development server:
    ```bash
    python app.py
    ```
2. Open your web browser and go to `http://127.0.0.1:5000` to play the game.

### Usage

- Enter a 5-letter word as your guess.
- The game will provide feedback on each guess.
- Try to guess the secret word within 6 attempts!

### Future Enhancements

- Add a leaderboard to track high scores.
- Implement a hint system for more challenging words.
- Add more word lists for increased difficulty.

## License

This project is licensed under the MIT License.

---

Feel free to customize this `README.md` as needed!
