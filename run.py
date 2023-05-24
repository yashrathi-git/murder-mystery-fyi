from murder_mystery import app
from murder_mystery.login import login_app
from murder_mystery.game import game_app
from rich.traceback import install

app.register_blueprint(login_app, url_prefix="/login")
app.register_blueprint(game_app, url_prefix="/game")


if __name__ == "__main__":
    install()

    app.run(debug=True)
