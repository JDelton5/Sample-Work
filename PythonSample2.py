#Name: Joshua Delton
#Description: This program asks the user for a temperature and what degree format they wanted it changed into and then does the calculations for them.
#--------------------
def main():
    again = ''
    while again != 'no':
        print('This program will convert temperatures for you!')
        display()
        num = int(input('Please select and option: '))
        while num < 1 or num > 6:
            num = int(input('Invalid choice. Please re-select and option: '))
        temp = int(input('Enter a temperature: '))
        option = {1: f'{temp} degrees Celsius is {ctf(temp):.2f} degrees Fahrenheit',2:f'{temp} degrees Celsius is {ctk(temp):.2f} degrees Kelvin',3:f'{temp} degrees Fahrenheit is {ftc(temp):.2f} degrees Celsius',4:f'{temp} degrees Fahrenheit is {ftk(temp):.2f} degrees Kelvin',5:f'{temp} degrees Kelvin is {ktc(temp):.2f} degrees Celsius',6:f'{temp} degrees Kelvin is {ktf(temp):.2f} degrees Fahrenheit'}
        print(option[num])
        again = str(input('Would you like to convert another temperature? ')).lower()
        print()
        
    

def display():
    print('1. Convert from Celsius to Fahrenheit')
    print('2. Convert from Celsius to Kelvin')
    print('3. Convert from Fahrenheit to Celsius')
    print('4. Convert from Fahrenheit to Kelvin')
    print('5. Convert from Kelvin to Celsius')
    print('6. Convert from Kelvin to Fahrenheit')

def ctf(temp):
    f = (9 / 5) * (temp) + 32
    return f
def ctk(temp):
    k = temp + 273.15
    return k
def ftc(temp):
    c = (5 / 9) * (temp - 32)
    return c
def ftk(temp):
    k = (5 / 9) * (temp - 32) + 273.15
    return k
def ktc(temp):
    c = temp - 273.15
    return c
def ktf(temp):
    f = (9 / 5) * (temp - 273.15) + 32
    return f

main()
