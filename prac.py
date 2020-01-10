
# ----- VARIABLES-----

a = 20
b = "salam"
c = str(a) + ' ' +b
f = 20.6
name ="zumrud"

# print(c)
# print ("the number is %d and %f" %(a,f))
# print ("salam, " + name)
# print ("salam, %s" %name) 
#print ("the numbers are {} and {} and the name is {}".format(a, f, name))
#print (f"the numbers are {a} and {f} and the name is {name}")

# -------- LIST ------------

# list_1 = ["zumrud", "davud", "maryam", "zeyneb"]

# a = list_1[1]
# b = list_1[-4]
# c =len(list_1)

# list_2 = [1,2,3]

# list_1.append(list_2)

# d= list_1[-1][1]

# list_2.insert(2, "salam")

# print(list_1, a,b, c, d)


# --------- INPUT -------------

# print("please, type your name")
# name = input()

# print("please, type your family-name")
# family_name = input()

# print("hello,  " + name + " "+ family_name +"!")


# --------IF Condition -----------

# print("enter your age, please")

# age = int(input())

# if age >= 18:
#     print ("velcome")

# elif age >60:
#     print ("you are so old")

# elif age <18:
#     print("sorry, you can't enter")

# else: 
#     print("enter your age")


# --------- FOR Loop ----------

# in range(0,10) or in range(10) or in range(0,10,2)
# for i in range(5):
#     print("salam,")
#     print(i)

# str ="salam"
# for i in str:
#     print(i)

    
list = [1,1, 2,34,54,23]

# #--- delete the last item of list
# print(list.pop()) 
# #--- delete item with index
# del list[3]
# print(list)
# #--- delete Item with value
# while 1 in list:
#     list.remove(1)
# print(list)

# for i in list:
#     print(i)

# b =list[0:3] 
# c = list[3::] #till the end
# d = list[0::2] # 2 between
# e = list[len(list)::-1] # reverse
# print(b,c,d,e)

# for i in range(len(list)):
#     print(list[i])



# l=[]

# if l:
#     print(l)
# else:
#     print("there is no items")
#     name = str(input("enter your name: "))
#     l.append(name)
#     print(l)



# l = ["maryam", "davud", "zeynab"]

# name = input("please enter your name: ")

# if name not in l:
#     print("your name is not in our list, sorry")
# else: 
#   print(f"welcome, {name}")
    


# squares = []

# for value in range(1,11):
#     square = value ** 2
#     squares.append(square)

# for i in squares:
#     print(i)


# digits = [2,4,54,2,7,8,9,0,123]
# digits.sort()
# print(digits)
# print(sum(digits))
# print(max(digits))
# print(min(digits))


# players = ['davud', 'maryam', 'zeynab', 'zumrud', 'farac']

# for player in players[:3:-1]:
#     print(player.title())


# a = [1,2,3]+[4,5,6,7]
# print(a)
# print('salam  ' * 4)
# print(['salam']* 5)

# a= '321'
# print(a[1])

# a = list('34')
# print(a)



# --------- DICTIONARY ---------

my_dict = {
    'name': 'zumrud',
    'age': 36,
    'language': ['html', 'css', 'js', 'python']
}

# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())

# del my_dict['name']
# print(my_dict)

# d = my_dict.copy()
# print(d)
# d['name'] = "ali"
# print(my_dict)
# print(d)

# d = {}
# d.update(my_dict)
# my_dict['name'] = "ali"
# d['age'] = 37
# print(my_dict)
# print(d)


# d = {
#     'user1' : {'name':'zumrud', 'age':37},
#     'user2': {'name':'ali', 'age':30},
#     'user3': {'name':'mohammed', 'age':40}
# }

# for key, value in d.items():
#     print(key, value)

d = {
    "movie1": 2003,
    "movie2": 2005,
    "movie3": 2007,
    "movie4": 2003,
    "movie5": 2001
}

# year = int(input('please enter year of movie  '))

# for k, v in d.items():
#     if v == year:
#         print(k)
#     else: 
#         print('movie is not found')
#         break

# movie_list = [k for (k,v) in d.items() if v == year ]

# print(movie_list)

# for k in d:
#     print(k)

# for k in d.items():
#     print(k)

# for k, v in d.items():
#     print(k, v)

# my_d = [(k, v) for (k,v) in d.items() ]
# print(my_d)

# for i in d.values():
#     print(i)


# ---------- While -----------

i=0

# while i<=5:
#     print(i)
#     i= i+1

# while i<=10:
#     if i%2 ==0:
#         print(i)
#     i=i+1

# str = "zumrud"
# print("len str is:  ", len(str))
# while i< len(str):
#     print('i is:  ', i)
#     print(str[i])
#     i=i+1

# while True:
#     i = i+1
#     if i % 2 == 0:
#         print(f'skipping {i}')
#     else:
#         print(i)
#     if i == 10:
#         print("break")
#         break
# print("finish")
    
# active_users = ['u1', 'u2', 'u3']
# users = []

# while active_users:
#     current_user = active_users.pop()
#     print('current user is:  ', current_user)
#     users.append(current_user)
# print(users)

# for i in users[::-1]:
#     print(i.title())


# while True:
#     print('enter your name:')
#     name = input(">> ")
#     if name == "exit" or name == "e":
#         break
#     print("for exit press 'e' or enter 'exit'")
 
   
# res = {}

# active = True
# prompt= "> "

# while active:
#     print('enter your name')
#     name = input(prompt)
#     response = input("please enter your family_name:  ")
#     res[name] = response
#     print('do you want to repeat')
#     repeat = input("y / n >>>  ")
#     if repeat == "n":
#         active = False

# for k, v in res.items():
#     print(k, "___", v)

# words = ['hi', 'hello', 'sorry', 'by']

# counter = 0

# while counter < len(words):
#     print(words[counter],'!')
#     counter += 1


# ---------- Calculator --------

while True:
    print('Welcome, this is a simple calculator.')
    print("Enter + , - , * , / or ** for calculating.")
    print("Press e for exit.")
    users_input = input(">> ")

    if users_input == "e":
        break
    elif users_input == "+":
        print("Please enter two numbers for addition:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a+b
    elif users_input == "-":
        print("Please enter two numbers for subtraction:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a-b
    elif users_input == "*":
        print("Please enter two numbers for mutliplicate:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a*b 
    elif users_input == "/":
        print("Please enter two numbers for divide:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a/b
    elif users_input == "**":
        print("Please enter two numbers for power:")
        a = float(input('first number >>  ')) 
        b = float(input('second number >>  '))
        c = a**b

    print(f'The answer is >> {c}')

print("Thanks for using our calculator :)")

