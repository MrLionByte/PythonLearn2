###                     List Comprehension:
"""Problem: Squares of Even Numbers
Write a single line of Python code using list comprehension to generate a list containing the squares of even numbers from 1 to 10."""

new_list=[i**2 for i in range(1,11) if i%2==0]
print(new_list)

"""Problem: Filtering Vowels
Given a string, use list comprehension to create a list containing only the vowels present in the string."""

stringg="key of car  is my drea one day"
vovels=[x for x in stringg if x=='a' or x=='e' or x=='i' or x=='o' or x=='u']
print(vovels)

##                  Dictionary Comprehension:
"""Problem: Squares of Numbers as Key-Value Pairs
Write a dictionary comprehension to create a dictionary where keys are numbers from 1 to 5, 
and values are the squares of the corresponding keys."""

dictonory={key:key**2 for (key) in range(1,6)}
print(dictonory)

"""Problem: Extracting Even Numbers
Given a dictionary with integer keys and values, use dictionary 
comprehension to create a new dictionary containing only the key-value pairs where the key is an even number."""

number_dictonary={1:1,2:5,3:3,4:7,5:5,6:9}
even_numbers={key:value for (key,value) in number_dictonary.items() if key%2==0}
print(even_numbers)

##      Set Comprehension:
"""Problem: Squares of Odd Numbers
Generate a set using set comprehension that contains the squares of odd numbers from 1 to 10."""

set={items**2 for items in range(1,11) if items%2==1}
print(set)

"""Problem: Unique Characters in a String
Given a string, create a set using set comprehension to store unique characters present in the string."""

string_input="The syntax is a dictionary comprehension that creates key-value pairs, where the key is the number"
set={unique for unique in string_input }
print(set)

