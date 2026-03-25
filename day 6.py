

'''
vowel_con = input("Enter a letter")
if vowel_con in "AEIOUaeiou":
   print("vow")
else:
    print("con")

Time_aday = input("Enter 24 hours time (HH:MM): ")

parts_ = Time_aday.split(":")

hours_ = int(parts_[0])
Min_ = int(parts_[1])

if hours_ >= 13 and Min_ < 60:
    print("Time is valid and in afternoon/evening")
else:
    print("Invalid time or not in expected range")


List are created using space brackets:
example : mylist = ["vidya","san","ram"] 

List =[1,2,3,"python",[1,2,["python", "java"],"Language"]]
print(List[4][2][0][3])


List_1 = [2, 5, 7, "python", "java", [6, 7, 9, ["python", "java"], "c++", "language"]]
print(List_1[5][3][1][2])

List_1 = [2, 5, 7, "python", "java", [6, 7, 9, ["python", "java"], "c++", "language"]]

print(List_1)
1. append()-> Add element at end ..Mutable means can be changed after creation immutable means cannot modify directly on the variable 

nums = [1,2,3]
num_1 =[2,0,4,5]
nums.append(4)
nums.append([5,6])
nums.append("vid")
nums.extend("vid")
nums.extend("2.0")
print(nums)   

#extend() --> this method is used to add multiple items to a list at the end,
#while each element for character in astring is added as a seperate item.
# Definition:
# remove() is a list method used to delete a specific value from a list.
# It removes only the FIRST occurrence of that value 
a = [1,2,3,2]

a.remove(2)  
a.remove(2)

print(a)
'''
# Definition:
# pop() is a list method used to remove an element using its index.
# It also returns the removed element.


a = [10, 20, 30, 40]


a.pop(0)  


print(a)        




      
    

