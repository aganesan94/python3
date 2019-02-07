#!/bin/python3

# Sample - 1
print ("This program demonstrates how to unpack variables from a given list of sequences")
fullName = ("Arun","Prakash","Ganesan")
firstName,middleName,lastName=fullName
print("First name is ", firstName)
print("Middle name is ", middleName)
print("Last name is ", lastName)

# Sample - 2
# Unpacking can work with any object that is iterable

name = "Arun"
first,second,third,fourth=name
print ("First Character ", first)
print ("Second Character ", second)
print ("Third Character ", third)
print ("Fourth Character ", fourth)

#Sample 3
# You can have a list inside a list and still extract
details=("Arun", "Ganesan",(1,1,1961))
firstName,lastName,dob=details
day,month,year=dob
print ("Day ", day)
print ("Month ", month)
print ("Year ", year)

#Sample 4
# Extracting what is required
animals=("cow","buffalo","deer")
_,animal1,_=animals
print("Animal is ", animal1)

#Sample 5
# Iterating over tuples of varying length
students=[
    ('Arun',(1,1,1961)),
    ('Sam',(2,2,1931)),
    ('Joel',(3,4,1961)),
]

def printArunsDetails(details):
    print("Arun ", details)    

def printSamDetails(details):
    print("Arun ", details)

def printJoelDetails(details):
    print("Joel ", details)

for name,*args in students:
    if name == 'Arun':
        printArunsDetails(*args)
    elif name == 'Sam':
        printSamDetails(*args)
    elif name == "Joel":    
        printJoelDetails(*args)

#Sample 6
# To parse the top and bottom of a list
numbers=(100, 200, 300, 400, 500)
firstDigit, *_, lastDigit=numbers
print("First Digit is ", firstDigit)
print("Last Digit is ", lastDigit)
firstDigit, *lastDigit=numbers
print("First Digit is ", firstDigit)
print("Last Digit is ", lastDigit)
print("Sum of the last few digits ", sum(lastDigit))