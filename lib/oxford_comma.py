def oxford_comma(arr):
    if len(arr) == 0:
        return ""
    elif len(arr) == 1:
        return arr[0]
    elif len(arr) == 2:
        return f"{arr[0]} and {arr[1]}"
    else:
        elements_except_last = ", ".join(arr[:-1])
        return f"{elements_except_last}, and {arr[-1]}"

