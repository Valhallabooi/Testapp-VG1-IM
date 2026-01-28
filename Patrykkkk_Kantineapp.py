from flask import Flask, render_template
# Oppretter en Flask applikasjon

app = Flask(__name__)

# her ser du alle menyene som er i kantinemenyen. 
meny = [
    {"navn": "Pølse i brød", "pris": 25, "beskrivelse": "Klassisk pølse i brød, fersk brød, og god pølse", "bilde_url": "https://i.pinimg.com/originals/16/c2/20/16c220a4229b1658d982c7664742e565.png"},
    {"navn": "Pizza bit", "pris": 35 , "beskrivelse": "Sprø bund med masse ost, saus, sopp og korn", "bilde_url": "https://pizzabit.com.ua/img/21344994.jpg"},
    {"navn": "Burger", "pris": 60  , "beskrivelse": " Juicy burger med masse ingredienser som salat, agurt og kjøtt", "bilde_url": "https://tse4.mm.bing.net/th/id/OIP.Muo6k_4TwnZbpiYbKQt9QwHaE8?cb=ucfimg2&ucfimg=1&rs=1&pid=ImgDetMain&o=7&rm=3"},
    {"navn": "taco", "pris": 45   , "beskrivelse": " Fin mexicans taco med kjøtt, ost, sterk saus og korn", "bilde_url": "https://th.bing.com/th/id/R.29fcbeacb7943073b0f49676b4f4e3d8?rik=MTOXjA1QmE%2fNdA&pid=ImgRaw&r=0"},
]

# Her er det routes som brkers for å navigere mellom sidene i applikasjonen. her har jeg 3 forskjellige sider.
@app.route("/")
def index():
    return render_template("index.html", meny=meny)

@app.route("/info")
def info():
     return render_template("index_info.html", )

@app.route("/bilder")
def bilder():
    return render_template("bilder01.html", )

# Starter flask applikasjonen på port 6565
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6565)

