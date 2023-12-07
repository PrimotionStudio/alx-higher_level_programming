#1/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list):
        return (0)
    if (len(my_list) == 0):
        return (0)
    su = 0
    av = 0
    for i in my_list:
        su += i[0] * i[1]
        av += i[1]
    return (su / av)
