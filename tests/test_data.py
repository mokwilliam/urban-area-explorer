from app.database.data import _data_structure, get_data


def test_data_structure() -> None:
    href_city: str = "https://api.teleport.org/api/urban_areas/slug:paris/"
    expected_data_keys: list = [
        "Housing",
        "Cost of Living",
        "Startups",
        "Venture Capital",
        "Travel Connectivity",
        "Commute",
        "Business Freedom",
        "Safety",
        "Healthcare",
        "Education",
        "Environmental Quality",
        "Economy",
        "Taxation",
        "Internet Access",
        "Leisure & Culture",
        "Tolerance",
        "Outdoors",
    ]
    assert list(_data_structure(href_city).keys()) == expected_data_keys


def test_get_data() -> None:
    expected_data_keys: list = [
        "count",
        "urban_areas",
    ]
    assert list(get_data().keys()) == expected_data_keys
