
from flask import Flask, render_template

app = Flask(__name__)

#lagde en liste over inlegg som jeg da kalte posts
posts = [
    [1, "Første innlegg", "<p>Innlegg 1"],
    [2, "Andre innlegg", "<p>Innlegg 2"],
    [3, "Tredje innlegg", "<p>Innlegg 3"],
    [4, "Fjerde innlegg", "<p>Innlegg 4"]
]

@app.route("/")
def hello():
    return render_template('index.html', posts=posts)

@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = get_post_by_id(post_id)
    if not post:
        abort(404)
    return render_template("post.html", post=post)

from flask import abort

def get_post_by_id(post_id: int):
    for p in posts:
        if p[0] == post_id:
            return p
    return None


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404    

if __name__ == "__main__":
    app.run(debug=True)