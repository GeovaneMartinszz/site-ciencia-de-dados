from flask import Flask, render_template

app = Flask(__name__,
            template_folder="siteciencia/templates", static_folder="siteciencia/static")

@app.route("/")
def index():
    # return "<h1>Bom Dia, professor.</h1>"
    return render_template("Index.html")

@app.route("/analise", defaults={'usuario':'Visitante'})
@app.route("/analise/<usuario>")
def analise(usuario):
    return render_template("analise.html", usuario=usuario)

if __name__=="_main_":
    app.run(debug=True)
