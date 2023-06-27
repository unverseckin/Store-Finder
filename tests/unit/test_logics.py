from logics import Calculations
from validations import Location, Store


def test_find_distance_from_stores():
    client_location = Location(latitude=52.1234, longitude=4.5678)
    stores = [
        Store(latitude=52.1111, longitude=4.5555),
        Store(latitude=53.2222, longitude=5.6666),
        Store(latitude=51.9876, longitude=4.1234)
    ]

    result = Calculations.find_distance_from_stores(client_location, stores)

    assert result[0] == stores[0]
    assert result[1] == stores[2]
    assert result[2] == stores[1]
