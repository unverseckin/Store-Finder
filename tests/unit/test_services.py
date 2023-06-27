import requests
from unittest.mock import Mock

from validations import Location, Store
from services import StoreFinderService


def test_get_distances_from_client_to_store(monkeypatch):
    client_location = Location(latitude=52.1234, longitude=4.5678)
    selected_nearby_stores = [
        Store(latitude=52.1111, longitude=4.5555),
        Store(latitude=53.2222, longitude=5.6666),
        Store(latitude=51.9876, longitude=4.1234)
    ]
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "distances": [
            [0, 100, 300, 200]
        ]
    }

    monkeypatch.setattr(requests, "get", Mock(return_value=mock_response))

    result = StoreFinderService._get_distances_from_client_to_store(client_location, selected_nearby_stores)

    assert result[0] == selected_nearby_stores[0]
    assert result[1] == selected_nearby_stores[2]
    assert result[2] == selected_nearby_stores[1]
