x = [ [5,2,3], [10,8,9] ]
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


# # <----------------------------------------->
# # Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

x[1][0]= 15
print(x)
# # <----------------------------------------->
# # Change the last_name of the first student from 'Jordan' to 'Bryant'

students[0]["last_name"] = 'Bryant'
print(students[0])
# # <----------------------------------------->
# # In the sports_directory, change 'Messi' to 'Andres'

sports_directory["soccer"][0] = 'Andres'
print(sports_directory)
# # <----------------------------------------->
# # Change the value 20 in z to 30

z[0]["y"] = 30
print(z)

# <------------------END OF QUESTION 1---------------------------------------------------------------------------->
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]

def iterateDictionary(some_list):
    for all in some_list:
        for b in all:
            print(all[b])
    
iterateDictionary(students)


# ALL: prints whole dict 2x
# B: prints keys
# print(all[b]): prints just values/ names

# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel
# <------------------END OF QUESTION 2---------------------------------------------------------------------------->
# students = [
#     {'first_name':  'Michael', 'last_name': 'Jordan'},
#     {'first_name': 'John', 'last_name': 'Rosales'},
#     {'first_name': 'Mark', 'last_name': 'Guillen'},
#     {'first_name': 'KB', 'last_name': 'Tonel'}
# ]


def iterateDictionary2(first_name, students):
    for all in students:
            print(all[first_name])

# iterateDictionary2('first_name', students)

# Get Values From a List of Dictionaries
# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries 
# and a key name, the function prints the value stored in that key for each dictionary. For example, 
# iterateDictionary2('first_name', students) should output:

# Michael
# John
# Mark
# KB


def iterateDictionary2(last_name, students):
    for all in students:
        # for first_name in all:
            print(all[last_name])

iterateDictionary2('last_name', students)

# And iterateDictionary2('last_name', students) should output:
# Jordan
# Rosales
# Guillen
# Tonel
# <------------------END OF QUESTION 3---------------------------------------------------------------------------->

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(dojo):
    for key, value in dojo.items():
        print(len(value))
        print(key, value)
        for left in value:
            print(left)
printInfo(dojo)

# Create a function printInfo(some_dict) that given a dictionary whose 
# values are all lists, prints the name of each key along with the size 
# of its list, and then prints the associated values within each key's list. For example:
# printInfo(dojo)
# # output:
# 7 LOCATIONS
# San Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
    
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon
