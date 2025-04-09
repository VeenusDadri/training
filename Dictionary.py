person={
    "first_name": 'Veenus',
    "last_name" : 'Dadri',
    'State' : 'West Bengal',
    'email' : 'veenus.dadri@infoobjects.com',
    'Gender': 'Female',
    'phone_no': 7988072645
}

print (person)
print (f"Email id of person is : {person['email']} ")
print ("length of dictionary:")
print (len(person))
print (f"type of person:  {type(person)}")
print (f"type of person's first name:  {type(person['first_name'])}")
print (f"type of person's phone no:  {type(person['phone_no'])}")

# All the details
print ("\nComplete details: ")
for x in person:
    print (x)


# All the keys
print ( "\nAll Keys: ")
for x in person.keys():
    print (x)

# All the values
print ("\nAll values: ")
for x in person.values():
    print (x)

# All the items
print ("\nAll items: ")
for x in person.items():
    print (x)


# Nested loop

child1 = {
    'name': 'shiv',
    'age': 7
}
child2 = {
    'name': 'ved',
    'age': 4
}

family ={
    'child1': child1,
    'child2': child2
}

print (f"2nd chlid name is {family['child2']['name']}")

