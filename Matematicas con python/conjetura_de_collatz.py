def steps(number):
    list_nums = []
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    else:
        while number > 1:
            if number % 2 == 0:
                number //= 2
            else:
                number = 3*number+1
            list_nums.append(number)
    return list_nums, f'Numero de pasos para llegar a 1: {len(list_nums)} pasos'

print(steps(12))