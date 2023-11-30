import json
import os
import random

import requests

SUBJECTS: list = [
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


def _data_structure(href_city: str):
    """Data structure for the city

    Args:
        href_city (str): href to city

    Returns:
        dict: Data structure for the city
    """
    response_scores = requests.get(f"{href_city}scores")
    data_scores: list = json.loads(response_scores.text)["categories"]
    return {
        subject["name"]: subject["score_out_of_10"]
        for subject in data_scores
        if subject["name"] in SUBJECTS
    }


def _data_from_api():
    """Download data from API and save it to a json file

    Returns:
        dict: Data from API
    """
    url: str = "https://api.teleport.org/api/urban_areas/"
    response = requests.get(url)
    json_file: str = os.path.join(os.path.dirname(__file__), "data.json")

    urban_areas: list = json.loads(response.text)["_links"]["ua:item"]
    data: dict = {
        "count": len(urban_areas),
        "urban_areas": {
            urban_area["name"]: _data_structure(urban_area["href"])
            for urban_area in urban_areas
        },
    }

    # Save data if not exists
    if not os.path.exists(json_file):
        with open(json_file, "w") as outfile:
            json.dump(data, outfile, indent=2)
    return data


def get_data():
    """Get data from json file

    Returns:
        dict: Data from json file
    """
    json_file: str = os.path.join(os.path.dirname(__file__), "data.json")
    if os.path.exists(json_file):
        with open(json_file, "r") as infile:
            data: dict = json.load(infile)
            return data
    return _data_from_api()


def simulate_update_data():
    """Simulate update data

    Returns:
        dict: Data from json file
    """
    json_file: str = os.path.join(os.path.dirname(__file__), "data.json")
    try:
        with open(json_file, "r") as infile:
            data: dict = json.load(infile)
            for city in data["urban_areas"]:
                for subject in data["urban_areas"][city]:
                    current_score = data["urban_areas"][city][subject]
                    change = random.uniform(-0.2, 0.2)
                    new_score = max(min(current_score + change, 10), 0)
                    data["urban_areas"][city][subject] = new_score
            with open(json_file, "w") as outfile:
                json.dump(data, outfile, indent=2)
            return data
    except FileNotFoundError:
        return "Get data first"
