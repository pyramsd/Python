def binary_search(search_list, value):
    search_list.sort()
    first_index = 0
    last_index = len(search_list) - 1

    while first_index <= last_index:
        pointer = (first_index + last_index) // 2
        if value == search_list[pointer]:
            return pointer
        elif value > search_list[pointer]:
            first_index = pointer + 1
        else:
            last_index = pointer - 1

    raise ValueError("value not in array")

Lista = [34,5,765,74,53,2,1,24,6]
print(binary_search(Lista, 34))
