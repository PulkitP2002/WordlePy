from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# Load the word lists
def load_dictionary(file_path):
    with open(file_path) as f:
        words = [line.strip() for line in f]
    return words

guesses_dictionary = "guesses.txt"
answers_dictionary = "answers.txt"

guesses = load_dictionary(guesses_dictionary)
answers = load_dictionary(answers_dictionary)

# Game state variables
attempts = 0
max_attempts = 6
feedback = []
secret_word = ""
game_over = False
message = ""
error_message = ""

def reset_game():
    global attempts, feedback, secret_word, game_over, message, error_message
    attempts = 0
    feedback = []
    secret_word = random.choice(answers).lower()
    game_over = False
    message = ""
    error_message = ""

# Initialize game state
reset_game()

# Evaluate the guess
def evaluate_guess(guess, word):
    result = ""
    for i in range(5):
        if guess[i] == word[i]:
            result += f'<span class="text-white bg-green-500 px-2 py-1 rounded">{guess[i].upper()}</span>'
        elif guess[i] in word:
            result += f'<span class="text-white bg-yellow-500 px-2 py-1 rounded">{guess[i].upper()}</span>'
        else:
            result += f'<span class="text-gray-900 bg-gray-300 px-2 py-1 rounded">{guess[i].upper()}</span>'
    return result

@app.route('/', methods=['GET', 'POST'])
def wordle():
    global attempts, feedback, secret_word, game_over, message, error_message
    if request.method == 'POST' and not game_over:
        guess = request.form['guess'].lower()
        if len(guess) == 5 and guess in guesses:
            attempts += 1
            result = evaluate_guess(guess, secret_word)
            feedback.append(result)
            error_message = ""
            if guess == secret_word:
                message = f"Congratulations! You guessed the word: {secret_word.upper()}"
                game_over = True
            elif attempts >= max_attempts:
                message = f"Game over. The secret word was: {secret_word.upper()}"
                game_over = True
        else:
            error_message = "Invalid guess. Please enter a valid 5-letter word."

    return render_template('index.html', feedback=feedback, attempts=attempts, max_attempts=max_attempts, game_over=game_over, message=message, correct_guess=secret_word.upper() if game_over else None, error_message=error_message)

@app.route('/reset')
def reset():
    reset_game()  # Reset the game state
    return redirect(url_for('wordle'))

# Force game reset on reload
@app.route('/start')
def start():
    reset_game()  # Reset the game state
    return redirect(url_for('wordle'))

if __name__ == '__main__':
    app.run(debug=True)
