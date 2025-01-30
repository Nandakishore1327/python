class bank:
    print("WELCOME TO ABC BANK")
    acno = int(input("ENTER YOUR CUSTOMER NUMBER:"))
    pin = int(input("ENTER YOUR PIN:"))
    bal = int(input("ENTER YOUR BALANCE:"))
    def cust(self):
        p = int(input("ENTER YOUR 4 DIGIT PIN"))
        self.choices(p)
    def choices(self,p):
        print("Press 1 to deposit")
        print("Press 2 to withdraw")
        print("Press 3 to display balance")
        print("Pres 4 to exit")
        c = int(input())
        if c != 4:
            if self.pin == p:
                print("YOUR AC NO IS: ", self.acno)
                if c == 1:
                    print("AMOUNT TO BE DEPOSITED")
                    am = int(input())
                    self.bal = self.bal + am
                if c == 2:
                    print("AMOUNT TO BE WITHDRAWED")
                    wd = int(input())
                    if self.bal - wd > 1000:
                        self.bal = self.bal - wd
                    else:
                        print("INSUFFICIENT FUND")
                        print("IT VIOLATE THE MINIMUM BALANCE OF THE ACCOUNT")
                        print("Available balance is:",self.bal)
                if c == 3:
                    print("YOUR BALANCE IS :", self.bal)
            else:
                print("YOU ENTERED WRONG PASSWORD")
            print("Do you want to continue transaction:")
            confirm = input().lower()
            if confirm == 'yes':
                self.choices(p)

if __name__ == "__main__":
 print("CUSTOMER ONE")
 a=bank()
 a.cust()
 print("CUSTOMER TWO")
 b=bank()
 b.cust()

