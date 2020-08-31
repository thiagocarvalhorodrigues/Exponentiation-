def multiply(x, y):
    result = x
    for _ in range(y-1):
        result += x
    return result

def exponentiation(x, y):
    result = x
    for _ in range(y-1):
        result = multiply(result, x)
    return result


x= int(input('Enter the first non-negative value to perform the calculation:'))
if(x < 0):
    print("Negative Value")
while x < 0:
    x= int(input("Please enter a Positive value, please!!"))



y = int(input('Enter the second non-negative value to perform the calculation:'))
if(y < 0):
    print("Negative Value")
while y < 0:
    y= int(input("Please enter a Positive value, please!!"))

result = exponentiation(x,y)
print('{} * {} = {}'.format(x, y, result))

