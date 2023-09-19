from data_manager import DataManager
from flight_search import FlightSearch

dm = DataManager()
fs = FlightSearch()
data = dm.data

for index, row in data.iterrows():
    if str(row['IATA Code']) == "nan":
        dm.update_iata_code(row['City'], index)
        data = dm.data
for index, row in data.iterrows():
    fs.search_fly(row['IATA Code'])
    dm.update_flight_details(index, fs.ticket_price, fs.utc_arrival,
                             fs.airlines, fs.bags_price, row['City'])
print("Everything is Ok ❤️. Check the 'Flight Deals price list'.")
