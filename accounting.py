MELON_COST = 1.00

def customer_order(filepath):
    """Calculate cost of melons and determine who has incorrectly paid."""
    #open the file
    file = open(filepath)
    #iterate over lines in file
    for line in file:
        #trim data and split accordingly
        customerData = line.rstrip()
        customerLst = customerData.split("|")
        #get customer ide, name, quanity purchased, price paid
        orderID, name, quantity, paid = customerLst
        #calculate expected cost
        expectedPrice = float(quantity) * MELON_COST
        #print amount expected vs actually paid
        if expectedPrice != float(paid):
            print(f"{name} paid ${float(paid):.2f} \nexpected ${expectedPrice:.2f}")
            #determine if the payment is under or over expected amount
            paymentStatus = 'over' if expectedPrice < float(paid) else 'under'
            print(f"{name} has {paymentStatus}paid for their melons.\n")

    #close file
    file.close()

#call the function
customer_order("customer-orders.txt")