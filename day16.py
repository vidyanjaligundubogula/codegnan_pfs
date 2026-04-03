''' #print a pattern
num = int(input("Enter the limit:"))
for j in range(num):
    for i in range(j):
        print("*",end = "")
    print() 
        

num = int(input("Enter the limit:"))
for j in range(num):
    for i in range(1,j):
        print(i,end = "")
    print() 

num = int(input("Enter the limits: "))#print a square patterns
for j in range(num):
    for i in range(num):
        print("*",end = "")
    print() 

num = int(input("Enter the limits:"))#reverse triangle pattern
for j in range(num):
    for i in range(num-j):
        print("*",end = "")
    print() 

num = int(input("Enter the limits:"))
for j in range(num):
    print(" " *(num-j),end = "")
    print("*") 
          
num = int(input("Enter the limits:"))#print a triangle pattern
for j in range(num):
    print(" " *(num-j),end = "")
    for i in range(j+1):
        print("*",end= " ")
    print()''' 
    
#ATM
ICIC_vidhya_AC_details = {"Name":"vidhya","ATM PIN": "2266","Balance":70000} #Atm pin

print("Welcome to the ICIC ATM")
print("pls insert your ATM card")
ICIC_user_pin = input("pls enter your 4 digits ATM pin: ")
if len(ICIC_user_pin) == 4:
    if ICIC_user_pin in ICIC_vidhya_AC_details['ATM PIN']:
       user_choice=int(input("enter \n 1.withdraw: "))
       if user_choice==1:
          money_w=int(input("enter the amount you want to withdraw: "))
          if money_w<=ICIC_vidhya_AC_details['Balance']:
             ICIC_vidhya_AC_details['Balance']-=money_w
             print(ICIC_vidhya_AC_details['Balance'])
          else:
             print("insufficient balance")
    else:
        print("you have entered invalid pin")
else:
    print("check and enter your 4-digit pin")
        
    

              
