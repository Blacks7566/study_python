def mydiv(div):

    def inner (a,b):
        if a<b:

            a,b = b,a

            return div(a,b)
        return inner

@mydiv
def div(a,b):

    print(a/b)




div(10,2)