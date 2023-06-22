from dataclasses import dataclass, field


@dataclass
class Store:
    city: str = field(default_factory=str)
    postalCode: str = field(default_factory=str)
    street: str = field(default_factory=str)
    street2: str = field(default_factory=str)
    street3: str = field(default_factory=str)
    addressName: str = field(default_factory=str)
    uuid: str = field(default_factory=str)
    longitude: float = field(default_factory=float)
    latitude: float = field(default_factory=float)
    complexNumber: str = field(default_factory=str)
    showWarningMessage: bool = field(default_factory=bool)
    todayOpen: str = field(default_factory=str)
    locationType: str = field(default_factory=str)
    sapStoreID: str = field(default_factory=str)
    todayClose: str = field(default_factory=str)
    collectionPoint: bool = field(default_factory=bool)


@dataclass
class Location:
    latitude: float = field(default_factory=float)
    longitude: float = field(default_factory=float)


@dataclass
class StoreFinderRequest:
    client_location: Location
