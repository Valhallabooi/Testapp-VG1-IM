from flask import Flask, render_template

app = Flask(__name__)


meny = [
    {"navn": "Pølse i brød", "pris": 25, "beskrivelse": "Klassisk pølse i brød", "bilde_url": "https://i.pinimg.com/originals/16/c2/20/16c220a4229b1658d982c7664742e565.png"},
]


@app.route("/")
def index():
    return render_template("index.html", meny=meny)

@app.route("/info")
def info():
     return render_template("index_info.html", )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)

