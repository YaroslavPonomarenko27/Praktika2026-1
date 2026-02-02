def int_to_string(n):
    result = ""
    while n > 0:
        result = chr(n % 19 + 88) + result
        n //= 19
    return result

number = int(input("Enter number: "))
print("String:", int_to_string(number))
