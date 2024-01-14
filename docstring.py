#docstring: herkesin anayabilecegi sekilde fonxlara bilgi notu vermek

'''
İlk bölümde fonxun ne yaptıgı anlatılır
2. de parametrler/args
    arg1: tipleri(int/float)
    arg2: int/float
3. returns

google ve numpy ile 
'''

import numpy


def summer(arg1 , arg2):
    
    """
    Sum of two numbers
    Args:
        arg1: int, float
        arg2: int,floar

    Returns:
        int, float
    
    Examples:
        arg1: 4
        arg2:3
        return: 4+3
    
    """
    print(arg1+arg2)

summer(2,3) 
#summerin üstüne gelince yukardaki docs hemen geliyor.


print(help(summer))

'''summer(arg1, arg2)
   Sum of two numbers
    Args:
        arg1: int, float
        arg2: int,float '''