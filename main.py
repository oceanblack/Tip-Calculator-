#TIP Caculator
print("welcome to the tip caculator")

bill = float(input("what was the total bill $"))

tip = int(input("how much  tip would you like to give 10,12,or 15"))
          
people = int(input("How many people to split the bill"))
#bill_with_tip = tip / 100 * bill + bill alternate 
tip_as_percent = tip / 100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")