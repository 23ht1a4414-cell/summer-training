'''
An E-commerence company wants to vallidate order processing
the system should be
raise exeception if:
1.stock unavailable
2.payment failed
3.address is empty
if all validation pass:
print("order successfully placed")

'''
class OrderException(Exception):
    pass

stock = input("Stock available (yes/no): ")
payment = input("Payment successful (yes/no): ")
address = input("Enter address: ")

if stock == "no":
    raise OrderException("Stock unavailable")

if payment == "no":
    raise OrderException("Payment failed")

if address == "":
    raise OrderException("Address is empty")

print("Order successfully placed")

