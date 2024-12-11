
class Property:
    def __init__(self, property_number, condition, additional_maintenance, location):
        self.property_number = property_number
        self.condition = condition
        self.additional_maintenance = additional_maintenance
        self.location = location

    def turn_property_into_list(self):
        return [self.property_number, self.condition, self.additional_maintenance, self.location]
    
    def turn_list_into_property(property: list):
        if len(property) != 4:
            raise ValueError("Something went wrong while decoding properties")
        
        return Property(*property)
    
    def __str__(self) -> str:
        return f"{self.property_number} {self.condition} {self.additional_maintenance} {self.location}"
