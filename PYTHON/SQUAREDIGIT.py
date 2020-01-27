def square_digits(num):
    words = list(str(num))
    n= ''.join([str(int(i)**2) for i in list(str(num))])
    return int(n)
            
