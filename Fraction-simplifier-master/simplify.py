def gcd(a, b): 
	if a == 0 : 
		return b 
	
	return gcd(b%a, a) 

print('Enter the numerator:')
a = int(input())
print('Enter the denominator:')
b = int(input())

def simplify(numerator, denominator):
    result = gcd(numerator, denominator)
    new_numerator = int(numerator / result)
    new_denominator = int(denominator / result)
    return [new_numerator, new_denominator]

result = simplify(a,b)
print('Simple:', result[0], ' / ', result[1])

print('Would you like that as a fraction? (y or n)')
yes = input()
if(yes == 'y'):
    fraction = result[0] / result[1]
    print(fraction)