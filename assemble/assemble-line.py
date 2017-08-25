# -*- coding: utf-8 -*-
# Author: lizhenyang_2008@163.com
# Description: assemble the data of the fixed interval.
import math
import sys
import os

infile = sys.argv[2]

STEP = int(sys.argv[1])

MIN_PRICE = 0

dimension_checker = 2

# colomn to group
amount_index = 1

# column to assemble
quantity_index = 0


# delimiter
separator = ','

# has header or not
has_header = True


def genKey(floatValue, step = STEP):

    return str(int(math.floor(floatValue / step) * step))

def printInfo():
    print '--------------------------------------------'
    print 'Step: ', STEP

    print 'Min price: ', MIN_PRICE

    print 'Dimension limitation: ', dimension_checker

    # colomn to group
    print 'Amount index: ', amount_index

    # column to assemble
    print 'Quantity index: ', quantity_index


    # delimiter
    print 'Separator: ', separator

    # has header or not
    if has_header:
        print 'Has header:'
    else:
        print 'Doesn\'t has header'

    print '--------------------------------------------'
    print ''


def main():
    printInfo()

    res_dict = dict()
    with open(infile, 'r') as inf:
        lines = inf.readlines()

        if has_header:
            print('header:', lines[0])
            del lines[0]

        for line in lines:
            line = line.strip().split(separator)
            #print int(line[0]), float(line[1])
            if len(line) != dimension_checker:
                continue
            quantity = int(line[amount_index])
            amount = float(line[quantity_index])
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
