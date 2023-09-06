import requests
from flight_search import FlightSearch


class DataManager:
    get_data_from_sheety_url = 'https://api.sheety.co/56967c3701d5f22d04594e57bb8b8627/flightDeals/prices'
    flight_iata_search = FlightSearch()

    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices = None
        self.response = requests.get(url=self.get_data_from_sheety_url)
        self.sheety_data = self.response.json()
        print(self.sheety_data)

    def get_destination_data(self):
        self.prices = [price for price in self.sheety_data['prices']]
        return self.prices

    def update_shetty_iata(self, city_name, row_id):
        flight_iata = self.flight_iata_search.get_destination_code(city_name)
        put_body = {'price': {
            'iataCode': flight_iata,
        }
        }
        put_sheety_data_url = f'https://api.sheety.co/56967c3701d5f22d04594e57bb8b8627/flightDeals/prices/{row_id}'
        response = requests.put(url=put_sheety_data_url, json=put_body)
        response.raise_for_status()

    def update_shetty_flight_data(self, row_id, utc_arrival, ticket_price, airlines, bags_price):
        put_body = {'price': {
            'utcArrival': utc_arrival,
            'ticketPrice': ticket_price,
            'airlines': airlines,
            'baggagePrice': bags_price
        }
        }
        put_sheety_data_url = f'https://api.sheety.co/56967c3701d5f22d04594e57bb8b8627/flightDeals/prices/{row_id}'
        response = requests.put(url=put_sheety_data_url, json=put_body)
        response.raise_for_status()
