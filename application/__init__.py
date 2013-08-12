
from flask import Flask

app = Flask(__name__)

try:
    import sae
    kvdb = sae.kvdb.KVClient(debug=0)
except:
    pass

@app.before_request
def before_request():
    pass

@app.teardown_request
def teardown_request(exception):
    print exception

from application.views import index
from application.views import oneday

import application.apps.oneday.base
import application.apps.oneday.map_api
import application.apps.oneday.getLine
