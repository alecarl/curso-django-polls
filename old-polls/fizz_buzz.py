def solution(n):
    
    if n % 3 == 0 and n % 5 == 0:
        return "fizz-buzz"

    if n % 3 == 0:
        return "fizz"
    elif  n % 5 == 0:
        return "buzz"
    else:
        return n