"""Simple Arithmetic:
Create a lambda function that takes two parameters and returns their sum."""

entry_one=int(input("Enter 1st number :"))
entry_two=int(input("Enter 2nd number :"))
sum=lambda a,b:a+b
print(sum(entry_one,entry_two))

"""Even or Odd:
Write a lambda function to check if a given number is even or odd."""

user_input=int(input("Enter a number :"))
result=lambda a:"even" if a%2==0  else "odd" 
print(result(user_input))

"""String Reversal:
Define a lambda function to reverse a given string."""

User_input=str(input("enter a word"))
x=lambda a: a[::-1]
print(x(User_input))

"""Filtering Numbers:
Use a lambda function with filter to extract even numbers from a list."""

lis1=[1,2,3,4,5,56,6,67,7,87,98]
even_numbers=list(filter(lambda x:x%2==0,lis1))
print(even_numbers)

"""Dictionary Sorting:
Sort a list of dictionaries based on a specific key using a lambda function."""

dict_test=[
    {"7th":28,"age":14},
    {"9th":30,"age":16},
    {"6th":26,"age":12},
    {"8th":28,"age":15}
]
user=str(input("Key Word"))
final_test_sorted=sorted(dict_test,key=lambda x:x[user],reverse=True)

for i in final_test_sorted:
    print(i)
#find prime numbers:
k=[i for i in range(0,100)]
print(k)
new=[]
for i in k:
    flag=0
    length=int((i/2)+1)
    if i<2:
        continue
    else:
        for j in range(2,length):
            if i%j==0:
                flag=1
                break
            else:
                flag=0
    if flag==0:
        new.append(i)

print(new)