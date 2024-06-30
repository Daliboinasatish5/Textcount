from flask import Flask, render_template, request

app = Flask(__name__)

def count_words(text):
    """
    Count the number of words in the given text.
    Args:
        text (str): The input text from the user.
    Returns:
        int: The number of words in the text.
    """
    words = text.split()
    return len(words)

@app.route('/', methods=['GET', 'POST'])
def index():
    word_count = None
    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            word_count = count_words(text)
    return render_template('index.html', word_count=word_count)

if __name__ == "__main__":
    app.run(debug=True)
