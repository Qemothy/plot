from typing import Dict
from constants import *


class Spot():
    def __init__(self, id, spot_type, available=True):
        self.id = id
        self.type = spot_type
        self.available = available
        

    def get_id(self):
        return self.id
    
    def is_available(self):
        return self.available
    
    def set_availability(self, available: bool):
        self.available = available
    
    def get_type(self):
        return self.type


class Display():
    def update_display(free_spots):
        pass

class Floor():
    def __init__(self,level: int, display_ammount, total_spots: int, spots_per_type: Dict[VehicleType,int]):
        self.level = level
        self.display_ammount = display_ammount
        self.total_spots = total_spots
        self.free_spots = spots_per_type
        self.spots_per_type = spots_per_type
        
        self.floor_spots = dict()
        self.__instantiate_spots()
        
        self.displays = []
        self.__instantiate_displays()
    
    

    def __instantiate_spots(self):
        for spot_type, ammount in self.spots_per_type:
            self.floor_spots[spot_type] = dict()
            for id in range(ammount):
                self.floor_spots[spot_type][id] = Spot(id, spot_type)
    
    def __instantiate_displays(self, display_ammount):
        
        for display in self.displays_ammount:
            self.displays.append(Display())

    def update_displays(self):
        for display in self.displays:
            display.update_display(self.free_spots)


    def find_spot(self, spot_type):
        if self.get_free_spots(spot_type) > 0:
            for spot in self.floor_spots[spot_type]:
                if spot.is_available():
                    return spot
        return None

    
    def assign_to_spot(self, spot_type: VehicleType):
        spot_to_be_taken = self.find_spot(spot_type)
        if spot_to_be_taken:
            spot_to_be_taken.set_availability(False)
            self.decrement_free_spots(spot_type)
            self.update_displays()
            return spot_to_be_taken.get_id()
        return False
    

    def release_spot(self, id: int, spot_type: VehicleType):
        self.floor_spots[spot_type][id].set_availability(True)
        self.increment_free_spots(spot_type)
        self.update_displays()
        return True
    


class Ticket:
    def __init__(self, vehicle=None, parking_floor=None, spot_type=None, spot_id=None):
        self.vehicle
        self.parking_floor
        self.spot_type
        self.spot_id
    
    def set_vehicle(self, vehicle):
        self.vehicle = vehicle

    def set_parking_floor(self, level):
        self.parking_floor = level

    def set_spot_type(self, spot_type):
        self.spot_type = spot_type

    def set_spot_id(self, spot_id):
        self.spot_id = spot_id




class Parking:

    def __init__(self, name, address, floors_amount:int):
        self.name = name
        self.address = address
        self.floors_amount = floors_amount
        self.__instantiate_floors()
    
    def __instantiate_floors(self):
        self.floors = []
        for floor_level in self.floors_amount:
            self.floors.append(self.create_single_floor(floor_level))
    

    def create_single_floor(self, floor_level):
        level = floor_level
        display_ammount = self.set_floor_displays(floor_level)
        total_spots = self.set_floor_total_spots(floor_level)
        spots_per_type = self.set_floor_spots_per_type(floor_level)
        return Floor(level, display_ammount, total_spots, spots_per_type)


    def set_floor_displays(self, floor_level)-> int:
        pass
    
    def set_floor_total_spots(self, floor_level)-> int:
        pass
    
    def set_floor_spots_per_type(self, floor_level) -> dict[VehicleType,int]:
        pass
