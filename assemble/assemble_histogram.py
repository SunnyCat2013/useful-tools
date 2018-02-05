# -*- coding: utf-8 -*-
# Author: lizhenyang@jd.com
# Description: assemble the data of the fixed interval.
import math
import sys
import os

infile = sys.argv[2]

STEP = int(sys.argv[1])

MIN_PRICE = 0


def genKey(floatValue, step = STEP):

    return str(int(math.floor(floatValue / step) * step))

def main():
    res_dict = dict()
    with open(infile, 'r') as inf:
        lines = inf.readlines()
        for line in lines:
            line = line.strip().split(',')
            #print int(line[0]), float(line[1]) 
            if len(line) != 2:
                continue
            quantity = int(line[0])
            amount = float(line[1])
            key =  genKey(amount)

            if res_dict.has_key(key):
                res_dict[key] += quantity
            else:
                res_dict[key] = quantity
    print res_dict
    output(res_dict)

def output(res_dict, step = STEP):
    base_name = os.path.basename(infile)
    file_name = base_name.split('.')[0] + '_' + str(STEP) + '.csv'
    
    with open(os.path.join('result', file_name), 'w') as outf:
        ks = [int(i) for i in res_dict.keys()]
        ks.sort()
        ks = [str(i) for i in ks]

        print >> outf, ', amount, quantity'
        for k in ks:
            print >> outf, k,',', 'bar_' + str(k), ',', res_dict[k]
    

if __name__ == '__main__':
    main()
