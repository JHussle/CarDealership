#discount on cars after purchase.
amount = int(input("Enter Sales Amount: "))

# checking comnditions and calculating discount
# this is temp logic, placeholder

if(amount>0):
    if amount<= 5000:
        discount = amount*0.25
    elif amount<=15000:
        discount = amount*0.30
    elif amount<=25000:
        discount=0.2 * amount
    else:
        discount=0.3 * amount

    print("Discount : ", discount)
    print("Net Pay : ", amount-discount)
else:
    print("Invalid Amount")