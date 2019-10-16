import copy
from pprint import PrettyPrinter
pp = PrettyPrinter()

def fib(n):

    fib_list = []

    first_num = 0
    second_num = 1

    result = first_num + second_num

    fib_json = {
        'first': 0,
        'second': 1,
        'result': result
    }

    fib_list.append(copy.deepcopy(fib_json))

    for x in range(first_num, n, 1):

        # print(x, '\n')

        fib_json['first'] = fib_json['second']

        fib_json['second'] = fib_json['result']

        fib_json['result'] = fib_json['first'] + fib_json['second']


        fib_list.append(copy.deepcopy(fib_json))



    return fib_list



pp.pprint(fib(5))
