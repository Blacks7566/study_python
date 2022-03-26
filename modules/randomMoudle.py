from random import *

#1. random():
# it will generate random float values by default between 0 and 1(not include)
print("random() fucntion")
print()

for i in range(5):
    print(random())

print()



#2. ranint():
# it will generate random int values between two given numbers(include)
print("randint() fucntion")
print()

for i in range(10):
    print(randint(1000,3000))


print()





#3. uniform()
# it will genetate random float values by default between two given numbers (not inlcude)
print("uniform() fucntion")
print()


for i in range(5):

    print(uniform(2,21))

print()




#4. randrange():
# randrange(start,stop,step)

print("randrange() fucntion")
print()

for i in range(5):
    print(randrange(2,20,3))

# 2,5,8,11,14,17,20 because step = 3

print()

#5.choice():
# it will not generate any random numbers but it returns random object
print("choice() fucntion")
print()

l=['nitin','sudeep','kuldeep','black','soni','gullu','dharmendra','sibbu']

print(choice(l))