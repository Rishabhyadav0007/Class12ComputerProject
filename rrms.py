
"""<----function to add train info---->"""

def addTrainInfo(mydb, cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS train_info(Train_name VARCHAR(100) UNIQUE NOT NULL, Train_no VARCHAR(10) PRIMARY KEY, Route TEXT NOT NULL, no_of_general_seat INT NOT NULL, no_of_sleeper_seat INT, no_of_AC1_seat INT , no_of_AC2_seat INT );")
    
    password = "@ddTr@inRRM$"
    while True:
        password_input = input("Enter your password: ")
        checker = 1
    
        if (password_input.lower() == password.lower()):
            while checker != 0:
                checker1 = 1
                train_no = input("Enter train no.: ")

                a = 0
                cursor.execute("SELECT Train_no FROM train_info;")
                list_of_train_no = cursor.fetchall()
                for i in range(len(list_of_train_no)):
                    if (train_no == list_of_train_no[i][0]):
                        a+= 1

                if(a == 1):
                    print(f"The train having train no. '{train_no}' already exist")
                    while checker1 != 0:
                        decisional_input = input(f"if you want to modify the information about train having train no. {train_no} press 1\nif you want to reinput the train no. press 2\nif you want to end the process press 3\n: ")

                        if (decisional_input == "1"):
                            modifyTrainInfo()
                        elif (decisional_input == "2"):
                            checker1 = 0
                        elif (decisional_input == "3"):
                            checker1, checker = 0,0
                        else:
                            continue

                else:
                    
                    train_name = input("Enter train name: ")
                    train_route = input("Enter the route of the train: ")
                    no_of_general_seat = int(input("Enter the total no.of general seat"))
                    no_of_sleeper_seat = int(input("Enter total no.of   sleeper seat: "))
                    no_of_AC1_seat = int(input("Enter total no.of AC-1  seat: ") )
                    no_of_AC2_seat = int(input("Enter total no.of AC-2  seat: ") )

                    #TODO: create a database were you can enter all these information
                    train_entry_list = [train_name, train_no, train_route.lower(), no_of_general_seat, no_of_sleeper_seat, no_of_AC1_seat, no_of_AC2_seat]
                    cursor.execute("insert into train_info (Train_name, Train_no, Route, no_of_general_seat, no_of_sleeper_seat, no_of_AC1_seat, no_of_AC2_seat) values(%s, %s, %s, %s, %s, %s, %s);",train_entry_list ); 
                    mydb.commit()
                    checker = 0

            break

        else:
            print("Incorrect password")            
            decisional_input_1 = input("if you want to try again press 1: ")
            if (decisional_input_1 == "1"):
                continue
            else:
                break

"""<----function to modify the train info---->"""
def modifyTrainInfo(mydb, cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS train_info(Train_name VARCHAR(100) UNIQUE NOT NULL, Train_no VARCHAR(10) PRIMARY KEY, Route TEXT NOT NULL, no_of_general_seat INT NOT NULL, no_of_sleeper_seat INT, no_of_AC1_seat INT , no_of_AC2_seat INT );")

    password = "M0difyTr@inRRM$"
    while True:
        checker = 1
        password_input = input("Enter your password: ")
        if (password_input.lower() == password.lower()):
            print("correct password")
            while checker != 0:
                checker1 = 1
                train_no = input("Enter train no.: ")

                #TODO: write the condition statement to check that train no. already exist in database or not
                a = 0
                cursor.execute("SELECT Train_no FROM train_info;")
                list_of_train_no = cursor.fetchall()
                for i in range(len(list_of_train_no)):
                    if (train_no == list_of_train_no[i][0]):
                        a+= 1
                
                if(a == 1):
                    while checker1 != 0:
                        modification_input = input("Press\n1 -> to modify  Train name\n2 -> to modify Route\n3 -> to modify no.of general seat\n4 -> to modify no.of sleeper seat\n5 ->  to modify no.of AC-1 seat\n6 -> to modify no.of AC-2 seat\n: ")

                        if(modification_input=="1"):
                            new_train_name = input("Enter new train name: ")
                            
                            cursor.execute(f"UPDATE Train_info SET Train_name = '{new_train_name}' WHERE Train_no = '{train_no}';")
                            mydb.commit()
                            checker1 = 0

                        elif(modification_input=="2"):
                            new_route = input("Enter new route: ")
                            
                            cursor.execute(f"UPDATE Train_info SET Route = '{new_route}' WHERE Train_no = '{train_no}';")
                            mydb.commit()
                            checker1 = 0

                        elif(modification_input=="3"):
                            modified_no_of_gen_seat = int(input("Enter no.of general seat: "))
                            
                            cursor.execute(f"UPDATE Train_info SET no_of_general_seat = '{modified_no_of_gen_seat}' WHERE Train_no = '{train_no}';")
                            mydb.commit()
                            checker1 = 0

                        elif(modification_input=="4"):
                            modified_no_of_sleeper_seat = int(input("Enter no.of sleeper seat: "))
                            
                            cursor.execute(f"UPDATE Train_info SET no_of_sleeper_seat = '{modified_no_of_sleeper_seat}' WHERE Train_no = '{train_no}';")
                            mydb.commit()
                            checker1 = 0

                        elif(modification_input=="5"):
                            modified_no_of_AC1_seat = int(input("Enter no.of AC-1 seat: "))
                            
                            cursor.execute(f"UPDATE Train_info SET no_of_AC1_seat = '{modified_no_of_AC1_seat}' WHERE Train_no = '{train_no}';")
                            mydb.commit()
                            checker1 = 0

                        elif(modification_input=="6"):
                            modified_no_of_AC2_seat = int(input("Enter no.of AC-2 seat: "))
                            
                            cursor.execute(f"UPDATE Train_info SET no_of_AC2_seat = '{modified_no_of_AC2_seat}' WHERE Train_no = '{train_no}';")
                            mydb.commit()
                            checker1 = 0

                        else:
                            print("Choose according to this...")

                    checker = 0
                else:
                    print("Train not Exists..\nPlease enter Train No. of existing train..")

            break                        
            
        else:
            print("Incorrect password")
            decisional_input_1 = input("if you want to try again press 1: ")
            if (decisional_input_1 == "1"):
                continue
            else:
                break

"""<----seat reaservation function---->"""
def seatReservation(mydb, cursor, userName, phoneNumber):
    import datetime as dt
    train_no = None
    while True:
        
        choice_input = input("Press\n1 -> To search your train by name\n2 ->to search your train by Train No.\n3 -> To search running on respective route\n: ")
        if (choice_input == "1"):
            while True:
                train_name = input("Enter the name of the train: ")

                cursor.execute("SELECT Train_name FROM train_info;")
                list_of_train_name = cursor.fetchall()
                
                b = 0
                for i in range(len(list_of_train_name)):
                    if (train_name in list_of_train_name[i][0]):
                        cursor.execute(f"SELECT Train_no FROM train_info WHERE Train_Name ='{train_name}';")
                        train_no_fetched_list = cursor.fetchall()
                        train_no = train_no_fetched_list[0][0] 
                        break
                    else:
                        b+= 1
                
                if (b == len(list_of_train_name)):
                    print(f"Train Having train name {train_name} not exist..")
                    termination_input = input("Press\n1-> to retry\nOtherwise press any other key: ")
                    if (termination_input == "1"):
                        continue
                    else:
                        break
                else:
                    break
                
            break
                                
        elif(choice_input == "2"):
            while True:
                train_no = input("Enter the train no.: ")
                cursor.execute("SELECT Train_no FROM train_info;")
                list_of_train_no = cursor.fetchall()
                b = 0
                for i in range(len(list_of_train_no)):
                    if(train_no != list_of_train_no[i][0]):
                        b+=1
                    else:
                        break
                if (b == len(list_of_train_no)):
                    print(f"Train Having train no {train_no} not exist..")
                    termination_input = input("Press\n1-> to retry\nOtherwise press any other key: ")
                    if (termination_input == "1"):
                        continue
                    else:
                        break
                break
            break

                    
        elif(choice_input == "3"):
            while True:
                from_station = input("Enter from which station you want to take the train: ")
                to_station = input("Enter to which station you want to go: ")
                cursor.execute("SELECT Route FROM Train_info;")
                route_list = cursor.fetchall()
                starting_station_found = 0
                starting_station_not_found = 0
                end_station_not_found = 0
                for i in range(len(route_list)):
                    route = str(route_list[i][0])
                    splited_route = route.split("-")
                    for j in range(len(splited_route)):
                        b= 0
                        if (splited_route[j] == from_station):
                            starting_station_found += 1
                            a = 0
                            for k in range(j, len(splited_route)):
                                
                                if (splited_route[k] == to_station):
                                    cursor.execute(f"SELECT Train_name FROM Train_info WHERE Route = '{route}' ")
                                    train_name_list = cursor.fetchall()
                                    list_ = []
                                    for i in range(len(train_name_list)):
                                        list_.append(f"{train_name_list[i][0]}")
                                    
                                    
                                    checker2 = 1
                                    print(list_)
                                    while checker2 != 0:
                                        print("Press")
                                        for j in range(len(list_)):
                                            print(f"{j+1}->{list_[j]}\n")
                                        train_name_selector_input = int(input("Enter your choice: "))
                                        
                                        try:
                                            cursor.execute(f"SELECT Train_no FROM Train_info WHERE train_name = '{list_[train_name_selector_input-1]}'")
                                            train_no_fetched_list = cursor.fetchall()
                                            train_no = train_no_fetched_list[0][0]
                                            checker2 = 0

                                        except:
                                            print("Choose According to This...")                                   

                                    break
                                else:
                                    a+= 1
    
                            if(a ==(len(splited_route)-j)):
                                end_station_not_found += 1
                            else:
                                break
                            
                                                            
                        else:
                            b+= 1

                    if (b == len(splited_route)):
                        starting_station_not_found+=1
                    elif (starting_station_found>end_station_not_found):
                        break
                    else:
                        pass

                if (starting_station_not_found == len(route_list)):
                    print("Their is no such station of such name in our database..")
                    termination_input = input("Press\n1-> to retry\nOtherwise press any other key: ")
                    if (termination_input == "1"):
                        continue
                    else:
                        break

                elif(starting_station_found == end_station_not_found):
                    print(f"Their is no any train from {from_station} to {to_station}")
                    termination_input = input("Press\n1-> to retry\nOtherwise press any other key: ")
                    if (termination_input == "1"):
                        continue
                    else:
                        break
                else:
                    break
            break

        else:
            print("Choose according to this...")

    """code to allot the seat to the user"""
    if train_no != None:
        while True:
            prize1 = 25
            prize2 = 50
            prize3 = 250
            prize4 = 500
            seat_input = input("Enter\n1-> for general class seat\n2-> for sleeper class seat\n3-> for AC-1 class seat\n4-> for AC-2 class seat\n<-----Guideline to input you seat----->\nfor seat put (-)sign and then write no.of seat and then put (,) for getting the seat of other kind.\nEnter (type of seat-no of seat, ):  ")
            amount = 0
            l = [f"<----Ticket is valid for train no = {train_no}---->\n"]
            seat_class = seat_input.split(",")
            for i in range(len(seat_class)):
                seat_info = seat_class[i].split("-")
            
                if (seat_info[0] == "1"):
                    
                    cursor.execute(f"SELECT no_of_general_seat FROM train_info WHERE Train_no = {train_no}")
                    no_general_seat = cursor.fetchall()[0][0]
                    if no_general_seat != 0:
                        cursor.execute(f"UPDATE train_info SET no_of_general_seat = no_of_general_seat-{seat_info[1]} WHERE Train_no = '{train_no}' AND no_of_general_seat != 0")
                        mydb.commit()
                        amount += int(seat_info[1])*prize1
                        l.append(f"No of General Seat= {seat_info[1]}\n")
                    else:
                        print("No More General Seat Not Available..")

                elif (seat_info[0] == "2"):
                    cursor.execute(f"SELECT no_of_sleeper_seat FROM train_info WHERE Train_no = {train_no}")
                    no_sleeper_seat = cursor.fetchall()[0][0]
                    if no_sleeper_seat != 0:
                        cursor.execute(f"UPDATE train_info SET no_of_sleeper_seat = no_of_sleeper_seat-{seat_info[1]} WHERE Train_no = '{train_no}' AND no_of_sleeper_seat != 0")
                        mydb.commit()
                        amount += int(seat_info[1])*prize2
                        l.append(f"No of Sleeper Seat= {seat_info[1]}\n")
                    else:
                        print("Sleeper Seat Not Available..")


                elif (seat_info[0] == "3"):
                    cursor.execute(f"SELECT no_of_AC1_seat FROM train_info WHERE Train_no = {train_no}")
                    no_AC1_seat = cursor.fetchall()[0][0]
                    if no_AC1_seat != 0:
                        cursor.execute(f"UPDATE train_info SET no_of_AC1_seat = no_of_AC1_seat-{seat_info[1]} WHERE Train_no = '{train_no}' AND no_of_AC1_seat != 0")
                        mydb.commit()
                        amount += int(seat_info[1])*prize3
                        l.append(f"No of AC-1 Seat= {seat_info[1]}\n")
                    else:
                        print("AC-1 Seat Not Available..")

                elif (seat_info[0] == "4"):
                    cursor.execute(f"SELECT no_of_AC2_seat FROM train_info WHERE Train_no = {train_no}")
                    no_AC2_seat = cursor.fetchall()[0][0]
                    if no_AC2_seat != 0:
                        cursor.execute(f"UPDATE train_info SET no_of_AC2_seat = no_of_AC2_seat-{seat_info[1]} WHERE Train_no = '{train_no}' AND no_of_AC2_seat != 0")
                        mydb.commit()
                        amount += int(seat_info[1])*prize4
                        l.append(f"No of AC-2 Seat= {seat_info[1]}\n")
                    else:
                        print("AC-2 Seat Not Available..")

                else:
                    print("Enter according to this...")
                    break
            print(f"Amount you have to pay: {amount}")
            with open(f"{userName}_{phoneNumber}_{train_no}_{dt.date.today()}_ticket.txt", "a") as file:
                file.writelines(l)
            break
        
    else:
        print("Train which you have searched do not exists...")




