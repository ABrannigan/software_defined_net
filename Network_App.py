# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 17:28:06 2018

@author: adam
"""

from ip_file_valid import checkIpfile
from ipp_addr_valid import validateIp
from ip_reach import pingIps
from ssh_connection import checkFile,config
from create_threads import cmdSession


#filename = 'Address_List.txt'
#userFilename = 'Uname_Pass.txt'
#cmdFilname = 'Command.txt'
def main():
    
        #ask User For path and filename for ip addresses store in a list
        ipFilename = str(input('Please enter the path and filename where ip addresses are held :'))
        ip_list  = checkIpfile(ipFilename)
        #Check each IP addresses is valid
        validateIp(ip_list)
        print("\n ")
        #check each IP addresses can be reached ping 
        pingIps(ip_list)
        print("\n ")
        #Check username/pass file and command file exist
        userFilename = input('Please enter the path and filename where Username and password are held :')
        checkFile(userFilename)
        cmdFilname = input('Please enter the path and filename where Commands are held :')
        checkFile(cmdFilname)
        print('Opening ssh connection and configuring routers')
        config(cmdFilname,userFilename,ip_list)
       
        '''
        print ('Opening command session')
        cmdSession(userFilename,ip_list,cmdFilname)'''
        
    
       
    #

    
    
    
    
if __name__ == '__main__':
    main()