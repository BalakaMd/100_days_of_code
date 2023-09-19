import pandas as pd
from flight_search import FlightSearch
from notification_manager import NotificationManager

nm = NotificationManager()


def get_flight_data_from_csv():
    with open('Flight Deals - prices.csv') as file:
        new_data = pd.DataFrame(pd.read_csv(file))
        return new_data


def get_user_data_from_csv():
    with open('users_data.csv') as file:
        new_data = pd.DataFrame(pd.read_csv(file))
        return new_data


class DataManager:
    def __init__(self):
        self.data = get_flight_data_from_csv()
        self.user_data = get_user_data_from_csv()
        self.iata_search = FlightSearch()

    def update_iata_code(self, city_name, row_id):
        flight_iata = self.iata_search.get_destination_code(city_name)
        self.data.at[row_id, 'IATA Code'] = flight_iata
        self.data.at[row_id, 'Lowest Price'] = "None"
        self.data.to_csv('Flight Deals - prices.csv', index=False)

    def update_flight_details(self, row_id, lowest_price, utc_arrival, airlines, bags_price, city):
        if self.check_price_drop(row_id, lowest_price, utc_arrival, airlines, bags_price, city):
            self.data.at[row_id, 'Lowest Price'] = lowest_price
            self.data.at[row_id, 'UTC Arrival'] = utc_arrival
            self.data.at[row_id, 'Airlines'] = airlines
            self.data.at[row_id, 'Baggage Price'] = str(bags_price)
            self.data.to_csv('Flight Deals - prices.csv', index=False)

    def check_price_drop(self, row_id, new_price, utc_arrival, airlines, bags_price, city):
        old_price = self.data.at[row_id, 'Lowest Price']
        if old_price == 'None':
            return True
        else:
            if old_price > new_price:
                nm.send_message(new_price, old_price, utc_arrival, airlines, bags_price, city)
                return True
            else:
                return False


data = DataManager()
get_flight_data_from_csv()
