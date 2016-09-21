#Assignment1: Write an  application in Python to parse different files.
#On running app it should show a prompt
#On the prompt user can input following commands
#exit : to exit
#parse <filename> : parse given file
#show last  : show info of last parsed files
#show : show info of all parsed files individually
#del: delete info of oldest fil parsed.

#!usr/bin/python

import os
import sys
from all_class import text_file
from all_class import csv_operation
from all_class import Stack

stack_instance = Stack()
def display_menu():
    while (True) :

        print "/*=======================File_Paraser=====================*/\n "
        print "  *****  Please Choose File  parse operation:  *****"
        print "         1.Parse <File name> : Parse Given File.              "
        print "         2.Show Last : Show Info of Last Parsed File.         "
        print "         3.Show all :Show Info all Parsed Files Individually  "
        print "         4.Delete File : To Delete Info oldes file parsed.    "
        print "         5.Exit:To Exit                                      "
        print "/*=======================*End_Of_Menu*=====================*/\n"


        dict_func = {1:parseFile,
             2:show_last,
             3:show_all,
             4:deleteFile,
             5:exit
                   }
        try :
            key = int( raw_input("Please Enter Your Option: "))

        except :
            print ("Please enter a valid option!!\n")
            continue

        function = dict_func.get(key,'Not a valid choice!! Try again!!\n')
        print function
        previous_file_info = function()
        print stack_instance
        stack_instance.push(previous_file_info)

def parseFile():

#path = sys.argv[1]
    print("\n")
    path=raw_input("Enter path for File :")
    if os.path.exists(path) :
        fileName = os.path.basename(path) #this returns string after last slash


        if fileName.endswith(".txt"):
            text_instance = text_file(fileName)
            file_info = text_instance.show_text_info_method()
            return file_info

        if fileName.endswith(".csv"):
            csv_instance = csv_operation(fileName)
            file_info =  csv_instance.csv_read_method()
            return file_info

    else :
        print "Path dosn't exists!! Try again!!\n"
        return

def show_last():

    try:
        print "show last\n"
        print stack_instance.pop()

    except:
        print "Stack is Empty!!"

def show_all():
    try :
        while stack_instance:
            print stack_instance.pop()

    except :
        print "Stack is Empty!!"

def deleteFile():

    try:
        oldestFile = stack_instance.last()
        fileName = oldestFile['fileType']
        os.unlink(fileName) #will delete the file at path
        print "File Deleted!!"

    except:
        print "No File For Delete !! Try again!!"

def exit():

    try:
        print "exit"
        sys.exit(1)

    except:
        print "Error: In Exit"

if __name__ == '__main__':
    display_menu()

