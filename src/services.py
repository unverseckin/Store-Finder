import requests
import polyline
from typing import List, Dict

from src.configs import Configs
from src.logics import Calculations
from src.data import DataPreparation
from src.validations import StoreFinderRequest, Location, Store
from src.utils import Utils


class StoreFinderService:
    @staticmethod
    def find_nearest_stores(data: StoreFinderRequest) -> Dict:
        """Find the nearest stores based on the client location.

        Args:
            data (StoreFinderRequest): An object containing the client's location.

        Returns:
            Dict: A dictionary containing information about the nearest stores.

        """
        stores = DataPreparation.obtain_stores_data()
        client_location = data.client_location
        selected_nearby_stores = Calculations.find_distance_from_stores(client_location, stores)
        selected_stores = StoreFinderService._get_distances_from_client_to_store(client_location, selected_nearby_stores)
        solutions = StoreFinderService._get_routes_from_client_to_stores(client_location, selected_stores)

        response = {"NearestStores": []}
        for result in solutions:
            for store in selected_stores:
                if store.sapStoreID == result["store_id"]:
                    store_dict = vars(store)
                    DataPreparation.join_route_to_store(store_dict, result)
                    response["NearestStores"].append(store_dict)

        return response

    @staticmethod
    def _get_distances_from_client_to_store(client_location: Location, selected_nearby_stores: List[Store]) -> List[Store]:
        """Calculates the distances from the client's location to a list of selected nearby stores.

        Args:
            client_location (Location): The location of the client.
            selected_nearby_stores (List[Store]): The list of selected nearby stores.

        Returns:
            List[Store]: The list of stores sorted by distance in ascending order, limited to a desired number of stores.
        """
        base_url = "http://router.project-osrm.org/table/v1/driving/"

        coordinates = "{},{}".format(client_location.longitude,
                                     client_location.latitude)
        for store in selected_nearby_stores:
            coordinates = coordinates + (";{},{}".format(store.longitude,
                                                         store.latitude))

        response = requests.get(base_url + coordinates + "?sources=0&annotations=distance")

        if response.status_code != 200:
            raise Exception("An error occurred while getting OSRM distances")

        else:
            data = response.json()
            store_list_by_distance = [
                (store, distance) for store, distance in zip(selected_nearby_stores, data["distances"][0][1:])
                ]  # we exclude index 0 since it is the client location


        sorted_store_list_by_distance = [
            store[0] for store in sorted(store_list_by_distance, key=Utils.take_distance)
            ]

        return sorted_store_list_by_distance[0:Configs.NUMBER_OF_POTENTIAL_STORES_TO_FIND]

    @staticmethod
    def _get_routes_from_client_to_stores(client_location: Location, selected_stores: List[Store]) -> List[dict]:
        """Retrieve the shortest routes by walking from the client's location to the selected stores.
        Args:
            client_location (Location): The location of the client.
            selected_stores (List[Store]): The list of selected stores.

        Returns:
            List[dict]: A list of dictionaries containing information about the shortest routes from the client to the stores.
                   Each dictionary contains the following keys:
                   - 'profile': The vehicle profile of the route. It contains the following infos:
                       - 'route': A list of coordinates representing the polyline route.
                       - 'start_point': The latitude and longitude of the starting point of the route.
                       - 'end_point': The latitude and longitude of the ending point of the route.
                       - 'distance': The distance of the route in meters.
        """
        base_url = "https://graphhopper.com/api/1/route"

        api_key = "7fa0b8ef-9c94-49e9-9ca6-ff1b98be43a3"

        solutions = []

        profiles = {"car", "bike", "foot"}

        session = requests.Session()
        for store in selected_stores:

            out = {}
            for profile in profiles:
                params = {
                    "point": [f"{client_location.latitude},{client_location.longitude}", f"{store.latitude},{store.longitude}"],
                    "vehicle": profile,
                    "weighing": "shortest",
                    "key": api_key
                }

                # Send GET request to GraphHopper API
                response = session.get(base_url, params=params)

                if response.status_code != 200:
                    raise Exception("An error occurred while getting routes from Graphhopper")

                else:
                    data = response.json()

                    routes = polyline.decode(data["paths"][0]["points"])
                    start_point = [client_location.latitude, client_location.longitude]
                    end_point = [store.latitude, store.longitude]
                    distance = data["paths"][0]['distance']

                    out.update({profile: {'route': routes,
                                          'start_point': start_point,
                                          'end_point': end_point,
                                          'distance': distance,
                                           }
                                })
            out.update({'store_id': store.sapStoreID})
            solutions.append(out)

        solutions.sort(key=lambda x: x["foot"]["distance"])

        return solutions[0: Configs.DESIRED_NUMBER_OF_STORES_TO_FIND]
