def rect(a,b):
    '''
    Function rect drawing rectangle with given width and high
    INPUT:width, high (equals 1 or more)
    OUTPUT:rectangle
    '''
    print("*" * a)
    if b >1:
        for i in range(0,b-2):
            print("*"+" "*(a-2)+"*")
        print("*" * a)
rect(10,10)