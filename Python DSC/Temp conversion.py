#to convert temperature program

import temperature as temp

def display_menu():
    print('MENU')
    print('1.Fahrenheit to Celsius')
    print('2.Celsius to Fahreheit')
    print()

def convert_temp():
    option= eval(input('Enter a Menu Option:'))
    if option == 1:
        f = eval(input('Enter Degree Fahrenheit:'))
        c = temp.to_celcius(f)
        c = round(c,2)
        print('Degree Celsius:',c)
    elif option == 2:
        c = eval(input('Enter Degree Celsius:'))
        f = temp.to_fahrenheit(c)
        f = round(f,2)
        print('Degree Fahrenheit:',f)
    else:
        print('You must Enter a valid Menu number')

def main():
    display_menu()
    again = 'y'
    while again.lower()== "y":
        convert_temp()
        print()
        again = input("Convert Anoter Temperature?(y/n):")
        print()
    print('Bye!!')

if __name__ == "__main__":
    main()
        
                      
                
    
    
