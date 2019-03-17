from jinja2 import StrictUndefined

from flask import Flask
from flask_debugtoolbar import DebugToolbarExtension

from model import connect_to_db, db


app = Flask(__name__)
app.secret_key = "secret!"

app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    return "<html><body>Placeholder for the homepage.</body></html>"


if __name__ == "__main__":

    app.debug = True
    app.jinja_env.auto_reload = app.debug

    connect_to_db(app)

    DebugToolbarExtension(app)

    app.run(port=5000, host='0.0.0.0')


# db.create_all()
#
# User.query.delete()
#
# melissa = User(name='melissa', password='12345')
# ashay = User(name='ashay', password='12345')
# ryan = User(name='ryan', password='12345')
#
# db.session.add(melissa)
# db.session.add(ashay)
# db.session.add(ryan)
# db.session.commit()
