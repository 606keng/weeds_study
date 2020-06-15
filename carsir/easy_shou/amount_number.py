def dispose_num_up(number):

    if number % 100 == 0:
        return int(number)
    elif number % 1 > 0:
        return (int(number / 100) + 1) * 100
    elif number / 1 == int(number):
        if str(int(number))[-1] == '0' and str(int(number))[-2] == '0':
            return int(number / 100) * 100
        return (int(number / 100) + 1) * 100


def dispose_num_down(number):
    return int(int(number/100) *100)

