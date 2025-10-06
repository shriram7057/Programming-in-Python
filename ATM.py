balance =0
def check_balance():
    global balance
    print("Your current balance is:", balance)

def deposit(amount):
    global balance
    balance += amount
    print(amount, "Rs. deposited!")

def withdraw(amount):
    global balance
    if balance >= amount:
        balance -= amount
        print(amount, "Rs. withdrawn!")
    else:
        print("Insufficient balance!")

# balance = 0

while True:
    ch = int(input("ENTER CHOICE: \n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit\n"))
    if ch == 1:
        check_balance()
    elif ch == 2:
        d_amt = int(input("Enter the amount you want to deposit: "))
        deposit(d_amt)
    elif ch == 3:
        w_amt = int(input("Enter the amount you want to withdraw: "))
        withdraw(w_amt)
    elif ch == 4:
        print("THANK YOU!")
        break
    else:
        print("INVALID CHOICE!")