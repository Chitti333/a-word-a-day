from flask import Flask, render_template
import csv
import random
import datetime

app = Flask(__name__)

# Load words from the CSV file
def load_words():
    words = []
    with open('words_list.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # Skip the header
        for row in reader:
            words.append({
                'word': row[0],
                'meaning': row[1],
                'example': row[2]
            })
    return words

words = load_words()

# Get word of the day based on the current date
def get_word_of_the_day():
    today = datetime.date.today()
    index = today.toordinal() % len(words)
    return words[index]

@app.route('/')
def index():
    word_of_the_day = get_word_of_the_day()
    return render_template('index.html', word=word_of_the_day)
from flask import jsonify

@app.route('/new-word')
def new_word():
    word = random.choice(words)
    return jsonify(word)


if __name__ == '__main__':
    app.run(debug=True)
