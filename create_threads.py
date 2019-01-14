# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 21:00:47 2018

@author: adam
"""
import os
import paramiko
import threading
from ssh_connection import getUser

def cmdSession(userFile,ip,cmdFile):
    #create ssh client object and set policy to add ip automatically to known
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    userName,passWord = getUser(userFile)
    try:
        ssh_client.connect(hostname = ip
                           ,username=userName,password=passWord)
    except paramiko.AuthenticationException:
        print (" Authentication Exception!")
    except paramiko.SSHException:
        print (" SSH Exception!")
    connection = ssh_client.invoke_shell()
    print('Enter commands below and enter q to end session')
    #open and read commands file 
    cmds = open(cmdFile,'r')
    connection.send(cmds + '\n')
    try:
        print(paramiko.stdout.read())
    except 'e':
        print('No output recieved')
    
    ssh_client.close()  
    exit()
        
def  multiSession(ip_list,userFile):   
    #Start threads for each command sesion for each devices
    processes = []
    for x in ip_list:
        ip = x
        new_thread = threading.Thread(target = cmdSession, args = (userFile,ip))
        new_thread.start()
        #add each new thread to list and sychronise
        processes.append(new_thread)
        
            
   
    