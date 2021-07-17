from flask import Flask
from flask_restful import Api

from controllers.blacklist_scan_api import BlacklistScan

app = Flask(__name__)
api = Api(app)

api.add_resource(BlacklistScan, "/v2/blacklist")

if __name__ == "__main__":
    app.run()
