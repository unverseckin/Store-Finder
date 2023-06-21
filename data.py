import json

from validations import Store


class DataPreparation:
    @staticmethod
    def obtain_stores_data():
        with open('/home/seckinunver/Jumbo/stores.json') as store_data:
            raw_data = store_data.read()
            data = json.loads(raw_data)
        stores = [Store(**store) for store in data["stores"]]
        for store in stores:
            store.latitude = float(store.latitude)
            store.longitude = float(store.longitude)
        return stores

    @staticmethod
    def join_route_to_store(store: dict, route: dict):
        store.update({"shortestPath": route})