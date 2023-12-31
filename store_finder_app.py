from flask import Flask, request, render_template
from flask_cors import CORS
from pyvalidator import is_lat_long

from src.services import StoreFinderService
from src.validations import StoreFinderRequest, Location
from src.utils import Utils

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route('/store-finder', methods=['GET'])
def find_stores():
    try:
        latitude=float(request.args['latitude'])
        longitude=float(request.args['longitude'])
        if not is_lat_long(str((latitude, longitude))):
            return Utils.custom_error("Invalid latitude and/or longitude", 400)

        client_location = StoreFinderRequest(
            client_location=Location(latitude=latitude, longitude=longitude)
            )

        response = StoreFinderService.find_nearest_stores(client_location)

    except:
        return Utils.custom_error("Please provide valid numeric latitude and longitude values", 400)

    return response
