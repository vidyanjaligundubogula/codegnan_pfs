''' #Break---> this is used to exit from the loop,when we found the required value...

for j in range(1,10):
    if j == 5:
       break
    print(j) 

#inlists

numbers = [10,20,30,40,50]

for num in numbers:
    print(num)
    if num == 30:
        break 

#continue ---> this is used to skip that particular loop

for j in range(1,10):
    if j == 5:
        continue
    print(j) 

list_ = [5,6,7,8]

for n in list_:
    if n == 7:
        continue
    print(n) 


#pass this is called as space holder
#incase any statement like(if, for, else, elif...) this should complete,if not we will get syntax error to avoid this we are using pass

for j in range(1,100):
    pass 

#for loop --- else it will fall block, when all loops are completed

for m in range(1,10):
    print(m)
else:
    print("else block")  

#while loop ---> this is a combination for and if statements, if we did not,
#end the loop in proper way it will run upto the memory space in the becomes empty
num = 1
while num<5:
    print(num)
    num += 1 '''

#generating fabinocci in series
user_in = int(input("Enter the limits: "))
num_1 = 0
num_2 = 1
print(num_1,num_2)
for v in range(user_in+1):
    num_3 = num_1 + num_2
    num_1 = num_2
    num_2 = num_3
    print(num_3,end=" ")


    


   
