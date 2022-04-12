

def decoDiv(div):

    def inner(a,b):

        if a<b:

            a,b=b,a

        return div(a,b)
    
    return inner




@decoDiv
def div(a,b):

    print(a/b)



    

div(2,10)
div(10,2)