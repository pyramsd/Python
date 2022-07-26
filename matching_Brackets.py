def is_paired(input_string):
    Dict = {'(': ')', '[': ']', '{': '}'}
    List = []
    for i in input_string:
        if i in Dict:
            List.append(i)
        elif i in Dict.values():
            # Top item on the stack must be present and of matching type.
            if len(List) == 0 or Dict[List.pop()] != i:
                return False
    return len(List) == 0
