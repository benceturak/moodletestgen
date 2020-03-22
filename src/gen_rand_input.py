import random
import json

def gen_rand_input(input):
    '''generate random input within the specified interval
        :param input: {min, max, round} (dict)
        :return: list of input params
    '''
    ret = []
    for i in input:
        r = round(i['min'] + (i['max'] - i['min'])*random.random(), i['round'])
        if i['round'] == 0:
            r = int(r)
        ret.append(r)
    return ret
