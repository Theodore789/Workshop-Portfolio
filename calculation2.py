print("Enter the total bill in pounds e.g. 12.99")
bill = input()
bill = float(bill)
bill_p = int(bill*100)

print("Enter the number of people:")
people = input()
people = int(people)

X = bill_p//people 
if X*people < bill_p:
    X=X+1

X_pounds = X/100

print(f"Each person should pay {X_pounds} so the bill is fully covered.")













