import csv

class LocationData:
    def __init__():
        pass
                
    def get_locations():
        locations = []
        try:
            with open("locations.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    locations.append(line)
            return locations
        except: raise 
