import random
from flask import Flask, render_template, jsonify

app = Flask(__name__)

# List of football players from top five leagues
top_five_leagues_players = [
     "Marco Asensio - La Liga",
    "Pierre-Emerick Aubameyang - English Premier League",
    "Romelu Lukaku - Serie A",
    "Kylian Mbappé - Ligue 1",
    "Jan Oblak - La Liga",
    "Kevin De Bruyne - English Premier League",
    "Robert Lewandowski - Bundesliga",
    "Lionel Messi - La Liga",
    "Sadio Mané - English Premier League",
    "Joshua Kimmich - Bundesliga",
    "Ciro Immobile - Serie A",
    "Manuel Neuer - Bundesliga",
    "Renato Sanches - Ligue 1",
    "Dries Mertens - Serie A",
    "Jadon Sancho - Bundesliga",
    "Harry Kane - English Premier League",
    "Karim Benzema - La Liga",
    "N'Golo Kanté - English Premier League",
    "Florian Thauvin - Ligue 1",
    "Cristiano Ronaldo - Serie A",
    "Memphis Depay - Ligue 1",
    "Lorenzo Insigne - Serie A",
    "Mohamed Salah - English Premier League",
    "Jamie Vardy - English Premier League",
    "Gerard Piqué - La Liga",
    "Timo Werner - Bundesliga",
    "Zlatan Ibrahimović - Serie A",
    "Luis Suárez - La Liga",
    "Toni Kroos - La Liga",
    "Angel Di María - Ligue 1",
    "Virgil van Dijk - English Premier League",
    "Gianluigi Donnarumma - Serie A",
    "Burak Yılmaz - Ligue 1",
    "Thomas Müller - Bundesliga",
    "Neymar Jr. - Ligue 1",
    "Dayot Upamecano - Bundesliga",
    "Paulo Dybala - Serie A",
    "Marco Verratti - Ligue 1",
    "Sergio Ramos - La Liga",
    "Andrew Robertson - English Premier League",
    "Marquinhos - Ligue 1",
    "Duván Zapata - Serie A",
    "Thibaut Courtois - La Liga",
    "Jack Grealish - English Premier League",
    "Achraf Hakimi - Serie A",
    "Presnel Kimpembe - Ligue 1",
    "Milan Škriniar - Serie A",
    "Heung-Min Son - English Premier League",
    "João Cancelo - English Premier League",
    "Frenkie de Jong - La Liga",
    "Sergej Milinković-Savić - Serie A",
    "Dani Carvajal - La Liga",
    "Eduardo Camavinga - Ligue 1",
    "Ángel Correa - La Liga",
    "Wilfred Ndidi - English Premier League",
    "Alessandro Bastoni - Serie A",
    "Benjamin Pavard - Bundesliga",
    "Youri Tielemans - English Premier League",
    "Serge Gnabry - Bundesliga",
    "Francesco Caputo - Serie A",
    "Yann Karamoh - Ligue 1",
    "Sergio Agüero - English Premier League",
    "Moussa Diaby - Bundesliga",
    "Erling Haaland - Bundesliga",
    "Fabián Ruiz - Serie A",
    "Piotr Zieliński - Serie A",
    "Thorgan Hazard - Bundesliga",
    "Martin Ødegaard - La Liga",
    "Mason Mount - English Premier League",
    "Lucas Ocampos - La Liga",
    "Lucas Paquetá - Ligue 1",
    "Achraf Hakimi - Serie A",
    "Houssem Aouar - Ligue 1",
    "Raphinha - English Premier League",
    "Manuel Locatelli - Serie A",
    "Kalidou Koulibaly - Serie A",
    "Caglar Söyüncü - English Premier League",
    "Éver Banega - La Liga",
    "Diogo Jota - English Premier League",
    "Ferland Mendy - La Liga",
    "Jules Koundé - La Liga",
    "Ibrahima Konaté - Bundesliga",
    "Benjamin Mendy - English Premier League",
    "Federico Valverde - La Liga",
    "Alassane Pléa - Bundesliga",
    "Mateo Kovačić - English Premier League"
]

# Function to fetch a random player name from the list
def get_random_player_from_list():
    return random.choice(top_five_leagues_players)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get_random_player")
def get_random_player():
    random_player = get_random_player_from_list()
    return jsonify({"player": random_player})

if __name__ == "__main__":
    app.run(debug=True)
