def fibonacci(number):
        # if number<=1:
        #     return number
        if number==0:
            return 0
        if number==1:
            return 1
        return (fibonacci(number-1)+fibonacci(number-2))


def fibonacci_list(list):
    # output=[]
    # for number in list:
    #     output.append(fibonacci(number)) 
    # return output

    return [fibonacci(number)  for number in list]

def lucas(number):
        if number==0:
            return 2
        if number==1:
            return 1
        return (lucas(number-1)+lucas(number-2))


def lucas_list(list):
    return [lucas(number)  for number in list]


def sum_series(number,first_number=2,second_number=1):
    if number==0:
        return first_number
    if number==1:
        return second_number
    return (sum_series(number-1)+sum_series(number-2))


def sum_series_list(list,first=0,second=1):
    output=[]
    for number in list:
        output.append(sum_series(number,first,second)) 
    return output

    # return [sum_series(number,first_number,second_number)  for number in list]


# [2,1,3,4,7,11,18,29,47]

# [0,1,2,3,4,5,6,7,8],2,1