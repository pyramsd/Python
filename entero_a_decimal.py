def int_to_roman(n):
    nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    num_romans = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]

    roman = ""
    i = 0

    while n > 0:
        for _ in range(n // nums[i]):
            roman += num_romans[i]
            n -= nums[i]
        i += 1
    return roman

num = int(input("Numero decimal: "))
print(int_to_roman(num))
