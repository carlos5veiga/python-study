def fizzbuzz(num):
    if divTres(num):
        if divCinco(num):
            return("FizzBuzz")
        else:
            return("Fizz")
    else:
        if divCinco(num):
            return("Buzz")
        else:
            return num
            
def divTres(num):
    if (num%3==0):
        return True
    else:
        return False
        
def divCinco(num):
    if (num%5==0):
        return True
    else:
        return False