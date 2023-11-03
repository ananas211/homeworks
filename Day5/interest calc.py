#balance

#balance at beginning
balance = float(input("enter your balance:; "))

#calculate percentage 24 months
rate = (balance / 100) * 1.5 * 24

#final balance + interest for 24 months
balance2 = float(input("How much money is in your account after 2 years?: "))
print("Next month your balance will be " + str(rate + balance2))