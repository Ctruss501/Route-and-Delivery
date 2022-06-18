import csv
from hashTable import *
from package import *

hashTable = HashTable()


# Reading the WGUPSPackages csv file. Creating package object and adding to hash table using key value pair, the id and object.
# O(n)
def getPackages():
    addresses = getDistanceAddresses()
    with open('WGUPSPackages.csv') as packagesCsv:
        packages = csv.reader(packagesCsv, delimiter=',')
        for pack in packages:
            packId = int(pack[0])
            addr = pack[1]
            city = pack[2]
            state = pack[3]
            postal = pack[4]
            deliverBy = pack[5]
            weight = pack[6]
            notes = pack[7]
            packStatus = 'At The Hub'
            toLeave = ''
            packDelivered = ''

            for addrData in addresses:
                if addr == addrData[2].strip():
                    addrId = addrData[0]
                    break
            pack = Package(packId, addr, city, state, postal, deliverBy, weight, notes, packStatus, toLeave, packDelivered, addrId)

            hashTable.insert(packId, pack)
    return hashTable


# Reading the WGUPSDistanceAddresses csv file.
def getDistanceAddresses():
    with open('WGUPSDistanceAddresses.csv') as distanceAddressesCsv:
        distanceAddresses = list(csv.reader(distanceAddressesCsv, delimiter=','))
        return distanceAddresses


# Reading the WGUPSDistances csv file.
def getDistances():
    with open('WGUPSDistances.csv') as distancesCsv:
        distances = list(csv.reader(distancesCsv, delimiter=','))
        return distances


# Getting the hash table.
# O(1)
def getHashTable():
    return hashTable
