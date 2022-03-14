# anonymous or lamda functions:
#--------------------------------

# sometimes we can declare a function without any name such kind of nameless function are called lamda function.

#1. using lamda we can write very less no of lines of code
#2. using lamda we can write very concise code(short hand way of writing code)
#3. using lambda mostly we can write a single line expressions
#4. using lambda we can reduce the lenght odt he code and improve readbility of the program
#5. lambdas are for instant usage i.e only one tile 


# some function will expect other function as an agument in this situation lambda is best choice.

# sometimes we should pass a function as an argument to other function then we should use lambda function

# def f1():
#     pass


# def f2(f1):
#     pass







# lambda argumentslist:expression

# lambda n: n*n
# lambda a,b:a+b
# lambda a,b:a if a>b else b

s = lambda n:n*n # labdma function return it self result 

print(s(5))


c = lambda a,b,c: a if a>b and a>c else b if a>c else c


print(c(17,80,65,))

even = lambda n:"is even" if n%2==0 else "is odd"

print(even(7))


#1. filter (): is used to filter the vlaues from given sequence based on condition

# syntax : filter(fucntion,sequence)

# here first parameter is a function for condtional check
# here second parameter is a sequence (list,tuple,set)



#2. map() : for every element present in sequence, apply some condition and return the new sequence of elements for this purpose we use map() function.

# map(function,sequence) 

#3. reduce()

# reduce(function,sequence)
# it return interger value like single value