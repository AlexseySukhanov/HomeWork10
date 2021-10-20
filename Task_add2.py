def biggest_3x_pallindrome():

    '''
    Function biggest_3x_pallindrome searching biggest possible pallindrome as result of multiply two 3 digit numbers
    INPUT:
    OUTPUT:biggest possible pallindrome as result of multiply two 3 digit numbers
    '''

    max=0
    maxi=0
    maxj=0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            res=i*j
            x=list(str(res))
            if x==x[::-1]:
                if res>max:
                    max=res
                    maxi=i
                    maxj=j

    print(f"Pallindrome {max} as result of multyply {maxi} and {maxj}")

biggest_3x_pallindrome()
