#login system
class LoginSystem(Exception):
    pass

username = input()
password = input()

if username != "admin" or password != "admin123":
    raise LoginSystem("Invalid credentials")

print("Login successful")

#Accept account balance and withdrawal amount
# raise the exeception if
#1.withdrawl amount is -ve
#2.withdrawl amount exceeds balance
#3.withdrawl amount exceeds daily limit of 25000
#4.display remaining balance if transaction successful

class WithdrawalException(Exception):
    pass
Balance = int(input("Enter account balance:"))
withdrawal_amount = int(input("Enter withdrawal amount:"))
daily_limit = 25000
try:
    if withdrawal_amount < 0:
        raise WithdrawalException("Withdrawal amount cannot be negative.")
    elif withdrawal_amount > Balance:
        raise WithdrawalException("Withdrawal amount exceeds account balance.")
    elif withdrawal_amount > daily_limit:
        raise WithdrawalException("Withdrawal amount exceeds daily limit of 25000.")
    else:
        Balance -= withdrawal_amount
        print("Transaction successful. Remaining balance:", Balance)
except WithdrawalException as e:
    print("Error:", e)


 