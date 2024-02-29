#Name: Joshua Delton
#Description: This program asks a user to input a numerator and denominator, and then out puts what type of a fraction it is, what the fraction can be reduced to, and if needed the fraction as a whole number.
#-------------------
import math
num = int(input('Enter a numerator: Value must be greater than 0: '))
while num <= 0:
    num = int(input('Please re-enter a numerator: Value must be greater than 0: '))
den = int(input('Enter a denominator: Value must be greater than 0: '))
while den <= 0:
    den = int(input('Please re-enter a denominator: Value must be greater than 0: '))
gcd = math.gcd(num,den)
rem = int(num % den)
mix = int(num // den)
if num < den:
    print(f'{num} / {den} is a proper fraction.')
    if gcd == 1:
        print('This proper fraction cannot be reduced any further.')
    else:
        print('This proper fraction can be reduced to: ', int(num / gcd), '/', int(den / gcd))
elif num >= den:
    print(f'{num} / {den} is an improper fraction.')
    if gcd == 1 and rem > 0:
        print('This improper fraction cannot be reduced any further.')
        print('The mix number is ', mix, ' and ', rem, '/', den)
    elif gcd == 1 and rem == 0:
        print('This improper fraction cannot be reduced any further.')
        print('The whole number is ', int(num / den))
    elif rem == 0:
        print('This improper fraction can be reduced to: ', int(num / gcd), '/', int(den / gcd))
        print('The whole number is ', int(num / den))
    elif rem > 0:
        print('This improper fraction can be reduced to: ', int(num / gcd), ' / ', int(den / gcd))
        print('The mix number is ', mix, ' and ', int(rem / gcd), '/', int(den / gcd))


