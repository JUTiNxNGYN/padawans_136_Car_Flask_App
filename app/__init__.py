from flask import Flask

app = Flask(__name__)

from resources.cars import routes
from resources.users import routes