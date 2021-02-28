# single dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

travel_log_1 = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

travel_log = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5
    }
]


def add_new_country(country_visited, times_visited, cities_visited):
    new_country = {"country": country_visited, "total_visits": times_visited, "cities_visited": cities_visited}
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])

print(travel_log)