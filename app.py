from flask import Flask, render_template

app = Flask(__name__,
            template_folder="siteciencia/templates", static_folder="siteciencia/static")

@app.route("/")
def index():
    # return "<h1>Bom Dia, professor.</h1>"
    return render_template("Index.html")