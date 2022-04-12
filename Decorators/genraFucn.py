def f1():

    yield "A"
    yield "nikkk"
    yield "black"
    yield 100



g = f1()


# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

print(next(g))
print(next(g))
print(next(g))
print(next(g))