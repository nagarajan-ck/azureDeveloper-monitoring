import logging
from flask import Flask

app = Flask(__name__)
app.logger.setLevel(30)
wsgi_app = app.wsgi_app
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes
#
#logging.Logger.setLevel(level=30)
import FlaskExercise.views