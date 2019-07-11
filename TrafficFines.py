#!/bin/python3


class PoliceNode:

    def __init__(self, police_id, fine_amt):
        self.police_id = police_id
        self.fine_amt = fine_amt
        self.left = None
        self.right = None


class PoliceRecord:

    def __init__(self, police_id, fine_amt,license_num):
        self.police_id = police_id
        self.fine_amt = fine_amt
        self.license_num = license_num


class TrafficFines:

    def __init__(self):
        self.driver_hash_table = None
        self.root = None
        self.total_fine = 0

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
                voilators.write("{key},{value}\n".format(key=k, value=v))
        voilators.close()

    def destroyHash(self, driverhash):
        if driverhash is None:
            driverhash = self.driver_hash_table
        driverhash.clear()

    def insertByPoliceId(self, policeRoot, policeId, amount):
        if policeRoot is None:
            self.root = PoliceNode(police_id=policeId,fine_amt=amount)
            self.total_fine = amount
        else:
            police_node = self.find_police_id(policeId)
            if police_node is None:
                self._add_with_police_id(policeId,amount,self.root)
                self.total_fine = self.total_fine + amount
            else:
                police_node.fine_amt = police_node.fine_amt + amount
                self.total_fine = self.total_fine + amount
        return self.root

    def _add_with_police_id(self, police_id, amount, node):
        if police_id < node.police_id:
            if node.left is not None:
                self._add_with_police_id(police_id, amount, node.left)
            else:
                node.left = PoliceNode(police_id,amount)
        else:
            if node.right is not None:
                self._add_with_police_id(police_id,amount, node.right)
            else:
                node.right = PoliceNode(police_id,amount)

    def find_police_id(self,police_id):
        if self.root is not None:
            return self._find_police_id(police_id, self.root)
        else:
            return None

    def _find_police_id(self,police_id, node):
        if police_id == node.police_id:
            return node
        elif police_id < node.police_id and node.left is not None:
            self._find_police_id(police_id, node.left)
        elif police_id > node.police_id and node.right is not None:
            self._find_police_id(police_id, node.right)


    def reorderByFineAmount(self, policeRoot):
        if policeRoot is None:
            policeRoot = self.root
        amountRoot = PoliceNode(police_id=policeRoot.police_id,fine_amt=policeRoot.fine_amt)


    def _add_with_fine_amt(self, police_id, amount, node):
        if police_id <= node.police_id:
            if node.left is not None:
                self._add_with_fine_amt(police_id, amount, node.left)
            else:
                node.left = PoliceNode(police_id,amount)
        else:
            if node.right is not None:
                self._add_with_fine_amt(police_id,amount, node.right)
            else:
                node.right = PoliceNode(police_id,amount)

    def printBonusPolicemen(self, policeRoot):
        if policeRoot is None:
            policeRoot = self.root
        max_fine = self._get_max_fine_amt()


    def _get_max_fine_amt(self):
        fine = self.total_fine
        max_fine = fine * 0.9
        return max_fine

    def destroyPoliceTree(self, policeRoot):
        policeRoot = None
        self.root = policeRoot

    def printPoliceTree(self, policeRoot):
        if policeRoot is None:
            policeRoot = self.root
        if policeRoot is not None:
            self._print_police_tree(policeRoot)

    def _print_police_tree(self, node):
        if node is not None:
            self._print_police_tree(node.left)
            print(str(node.police_id) + ' ')
            print(str(node.ammount) + ' ')
            self._print_police_tree(node.right)

    def parse_input_file(self, input_file='inputPS3.txt'):
        input_data = []
        with open(input_file) as reader:
            line = reader.readline()
            while line != '':
                data = line.strip('\n').split('/')
                if len(data) < 3:
                    print('Data is not proper and hence continuing')
                    continue
                input_data.append(PoliceRecord(police_id=int(data[0]), license_num= int(data[1]), fine_amt= int(data[2])))
                line = reader.readline()
            reader.close()
        return input_data


if __name__ == "__main__":
    traffic_fines = TrafficFines()
    traffic_fines.initializeHash()
    input_data = traffic_fines.parse_input_file()
    for fines in input_data:
        traffic_fines.insertHash(fines.fine_amt,fines.license_num)
        traffic_fines.insertByPoliceId(None,fines.police_id,fines.fine_amt)
        traffic_fines.printViolators()
