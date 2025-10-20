
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

posts = [
    [1, "Første innlegg", "<p>Innlegg 1"]
    [2, "Andre innlegg", "<p>Innlegg 2"]
    [3, "Tredje innlegg", "<p>Innlegg 3"]
    [4, "Fjerde innlegg", "<p>Innlegg 4"]
]

if __name__ == "__main__":
    app.run(debug=True)
