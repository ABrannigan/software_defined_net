# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:19:42 2018

@author: adam
"""

import os
import sys
#filename = 'Address_List.txt'

def checkIpfile(filename):
    ipList = []
    if os.path.isfile(filename) == False:
        print('Sorry Incorrect filename or path')
        sys.exit
            
    else:
        print(filename + ' File Located')
        f = open(filename,'r')
        for x in f:
            ip = x.strip('\n')
            ipList.append(ip)
        f.close()
        return ipList    
       
        
    
    
#ip = checkIps(filename) 
#print(ip)   
    
#if __name__ == '__main__':
    #checkIps(filename)