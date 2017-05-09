# Write a fruitful function sum_to(n) that returns the sum of all integer
# numbers up to including n. So sum_to(10) would be 1+2+3...+10 which would
# return the value 55

def sum_to(n):
    sum = 0
    for i in range(n + 1):
        sum += n

    return sum


sum_to(10)  # the returned value should be 55
