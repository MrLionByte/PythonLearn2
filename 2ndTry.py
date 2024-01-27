"""Problem 1: List Manipulation
Write a program that initializes a list of numbers and then performs the following operations:"""

user_list=[1,2,5,4,8,6,3,7,9,4]
#Add a new number to the end of the list.
new_number=int (input("Enter the number to be added :"))
user_list.append(new_number)
print(user_list)
#Insert a number at a specific position in the list.
insert_input=int (input("Enter the number to be added :"))
user_list.insert(3, insert_input)
print(user_list)
#Remove a number from the list.Print the final list.
user_list.remove(8)
print(user_list)

"""Problem 2: List Sorting
Create a list of names and implement a program that sorts the list alphabetically. Print the sorted list."""

user_list=['Tiny','Miny','Ciny','viny']
print(sorted(user_list))

"""Problem 3: List Filtering Given a list of numbers, write a program that filters out the even numbers and
creates a new list with only the odd numbers.Print the original list and the filtered list."""

user_list=[1,4,8,9,6,5,7,2,6,4,5,8]
result=[]
for i in user_list:
     if i%2==1:
          result.append(i)

print(user_list)
print (result)
            #OR
print([i for i in user_list if i%2==1])

"""Problem 4: List Searching
Implement a program that searches for a specific element in a list. Print whether the element is found in the list or not."""

user_list=[3,'me','you',44,6,3.78,5.43,'h']
print("m" in user_list)

"""Problem 5: List Statistics
Create a list of numeric values and write a program to calculate and print the following statistics:"""

user_list=[1,4,8,9,6,5,7,2,6,4,5,8]
#Sum of all elements.
print(sum(user_list))
#Average of the elements.
average=sum(user_list)/len(user_list)
print(average)
#Maximum and minimum values in the list.
print("Minimum value is ",min(user_list))
print("Maximum value is ",max(user_list))


####                                    TUPLE                                             ####
"""Problem 1: Tuple Creation and Access
Create a tuple with your favorite colors. Write a program to print each color from the tuple individually."""

color=("black","yellow","white","blue")
for i in color  :
    print (i)

"""Problem 2: Tuple Concatenation
Create two tuples with the names of fruits and vegetables. Write a program to concatenate the two tuples and print the combined list."""

fruits=("apple","banana","kiwi")
fruits2=("mango","orange","cherry")
print(fruits+fruits2)

"""Problem 3: Tuple UnpackingCreate a tuple with information about a person (e.g., name, age, city). 
Write a program to unpack the tuple and print each piece of information."""

person=("FMN","2_","IRB")
name,age,place=person
print("Name :",name)
print("Age :",age)
print("City :",place)

"""Problem 4: Tuple Slicing
Create a tuple with numbers from 1 to 10. Write a program to print a slice of the tuple, including elements from the 3rd to the 7th position."""

number_tuple=tuple(range(1,11))
print(number_tuple[2:7])

"""Problem 5: Tuple Comparison
Create two tuples with numeric values. Write a program to compare the two tuples and print whether they are equal or not."""

tuple1=("T","p","k")
tuple2=("T","Y","k")

if tuple1[:] == tuple2[:]:
    print("Tuples are the same.")
else:
    print("Tuples are not the same.")

####                                String                              ####

"""String Concatenation:
Create two strings, one containing your first name and the other containing your last name.
Write a program to concatenate the two strings and print the full name."""

fname="Mr"
lname="LionByte"
print(fname+"."+lname)

"""String Formatting:
Create a program that takes user input for their favorite color and then prints a message using string formatting, 
incorporating the user's input."""

user_fav_color=str(input("Whats your Favorite color :"))
print("Your favorite color is {}".format(user_fav_color))

"""String Length:
Write a program that prompts the user to enter a sentence and then prints the length of the entered sentence."""

user_input=str(input("Enter a sentence :"))
length=len(user_input)
print("Length of string is :",length)

"""Substring Check:
Create a string variable containing a sentence. Write a program to check if a specific word is present in the sentence and print the result."""

user_input=str(input("Enter the sentence :"))
user_word_checker=str(input("Enter word to be checked"))

print(user_word_checker in user_input)

"""String Reversal:
Take a user input string and write a program to print the reverse of the input string."""

user_input=str(input("Enter the sentence :"))
print("Reversed",user_input[::-1])

####                            DICT                    ####

"""Dictionary Creation:
Create a dictionary representing information about a person, including keys for name, age, and city. Print the dictionary."""

personal_details={
    "name":"JackSparrow",
    "age":"24",
    "city":"NewYork"
}
print(personal_details)

"""Dictionary Access:
Given a dictionary representing a student's grades (subject: score),
write a program that takes user input for a subject and prints the corresponding grade."""

student={
    "physics":"70",
    "Chemistry":"50",
    "maths":"75"
}
user_input=str(input("Enter the subject :"))
print(student[user_input])

"""Dictionary Modification:
Create a dictionary of prices for items (item: price). Write a program that allows the user to update the price of a specific item."""

price_market={
    "Mango":80,
    "Apple":150,
    "Banana":40
}
user_item=str(input("Enter the item name :"))
user_price=int(input("Enter the updated price :"))
price_market[user_item]=user_price
print(price_market)

"""Dictionary Iteration:
Given a dictionary representing words and their meanings, write a program to iterate through the dictionary 
and print each word along with its meaning."""

dictionary={
    "king":"a male sovereign or monarch; a man who holds by life tenure, and usually by hereditary right, the chief authority over a country and people.",
    "queen":"a female sovereign or monarch",
    "minister":"a person authorized to administer sacraments, as at Mass.",
    "ruler":"a person who rules or governs; sovereign."
}

for word,meaning in dictionary.items():
    print(f"{word} : {meaning}")

"""Dictionary Removal:
Create a dictionary representing a shopping list (item: quantity). Write a program that removes a specific 
item from the shopping list based on user input."""

shopping={
    "paper": 20,
    "water bottle": 100,
    "bread": 50,
    "tomato":10
}

user_input=str(input("Enter the item name :"))
del shopping[user_input]
print(shopping)

####                SET                     ####

"""Set Creation:
Create two sets, one containing even numbers up to 10 and the other containing odd numbers up to 10. Print both sets."""

set_odd={1,3,5,7,9}
set_even={2,4,6,8,10}
print(set_odd, set_even)

"""Set Intersection:
Given two sets of fruits and vegetables, write a program to find and print the common items (intersection) between the two sets."""

fruits={"apple","tomato","kiwi"}
vegetable={"onion","carrot","tomato"}
print(fruits.intersection(vegetable))

"""Set Union:
Create two sets representing the colors of your favorite fruits and vegetables. Write a program to find and print 
the combined set (union) of colors."""

fruits_color={"green","yellow","red"}
vegetables_color={"orange","white"}

all_color=fruits_color.union(vegetables_color)
print(all_color)

"""Set Difference:
Given two sets representing your favorite subjects and the subjects you're currently studying,
write a program to find and print the subjects you like but are not currently studying (difference)."""

studying_before={"programming","maths","electrical"}
studying_now={"programming","python"}

diffrance_set=studying_before.difference(studying_now)
print(diffrance_set)

"""Set Membership:
Create a set of programming languages. Write a program that takes user input for 
a specific language and prints whether it is present in the set."""

programming_languages={"python","java","C#","javaScript","C","Dart","Go"}
user_search=str(input("Enter a programming language :"))
print(user_search in programming_languages)