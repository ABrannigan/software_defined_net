# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 19:07:57 2018

@author: adam
"""

#ipl = ['192.168.2.101', '192.168.2.102', '192.168.2.103', '8.8.8.8','192.168.8.105']

import subprocess
# subprocess.call('ping %s -n 2' % ('8.8.8.8',), stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
def pingIps(ipl):
    '''this funtion vlidates the ip address is reachable by pinging each'''
    print('Please wait While we try reach ip addresses \n')
    for i in ipl:
        #iString = '\''+i+'\''
        #print(iString)
        check =  subprocess.call('ping %s -n 2' % (i,), 
                             stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if check == 0:
            print('IP address: ' + i + '  Reachable')
            
        else:
            print('IP address: ' + i + '  Un-Reachable')
            
            
#ip = checkIps(filename) 
#print(ip)   
    
#if __name__ == '__main__':
    #pingIps(ipl)