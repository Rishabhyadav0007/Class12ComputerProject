# Railway Reservation and Management Service (RRMS)

import mysql.connector
import rrms

mydb = mysql.connector.connect(host="localhost", user="root", password="root", database="railway_reservation_and_management_service")# change the password from root to your password

cursor = mydb.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS railway_reservation_and_management_service")
cursor.execute("USE railway_reservation_and_management_service")
cursor.execute("CREATE TABLE IF NOT EXISTS user_info(Name VARCHAR(100) NOT NULL, Phone_number VARCHAR(15) PRIMARY KEY, Email_add VARCHAR(100) NOT NULL, password VARCHAR(100) NOT NULL)")

print("Welcome to Railway Reservation and Management Service (RRMS)")

# function handel the login functionality
#login() return Username and Phone number of the user who login and insert the info of new user in database
def login():
    checker = 1
    #while loop to make this block of code to loop till user login correctly
    while checker != 0:
        print("\n===== Login =====")
        name_input = input("Enter your username: ")
        email_input = input("Enter your email address: ")
        phone_number = input("Enter your phone number: ")
        password_input = input("Enter your password: ")
        print("\n=====\=====/=====")

        cursor.execute("SELECT Phone_number FROM user_info;")
        user_info_list = cursor.fetchall()#fetch the phone number of all user from database (return=> a list[list]=> [[],[],...])
        a = 0
        for i in range(len(user_info_list)):#(TODO :Use binary search to search it faster.)                
            if(phone_number in user_info_list[i]): #check weather the phone number which user entered exists in the database or not.

                print("User already exists..")
                input_ = input("Press \n1-> To SignUp \n2-> Try Again\nEnter your choice: ")
                if (input_ == "1"):
                    print("\n===== SignUp =====")
                    userName , phoneNumber = signUp(phone_number)# calls a signUp() which return to values.. 1-:> Name of user 2-:> Phone number of user
                    checker = 0
                    break
                elif(input_ == "2"):
                    break
                else:
                    print("Enter Correct info: ")
                break
            else:
                a+=1 #increment a by 1 (Reason: when phone number don't exist it inc. the value of a by 1 so at the end if the value of a is equal to the lenght of the fetched list.)

        if (a == len(user_info_list)):
            user_entry_list = [name_input, phone_number, email_input, password_input]
            cursor.execute("USE railway_reservation_and_management_service")
            cursor.execute("""INSERT INTO user_info(Name, Phone_number, Email_add, password) VALUES (%s,%s,%s,%s)""", user_entry_list)
            mydb.commit()
            userName, phoneNumber = name_input, phone_number
            checker = 0
            
    return userName, phoneNumber

# function handel the Sign Up functionality
#signUp() return Username and Phone number of the user who Sign Up
def signUp(phoneNumber):
    checker = 1
    while checker != 0:
        sign_up_password = input("Enter your password: ")
        cursor.execute(f"SELECT password FROM user_info WHERE Phone_number = {phoneNumber}")
        fetched_password = cursor.fetchall() #fetch the password of the user from database, whose phone number is provider
        try:                          
            if(sign_up_password not in fetched_password[0][0]):
                print("Incorrect password...")
            
            else:
                checker = 0
                phoneNumber = phoneNumber
                cursor.execute(f"SELECT Name FROM user_info WHERE Phone_number =     {phoneNumber}")
                name = cursor.fetchall()
                userName = name[0][0]
                print("\n=====\======/=====")
                return userName, phoneNumber
        except:
            print("User with this Phone number does not exists!")
            while checker!= 0:
                input_  = input("Press \n1-> To login \n2-> Try Again\nEnter your choice: ")
                if(input_ == "1"):
                    userName, phoneNumber = login()
                    checker = 0
                    return userName, phoneNumber
                                        
                elif(input_ =="2"):
                    print("\n===== SignUp =====")
                    phoneNumber = input("Enter your phone Number: ")
                        
                else:
                    print("Enter Correct option! ")          
    
#login/signup page
while True:
    
    print("\n=====Login/SignUp=====")
    setup_input = input("press\n1-> To login\n2-> To sign up\nEnter your choise: ")
    print("\n=====\============/=====")
    if (setup_input == "1"):
        userName, phoneNumber = login()              
        break

    elif(setup_input == "2"):
        checker = 1
        print("\n===== SignUp =====")
        sign_up_phone_number = input("Enter your phone Number: ")
        userName, phoneNumber = signUp(sign_up_phone_number)
        break
                
    else:
        print("Enter according to this...")

#menu page
while True:
    checker = 1
    print("\n===== Menu =====\n")
    print("Press \n1 -> to Add Informaton about new Train\n2 -> to Modify Information about already existing train\n3 -> to Reserve your Seat\n4 -> to exit")

    initial_input = input("\nEnter your choice: ")
    print("\n=====\====/=====\n")
    if (initial_input == "1"):
        while checker != 0:
            rrms.addTrainInfo(mydb, cursor)

            termination_input = input("If you want to add more trains then press 1: ")
            if (termination_input == "1"):
                continue
            else:
                checker = 0

        termination_input1 = input("If you want to continue press 1 otherwise press any other key: ")
        if termination_input1 == "1":
            continue
        else:
            break

    elif (initial_input == "2"):
        while checker != 0:
            rrms.modifyTrainInfo(mydb, cursor)

            termination_input = input("If you want to modify more trains then press 1: ")
            if (termination_input == "1"):
                continue
            else:
                checker = 0

        termination_input1 = input("If you want to continue press 1 otherwise press any other key: ")
        if termination_input1 == "1":
            continue
        else:
            break
        
    elif (initial_input == "3"):
        while checker != 0:
            rrms.seatReservation(mydb, cursor, userName, phoneNumber)

            termination_input = input("If you want to reserve more seats then press 1: ")
            if (termination_input == "1"):
                continue
            else:
                checker = 0

        termination_input1 = input("If you want to continue press 1 otherwise press any other key: ")
        if termination_input1 == "1":
            continue
        else:
            break
    elif(initial_input == "4"):
        break
    
    else:
        print("Enter your choice according to this...")

