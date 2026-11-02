file =  open("electricity_bill.csv","a+")
file.seek(0)
if file.read()=="":
    file.write ("name,c_a_no,bill_amount\n")
file.close()

file = open ("electricity_bill.csv", "a")

name = input("enter your name ")
c_a_no = input("enter your c_a_no ")
previous_unit = int(input("enter your previous unit "))
current_unit= int (input("enter your current unit "))
# to calculate unit consumed
unit_consumed = current_unit - previous_unit
print("unit consumed : ", unit_consumed)
#electricity chaerge 
if unit_consumed >200:
    electricity_charge = unit_consumed * 15
elif unit_consumed >100:
    electricity_charge = unit_consumed * 10
else:
    electricity_charge = unit_consumed * 3
print ("electricity_charge :" , electricity_charge)
#surcharge 
if electricity_charge >5000:
    surcharge = electricity_charge * 0.05
elif electricity_charge >1000:
    surcharge = electricity_charge *0.03
else:
    surcharge = 0
    print(surcharge)
print ("your charge is : " , surcharge)
bill_amount = electricity_charge + surcharge
print ("your bill amount is : ",bill_amount)

file.write(name + ","+ str(c_a_no) + "," + str(bill_amount) + "\n")
file.close()

file = open("electricity_bill.csv","r")
print(file.read())

print("electricity_bill.csv")
file.close()

