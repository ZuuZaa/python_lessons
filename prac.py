
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

    
list = [1,1,2,34,54,23]

# for i in list:
#     print(i)

b =list[0:3] 
c = list[3::] #till the end
d = list[0::2] # 2 between
e = list[len(list)::-1] # reverse
print(b,c,d,e)

# for i in range(len(list)):
#     print(list[i])
