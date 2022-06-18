import readCSV
from truck import *
from package import *
import datetime
from datetime import timedelta


# Getting the distance between two addresses.
# O(1)
def distanceBetweenAddrs(addr1, addr2):
    distances = readCSV.getDistances()
    distance = distances[addr1][addr2]
    if distance == '':
        distance = distances[addr2][addr1]
    return float(distance)


# Getting the minimum distance between two addresses. Using distanceBetweenAddrs to compare from the list of packages.
# O(n^2)
def minDistanceFrom(fromAddrs, truckPacks):
    minDistance = 0
    for i, pack1 in enumerate(truckPacks):
        for pack2 in truckPacks[i + 1:]:
            distance1 = distanceBetweenAddrs(int(fromAddrs), int(pack1.addrId))
            distance2 = distanceBetweenAddrs(int(fromAddrs), int(pack2.addrId))
            if minDistance == 0:
                minDistance = distanceBetweenAddrs(int(fromAddrs), int(pack1.addrId))
            if distance1 < distance2 and distance1 < minDistance:
                minDistance = distance1
            if distance2 < distance1 and distance2 < minDistance:
                minDistance = distance2
    for i, pack in enumerate(truckPacks):
        if distanceBetweenAddrs(int(fromAddrs), int(truckPacks[i].addrId)) == minDistance:
            return pack


# Sorting the packages by their minimum addresses from one another. When a package is found, it is added to the list and then removed
# from the packsOnTruck list and returns the sorted packages. Breaking after each append because the packages is removed
# and the next time through, a different package will be at index 0.
# O(n)
def sortedPacks(packsOnTruck):
    fromAddr = 0
    sortPacks = []
    while len(packsOnTruck) > 0:
        if len(packsOnTruck) < 2:
            sortPacks.append(packsOnTruck[0])
            break
        pack = minDistanceFrom(fromAddr, packsOnTruck)
        sortPacks.append(pack)
        fromAddr = pack.addrId
        packsOnTruck.remove(pack)
    return sortPacks


# Manually loading three trucks then using sortTruckPacks to have the truck packages sorted by their minimum distance
# from addresses. Fixing the address of package 9.
# O(n)
def loadTruckPacks():
    hashTable = readCSV.getPackages()
    truck1 = Truck([1, 8, 12, 13, 14, 15, 16, 19, 20, 22, 23, 29, 30, 34, 37], timedelta(hours=8, minutes=0, seconds=0))
    truck2 = Truck([3, 6, 7, 10, 18, 21, 24, 25, 26, 28, 31, 32, 36, 38, 40], timedelta(hours=9, minutes=5, seconds=0))
    truck3 = Truck([2, 4, 5, 9, 11, 17, 27, 33, 35, 39], timedelta(hours=10, minutes=30, seconds=0))
    for packId in truck1.packsOnTruckId:
        pack = hashTable.search(packId)
        pack.toLeave = truck1.toLeave
        truck1.loadPack(pack)
    for packId in truck2.packsOnTruckId:
        pack = hashTable.search(packId)
        pack.toLeave = truck2.toLeave
        truck2.loadPack(pack)
    for packId in truck3.packsOnTruckId:
        pack = hashTable.search(packId)
        pack.toLeave = truck3.toLeave
        truck3.loadPack(pack)
    truck1.packsOnTruck = (sortedPacks(truck1.getPacksOnTruck()))
    truck2.packsOnTruck = (sortedPacks(truck2.getPacksOnTruck()))
    truck3.packsOnTruck = (sortedPacks(truck3.getPacksOnTruck()))
    package = hashTable.search(9)
    package.addr = '410 S State St.'
    package.city = 'Salt Lake City'
    package.state = 'UT'
    package.postal = '84111'
    package.addrId = 19
    truckPacksList = [truck1, truck2, truck3]
    return truckPacksList


# Delivering packages on the trucks. Updating the miles, time and hash table.
# O(n^2)
def truckDeliverPackages(trucks, hashTable):
    for i, truck in enumerate(trucks):
        truckLeaving = truck.toLeave
        truckPacks = truck.packsOnTruck
        for pack in truckPacks:
            hashTable.update(pack.packId, updatePack(pack, truckLeaving, 'En Route'))
        for j, pack in enumerate(truckPacks):
            if j == 0:
                distance = distanceBetweenAddrs(0, int(truckPacks[j].addrId)) / 18
                toDeliverBy = datetime.timedelta(hours=distance)
                truckLeaving += toDeliverBy
                truck.increaseMiles(distanceBetweenAddrs(0, int(truckPacks[j].addrId)))
                hashTable.update(truckPacks[j].packId, updatePack(pack, truckLeaving, 'Delivered'))
                continue
            distance = distanceBetweenAddrs(int(truckPacks[j - 1].addrId), int(truckPacks[j].addrId)) / 18
            toDeliverBy = datetime.timedelta(hours=distance)
            truckLeaving += toDeliverBy
            truck.increaseMiles(distanceBetweenAddrs(int(truckPacks[j - 1].addrId), int(truckPacks[j].addrId)))
            hashTable.update(truckPacks[j].packId, updatePack(pack, truckLeaving, 'Delivered'))
            finalPack = hashTable.search(truckPacks[-1].packId)
            if finalPack.packStatus == 'Delivered':
                truck.increaseMiles(distanceBetweenAddrs(0, int(truckPacks[-1].addrId)))
                truckLeaving += toDeliverBy
    return trucks


# Used to update packages.
# O(1)
def updatePack(pack, packDelivered, packStatus):
    packId = pack.packId
    addr = pack.addr
    city = pack.city
    state = pack.state
    postal = pack.postal
    deliverBy = pack.deliverBy
    weight = pack.weight
    note = pack.note
    toLeave = pack.toLeave
    packDelivered = packDelivered
    packStatus = packStatus
    addrId = pack.addrId
    updatedPack = Package(packId, addr, city, state, postal, deliverBy, weight, note, toLeave, packDelivered, packStatus, addrId)
    return updatedPack


# Printing report to show the total miles traveled for all trucks during the deliveries.
# O(n)
def report(truckReport):
    hashTable = readCSV.getHashTable()
    for i in range(1, 41):
        print(hashTable.search(i))
    print('\n' + '\033[34m' + 'Truck 1 Distance: ' + '\033[0m' + str(truckReport[0].getTotalMiles()))
    print('\033[34m' + 'Truck 2 Distance: ' + '\033[0m' + str(truckReport[1].getTotalMiles()))
    print('\033[34m' + 'Truck 3 Distance: ' + '\033[0m' + str(truckReport[2].getTotalMiles()))
    totalMiles = truckReport[0].getTotalMiles() + truckReport[1].getTotalMiles() + truckReport[2].getTotalMiles()
    print('\033[34m' + 'Combined Total Distance Traveled: ' + '\033[0m' + str(totalMiles))
