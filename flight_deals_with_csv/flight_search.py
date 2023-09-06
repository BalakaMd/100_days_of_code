import requests
from datetime import datetime as dt
from datetime import timedelta as td

today = dt.now() + td(days=1)
str_today = today.strftime("%d/%m/%Y")
str_six_months = (today + td(days=180)).strftime("%d/%m/%Y")


class FlightSearch:
    def __init__(self):
        self.fly_to = None
        self.bags_price = None
        self.airlines = None
        self.ticket_price = None
        self.utc_arrival = None
        self.TEQUILA_ENDPOINT = "https://api.tequila.kiwi.com"
        self.TEQUILA_API_KEY = 'BwhP4CVEOaqTv9OCXHWQg4MpRO7tHOYU'
        self.headers = {"apikey": self.TEQUILA_API_KEY}
        self.fly_from = "TLV"

    def get_destination_code(self, city_name):
        location_endpoint = f"{self.TEQUILA_ENDPOINT}/locations/query"
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint,
                                headers=self.headers,
                                params=query)
        response.raise_for_status()
        code = response.json()['locations'][0]['code']
        return code

    def search_fly(self, fly_to):
        self.fly_to = fly_to
        search_location_endpoint = f"{self.TEQUILA_ENDPOINT}/v2/search"
        query = {"fly_from": self.fly_from,
                 "fly_to": fly_to,
                 "date_from": str_today,
                 "date_to": str_six_months,
                 'one_for_city': 1
                 }
        response = requests.get(url=search_location_endpoint,
                                params=query,
                                headers=self.headers)
        response.raise_for_status()
        try:
            flights_data = response.json()['data'][0]
            print(flights_data)
            self.utc_arrival = flights_data['utc_arrival'].split("T")[0]
            self.ticket_price = flights_data['price']
            self.airlines = flights_data['airlines'][0]
            self.bags_price = flights_data['bags_price']
        except IndexError:
            self.utc_arrival = "None"
            self.ticket_price = 0
            self.airlines = "None"
            self.bags_price = "None"
            return None

