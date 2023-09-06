from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fl = FlightSearch()
sheet_data = dm.get_destination_data()
print(sheet_data)

for city in sheet_data:
    print(city['id'])
    if city['iataCode'] == "":
        dm.update_shetty_iata(city['city'], city['id'])
    fl.search_fly(city['iataCode'])
    dm.update_shetty_flight_data(city['id'], fl.utc_arrival, fl.ticket_price, fl.airlines, fl.bags_price)

