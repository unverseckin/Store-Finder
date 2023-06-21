from typing import List
from haversine import haversine

from configs import Configs
from validations import Location, Store
from utils import Utils


class Calculations:
    @staticmethod
    def find_distance_from_stores(client_location: Location, stores: List[Store]) -> List[Store]:
        """
        Finds the haversine distance from a client's location to a list of stores and returns the nearest stores.

        Args:
            client_location (Location): The location of the client.
            stores (List[Store]): A list of stores to compare the distances with.

        Returns:
            List[Store]: The nearest stores based on the distance from the client's location.

        """

        store_list_by_distance = [
            (store, haversine((client_location.latitude, client_location.longitude),
                              (store.latitude, store.longitude))) for store in stores
                              ]

        sorted_store_list_by_distance = [
            store[0] for store in sorted(store_list_by_distance, key=Utils.take_distance, reverse=False)
            ]

        return sorted_store_list_by_distance[0:Configs.NUMBER_OF_INVESTIGATED_STORES]
