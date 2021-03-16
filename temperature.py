'''This module contain functions for converting temperature between  degee fahrenheit and degree ceclsius.'''
def to_celcius(fahrenheit):
    """ Accept Degree Fahrenheit (Fahrenheit argument) and returns Degree Celcius"""
    celcius = (fahrenheit-32)*5/9
    return celcius

def to_fahrenheit(celcius):
    """Accept Degree Celcius (Celcius argument) and returns Degree Fahrenheit"""
    fahrenheit = celcius*9/5 +32
    return fahrenheit
    

    
