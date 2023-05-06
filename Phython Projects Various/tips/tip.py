bill= float(input("What was the total bill: $ \n"))
tip = int(input("How much will you give as a tip 10%, 20% or 15% \n" ))
people = int(input("How many people to split the bill : \n"))
bill_with_tip= tip/100* bill + bill
bill_per_person = bill_with_tip/people
final_amount = round(bill_per_person)
print(f"Each person should pay {final_amount}")

    
















