import csv

class ContractorReport:
    def __init__(self):
        pass
    def add_contractoreports(self, contractorreport):
        try:
            with open("contractorreports.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(contractorreport)
                return True
        except: raise
    def get_contractorReports(self):
        contractorreports = []
        try:
            with open("contractorreports.csv", "r", newline='', encoding='utf-8') as csv_file:
                contractorreports = []
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    contractorreports.append(line)
            return contractorreports      
        except: raise 