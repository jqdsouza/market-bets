import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "<h1>Market Bets</h1><p>This site is for degenerates who want to gamble away their life savings.</p>"

app.run()