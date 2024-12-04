import csv

class EmployeeData:
    def __init__(self):
        pass
    def add_employee(self, employee):
        try:
            with open("employees.csv", "a", newline='', encoding='utf-8') as csv_file:
                csv_file.write(employee)
                return True 
        except: raise 
            
    def get_employees(self):
        employees = []
        try:
            with open("employees.csv", "r", newline='', encoding='utf-8') as csv_file:
                csv_reader = csv.reader(csv_file)
                for line in csv_reader:
                    employees.append(line)
            return employees
        except: raise 
    def get_singular_employee(self, employee, newline='', encoding='utf-8'): 
        try:    
                with open("employees.csv", "r") as csv_file:
                    for line in csv_file:
                        line = line.split(",")
                        if self in line[0]:
                            return line
            
        except: raise  