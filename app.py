

from flask import Flask, render_template
import pandas as pd
import random  # Import random

app = Flask(__name__)

# Load the idioms data (assuming 'idioms.csv' is in the same directory)
data = pd.read_csv('english_idioms.csv')
idioms = data[['idioms', 'meaning']].to_dict('records')  # Convert to list of dicts

@app.route('/')
def index():
    # Select a random idiom from the loaded data
    random_idiom = random.choice(idioms)
    return render_template('index.html', idiom=random_idiom)

if __name__ == '__main__':
    app.run(debug=True)
