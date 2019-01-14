# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 15:30:38 2018

@author: adam
"""

def validateIp(ipl):
    '''this funtion vlidates the ip address by checking each condition'''
    for i in ipl:
        ipsplit = [int(x) for x in i.split('.')] # loop through ip split cast to int
        for j in ipsplit:
            if j > 255:
                print(i + ' IP address Octets must be < 255')
                print('please Enter Valid IP address')
                #return False
            elif j >= 224 and j <= 255:
                print(i + ' IP cannot be class D, class E or broadcast address')
                print('please Enter Valid IP address')
                #return False
        
            elif j >= 127 and j < 128 :
                print(i + 'IP cannot be loopback address')
                print('please Enter Valid IP address')
        if len(ipsplit) != 4:
            print(i + ' IP  must have 4 octets please enter valid IP address')
           # return False
        else:
            #return True
            print(i + ' Valid IP')