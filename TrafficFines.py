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
            policeRoot = PoliceNode(police_id=policeId,fine_amt=amount)
            self.total_fine = amount
        else:
            police_node = self.search_police_node(policeRoot,policeId)
            if police_node is None:
                self._add_with_police_id(policeId,amount,policeRoot)
                self.total_fine = self.total_fine + amount
            else:
                police_node.fine_amt = police_node.fine_amt + amount
                self.total_fine = self.total_fine + amount
        self.root = policeRoot
        return policeRoot

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

    def search_police_node(self, root, police_id):
        if root is None or root.police_id == police_id:
            return root
        if root.police_id < police_id:
            return self.search_police_node(root.right,police_id)
        return self.search_police_node(root.left, police_id)

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
        current = policeRoot
        stack = []
        bonus = open('bonus.txt','w')
        bonus.write('-------------- Bonus -------------\n')
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                if current.fine_amt >= max_fine:
                    bonus.write("{key},{value}\n".format(key=current.police_id, value=current.fine_amt))
                current = current.right
            else:
                break
        bonus.close()

    def _get_max_fine_amt(self):
        fine = self.total_fine
        max_fine = fine * 0.9
        return max_fine

    def destroyPoliceTree(self, policeRoot):
        policeRoot.right = None
        policeRoot.left = None
        policeRoot.police_id = None
        policeRoot.fine_amt = None
        self.root = policeRoot

    def printPoliceTree(self, policeRoot=None):
        if policeRoot is None:
            policeRoot = self.root
        if policeRoot is not None:
            self._print_police_tree(policeRoot)

    def _print_police_tree(self, node):
        if node is not None:
            self._print_police_tree(node.left)
            print('Police Id: ' +str(node.police_id) + ' Fine Amount: '+str(node.fine_amt))
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
    root = None
    for fines in input_data:
        traffic_fines.insertHash(fines.fine_amt, fines.license_num)
        root = traffic_fines.insertByPoliceId(root, fines.police_id, fines.fine_amt)
    traffic_fines.printViolators()
    traffic_fines.printBonusPolicemen(root)
    traffic_fines.printPoliceTree()
    print('police tree destroy initialized')
    traffic_fines.destroyPoliceTree(root)
    traffic_fines.printPoliceTree(root)
