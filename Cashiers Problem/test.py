import sys


class CashRegister:

    def __init__(self, pp, cash):
        self.purchase_price = pp
        self.cash = cash
        self.change = {}
        # self.self.change = {'ONE HUNDRED': 0,
        #                'FIFTY': 0,
        #                'TWENTY': 0,
        #                'TEN': 0,
        #                'FIVE': 0,
        #                'TWO': 0,
        #                'ONE': 0,
        #                'HALF DOLLAR': 0,
        #                'QUARTER': 0,
        #                'DIME': 0,
        #                'NICKEL': 0,
        #                'PENNY': 0
        #                }

    def calculate_change(self, diff):
        while diff >= 0.01:
            if diff >= 100:
                if self.change.has_key('ONE HUNDRED'):
                    self.change['ONE HUNDRED'] += 1
                else:
                    self.change['ONE HUNDRED'] = 1
                # self.change.append("ONE HUNDRED")
                diff = diff - 100
            elif diff >= 50:
                if self.change.has_key('FIFTY'):
                    self.change['FIFTY'] += 1
                else:
                    self.change['FIFTY'] = 1
                # self.change.append("FIFTY")
                diff = diff - 50
            elif diff >= 20:
                if self.change.has_key('TWENTY'):
                    self.change['TWENTY'] += 1
                else:
                    self.change['TWENTY'] = 1
                # self.change.append("TWENTY")
                diff = diff - 20
            elif diff >= 10:
                if self.change.has_key('TEN'):
                    self.change['TEN'] += 1
                else:
                    self.change['TEN'] = 1
                # self.change.append("TEN")
                diff = diff - 10
            elif diff >= 5.00:
                if self.change.has_key('FIVE'):
                    self.change['FIVE'] += 1
                else:
                    self.change['FIVE'] = 1
                # self.change.append("FIVE")
                diff = diff - 5
            elif diff >= 2.00:
                if self.change.has_key('TWO'):
                    self.change['TWO'] += 1
                else:
                    self.change['TWO'] = 1
                # self.change.append("TWO")
                diff = diff - 2
            elif diff >= 1.00:
                if self.change.has_key('ONE'):
                    self.change['ONE'] += 1
                else:
                    self.change['ONE'] = 1
                # self.change.append("ONE")
                diff = diff - 1
            elif diff >= 0.50:
                if self.change.has_key('HALF DOLLAR'):
                    self.change['HALF DOLLAR'] += 1
                else:
                    self.change['HALF DOLLAR'] = 1
                # self.change.append("HALF DOLLAR")
                diff = diff - 0.50
            elif diff >= 0.25:
                if self.change.has_key('QUARTER'):
                    self.change['QUARTER'] += 1
                else:
                    self.change['QUARTER'] = 1
                # self.change.append("QUARTER")
                diff = diff - 0.25
            elif diff >= 0.10:
                if self.change.has_key('DIME'):
                    self.change['DIME'] += 1
                else:
                    self.change['DIME'] = 1
                # self.change.append("DIME")
                diff = diff - 0.10
            elif diff >= 0.05:
                if self.change.has_key('NICKEL'):
                    self.change['NICKEL'] += 1
                else:
                    self.change['NICKEL'] = 1
                # self.change.append("NICKEL")
                diff = diff - 0.05
            elif diff >= 0.01:
                if self.change.has_key('PENNY'):
                    self.change['PENNY'] += 1
                else:
                    self.change['PENNY'] = 1
                # self.change.append("PENNY")
                diff = diff - 0.01

        return self.change

    def print_change(self):
        diff = self.cash - self.purchase_price
        print diff
        self.change = self.calculate_change(diff)
        # self.change.keys().sort()
        for key in sorted(self.change.iterkeys()):
            print "%s: %s" % (key, self.change[key])
        pass


def main():
    if len(sys.argv) is not 3:
        print "Invalid Arguments"
    else:
        purchase_price = float(sys.argv[1])
        cash = float(sys.argv[2])
        if purchase_price > cash:
            print "ERROR"
        elif purchase_price == cash:
            print "ZERO"
        else:
            cr = CashRegister(purchase_price, cash)
            cr.print_change()


if __name__ == '__main__':
    main()
