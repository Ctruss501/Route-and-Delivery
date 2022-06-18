# Truck class to handle the truck object.
class Truck:
    # Initializing truck object.
    # O(1)
    def __init__(self, packsOnTruckId, toLeave):
        self.packsOnTruckId = packsOnTruckId
        self.toLeave = toLeave
        self.packsOnTruck = []
        self.distanceMiles = 0

    # Loading packages onto the truck.
    # O(1)
    def loadPack(self, package):
        self.packsOnTruck.append(package)

    # Getting the packages that are on the truck.
    # O(1)
    def getPacksOnTruck(self):
        return self.packsOnTruck

    # Increase the number of miles the truck has driven.
    # O(1)
    def increaseMiles(self, increase):
        self.distanceMiles += increase

    # Getting the total miles the truck has driven.
    # O(1)
    def getTotalMiles(self):
        return self.distanceMiles
