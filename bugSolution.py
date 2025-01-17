def function_with_uncommon_error_fixed(a, b):
    if a == 0:
        if b == 0:
            return float('nan') #Handle the case where both a and b are 0
        else:
            return 0
    return b / a

result = function_with_uncommon_error_fixed(0, 10)
print(result)  # Output: 0

result = function_with_uncommon_error_fixed(10, 0)
print(result)  # Output: ZeroDivisionError: division by zero

result = function_with_uncommon_error_fixed(0,0)
print(result) # Output: nan