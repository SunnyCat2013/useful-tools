# This is a ACM file maker.
# Run this file you will get a ACM code source file, named xxxx.c.
# And in this file some enssential element was writen, such as author information, the main structure.
# Author: cslzy
# Email: lizhenyang@ruc.edu.cn
# Date : 20151009
import sys, os
import argparse
import time
def newFile(fileN, override=0, pre='#'):
    if os.path.exists(fileN) and not override:
        print 'file exists and no override option.'
        exit(0)
    nFile = open(fileN, 'w')
    
    infoStr = pre + ' -*- coding: utf-8 -*-\n' + pre + ' Author: IceBear\n' +  pre + ' Email: lizhenyang_2008@163.com\n' + pre + ' Description: CHANGING WHEN IT IS EDITED\n'

    
    infoStr +=  pre + ' Date: ' + time.strftime('%Y%m%d %X', time.localtime(time.time()))
    #print infoStr
    
    ext = os.path.splitext(fileN)[1]
    if ext=='.c' or ext=='.cpp':
        infoStr +='\n#include <stdio.h>\nint main(int argc, char* argv[])\n{\n\treturn 0;\n}\n'
    
    
    
    
    nFile.write(infoStr)
    nFile.close()
        
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parsing new file\'s name and override information.')
    parser.add_argument('-n','--name', help='the name of the file you want to build', default='newfile.c')
    parser.add_argument('-o','--override', action='store_true', help='whether to override the exist file, default false')
    args = parser.parse_args()
    
    preDict = {'.c':'//', '.py':'#', '.tex':'%', '.cpp':'//'}
    ext = os.path.splitext(args.name)[1]
    if ext in preDict.keys():
        pre = preDict[ext]
    else:
        pre = '#'

    new_info_file(args.name, args.override, pre)
