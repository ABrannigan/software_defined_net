# -*- coding: utf-8 -*-
"""
Created on Sun Dec 23 23:03:38 2018

@author: adam
"""
import os
import paramiko
import time

userFile = 'Uname_Pass.txt'
cmdFile = 'Command.txt'
def checkFile(filename):
    
    if os.path.isfile(filename) == True:
        print(filename + ' File Located')
    else:
        exit('Sorry Incorrect filename or path')
        #exit()
        
def sshConnect(ip_list,UserFile):
    
    #create ssh client object and set policy to add ip automatically to known
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) 
    userName,passWord = getUser(userFile)
    #loop through ip list and connect to each 
    for x in ip_list:
        try:
            ssh_client.connect(hostname = x,username=userName,password=passWord)
        except paramiko.AuthenticationException:
            print (" Authentication Exception!")
        except paramiko.SSHException:
            print (" SSH Exception!")
        
def getUser(UserFile):
     #open user/password file plist save to variable only one username and password
    print(userFile + ' File Located')
    f = open(userFile,'r')
    fString = f.readline()       #[lambda x: x.split(',') for x in f]
    userName,passWord = fString.split(',')
    f.close()
    return userName,passWord        

def config(cmdFile,userFile,ip_list):
    #open and read commands file 
    cmds = open(cmdFile,'r')
    # send commands to router
    sshConnect(userFile,ip_list)
    connection = sshConnect.ssh_client.invoke_shell()
    for i in cmds:
            connection.send(i + '\n')
            time.sleep(1)
        
    sshConnect.ssh_client.close()     

#sslConnect(userFile,cmdFile)        
#if __name__ == '__main__':
    #checkFile(filename)    
    