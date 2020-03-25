
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

# print('hello'.center(30,'*'))
# print('hello'.rjust(20))
# print('hello'.ljust(10, '-'))

# s = input("chat>>  ")
# print(s.strip())



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

    
# list = [1,1, 2,34,54,23]

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

# print(",  ".join(l))  


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

# while True:
#     print('Welcome, this is a simple calculator.')
#     print("Enter + , - , * , / or ** for calculating.")
#     print("Press e for exit.")
#     users_input = input(">> ")

#     if users_input == "e":
#         break
#     elif users_input == "+":
#         print("Please enter two numbers for addition:")
#         a = float(input('first number >>  ')) 
#         b = float(input('second number >>  '))
#         c = a+b
#     elif users_input == "-":
#         print("Please enter two numbers for subtraction:")
#         a = float(input('first number >>  ')) 
#         b = float(input('second number >>  '))
#         c = a-b
#     elif users_input == "*":
#         print("Please enter two numbers for mutliplicate:")
#         a = float(input('first number >>  ')) 
#         b = float(input('second number >>  '))
#         c = a*b 
#     elif users_input == "/":
#         print("Please enter two numbers for divide:")
#         a = float(input('first number >>  ')) 
#         b = float(input('second number >>  '))
#         c = a/b
#     elif users_input == "**":
#         print("Please enter two numbers for power:")
#         a = float(input('first number >>  ')) 
#         b = float(input('second number >>  '))
#         c = a**b

#     print(f'The answer is >> {c}')

# print("Thanks for using our calculator :)")


# while True:

#     age = input("enter your age")

#     if age.isdecimal():
#         print(f'your age is {age}.')
#         break
#     else:
#         print('please enter a number for yor age.')
#         continue



# ------------- FUNCTIONS --------------

# def test():
#     print('please enter your name')
#     name = input('>>  ')
#     print("hi, " + name)

# test()
# test()
# test()

# def n(name):
#     print("hi, " + name)

# print('please enter your name')
# name = input('>>  ')

# n(name)


# --- find phone number from text message -------

# def isphonenum(text):
#     if len(text) != 12:
#         return False
#     for i in range(0,3):
#         if not text[i].isdecimal:
#             return False
#     if text[3] != "-":
#         return False
#     for i in range(4,7):
#         if not text[i].isdecimal:
#             return False
#     if text[7] != "-":
#         return False  
#     for i in range(7,12):
#         if not text[i].isdecimal:
#             return False
#     return True

# message = "call me tomorrow, my phone number is 000-000-0000, my office number is 111-111-1111."

# for i in range(len(message)):
#     test = message[i:i+12]
#     if isphonenum(test):
#         print("phone number is:  " + test)

# print("done!")


# -------- decorator, lambda---

# def apply_once(func, arg):
#     return func(arg)

# def add_five(x):
#     return x+5

# print(apply_once(add_five, 10))
  
# def apply_twice(func, arg):
#     return func(func(arg)) 

# print(apply_twice(lambda x: x*2, 10))

# ----- normal function

# def test(x):
#     return x**2 + x*5 - 4
# print(test(5))

# # ----- lambda 
# print((lambda x: x**2 + x*5 - 4)(int(input("enter the number>> "))))

# ----- map and filter list -----

# nums = [3, 5, 66, 7, 89, 123, 32]

# #------- map list with normal function -----

# def add_five(x):
#     return x+5

# result = list(map(add_five, nums))

# print(result)

# # ----- map list With lambda ------

#print(list(map(lambda x: x+5, nums)))

# ---- filter the list with lambda -------

# print(list(filter(lambda x: x%2 == 0 , nums)))

# nums = [i for i in range(100)]

# print(list(filter(lambda x: x % 2 == 0 , nums)))



# ------ yield ---------


# def countdown(x):
#     while x>0:
#         yield x
#         x-=1

# for i in countdown(10):
#     print(i)

# def countdown(x):
#     for i in range(x):
#         if i%2 == 0:
#             yield i

# print(list(countdown(10)))

# for i in countdown(10):
#     print(i)

# def make_word(x):
#     word = ''

#     for w in x:
#         word += w 
#         yield w

# my_list = list(make_word('zumrud'))

# print(my_list)

# def fibonachi(n):
    
#     first = 1
#     second = 1
#     while second < n: 
#         f = first + second 
#         first = second
#         second =f

#         yield second
        
# fibo = list(fibonachi(34))

# fibo[0] = 1
# fibo[1] = 1

# print(fibo)


# def name(f_name, l_name, m_name=""):
#     if m_name:
#         full_name = f_name.title() + " " + l_name.title() + " " + m_name.title()
#     else:
#         full_name = f_name.title() + " " + l_name.title()
#     return(full_name)

# print(name('zumrud','nerman'))

# print(name('davud', 'bagirov', 'imran'))


# def make_pizza(size, topics):
#     print(f'we makin a {size} cm pizza with:')
#     for i in topics:
#         print('- ',i.title())

