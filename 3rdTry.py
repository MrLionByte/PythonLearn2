#####               Sample Method questions                     #####

"""Method for Area Calculation:
Create a method named calculate_area that takes the radius of a circle as a parameter and returns the area of the circle."""

def calculate_area(r):
    #pie=3.14
    area=3.14*(r**2)
    return area

user_input=int(input("Enter circle radius :"))
print(calculate_area(user_input),"cm2")    

"""Method for String Reversal:
Write a method named reverse_string that takes a string as input and returns the reversed version of the string."""

def reversal_method(input):
    return input[::-1]

user_input=str(input("Enter a word"))
print (reversal_method(user_input))

"""Method for Even or Odd:
Create a method named check_even_odd that takes an integer as a parameter and prints whether the number is even or odd."""

def input_checker(input):
    if input%2==1:
        print("It is odd")
    else: 
        print("It is Even")

user_input=int(input("Enter the number :"))
input_checker(user_input)

"""Method for List Sum:
Write a method named sum_list that takes a list of numbers as a parameter and returns the sum of all the elements in the list."""

class Solution:
    def sum_list(self, list1):
        return sum(list1)
    
p1=Solution()
answer=p1.sum_list(list1=[1,2,5,3,4,6,86,7,94,5,62,35,66])
print(answer)

"""Method for Dictionary Update:
Create a method named update_dict that takes a dictionary and key-value pairs as parameters and 
updates the dictionary with the new key-value pairs."""

def update_dict(details,changer,insert):
    details[changer]=insert
    return details

personal={
    "name":"fmn",
    "age":"23",
    "place":"irumbuzhi",
    "stack":"python"
}
change=str(input("Enter key to be changed :"))
data=str(input("Enter the data :"))
print(update_dict(personal,change,data))