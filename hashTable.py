# Hash Table class.
class HashTable:

    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Creating a hash key.
    # O(1)
    def hash(self, key):
        hashValue = int(key) % len(self.table)
        return hashValue

    # Inserting a package into the hash table.
    # O(n)
    def insert(self, key, package):
        # get the bucket list where this item will go.
        bucket = self.hash(key)
        bucketList = self.table[bucket]
        keyValue = [key, package]
        bucketList.append(keyValue)
        return True

    # Updating a package in the hash table if it is found.
    # O(n)
    def update(self, key, package):
        bucket = self.hash(key)
        bucketList = self.table[bucket]
        for keyValue in bucketList:
            if keyValue[0] == key:
                keyValue[1] = package
                return True

    def search(self, key):
        bucket = self.hash(key)
        bucketList = self.table[bucket]
        for keyValue in bucketList:
            if keyValue[0] == key:
                return keyValue[1]
        return None

    # Getting the package from the hash table if it is found.
    # O(n)
    def get(self, key):
        bucket = self.hash(key)
        bucketList = self.table[bucket]
        for keyValue in bucketList:
            if keyValue == key:
                return keyValue[1]

        return None

    # Removing the package from the hash table if it is found.
    # O(n)
    def remove(self, key):
        bucket = self.hash(key)
        bucketList = self.table[bucket]
        for keyValue in bucketList:
            # print (key_value)
            if keyValue[0] == key:
                bucketList.remove([keyValue[0], keyValue[1]])
