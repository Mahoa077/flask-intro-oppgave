import sqlite3
from flask import Flask, render_template, abort
 
app = Flask(__name__)
DB_PATH = "blog.db" 
# Hvert innlegg: [id, tittel, innhold_html]

def fetch_all_posts():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "SELECT id, title, content from posts ORDER BY id DESC;"
        ).fetchall()
    return [[r["id"], r["title"], r["content"]] for r in rows]
 
def fetch_post_by_id(post_id: int):
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        row = con.execute(
            "SELECT id, title, content FROM posts WHERE id = ?;",
            (post_id,)
        ).fetchone()
    if row is None:
        return None
    return [row["id"], row["title"], row["content"]]

@app.route("/slettinnlegg/<int:post_id>")
def slett_innlegg(post_id):
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        rows = con.execute(
            "DELETE FROM posts WHERE id = ?", (post_id,)
        ) 
        con.commit()
    posts = fetch_all_posts()
    return render_template("index.html", posts=posts)

@app.route("/legg/til/innlegg")
def legg_til_innlegg():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row

        title = input("Skriv inn titel: ")
        content = input("Skriv inn innhold: ")

        row = con.execute(
            "INSERT INTO posts (title, content) VALUES (?,?)", (title, content)
        )
    
@app.route("/post/rediger(innlegg)")
def rediger_innlegg():
    with sqlite3.connect(DB_PATH) as con:
        con.row_factory = sqlite3.Row
        innlegg_id = input("Skriv inn id til varen som skal redigeres: ")
        rows = con.execute(
            "SELECT * FROM posts WHERE id = ?", (innlegg_id), 
            post_id = input ("Skriv inn id-en: ")
        )

@app.route("/")
def index():
    posts = fetch_all_posts()
    return render_template("index.html", posts=posts)
 
@app.route("/post/<int:post_id>")
def post_detail(post_id):
    post = fetch_post_by_id(post_id)
    if not post:
        abort(404)
    return render_template("post.html", post=post)
 

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404
 
if __name__ == "__main__":

    app.run(debug=True)
 