from flask import Flask, request
from flask_cors import CORS
from pyvalidator import is_lat_long

from service import StoreFinderService
from validations import StoreFinderRequest ,Location
from utils import Utils

app = Flask(__name__)
CORS(app)


@app.route('/store-finder', methods=['GET'])
def find_stores():
    try:
        latitude=float(request.args['latitude'])
        longitude=float(request.args['longitude'])
        if not is_lat_long(str((latitude, longitude))):
            return Utils.custom_error("Invalid input", 400)

        client_location = StoreFinderRequest(
            client_location=Location(latitude=latitude, longitude=longitude)
            )

        response = StoreFinderService.find_nearest_stores(client_location)

    except ValueError:
        return Utils.custom_error("Invalid input", 400)

    return response
