import json
from typing import List

from validations import Store


class DataPreparation:
    @staticmethod
    def obtain_stores_data() -> List[Store]:
        """Reads store data from a JSON file and returns a list of Store objects.

        Returns:
            list: A list of Store objects.

        Raises:
            FileNotFoundError: If the specified file path is invalid or the file doesn't exist.
            JSONDecodeError: If there is an issue parsing the JSON data.
            ValueError: If there is an issue converting latitude or longitude values to float.

        """
        with open('/home/seckinunver/Jumbo/stores.json') as store_data:
            raw_data = store_data.read()
            data = json.loads(raw_data)
        stores = [Store(**store) for store in data["stores"]]
        for store in stores:
            store.latitude = float(store.latitude)
            store.longitude = float(store.longitude)
        return stores

    @staticmethod
    def join_route_to_store(store: dict, route: dict) -> None:
        """Updates the 'store' dictionary with the 'route' dictionary, adding a key 'shortestPath'.

        Args:
            store (dict): The store dictionary to be updated.
            route (dict): The route dictionary to be added.

        Returns:
            None: The function does not return a value directly. It modifies the 'store' dictionary in-place.
        """

        store.update({"shortestPath": route})