while True:
	out = input("Please insert card into machine followed by your account number :")
	if out == '0000000' : break
	print(out)

user = {
    'pin': 2095,
    'balance':7000,
}


def withdraw_cash():
    while True:
        amount = int(input("Enter the amount of money you would like to widthdraw: "))
        if amount > user['balance']:
            print("You don't have sufficient funds to make this widthdrawal")
        else:
            user['balance'] = user['balance'] - amount
            print(f"{amount} Funds successfully widthdrawn your remaining balance is {user['balance']} Dollars")
            print('')
            return False

def check_balance():
    print(f"Total balance {user['balance']} Dollars")
    print('')
    
def transfer_funds():
		while True:
				amount = int(input("Enter the amount of funds you would like to transfer: "))
				if amount > user['balance']:
						print("You don't have sufficient funds to make this transfer'")
				else:
						user['balance'] = user['balance'] - amount
						print("Enter the account number of the transfer recipient")
						print(f"{amount} Account number was succesfully entered and transfer was approved your remaining balance is {user['balance']} Dollars")
						print('')
						return False
						
def deposit_funds():
    while True:
        amount = int(input("Enter the amount of funds you would like to deposit: "))
        if amount > user['balance']:
            print('')
        else:
            user['balance'] = user['balance'] + amount
            print(f"{amount} Funds were succesfully deposited your new available balance is {user['balance']} Dollars")
            print('')
            return False
            
def atm_technician():
    while True:
        amount = int(input("Thank you for reporting an issue: "))
        print('')
        return False
        
def _quit():
    while True:
        amount = int(input("Thank you and have a nice day: "))
        print('')
        return False
						


is_quit = False

print('')
print("Welcome to the ButterScotch ATM service")

pin = int(input('Please enter your four digit pin: '))

if pin == user['pin']:
    while is_quit == False:
        print("what would you like to do")
        print("Enter 1 to Widthdraw Cash") 
        print("Enter 2 to Check Balance")
        print("Enter 3 to Transfer Funds")
        print("Enter 4 to Deposit Funds")
        print("Enter 5 to report a fault to our ATM technician")
        print("Enter 6 to Quit")

        query = int(input("Enter the number corresponding to the activity you would like to perform: "))

        if query == 1:
            withdraw_cash()
        elif query == 2:
            check_balance()
        elif query == 3:
            transfer_funds()
        elif query == 4:
        	  deposit_funds()
        elif query == 5:
        	  atm_technician()
        elif query == 6:
        	  _quit()

        else:
            print("Please enter the corresponding value shown")
else:
    print("Entered incorrect pin")
