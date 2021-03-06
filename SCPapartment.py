import os
import time
from datetime import datetime

def banner(Type,Data =""):
    if Type == "start":
        print('-----' *18)
        print('\t' *3, "South City Plaza Apartment")
        print('-----' *18)
        
    if Type == "rooms":
        a = """ Apartment Type A
               - 2 bedrooms and equiped with kitchen and laundry
               - Monthly rental is RM300 per room """
        b = """ Apartment Type B
               - 3 bedrooms including one master bedroom with attached bedroom
               - No kitchen and laundry facilities
               - Monthly rental is RM200 with normal room and additional 40% for master room """
        print(a)
        print()
        print(b)

    if Type == "menu":
        print("\t-- Main Menu --")
        print()
        print("\t1:" , "Login ")
        print("\t2:" , "Register ")
        print("\t0:" , "Exit ")

    if Type == "U_menu":
        print("\t-- User Menu --")
        print()
        print("\t1:" , "Book Accommodation ")
        print("\t2:" , "View Booking")
        print("\t3:" , "Payment ")
        print("\t4:" , "Cancel Booking or/ Checkout")
        print("\t5:" , "Logout")
    
    if Type == "welcome":
        print ("Welcome",Data, "!")

    if Type == 'payment':
        print('\t-- Payment --',end = '\n\n')
        print('Please bank in to: ',end = '\n\n')
        print('''\tASIA PACIFIC UNIVERSITY SDN BHD
\tAPU Foundation, APU Diploma, APU/SU
\tDegrees and APU Engineering Degrees
\tA/C Name : ASIA PACIFIC UNIVERSITY SDN BHD
\tRM Account No : 514413500658
\tBANK ADDRESS
\tMALAYAN BANKING BERHAD
\tLot No. G-1 & G-2, Ground Floor
\tSupport Service Building,
\tTechnology Park Malaysia,
\tLebuhraya Puchong-Sg. Besi, Bukit Jalil,
\t57000 Kuala Lumpur, Malaysia''')
    
    print()

def menu():
    
    clear()
    banner("start")
    banner("menu")   
    M_option = input("Please select an option   :")
    print()
    M_option = M_option.lower()

    if M_option.isnumeric():
        
        M_option = int(M_option)
        
        if M_option == 1:   #Login
            username = input("Please enter your username  : ")
            password = input("Please enter your password  : ")
            
            U_login(username,password)
            
        if M_option == 0:   #Exit
            exit()
            
    else:
        
        if "help" in M_option:
            banner(4)
        
def U_login(username,password,times = 0):


    times += 1 
    if username == "" or password == "" :

        print("Please enter a vaild username or/ password")
        print()
        if times < 5 : 
            username = input("Please enter your username  : ")
            password = input("Please enter your password  : ")
            print()
            
            U_login(username,password,times)
        else:
            menu()

    if username in [n for n,num in name.items()] and password[name[username]] == password :
        U_menu(username)

    else:
        print("Please enter a vaild username or/ password")
        print()
        if times < 5 : 
            username = input("Please enter your username  : ")
            password = input("Please enter your password  : ")
            print()
            
            U_login(username,password,times)
        else:
            menu()        
        
        U_login(username,password,times)


def U_menu(username):
    
    clear()
    banner("start")
    banner("welcome",username)
    banner("U_menu")       
    M_option = input("Please select an option   :")
    clear()

    if M_option.isnumeric():    #check is number or not
        
        M_option = int(M_option)
        if M_option == 1:
            Bk_menu(1,username)
        if M_option == 5:
            menu()


def Bk_menu(process,username):
    
    if process == 1:
        clear()
        banner('start')
        banner('rooms')
        M_option = input("Please select a room type : ")
        time.sleep(1)
        
        if M_option.isnumeric():    #check is number or not
            if R_check(int(M_option)):
                input('\nClick anykey to continue...')
                Bk_menu(2,username)
            else:
                print("Sorry, the room is full/ not available")

    if process == 2:
        cont = "y"
        while cont != "n":
            
            clear()
            banner('start') 
            print("\t--Personal Detail--\n")
            #My God personal detail
            userinfo = []
            userinfo.append(input('Full Name \t\t\t : '))
            userinfo.append(input('IC number \t\t\t : '))
            userinfo.append(input('Phone Number \t\t\t : '))
            print("Address : ")
            userinfo.append(input('\tStreet name \t\t : '))
            userinfo.append(input('\tStreet name 2 \t\t : '))
            userinfo.append(input('\tCity \t\t\t : '))
            userinfo.append(input('\tState \t\t\t : '))
            userinfo.append(input('\tZip Code \t\t : '))
            userinfo.append(input('E-Mail Address\t\t\t : '))
            cont = input("\nDo you want to edit? (Y/N) \t :").lower()

        #Store info here
        Bk_menu(3,username)

    if process == 3:
        banner('start')
        banner('payment')
        input('Enter any key to continue...')
        Bk_menu(4,username)

    if process == 4:
        print('You are finished! Here is your room\'s detail.')
            
def R_check(number):
    
    if number == 1 :
        return True
    else :
        return False


clear = lambda: os.system('cls')
name = {'benny':1,'chong':2,'yolo':3, 'admin':0}
password = ['1', 'nani','kao']
P_info =[['','','','','','','','','1'],['','','','','','','','','2']]
R_info = [[1,-2],[2,432]]
menu()
