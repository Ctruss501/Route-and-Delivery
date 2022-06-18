# Package class to handle the package object.
class Package:

    # Initializing package object.
    # O(1)
    def __init__(self, packId, addr, city, state, postal, deliverBy, weight, note, toLeave, packDelivered, packStatus, addrId):
        self.packId = packId
        self.addr = addr
        self.city = city
        self.state = state
        self.postal = postal
        self.deliverBy = deliverBy
        self.weight = weight
        self.note = note
        self.toLeave = toLeave
        self.packDelivered = packDelivered
        self.packStatus = packStatus
        self.addrId = addrId

    # Getting the package id.
    # O(1)
    def getPackId(self):
        return self.packId

    # Getting the address for the package.
    # O(1)
    def getAddrId(self):
        return self.addrId

    # Override print with string function so that it will not print the object reference.
    # O(1)
    def __str__(self):
        return "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s" % (self.packId, self.addr, self.city, self.state, self.postal,
                                                     self.deliverBy, self.weight, self.note, self.toLeave,
                                                     self.packDelivered, self.packStatus)
