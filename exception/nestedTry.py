

try:
    
    print("outer try")

    try:
        print(10/0)
        print("inner try")

    except ValueError:
        print("inner except")
    
    finally:
        print("inner finally")

except:
    print("outer except")


finally:
        print("outer finally")