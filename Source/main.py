# -*- coding: utf-8 -*-
# UTF-8
# Filename: main.py
# PATH: F:\github\SX1208 Kit

import os 
import sys
import time
#import ConfigParser

print "fucking high!"
print "Jr 出品必属精品 {— | —}！ 放屁！吹，继续吹 no zuo no die "
print "\r\n"

#read file
dict1 = {}
n = 0
#conf = ConfigParser.ConfigParser()
f = open("F:\github\Embedded_Pi\doc\sx1208ska.cfg",'r')
str1 = ""
str2 = ""
try:
    for line in f:
        print line,

        # can use for S.split simplify operation
        try: 
            #filter that no have REG of line
            temp = line.index('REG')
            #read Reg Name
            index = line.index('	')
            index_Space = line.index('	', index+1, len(line))
            RegName = line[index+1 : index_Space]
            #read Reg Value
            RegValue = line[-5 : -1]
            temp_list = [RegName, RegValue]
            dict1[n] = temp_list
            n = n + 1
        except ValueError:
            #can't find REG
            #print "ValueError"

            pass
        except:
            print "error"
            f.close()
            
    print "\r\n"
    print "SX1208 Reg config tab:"

    #['RegPayloadLength', '0x00'] to ['RegPayloadLength', 'SX1208_PAYLOADSIZE']
    tempList = dict1[56]
    tempList[1] = 'SX1208_PAYLOADSIZE' 
    dict1[56] = tempList
    #print dict1[56]
    
    for i,j in sorted(dict1.items(), key=lambda d:d[0]):
        #change case 
        str1 = ''.join(j[0])
        str1 = str1.upper()
        # + '_'
        str1 = str1.replace('REG', 'REG_', 1)
        str1 = str1.replace('RESERVED', 'REG_SERVED', 1)
        str1 = str1.replace('REG_DAGC', 'REG_TESTDAGC', 1)
        str1 = str1.replace('REG_PA1', 'REG_TESTPA1', 1)
        str1 = str1.replace('REG_PA2', 'REG_TESTPA2', 1)
        str1 = str1.replace('REG_AFCOFFSET', 'REG_TESTAFC', 1)
        #print tab 
        print '    {' + (str1+',').ljust(20) + j[1] + '},   ',
        str2 = str(i)
        print '//', str2.ljust(2),
        if i >= 80:
            if 80 == i:
                temp = 0x59
            elif  81 == i:
                temp = 0x6C
            elif  82 == i:
                temp = 0x6F
            elif  83 == i:
                temp = 0x5A
            elif  84 == i:
                temp = 0x5C
            else:
                temp = 0x71
            print "(0x%X)" %temp
        else:
            print "(0x%X)" %i
        
finally:
    f.close()
