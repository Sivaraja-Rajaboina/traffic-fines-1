#!/bin/python3


class PoliceNode:

    def __init__(self, police_id, fine_amt):
        self.police_id = police_id
        self.fine_amt = fine_amt
        self.left = None
        self.right = None


class TrafficFines:

    def __init__(self):
        self.driver_hash_table = None

    def initializeHash(self):
        self.driver_hash_table = {}
        print('driver map initialized')

    def insertHash(self, voilations, lic):
        table_lic = self.driver_hash_table.get(lic)
        if table_lic is None:
            self.driver_hash_table[lic] = voilations
        else:
            self.driver_hash_table[lic] = int(table_lic) + int(voilations)

    def printViolators(self, driverhash=None):
        if driverhash is None:
            driverhash = self.driver_hash_table
        voilators = open("violators.txt", "w")
        voilators.write("--------------Violators-------------\n")
        for k, v in driverhash.items():
            if v >= 3:
                voilators.write("{key},{value}\n".format(key = k,value = v))
        voilators.close()

    def destroyHash(self,driverhash):
        if driverhash is None:
            driverhash = self.driver_hash_table
        driverhash.clear()

    def insertByPoliceId(self,policeRoot, policeId, amount):
        pass

    def reorderByFineAmount(self,policeRoot):
        pass

    def printBonusPolicemen(self,policeRoot):
        pass

    def destroyPoliceTree(self,policeRoot):
        pass

    def printPoliceTree(self,policeRoot):
        pass


if __name__ == "__main__":
    traffic_fines = TrafficFines()
    traffic_fines.initializeHash()
    traffic_fines.insertHash(22,'tel1')
    traffic_fines.printViolators()
    print(traffic_fines.driver_hash_table)
