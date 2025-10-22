from flask import Flask, render_template, abort
 
app = Flask(__name__)
 
# Hvert innlegg: [id, tittel, innhold_html]

posts = [

    [1, "Første innlegg", "<p>Hei og velkommen til mini-bloggen!</p>"],

    [2, "Flask-tips", "<ul><li>Bruk <code>url_for</li><li>Arv fra base.html</li></ul>"],

    [3, "Dagens sitat", "<blockquote>«Code is like humor. When you have to explain it, it’s bad.»</blockquote>"],

]
 
def get_post_by_id(post_id: int):

    for p in posts:

        if p[0] == post_id:

            return p

    return None
 
@app.route("/")

def index():

    return render_template("index.html", posts=posts)
 
@app.route("/post/<int:post_id>")

def post_detail(post_id):

    post = get_post_by_id(post_id)

    if not post:

        abort(404)

    return render_template("post.html", post=post)
 

@app.errorhandler(404)

def page_not_found(e):

    return render_template("404.html"), 404
 
if __name__ == "__main__":

    app.run(debug=True)
 