# topics = ['tomato', 'peper', 'sousage', 'cheese', 'olive']

# make_pizza(30, topics)

# def test(*t):
#     print(t)

# test('ali','sahvar' )
# test('ali', 'shhahvar',33)


# # ------ ARGS KVARGS -----

# def calc(*args):
#     for i in args:
#         c = args[0] + args[1]
#     print(c)
    
# a = int(input("first number >>  "))
# b = int(input("second number >>  "))

# calc(a,b)


# def build_profile(first, last, **kvargs):
#     p = {}

#     p['f_name'] = first
#     p['l_name'] = last

#     for k , v in kvargs.items():
#         p[k] = v

#     print(p)

# build_profile('zumrud', 'nerman', age = 33, gender="f" )




# # ---------- CLASSES --------------


# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(self.name, str(self.age))

# person1 = Person('zumrud',33)
# person2 = Person('davud', 12)

# person1.info()
# person2.info() 

# -- child class --

# class Person():

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         print(self.name, str(self.age))   

# class New(Person):
#     def __init__(self, name,age):
#         super().__init__(name, age)


# person1 = New('zumrud', 37)
# person1.info()

# class Car():

#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.km = 0

#     def info(self):
#         print('about car:')
#         print(self.make, self.model, self.year)

#     def update_km(self,km):
#         self.km +=km

#     def read_km(self):
#         print("km:", self.km)

# my_car = Car('WV', 'polo', 2015)

# # my_car.info()
# # my_car.update_km(3000)
# # my_car.read_km()
# # my_car.update_km(55000)
# # my_car.read_km()

# # ---------- inherit from two different classes --------

# class ElectriCar(Car):
#     def __init__(self, make, model, year):
#         super().__init__(make, model, year)
#         self.battery = Battery()

#     def show_battery(self):
#         print('batteri ', self.battery)


# class Battery():
#     def __init__(self, battery=70):
#         self.battery = battery

#     def show_battery(self):
#         print("battery is:  ", str(self.battery))


# my_new_car = ElectriCar('WV', 'polo', 2015)

# my_new_car.info()
# my_new_car.battery.show_battery()

# test = Battery(98)
# test.show_battery()
# my_new_car.battery.show_battery()



# class Test():
#     def __init__(self, l):
#         self.l = l

#     def split_l(self):

#         if type(self.l) == type(''):
#             print(self.l, "is string")
#             for i in (self.l).split():
#                 print(i)
        
#         elif type(self.l) == type([]):
#             print(self.l, "is list")
#             for i in self.l:
#                 print(i)

# l1= "hi, this is me"
# s1 = Test(l1) 
# s1.split_l()  

# l2 = ['davud', 'maryam','zeynab']
# s2 = Test(l2)
# s2.split_l()

        


# ---------------- FILES -------------------

# f = open('test.txt', 'w')
# f.write("hello")
# f.close()
# f1 = open("test.txt", 'r')
# print(f1.read())

file_path ='/home/zumrud/Desktop/learning python/test.txt'

# with open(file_path, 'w') as f:
#     f.write("hi my name is zumrud \n this is test \n don't worry )))")

# with open(file_path) as file:
#     for f in file:
#         print(f.rstrip())

# with open(file_path) as f:
#     l = f.readlines()
# print(l)




# with open(file_path, 'w') as file:
#     file.write('i am learning python \n')

# string = " "

# with open(file_path, 'r') as file:
#     f2 = file.readlines()
#     for i in f2:
#         string += i

# print(f2)

# if 'python' in string:
#     print('yes')
# else:
#     print('no')

# print(string)


# ------- ARGV ---------

# from sys import argv

# script, user_name, file_name = argv

# print(f'welcome, {user_name}')

# print(f'loading your file by name: {file_name}')

# with open(file_name, 'r') as f:
#     print(f.read()) 


# from sys import argv, exit

# script, user, file = argv

# print(f'write something to your {file} file')
# print('enter e to exit')
# a = input('>>>  ') 
# if a == 'e':
#     exit(0)
# print('something else') 
# print('enter e to exit')
# b = input('>>>  ') 
# if b == 'e':
#     exit(0)

# target = open(file, 'w')

# target.truncate()

# target.write(a)
# target.write('\n')
# target.write(b)

# target.close()

# with open(file, 'r') as f:
#     f = f.read()

# print(f)


# ---------- TRY EXEPT -----------

# print('enter two numbers to devise.')
# print('enter q to quit')

# while True:

#     n1 = input("First number is:  ")
#     if n1 == "q":
#         break
#     n2 = input("Second number is:  ")
#     if n2 == "q":
#         break

#     try:
#         answer = float(n1) / float(n2)

#     except ZeroDivisionError:
#         print("can't devise to zero")

#     except ValueError:
#         print("can't devise strings")

#     else:
#         print(answer)


# --------- JSON ----------------



