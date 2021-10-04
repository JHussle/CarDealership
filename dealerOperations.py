import dealerSQLOps as sql
from os import system 
from Customer import Customer
system('cls')

def listCarsOp():
    sql.readVehicleInfo
    

customers = []

def inputCustomerOp():
    fName = input("Enter your first (given) name: ")
    lName = input("Enter your last (family) name: ")
    phone = input("Enter your phone number: ")
    email = input("Please enter your e-mail address: ")
    while True:
        response= input("Are you a veteran or considered a diabled person (documentation required for proof before delivery) Y/N?: ")
        if response.upper() == 'Y':
            vetDisabled = True
            break
        elif response.upper() == 'N':
            vetDisabled = False
            break
        else:
            print("Please select Y/N:")
            
    customer = Customer(fName, lName, phone, email, vetDisabled)
   # customers.append(customer)
    sql.insertCustomerInfo(customer)

inputCustomerOp()