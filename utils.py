from math import sqrt

def is_prime(n):
    """ Return a boolean value base on whether the argument n is a prime number.
    hope you enjoy it !
    """
    
    if n < 2:
        return False
    if n in (2,3):
        return True
    for i in range (2,int(sqrt(n+1))):
        if n % i ==0:
            return False
        
    return True
is_prime(99)


        
def say_hi(*names, greet="Hi",capitalized=False):
    """ Print a string ,with a greeting to everything.
    :param *names: tuple of names to be greeted
    :param capitalized : whether name shoud be coverted to capitalized before print False as default.
    :returns:None 
    
    """

    for name in names:
        if capitalized:
            name = name.capitalized()
        
            print(f'{greet},{name}!')
    
say_hi ('Jack','Rose','Lily', greet='Hello' ,capitalized=False)

