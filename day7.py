'''


a = [10 , "hello", 3.5, True]


print(type(a[10]))  # int
print(type(a[1]))   # str
print(type(a[2]))   # float
print(type(a[3]))   # list
print(type(a[4]))   # int
print(type(a[5]))   # str
print(type(a[6]))   # list
print(type(a[7]))   # int
print(type(a[8]))   # list  



print(9+8)
print("python" + " programming")
print([1,2]+[3,4])


#concatination

#Joining two or more values with '+' value.

case -1

#you can concatenate only same data types

print("Hello" + "World") #string + string
print([1,2] +[3,4])       #list + list
print(10 + 20)           #int + int

case-2

#** if we try to concatenate two different data types it will give type error

# print("Hello" + 10) #Error (beacacuse str and int) 

tuple() 
#A tuple is a collection which is ordered and unchangable.

#Tuples are written with round brackets. 

Thing = (1, "vidya", [3,4], (6,7))  

Thing =(12,89,"python",(23,"Teja",[67,"python is a language",(7,8), (8, ("python", [34, 9]))]))
print(Thing[3][2][1][9]) 

Num = 9
NUM_2 = 90
print(f"before swapping Num =(Num) and Num_2 =(Num_2)") 
Num, Num_2 = Num_2, Num
print(f"After swapping Num = (Num) and Num_2 =(Num_2)") '''


leap_year = int(input("Enter Year: "))
if (leap_year % 4 ==0 and leap_year % 100 != 0) or leap_year % 400 == 0:
      print(f"yes, (leap_year) is a leap year")

else:
    print(f"No, (leap_year) is not leap year ")


