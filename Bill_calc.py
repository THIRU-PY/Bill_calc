bill=input("What is the bill amount(INR)\n")
per=input("How much percentage of tip do you want to give(10,15 or 20)\n")
Con_bill=int(bill)
Con_per=int(per)
if (Con_per==10 or Con_per==15 or Con_per==20):

    tip=Con_bill*(10/100)
    amount_to_pay=Con_bill+tip
    round(amount_to_pay,2)
    print(f"Amount To Pay = Rs.{amount_to_pay}")


else:

    print("You can only tip 10 15 or 20 percent of the Con_bill!!")
