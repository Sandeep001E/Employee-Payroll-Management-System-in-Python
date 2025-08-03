import time
import os
import getpass
import msvcrt
import csv
import ctypes
import sys
import random


class Colour:
    red = "\033[0;31m"
    blue = "\033[0;34m"
    green = "\033[0;32m"
    cyan = "\033[0;36m"
    yellow = "\033[1;33m"
    light_green = "\033[1;32m"
    light_purple = "\033[1;35m"
    light_gray = "\033[0;37m"
    dark_gray = "\033[1;30m"
    light_red = "\033[1;31m"
    orange = "\033[38;5;208m"

    bold = "\033[1m"
    blink = "\033[5m"

    end = "\033[0m"


class COORD(ctypes.Structure):
    _fields_ = [("X", ctypes.c_short), ("Y", ctypes.c_short)]

    def __init__(self, x, y):
        self.X = x
        self.Y = y


class Position():
    STD_OUTPUT_HANDLE = -11
    hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)

    def __init__(self, x, y):
        self.pos = COORD(x, y)

    def show(self):
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.hOut, self.pos)

    def clearText(self):
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.hOut, self.pos)
        print(" "*self.maxlength)


class TextField():
    STD_OUTPUT_HANDLE = -11
    hOut = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
    TEXT = ""

    def __init__(self, x, y, maxlength):
        self.pos = COORD(x, y)
        self.maxlength = maxlength

    def setText(self, text):
        self.text = text

    def show(self):
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.hOut, self.pos)
        self.pw = getpass.getpass()
        return (self.pw)
        del self

    def clearText(self):
        ctypes.windll.kernel32.SetConsoleCursorPosition(self.hOut, self.pos)
        print(" "*self.maxlength)

    def _del_(self):
        self.clearText()


colour = Colour()


class Invalid_Choice(Exception):
    pass


def clear_screen():
    os.system('cls')


def delete_last_line():
    sys.stdout.write('\x1b[1A')
    sys.stdout.write('\x1b[2K')


def GUI():
    global flag
    if (flag == 0):
        clear_screen()
        print("\n\n\n\n\n\n")
        print(f"{colour.cyan}{colour.bold}EPMS{colour.end}".center(150))
        time.sleep(1.5)  # 1.5
        clear_screen()
        print("\n\n\n\n\n\n")
        print(
            f"{colour.cyan}{colour.bold}Employee Payroll Management System{colour.end}\n".center(150))
        time.sleep(1.5)  # 1.5
        print("Getting Started...".center(135))
        time.sleep(3)  # 3

    while (True):
        clear_screen()
        print("Employee Payroll Management System".center(140))
        print("***  LOGIN  ***".center(140))
        print()
        id = input("\t\t\t\t\t\t\t\tUser id:")
        if (id == "630021"):
            pw = getpass.getpass("\t\t\t\t\t\t\t\tpassword:")
            if (pw == "aaa"):
                print()
                print(
                    f"{colour.light_green}Login Successful{colour.end}".center(156))
                time.sleep(2)  # 1
                id = Admin_GUI()
                return (id)
            else:
                print()
                print(
                    f"{colour.red}Incorrect Password{colour.end}".center(156))
                time.sleep(2)  # 1
                continue
        else:
            file = open('DataBase.csv', "r")
            check = csv.reader(file)
            for row in check:
                if (id != row[0]):
                    continue
                else:
                    if (row[1] == "0"):
                        print(
                            f"\n\t\t\t\t\t\t\t\t{colour.light_green}NEW EMPLOYEE...")
                        time.sleep(2)  # 2
                        file.close()
                        id = New_Employee(row)
                        return (id)
                    pw = getpass.getpass("\t\t\t\t\t\t\t\tPassword:")
                    if (pw != row[1]):
                        print()
                        print(
                            f"\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Incorrect Password{colour.end}")
                        while (True):
                            textfield = TextField(x=64, y=4, maxlength=20)
                            textfield.setText("Password:")
                            pw = textfield.show()
                            if (pw != row[1]):
                                print()
                                print(
                                    f"\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Incorrect Password{colour.end}")
                                continue
                            else:
                                print()
                                print(
                                    f"{colour.light_green}Login Successful{colour.end}".center(156))
                                time.sleep(2)  # 3
                                file.close()
                                return (id)
                    else:
                        print()
                        print(
                            f"{colour.light_green}Login Successful{colour.end}".center(156))
                        time.sleep(2)  # 3
                        file.close()
                        return (row[0])
            print()
            print(
                f"\t\t\t\t\t\t\t\t{colour.red}{colour.bold}ID not found{colour.end}")
            time.sleep(3)


def Admin_Menu_Modifier():
    file = open('DataBase.csv', "r")
    DataBase = csv.reader(file)
    pw_count, work_count = 0, 0
    for row2 in DataBase:
        if (row2[1] == "0"):
            pw_count = pw_count+1
        elif (row2[7] == "0"):
            work_count = work_count+1
        elif (row2[6] == "630021"):
            if (row2[11] == "-1"):
                work_count = work_count+1
            elif (row2[11] == "1"):
                work_count = work_count+1
    file.close()
    return (pw_count, work_count)


def Admin_GUI():
    if (Admin_GUI_flag == 0):
        clear_screen()
        print("\n\n\n\n\n\n\n\n\n\n")
        print(
            f"{colour.green}{colour.bold}Welcome Mr.{Admin} {colour.end}\n".center(150))
        time.sleep(2)  # 1
    clear_screen()
    print(
        f"{colour.dark_gray}Employee Payroll Management System{colour.end}".center(150))
    print(f"{colour.green}{colour.bold}Mr.{Admin}")
    print(f"Admin{colour.end}")
    if (Admin_flag == 0):
        id = Admin_Menu()
        if (Admin_GUI_flag == 0):
            return (id)


def Admin_Menu():
    global flag
    global Admin_GUI_flag, Admin_flag
    pw_count, work_count = Admin_Menu_Modifier()
    while (True):
        print("\n\t\t\t\t\t\t\t\t1.Salary Payment")
        print("\t\t\t\t\t\t\t\t2.Add Team Leader")
        print("\t\t\t\t\t\t\t\t3.Add Employee")
        print("\t\t\t\t\t\t\t\t4.Employee List")
        print("\t\t\t\t\t\t\t\t5.Announce")
        if ((pw_count+work_count) == 0):
            print("\t\t\t\t\t\t\t\t6.Assign Work")
        else:
            print(
                f"\t\t\t\t\t\t\t\t6.Assign Work{colour.orange} ({pw_count+work_count}){colour.end}")
        print("\t\t\t\t\t\t\t\t7.Logout")
        try:
            op = int(input("\n\t\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > 7) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)  # 1
            Admin_GUI_flag = 1
            Admin_flag = 1
            Admin_GUI()
            Admin_flag = 0
            continue
    match(op):
        case 1:
            Admin_flag = 1
            Admin_GUI_flag = 1
            id = Salary_Payment()
            return (id)
        case 2:
            Admin_flag = 1
            Admin_GUI_flag = 1
            id = Add_Team_Leader(1)
            return (id)
        case 3:
            Admin_flag = 1
            Admin_GUI_flag = 1
            id = Add_Team_Leader(2)
            return (id)
        case 4:
            Admin_flag = 1
            Admin_GUI_flag = 1
            id = Employee_List()
            return (id)
        case 5:
            Admin_flag = 1
            Admin_GUI_flag = 1
            id = Announce()
            return (id)
        case 6:
            Admin_flag = 1
            Admin_GUI_flag = 1
            id = Assign_Work()
            return (id)
        case 7:
            flag = 1
            Admin_flag = 0
            Admin_GUI_flag = 0
            id = GUI()
            return (id)


def Team_Leader_GUI(row):
    if (row[3] == "male"):
        gender = "Mr"
    else:
        gender = "Miss"
    if (Team_Leader_GUI_flag == 0):
        clear_screen()
        print("\n\n\n\n\n\n\n\n\n\n")
        print(
            f"{colour.cyan}{colour.bold}Welcome {gender}. {row[2]}{colour.end}\n".center(150))
        time.sleep(2)  # 2
    clear_screen()
    print(f"{colour.dark_gray}Employee Payroll Management System{colour.end}".center(150))
    print(f"{colour.light_purple}{gender}. {row[2]}")
    print("Team Leader")
    print(f"Project : {row[7]}{colour.end}")
    if (Team_Leader_flag == 0):
        id = Team_Leader_Menu(row)
        if (Team_Leader_GUI_flag == 0):
            return (id)


def Team_Leader_Menu(row):
    global flag, Team_Leader_flag, Team_Leader_GUI_flag
    global Employee_flag, Employee_GUI_flag
    while (True):
        if (row[9] == "1"):
            print(
                f"\n\t\t\t\t\t\t\t\t1.Salary Status {colour.orange}(1){colour.end}")
        else:
            print("\n\t\t\t\t\t\t\t\t1.Salary Status")
        print("\t\t\t\t\t\t\t\t2.Profile")
        print("\t\t\t\t\t\t\t\t3.Team Members")
        if (row[10] == "1"):
            print(
                f"\t\t\t\t\t\t\t\t4.Announcements {colour.orange}(1){colour.end}")
        else:
            print("\t\t\t\t\t\t\t\t4.Announcements")
        if (row[11] == "-1"):
            print(
                f"\t\t\t\t\t\t\t\t5.Work Status {colour.orange}(1){colour.end}")
        else:
            print("\t\t\t\t\t\t\t\t5.Work Status")
        print("\t\t\t\t\t\t\t\t6.Logout")
        try:
            op = int(input("\n\t\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > 6) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(3)
            Team_Leader_GUI_flag = 1
            Team_Leader_flag = 1
            Team_Leader_GUI(row)
            Team_Leader_flag = 0
            continue

    match op:
        case 1:
            Team_Leader_flag = 1
            Team_Leader_GUI_flag = 1
            id = Salary_Status(row)
            return (id)
        case 2:
            Team_Leader_flag = 1
            Team_Leader_GUI_flag = 1
            id = Profile(row)
            return (id)
        case 3:
            Team_Leader_flag = 1
            Team_Leader_GUI_flag = 1
            id = Team_Members(row)
            return (id)
        case 4:
            Team_Leader_flag = 1
            Team_Leader_GUI_flag = 1
            id = Announcements(row)
            return (id)
        case 5:
            Team_Leader_flag = 1
            Team_Leader_GUI_flag = 1
            id = Work_Status(row)
            return (id)
        case 6:
            flag = 1
            Team_Leader_flag = 0
            Team_Leader_GUI_flag = 0
            Employee_GUI_flag = 0
            Employee_flag = 0
            id = GUI()
            return (id)


def Employee_GUI(row):
    if (row[3] == "male"):
        gender = "Mr"
    else:
        gender = "Miss"
    if (Employee_GUI_flag == 0):
        clear_screen()
        print("\n\n\n\n\n\n\n\n\n\n")
        print(
            f"{colour.cyan}{colour.bold}Welcome {gender}. {row[2]}{colour.end}\n".center(150))
        time.sleep(0.5)  # 2
    clear_screen()
    print(f"{colour.dark_gray}{colour.bold}Employee Payroll Management System".center(150))
    print(f"{colour.light_purple}{gender}. {row[2]}")
    file = open('DataBase.csv', "r")
    DataBase = csv.reader(file)
    for row2 in DataBase:
        if (row2[0] == row[6]):
            Team_Leader_Name = row2[2]
            break
    file.close()
    print(f"Team Leader : {Team_Leader_Name}")
    print(f"Project : {row[7]}{colour.end}")
    if (Employee_flag == 0):
        id = Employee_Menu(row)
        if (Employee_GUI_flag == 0):
            return (id)


def Employee_Menu(row):
    global flag
    global Team_Leader_flag, Team_Leader_GUI_flag
    global Employee_flag, Employee_GUI_flag
    while (True):
        if (row[9] == "1"):
            print(
                f"\n\t\t\t\t\t\t\t\t1.Salary Status {colour.orange}(1){colour.end}")
        else:
            print("\n\t\t\t\t\t\t\t\t1.Salary Status")
        print("\t\t\t\t\t\t\t\t2.Profile")
        print("\t\t\t\t\t\t\t\t3.Team Members")
        if (row[10] == "1"):
            print(
                f"\t\t\t\t\t\t\t\t4.Announcements {colour.orange}(1){colour.end}")
        else:
            print("\t\t\t\t\t\t\t\t4.Announcements")
        print("\t\t\t\t\t\t\t\t5.Logout")
        try:
            op = int(input("\n\t\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > 6) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(3)
            Employee_GUI_flag = 1
            Employee_flag = 1
            Employee_GUI(row)
            Employee_flag = 0
            continue
    match op:
        case 1:
            Employee_GUI_flag = 1
            Employee_flag = 1
            id = Salary_Status(row)
            return (id)
        case 2:
            Employee_GUI_flag = 1
            Employee_flag = 1
            id = Profile(row)
            return (id)
        case 3:
            Employee_GUI_flag = 1
            Employee_flag = 1
            id = Team_Members(row)
            return (id)
        case 4:
            Employee_GUI_flag = 1
            Employee_flag = 1
            id = Announcements(row)
            return (id)
        case 5:
            flag = 1
            Team_Leader_flag = 0
            Team_Leader_GUI_flag = 0
            Employee_GUI_flag = 0
            Employee_flag = 0
            id = GUI()
            return (id)


def Salary_Payment():
    global Admin_flag, file
    while (True):
        Admin_GUI()
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}SALARY PAYMENT{colour.end}")
        print("\n")
        filex = open('DataBase.csv', "r")
        DataBase = csv.reader(filex)
        payroll_yearly = 0
        for row in DataBase:
            payroll_yearly = payroll_yearly+int(row[8])
        filex.close()
        payroll_monthly = payroll_yearly/12
        if (payroll_yearly >= 100):
            print(
                f"\n\t\t\t\t\t\tYearly Payroll : {payroll_yearly/100} Crores")
        else:
            print(f"\n\t\t\t\t\t\tYearly Payroll : {payroll_yearly} Lakhs")
        if (payroll_monthly >= 100):
            print(
                f"\t\t\t\t\t\tMonthly Payroll : {round(payroll_monthly/100, 2)} Crores")
        else:
            print(
                f"\t\t\t\t\t\tMonthly Payroll : {round(payroll_monthly, 2)} Lakhs")
        print("\n")
        print("\t\t\t\t\t\t\t1.Pay Salary")
        print("\t\t\t\t\t\t\t2.Back")
        try:
            op = int(input("\n\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            continue
    match op:
        case 1:
            print(
                f"\n\t\t\t\t\t\tDate of Payment : {colour.dark_gray}dd-mm-yyyy{colour.end}")
            position = Position(x=66, y=17)
            position.show()
            dop = input()
            file1 = open('DataBase.csv', "r")
            file2 = open('modify.csv', "w", newline="")
            DataBase2 = csv.reader(file1)
            copy = csv.writer(file2)
            for row in DataBase2:
                data = row
                data[9] = "1"
                copy.writerow(data)
            file1.close()
            file2.close()
            file.close()
            os.remove('DataBase.csv')
            os.rename('modify.csv', 'DataBase.csv')
            file3 = open('Payments.csv', "r")
            file4 = open('modify.csv', "w", newline="")
            DataBase3 = csv.reader(file3)
            copy = csv.writer(file4)
            for row2 in DataBase3:
                data = row2
                data.insert(1, dop)
                copy.writerow(data)
            file3.close()
            file4.close()
            os.remove('Payments.csv')
            os.rename('modify.csv', 'Payments.csv')
            print(f"\n\t\t\t\t\t\t{colour.light_green}Processing Payments...")
            time.sleep(2)
            delete_last_line()
            print(f"\t\t\t\t\t\tPayments Successfull.{colour.end}")
            print(
                f"\t\t\t\t\t\t{colour.dark_gray}Press Enter for Main Memu...")
            msvcrt.getch()
            Admin_flag = 0
            id = Admin_GUI()
            return (id)
        case 2:
            Admin_flag = 0
            id = Admin_GUI()
            return (id)


def New_Employee(row):
    global flag, file
    Data = row
    clear_screen()
    print("\n\n\n\n\n\n")
    print(
        f"{colour.light_green}{colour.bold}WELCOME TO EMPS{colour.end}\n".center(150))
    time.sleep(1)
    print(
        f"{colour.light_green}{colour.bold}EMPLOYEE PAYROLL MANAGEMENT SYSTEM{colour.end}\n".center(150))
    time.sleep(2)
    clear_screen()
    print(f"{colour.dark_gray}{colour.bold}Employee Payroll Management System{colour.end}".center(150))
    pw = input(f"\n\t\t\t\t\t\t\tCreate Password : ")
    print(f"\n\t\t\t\t\t\t\t{colour.light_green}{colour.bold}Password Saved")
    Data[1] = pw
    time.sleep(2)
    clear_screen()
    print(f"{colour.dark_gray}{colour.bold}Employee Payroll Management System".center(150))
    print(
        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}DATA ENTRY{colour.end}")
    c = 0
    Name = input("\n\t\t\t\t\t\t\tName : ")
    print(f"\n\t\t\t\t\t\t\t\t{colour.light_green}Saving Data...{colour.end}")
    Data[2] = Name
    time.sleep(1)
    delete_last_line()
    delete_last_line()
    while (True):
        if (c == 1):
            clear_screen()
            print(
                f"{colour.dark_gray}{colour.bold}Employee Payroll Management System".center(150))
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}DATA ENTRY{colour.end}")
            print(f"\n\t\t\t\t\t\t\tName : {Name}")
        print("\n\t\t\t\t\t\t\tGender : ")
        print("\n\t\t\t\t\t\t\t\t1.Male")
        print("\t\t\t\t\t\t\t\t2.Female")
        try:
            op = int(input("\n\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            c = 1
        clear_screen()

    match op:
        case 1:
            Gender = "male"
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.light_green}Saving Data...{colour.end}")
            Data[3] = Gender
            time.sleep(1)
            delete_last_line()
        case 2:
            Gender = "female"
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.light_green}Saving Data...{colour.end}")
            Data[3] = Gender
            time.sleep(1)
            delete_last_line()
    while (True):
        clear_screen()
        print(
            f"{colour.dark_gray}{colour.bold}Employee Payroll Management System".center(150))
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}DATA ENTRY{colour.end}")
        print(f"\n\t\t\t\t\t\t\tName : {Name}")
        print(f"\t\t\t\t\t\t\tGender : {Gender}")
        print(
            f"\n\t\t\t\t\t\t\tDate of Birth : {colour.dark_gray}dd-mm-yyyy{colour.end}")
        position = Position(x=72, y=7)
        position.show()
        dob = input()
        dob = DOB_Modification(dob)
        if (dob == "0"):
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Date of Birth")
            time.sleep(2)
            continue
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.light_green}Saving Data...{colour.end}")
        Data[4] = dob
        time.sleep(1)
        delete_last_line()
        break
    while (True):
        clear_screen()
        print(
            f"{colour.dark_gray}{colour.bold}Employee Payroll Management System".center(150))
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}DATA ENTRY{colour.end}")
        print(f"\n\t\t\t\t\t\t\tName : {Name}")
        print(f"\t\t\t\t\t\t\tGender : {Gender}")
        print(
            f"\t\t\t\t\t\t\tDate of Birth : {dob}")
        email = input("\n\t\t\t\t\t\t\tEmail id : ")
        if ("@gmail.com" in email):
            pass
        else:
            print(
                f"\n\t\t\t\t\t\t\t{colour.orange}Entered email id is \"NOT VALID\"")
            print(
                f"\t\t\t\t\t\t\t{colour.light_red}Press Enter for \"TRY AGAIN\"...{colour.end}")
            msvcrt.getch()
            continue
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.light_green}Saving Data...{colour.end}")
        Data[5] = email
        time.sleep(1)
        delete_last_line()
        break
    clear_screen()
    print(f"{colour.dark_gray}{colour.bold}Employee Payroll Management System".center(150))
    print(
        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}DATA ENTRY{colour.end}")
    print(f"\n\t\t\t\t\t\t\tName : {Name}")
    print(f"\t\t\t\t\t\t\tGender : {Gender}")
    print(
        f"\t\t\t\t\t\t\tDate of Birth : {dob}")
    print(f"\t\t\t\t\t\t\tEmail id : {email}")
    print(f"\n\n\t\t\t\t\t\t\t{colour.light_green}Data Saved,Thankyou.")
    print(
        f"\t\t\t\t\t\t\t{colour.dark_gray}Press Enter to Log in...{colour.end}")
    file1 = open('DataBase.csv', "r")
    file2 = open('modify.csv', "w", newline="")
    DataBase = csv.reader(file1)
    copy = csv.writer(file2)
    for row2 in DataBase:
        if (row2[0] == Data[0]):
            copy.writerow(Data)
        else:
            copy.writerow(row2)
    file1.close()
    file2.close()
    os.remove('DataBase.csv')
    os.rename('modify.csv', 'DataBase.csv')
    msvcrt.getch()
    flag = 1
    id = GUI()
    return (id)


def Salary_Calculation(CTC):
    if (CTC <= 4):
        Tax = 0
    elif ((CTC > 4) and (CTC <= 8)):
        Tax = 5
    elif ((CTC > 8) and (CTC <= 12)):
        Tax = 10
    elif ((CTC > 12) and (CTC <= 16)):
        Tax = 15
    elif ((CTC > 16) and (CTC <= 20)):
        Tax = 20
    elif ((CTC > 20) and (CTC <= 24)):
        Tax = 25
    elif (CTC > 24):
        Tax = 30
    salary = Tax/100
    salary = int(salary*(CTC*100000))
    salary = int((CTC*100000)-salary-1000)
    salary = int(salary/12)
    return (salary, Tax)


def Salary_Status(row):
    global Team_Leader_flag
    global Employee_flag
    CTC = int(row[8])
    while (True):
        if (row[6] == "630021"):
            Team_Leader_GUI(row)
        else:
            Employee_GUI(row)
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}SALARY STATUS{colour.end}")
        print("\n")
        print(f"\t\t\t\t\t\t\tCTC= {CTC} LPA")
        Salary, Tax = Salary_Calculation(CTC)
        print(f"\t\t\t\t\t\t\tIncome Tax = {Tax} %")
        print("\t\t\t\t\t\t\tProfessional Tax = ₹ 1000")
        print(f"\t\t\t\t\t\t\tSalary (/month) = ₹ {Salary}")
        print("\n")
        if (row[9] == "1"):
            print(
                f"\n\t\t\t\t\t\t\t\t1.Payment History {colour.orange}(1){colour.end}")
        else:
            print("\n\t\t\t\t\t\t\t\t1.Payment History")
        print("\t\t\t\t\t\t\t\t2.Back")
        try:
            op = int(input("\n\t\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            continue
    match op:
        case 1:
            id = Payment_History(row)
            return (id)
        case 2:
            if (row[6] == "630021"):
                Team_Leader_flag = 0
                id = Team_Leader_GUI(row)
                return (id)
            else:
                Employee_flag = 0
                id = Employee_GUI(row)
                return (id)


def Payment_History(row):
    global Team_Leader_GUI_flag, Team_Leader_flag, file
    global Employee_GUI_flag, Employee_flag
    if (row[6] == "630021"):
        Team_Leader_GUI_flag = 1
        Team_Leader_flag = 1
        Team_Leader_GUI(row)
    else:
        Employee_GUI_flag = 1
        Employee_flag = 1
        Employee_GUI(row)
    print(
        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}PAYMENT HISTORY{colour.end}")
    filex = open('Payments.csv', "r")
    DataBase = csv.reader(filex)
    print("\t\t\t\t\t____________________________________________________________________")
    print(
        f"\t\t\t\t\t{colour.blue}{colour.bold}   S.No.     DATE OF PAYMENT    PAYMENT STATUS    PATMENT DEPOSITED{colour.end}")
    print("\t\t\t\t\t____________________________________________________________________")
    S_No = 1
    Salary, Tax = Salary_Calculation(int(row[8]))
    for row2 in DataBase:
        if (row2[0] == row[0]):
            payment = row2
    filex.close()
    if (row[9] == "1"):
        print(
            f"\t\t\t\t\t{colour.light_green}{colour.bold}    {S_No}          {payment[1]}       Successfull          {Salary}")
        S_No += 1
        for i in range(0, len(payment)):
            if ((i == 0) or (i == 1)):
                continue
            else:
                try:
                    print(
                        f"\t\t\t\t\t{colour.dark_gray}{colour.bold}    {S_No}          {payment[i]}       Successfull          {Salary}")
                    S_No += 1
                except:
                    pass
        file1 = open('DataBase.csv', "r")
        file2 = open('modify.csv', "w", newline="")
        DataBase2 = csv.reader(file1)
        copy = csv.writer(file2)
        data = row
        data[9] = "0"
        for row2 in DataBase2:
            if (row2[0] == row[0]):
                copy.writerow(data)
            else:
                copy.writerow(row2)
        file1.close()
        file2.close()
        file.close()
        os.remove('DataBase.csv')
        os.rename('modify.csv', 'DataBase.csv')
    else:
        for i in range(0, len(payment)):
            if (i == 0):
                continue
            else:
                try:
                    print(
                        f"\t\t\t\t\t{colour.dark_gray}{colour.bold}    {S_No}          {payment[i]}       Successfull          {Salary}")
                    S_No += 1
                except:
                    pass
    print(
        f"\n\n\t\t\t\t\t\t{colour.dark_gray}Press Enter for Main Menu...{colour.end}")
    msvcrt.getch()
    if (row[6] == "630021"):
        Team_Leader_flag = 0
        id = Team_Leader_GUI(row)
        return (id)
    else:
        Employee_flag = 0
        id = Employee_GUI(row)
        return (id)


def Profile(row):
    global Team_Leader_flag
    global Employee_flag
    while (True):
        if (row[6] == "630021"):
            Team_Leader_GUI(row)
        else:
            Employee_GUI(row)
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}PROFILE{colour.end}")
        print("\n")
        print(f"\t\t\t\t\t\t\t  Name : {row[2]}")
        print(f"\t\t\t\t\t\t\t  Employee ID : {row[0]}")
        print(f"\t\t\t\t\t\t\t  gender : {row[3]}")
        print(f"\t\t\t\t\t\t\t  Date of Birth : {row[4]}")
        print(f"\t\t\t\t\t\t\t  Email Address : {row[5]}")
        print("\n")
        print("\n\t\t\t\t\t\t\t\t1.Edit")
        print("\t\t\t\t\t\t\t\t2.Back")
        try:
            op = int(input("\n\t\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(1)  # 3
            continue
    match op:
        case 1:
            id = Edit_Profile(row)
            return (id)
        case 2:
            if (row[6] == "630021"):
                Team_Leader_flag = 0
                id = Team_Leader_GUI(row)
                return (id)
            else:
                Employee_flag = 0
                id = Employee_GUI(row)
                return (id)


def DOB_Modification(NewData):
    try:
        NewData_list = list(NewData)
        NewData_list.insert(0, "".join([NewData_list[0], NewData_list[1]]))
        del NewData_list[1]
        del NewData_list[1]
        NewData_list.insert(2, "".join([NewData_list[2], NewData_list[3]]))
        del NewData_list[3]
        del NewData_list[3]
        NewData_list.insert(4, "".join(
            [NewData_list[4], NewData_list[5], NewData_list[6], NewData_list[7]]))
        del NewData_list[5]
        del NewData_list[5]
        del NewData_list[5]
        del NewData_list[5]
    except:
        return ("0")
    if (NewData_list[2] == "01"):
        NewData_list.insert(2, "January")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "02"):
        NewData_list.insert(2, "February")
        if (int(NewData_list[0]) > 28):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "03"):
        NewData_list.insert(2, "March")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "04"):
        NewData_list.insert(2, "April")
        if (int(NewData_list[0]) > 30):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "05"):
        NewData_list.insert(2, "May")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "06"):
        NewData_list.insert(2, "June")
        if (int(NewData_list[0]) > 30):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "07"):
        NewData_list.insert(2, "July")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "08"):
        NewData_list.insert(2, "August")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "09"):
        NewData_list.insert(2, "September")
        if (int(NewData_list[0]) > 30):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "10"):
        NewData_list.insert(2, "October")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "11"):
        NewData_list.insert(2, "November")
        if (int(NewData_list[0]) > 30):
            return ("0")
        del NewData_list[3]
    elif (NewData_list[2] == "12"):
        NewData_list.insert(2, "December")
        if (int(NewData_list[0]) > 31):
            return ("0")
        del NewData_list[3]
    elif (int(NewData_list[2]) > 12):
        return ("0")
    elif ((int(NewData_list[4]) > 2025) or ((int(NewData_list[4]) < 1950))):
        return ("0")
    else:
        return ("0")

    NewData_list.insert(0, "".join(
        [NewData_list[0], NewData_list[1], NewData_list[2], NewData_list[3], NewData_list[4],]))
    NewData = NewData_list[0]
    return (NewData)


def File_Copy():
    global file
    file.close()
    os.remove('DataBase.csv')
    os.rename('modify.csv', 'DataBase.csv')
    print(
        f"\n\t\t\t\t\t\t\t  {colour.dark_gray}{colour.bold}Making Changes...{colour.end}")
    time.sleep(1)


def Edit_Profile(row):
    global Team_Leader_flag
    global Employee_flag
    while (True):
        file1 = open('DataBase.csv', "r")
        file2 = open('modify.csv', "w", newline="")
        DataBase = csv.reader(file1)
        copy = csv.writer(file2)
        Details = row
        if (row[6] == "630021"):
            Team_Leader_GUI(row)
        else:
            Employee_GUI(row)
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}EDIT PROFILE{colour.end}")
        print("\n")
        print(f"\t\t\t\t\t\t\t  1.Name : {row[2]}")
        print(f"\t\t\t\t\t\t\t  2.Employee ID : {row[0]}")
        print(f"\t\t\t\t\t\t\t  3.gender : {row[3]}")
        print(f"\t\t\t\t\t\t\t  4.Date of Birth : {row[4]}")
        print(f"\t\t\t\t\t\t\t  5.Email Address : {row[5]}")
        print(f"\t\t\t\t\t\t\t  6.For main menu")
        try:
            op = int(input("\n\t\t\t\t\t\t\t  While detail do you want to edit : "))
            if ((op > 6) or (op < 1)):
                raise Invalid_Choice
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            continue
        else:
            print("\n")
            match op:
                case 1:
                    NewData = input(f"\t\t\t\t\t\t\t  Enter new name : ")
                    for i in range(0, len(row)):
                        if (i == 2):
                            Details[2] = NewData
                    for row2 in DataBase:
                        if (row2[0] == row[0]):
                            copy.writerow(Details)
                        else:
                            copy.writerow(row2)
                    file1.close()
                    file2.close()
                    file.close()
                    File_Copy()
                    continue
                case 2:
                    print(
                        f"\t\t\t\t\t\t\t  {colour.orange}EMPLOYEE ID CANNOT BE CHANGED")
                    print(
                        f"\t\t\t\t\t\t\t  {colour.light_red}Press Enter to continue...{colour.end}")
                    msvcrt.getch()
                    continue
                case 3:
                    NewData = input(f"\t\t\t\t\t\t\t  Enter new data : ")
                    NewData = NewData.lower()
                    if ((NewData == "male") or (NewData == "female")):
                        pass
                    else:
                        print(
                            f"\n\t\t\t\t\t\t\t  {colour.orange}Gender can be either male or female")
                        print(
                            f"\t\t\t\t\t\t\t  {colour.light_red}Press Enter for \"TRY AGAIN\"...{colour.end}")
                        msvcrt.getch()
                        continue

                    for i in range(0, len(row)):
                        if (i == 2):
                            Details[3] = NewData
                    for row2 in DataBase:
                        if (row2[0] == row[0]):
                            copy.writerow(Details)
                        else:
                            copy.writerow(row2)
                    file1.close()
                    file2.close()
                    File_Copy()
                    continue
                case 4:
                    print(
                        f"\t\t\t\t\t\t\t  Enter new Date of Birth : {colour.dark_gray}dd-mm-yyyy{colour.end}")
                    position = Position(x=84, y=18)
                    position.show()
                    while (True):
                        NewData = input()
                        NewData = DOB_Modification(NewData)
                        if (NewData == "0"):
                            print(
                                f"\t\t\t\t\t\t\t  {colour.red}{colour.bold}Invalid Date of Birth{colour.end}")
                            time.sleep(1)  # 2
                            delete_last_line()
                            delete_last_line()
                            print(
                                f"\t\t\t\t\t\t\t  Enter new Date of Birth : {colour.dark_gray}dd-mm-yyyy{colour.end}")
                            position = Position(x=84, y=18)
                            position.show()
                            continue
                        break
                    for i in range(0, len(row)):
                        if (i == 2):
                            Details[4] = NewData
                    for row2 in DataBase:
                        if (row2[0] == row[0]):
                            copy.writerow(Details)
                        else:
                            copy.writerow(row2)
                    file1.close()
                    file2.close()
                    File_Copy()
                    continue
                case 5:
                    NewData = input(f"\t\t\t\t\t\t\t  Enter new Email id : ")
                    if ("@gmail.com" in NewData):
                        pass
                    else:
                        print(
                            f"\n\t\t\t\t\t\t\t  {colour.orange}Entered email id is \"NOT VALID\"")
                        print(
                            f"\t\t\t\t\t\t\t  {colour.light_red}Press Enter for \"TRY AGAIN\"...{colour.end}")
                        msvcrt.getch()
                        continue
                    for i in range(0, len(row)):
                        if (i == 2):
                            Details[5] = NewData
                    for row2 in DataBase:
                        if (row2[0] == row[0]):
                            copy.writerow(Details)
                        else:
                            copy.writerow(row2)
                    file1.close()
                    file2.close()
                    File_Copy()
                    continue
                case 6:
                    file1.close()
                    file2.close()
                    if (row[6] == "630021"):
                        Team_Leader_flag = 0
                        id = Team_Leader_GUI(row)
                        return (id)
                    else:
                        Employee_flag = 0
                        id = Employee_GUI(row)
                        return (id)


def Team_Members(row):
    global Team_Leader_flag, Team_Leader_GUI_flag
    global Employee_flag, Employee_GUI_flag
    if (row[6] == "630021"):
        Team_Leader_GUI(row)
    else:
        Employee_GUI(row)
    print(
        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}TEAM MEMBERS{colour.end}")
    print("\n")
    file = open('DataBase.csv', "r")
    DataBase = csv.reader(file)
    if (row[6] == "630021"):
        print(
            f"\t\t\t\t\t{colour.green}{colour.bold}Team Leader:{row[2]}\t\t\t\tProject:{row[7]}{colour.end}")
    else:
        for row2 in DataBase:
            if (row2[0] == row[6]):
                print(
                    f"\t\t\t\t\t{colour.green}{colour.bold}Team Leader:{row2[2]}\t\t\t\tProject:{row[7]}{colour.end}")
    print("\t\t\t\t\t__________________________________________________________________")
    print(
        f"\t\t\t\t\t      {colour.blue}{colour.bold}EMPLOYEE ID\t\t\t\t    NAME{colour.end}")
    print("\t\t\t\t\t__________________________________________________________________")
    file.seek(0)
    for row2 in DataBase:
        if (row[6] == "630021"):
            if (row2[6] == row[0]):
                print(f"\t\t\t\t\t        {row2[0]}\t\t\t\t\t {row2[2]}")
        else:
            if (row2[6] == row[6]):
                print(f"\t\t\t\t\t        {row2[0]}\t\t\t\t\t {row2[2]}")
    print("\n")
    print(
        f"\t\t\t\t\t{colour.dark_gray}{colour.bold}Press Enter for main Menu")
    msvcrt.getch()
    file.close()
    if (row[6] == "630021"):
        Team_Leader_flag = 0
        id = Team_Leader_GUI(row)
        return (id)
    else:
        Employee_flag = 0
        id = Employee_GUI(row)
        return (id)


def Announcements(row):
    global Team_Leader_GUI_flag, Team_Leader_flag, file
    global Employee_GUI_flag, Employee_flag
    if (row[6] == "630021"):
        Team_Leader_GUI_flag = 1
        Team_Leader_flag = 1
        Team_Leader_GUI(row)
    else:
        Employee_GUI_flag = 1
        Employee_flag = 1
        Employee_GUI(row)
    print(
        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ANNOUNCEMENTS{colour.end}")
    S_No = 1
    filex = open('Announcements.csv', "r")
    DataBase = csv.reader(filex)
    for row2 in DataBase:
        if (row2[0] == row[0]):
            ann = row2
    filex.close()
    print("\n")
    if (row[10] == "1"):
        try:
            print(
                f"\n\t\t{colour.light_green}{colour.bold}{S_No}.Date of Announcement : {ann[1]}")
            print(f"\t\t\t{ann[2]}")
        except:
            pass
        S_No += 1
        for i in range(0, len(ann), 2):
            if ((i == 0) or (i == 1) or (i == 2)):
                continue
            else:
                try:
                    print(
                        f"\t\t{colour.dark_gray}{S_No}.Date of Announcement : {ann[i-1]}")
                    print(f"\t\t\t{ann[i]}{colour.end}")
                    S_No += 1
                except:
                    pass
        file1 = open('DataBase.csv', "r")
        file2 = open('modify.csv', "w", newline="")
        DataBase2 = csv.reader(file1)
        copy = csv.writer(file2)
        data = row
        data[10] = "0"
        for row2 in DataBase2:
            if (row2[0] == row[0]):
                copy.writerow(data)
            else:
                copy.writerow(row2)
        file1.close()
        file2.close()
        file.close()
        os.remove('DataBase.csv')
        os.rename('modify.csv', 'DataBase.csv')
    else:
        for i in range(0, len(ann), 2):
            if (i == 0):
                continue
            else:
                try:
                    print(
                        f"\t\t{colour.dark_gray}{S_No}.Date of Announcement : {ann[i-1]}")
                    print(f"\t\t\t{ann[i]}{colour.end}")
                    S_No += 1
                except:
                    pass
    print(
        f"\n\n\t\t\t\t\t\t{colour.dark_gray}Press Enter for Main Menu...{colour.end}")
    msvcrt.getch()
    if (row[6] == "630021"):
        Team_Leader_flag = 0
        id = Team_Leader_GUI(row)
        return (id)
    else:
        Employee_flag = 0
        id = Employee_GUI(row)
        return (id)


def Work_Status(row):
    global Team_Leader_GUI_flag, Team_Leader_flag, file
    while (True):
        Team_Leader_GUI(row)
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}WORK STATUS{colour.end}")
        print(f"\n\t\t\t\t\t\tProject : {row[7]}")
        if (row[11] == "0"):
            print(
                f"\t\t\t\t\t\tWork Status : {colour.orange}In Progress{colour.end}")
        elif (row[11] == "1"):
            print(
                f"\t\t\t\t\t\tWork Status : {colour.green}Completed{colour.end}")
        elif (row[11] == "-1"):
            delete_last_line()
            print(
                f"\t\t\t\t\t\t\t     {colour.green}NEW  WORK  ASSIGNED\n{colour.end}")
            print(f"\t\t\t\t\t\t\tProject : {row[7]}")
            print("\n")
            print(
                f"\t\t\t\t\t\t{colour.dark_gray}Press enter to continue...{colour.end}")
            file1 = open('DataBase.csv', "r")
            file2 = open('modify.csv', "w", newline="")
            DataBase = csv.reader(file1)
            copy = csv.writer(file2)
            data = row
            data[11] = "0"
            for row1 in DataBase:
                if (row1[0] == row[0]):
                    copy.writerow(data)
                else:
                    copy.writerow(row1)
            file1.close()
            file2.close()
            file.close()
            os.remove('DataBase.csv')
            os.rename('modify.csv', 'DataBase.csv')
            msvcrt.getch()
            continue
        print("\n\t\t\t\t\t\t\t1.Update Work Status")
        print("\t\t\t\t\t\t\t2.Back")
        try:
            op = int(input("\n\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            continue
        match op:
            case 1:
                while (True):
                    Team_Leader_GUI(row)
                    print(
                        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}UPDATING WORK STATUS{colour.end}")
                    print(f"\n\t\t\t\t\t\t\tProject : {row[7]}")
                    print("\n\t\t\t\t\t\t\t1.In Progress")
                    print("\t\t\t\t\t\t\t2.Completed")
                    try:
                        op1 = int(input("\n\t\t\t\t\t\tEnter your choice : "))
                        if ((op1 > 2) or (op1 < 1)):
                            raise Invalid_Choice
                    except:
                        print(
                            f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
                        time.sleep(2)
                        continue
                    match op1:
                        case 1:
                            if (row[11] == "0"):
                                break
                            if (row[11] == "0"):
                                continue
                            elif (row[11] == "1"):
                                file1 = open('DataBase.csv', "r")
                                file2 = open('modify.csv', "w", newline="")
                                DataBase = csv.reader(file1)
                                copy = csv.writer(file2)
                                data = row
                                data[11] = "0"
                                for row1 in DataBase:
                                    if (row1[0] == row[0]):
                                        copy.writerow(data)
                                    else:
                                        copy.writerow(row1)
                                file1.close()
                                file2.close()
                                file.close()
                                os.remove('DataBase.csv')
                                os.rename('modify.csv', 'DataBase.csv')
                                break
                            continue
                        case 2:
                            if (row[11] == "1"):
                                break
                            if (row[11] == "1"):
                                continue
                            elif (row[11] == "0"):
                                file1 = open('DataBase.csv', "r")
                                file2 = open('modify.csv', "w", newline="")
                                DataBase = csv.reader(file1)
                                copy = csv.writer(file2)
                                data = row
                                data[11] = "1"
                                for row1 in DataBase:
                                    if (row1[0] == row[0]):
                                        copy.writerow(data)
                                    else:
                                        copy.writerow(row1)
                                file1.close()
                                file2.close()
                                file.close()
                                os.remove('DataBase.csv')
                                os.rename('modify.csv', 'DataBase.csv')
                                break
                            continue
                continue
            case 2:
                break
    Team_Leader_flag = 0
    id = Team_Leader_GUI(row)
    return (id)


def Add_Team_Leader(x):
    global Admin_flag
    while (True):
        Admin_GUI()
        if (x == 1):
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD TEAM LEADER{colour.end}")
        else:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD EMPLOYEE{colour.end}")
        print("\n")
        print("")
        if (x == 1):
            NewData = ["0", "0", "0", "0", "0",
                       "0", "630021", "0", "0", "0", "0", "-1"]
        else:
            NewData = ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
        print(f"\n\t\t\t\t\t\t\t\tNew Employee ID")
        print("\n\t\t\t\t\t\t\t\t1.Create an Id ")
        print("\t\t\t\t\t\t\t\t2.Create Random")
        print("\t\t\t\t\t\t\t\t3.Back")
        try:
            op = int(input("\n\t\t\t\t\t\t\t\tEnter Your Choice : "))
            if ((op > 3) or (op < 1)):
                raise Invalid_Choice
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            continue
        match op:
            case 1:
                Admin_GUI()
                if (x == 1):
                    print(
                        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD TEAM LEADER{colour.end}")
                else:
                    print(
                        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD EMPLOYEE{colour.end}")
                print("\n")
                print(
                    f"\t\t\t\t\t\t\tCreant a New Employee ID : {colour.dark_gray}00000{colour.end}")
                position = Position(x=83, y=7)
                position.show()
                NewData[0] = input()
                if (len(NewData[0]) != 5):
                    print(
                        f"\n\t\t\t\t\t\t\t  {colour.orange}ID should contain 5 digits")
                    print(
                        f"\n\t\t\t\t\t\t\t  {colour.light_red}Press Enter for Try Again...{colour.end}")
                    msvcrt.getch()
                    continue
                else:
                    pass
            case 2:
                while (True):
                    NewData[0] = random.randint(10000, 99999)
                    file = open('DataBase.csv', "r")
                    DataBase = csv.reader(file)
                    c = 0
                    if (True):
                        for row2 in DataBase:
                            if (row2[0] == NewData[0]):
                                c = 1
                        if (c == 1):
                            continue
                        else:
                            file.close()
                            break
                Admin_GUI()
                if (x == 1):
                    print(
                        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD TEAM LEADER{colour.end}")
                else:
                    print(
                        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD EMPLOYEE{colour.end}")
                print("\n")
                print(
                    f"\t\t\t\t\t\t\tNew Employee ID : {NewData[0]}")
            case 3:
                Admin_flag = 0
                id = Admin_GUI()
                return (id)
        while (True):
            print(
                f"\t\t\t\t\t\t\tAnual CTC of the employee : {colour.dark_gray}00 LPA{colour.end}")
            position = Position(x=84, y=8)
            position.show()
            NewData[8] = input()
            try:
                int(NewData[8])
                break
            except:
                print(f"\n\t\t\t\t\t\t\t{colour.red}Invalid CTC{colour.end}")
                time.sleep(2)
                delete_last_line()
                position = Position(x=56, y=8)
                position.show()
        break
    if (NewData[6] == "0"):
        NewData = Add_Employee(NewData)

    file = open('DataBase.csv', "a", newline="")
    Data = csv.writer(file)
    Data.writerow(NewData)
    file.close()
    print(f"\n\t\t\t\t\t\t\t{colour.light_green}Employee ID has created")
    print(
        f"\t\t\t\t\t\t\t{colour.red}Press Enter for main Menu...{colour.end}")
    file2 = open('Payments.csv', "a", newline="")
    Data = csv.writer(file2)
    Data.writerow([f"{NewData[0]}"])
    file2.close()
    file3 = open('Announcements.csv', "a", newline="")
    Data = csv.writer(file3)
    Data.writerow([f"{NewData[0]}"])
    file3.close()
    msvcrt.getch()
    Admin_flag = 0
    id = Admin_GUI()
    return (id)


def Add_Employee(NewData):
    global file
    while (True):
        a = 0
        if (a == 1):
            Admin_GUI()
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ADD TEAM LEADER{colour.end}")
            print("\n")
            print(
                f"\t\t\t\t\t\t\tNew Employee ID : {NewData[0]}")
            print(
                f"\t\t\t\t\t\t\tAnual CTC of the employee : {NewData[8]}")
        print(f"\t\t\t\t\t\t\tAdding to a Team")
        print("\t\t\t\t\t\t_____________________________________________________")
        print(
            f"\t\t\t\t\t\t{colour.blue}{colour.bold}  Choice    EMPLOYEE ID    PROJECT    TEAM MEMBERS{colour.end}")
        print("\t\t\t\t\t\t______________________________________________________")
        S_No = 1
        file1 = open('DataBase.csv', "r")
        DataBase1 = csv.reader(file1)
        file2 = open('copy.csv', "w", newline="")
        DataBase2 = csv.writer(file2)
        for row3 in DataBase1:
            DataBase2.writerow(row3)
        file2.close()
        file1.seek(0)
        for row in DataBase1:
            Team = 0
            if (row[6] == "630021"):
                E_id = row[0]
                project = row[7]
                file3 = open('copy.csv', "r")
                DataBase3 = csv.reader(file3)
                for row2 in DataBase3:
                    if (row2[6] == row[0]):
                        Team += 1
                file3.seek(0)
                print(
                    f"\t\t\t\t\t\t     {S_No}        {E_id}        {project}")
                position = Position(x=92, y=(13+(S_No-1)))
                position.show()
                print(Team)
                S_No += 1
        try:
            op = int(input("\n\t\t\t\t\t\t\tEnter your choice : "))
            if ((op > S_No) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(1)  # 3
            a = 1
            continue
    file1.seek(0)
    i = 1
    for row4 in DataBase1:
        if (row4[6] == "630021"):
            if (i == (op)):
                NewData[6] = row4[0]
                NewData[7] = row4[7]
            i += 1
    print(f"\n\t\t\t\t\t\t\tTeam Leader : {NewData[6]}")
    file1.close()
    file1 = open('DataBase.csv', "r")
    file2 = open('modify.csv', "w", newline="")
    DataBase2 = csv.reader(file1)
    copy = csv.writer(file2)
    for row in DataBase2:
        if (row[0] == NewData[6]):
            data = row
            data[10] = "1"
            copy.writerow(data)
        else:
            copy.writerow(row)
    file1.close()
    file2.close()
    os.remove('DataBase.csv')
    os.rename('modify.csv', 'DataBase.csv')
    file3 = open('Announcements.csv', "r")
    file4 = open('modify.csv', "w", newline="")
    DataBase3 = csv.reader(file3)
    copy = csv.writer(file4)
    for row2 in DataBase3:
        if (row2[0] == NewData[6]):
            data = row2
            data.insert(
                1, f"New Employee(ID : {NewData[0]}) added to your team")
            data.insert(1, "----------")
            copy.writerow(data)
        else:
            copy.writerow(row2)
    file3.close()
    file4.close()
    os.remove('Announcements.csv')
    os.rename('modify.csv', 'Announcements.csv')
    return (NewData)


def Employee_List():
    global Admin_flag, file
    Admin_GUI()
    print(
        f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}EMPLOYEE LIST{colour.end}")
    print("\n")
    print(f"\t\t\t\t\t\tTeam Leaders List")
    print("\t\t\t\t\t\t_______________________________________________________________________")
    print(
        f"\t\t\t\t\t\t{colour.blue}{colour.bold}  S.No.    EMPLOYEE ID    PROJECT    TEAM MEMBERS    PROJECT STATUS{colour.end}")
    print("\t\t\t\t\t\t________________________________________________________________________")
    S_No = 1
    file1 = open('DataBase.csv', "r")
    DataBase1 = csv.reader(file1)
    file2 = open('copy.csv', "w", newline="")
    DataBase2 = csv.writer(file2)
    for k in DataBase1:
        DataBase2.writerow(k)
    file2.close()
    file1.seek(0)
    for row in DataBase1:
        Team = 0
        if (row[6] == "630021"):
            E_id = row[0]
            project = row[7]
            file3 = open('copy.csv', "r")
            DataBase3 = csv.reader(file3)
            for row2 in DataBase3:
                if (row2[6] == row[0]):
                    Team += 1
            file3.seek(0)
            print(
                f"\t\t\t\t\t\t     {S_No}        {E_id}        {project}")
            position = Position(x=92, y=(11+(S_No-1)))
            position.show()
            print(Team)
            position = Position(x=104, y=(11+(S_No-1)))
            position.show()
            if (row[11] == "0"):
                print("In Progress")
            elif (row[11] == "1"):
                print("Completed")
            elif (row[11] == "-1"):
                print("Not Accepted")
            S_No += 1
    file1.seek(0)
    print(f"\n\n\t\t\t\t\t\tEmployee List")
    print("\t\t\t\t\t\t____________________________________________________")
    print(
        f"\t\t\t\t\t\t{colour.blue}{colour.bold}  S.No.    EMPLOYEE ID    TEAM LEADER    PROJECT{colour.end}")
    print("\t\t\t\t\t\t_____________________________________________________")
    S_No = 1
    for row3 in DataBase1:
        if (row3[6] != "630021"):
            print(
                f"\t\t\t\t\t\t   {S_No}         {row3[0]}          {row3[6]}         {row3[7]}")
            S_No += 1
    file1.close()
    file3.close()
    file.close()
    print(f"\n\t\t\t\t\t\t{colour.dark_gray}Press Enter for Main Menu...")
    msvcrt.getch()
    Admin_flag = 0
    id = Admin_GUI()
    return (id)


def Announce():
    global Admin_flag, file
    while (True):
        Admin_GUI()
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ANNOUNCE{colour.end}")
        print("\n")
        announcement = input("\tText for Announcement : ")
        print(
            f"\n\t\t\t\t\t\tDate of Payment : {colour.dark_gray}dd-mm-yyyy{colour.end}")
        position = Position(x=66, y=9)
        position.show()
        doa = input()
        print("\n")
        print("\t\t\t\t\t\t\t1.Announce")
        print("\t\t\t\t\t\t\t2.Back")
        try:
            op = int(input("\n\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(2)
            continue
    match op:
        case 1:
            file1 = open('DataBase.csv', "r")
            file2 = open('modify.csv', "w", newline="")
            DataBase2 = csv.reader(file1)
            copy = csv.writer(file2)
            for row in DataBase2:
                data = row
                data[10] = "1"
                copy.writerow(data)
            file1.close()
            file2.close()
            file.close()
            os.remove('DataBase.csv')
            os.rename('modify.csv', 'DataBase.csv')
            file3 = open('Announcements.csv', "r")
            file4 = open('modify.csv', "w", newline="")
            DataBase3 = csv.reader(file3)
            copy = csv.writer(file4)
            for row2 in DataBase3:
                data = row2
                data.insert(1, announcement)
                data.insert(1, doa)
                copy.writerow(data)
            file3.close()
            file4.close()
            os.remove('Announcements.csv')
            os.rename('modify.csv', 'Announcements.csv')
            print(f"\n\t\t\t\t\t\t{colour.light_green}Sending Announcement...")
            time.sleep(2)
            delete_last_line()
            print(f"\t\t\t\t\t\tSended Successfull.{colour.end}")
            print(
                f"\t\t\t\t\t\t{colour.dark_gray}Press Enter for Main Memu...")
            msvcrt.getch()
            Admin_flag = 0
            id = Admin_GUI()
            return (id)
        case 2:
            Admin_flag = 0
            id = Admin_GUI()
            return (id)


def Assign_Work():
    global Admin_flag
    while (True):
        Admin_GUI()
        print(
            f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ASSIGN WORK{colour.end}")
        print("\n")
        S_No = 1
        employee = []
        file1 = open('DataBase.csv', "r")
        DataBase = csv.reader(file1)
        for row2 in DataBase:
            if (row2[1] == "0"):
                print(f"\t\t{S_No} Employee ID : {row2[0]}")
                print(f"\t\t\tStatus : New Join")
                if (row2[6] == "630021"):
                    print("\t\t\tDesignation : Team Leader")
                else:
                    print("\t\t\tWork Status : Employee(Team member)")
                    print(f"\t\t\tTeam Leader : {row2[6]}")
                print(f"\t\t\tSign up : Not Signed up")
                print(f"\t\t\twork : To be assigned after Sign up")
                S_No += 1
            elif (row2[7] == "0"):
                print(f"\t\t{S_No} Employee ID : {row2[0]}")
                print(f"\t\t\tStatus : Current Employee")
                print("\t\t\tDesignation : Team Leader")
                print(f"\t\t\tProject : ----")
                S_No += 1
                employee.append(row2[0])
            elif (row2[6] == "630021"):
                if (row2[11] == "1"):
                    print(f"\t\t{S_No} Employee ID : {row2[0]}")
                    print(f"\t\t\tStatus : Current Employee")
                    print("\t\t\tDesignation : Team Leader")
                    print(f"\t\t\tProject : {row2[7]}")
                    print(
                        f"\t\t\tProject Status : {colour.green}Completed{colour.end}")
                    S_No += 1
                    employee.append(row2[0])
                elif (row2[11] == "-1"):
                    print(f"\t\t{S_No} Employee ID : {row2[0]}")
                    print(f"\t\t\tStatus : Current Employee")
                    print("\t\t\tDesignation : Team Leader")
                    print(f"\t\t\tProject : {row2[7]}")
                    print(
                        f"\t\t\tProject Status : {colour.red}Not Accepted{colour.end}")
                    S_No += 1
        file1.close()
        print("\n")
        print("\t\t\t\t\t\t\t1.Assign Work")
        print("\t\t\t\t\t\t\t2.Back")
        try:
            op = int(input("\n\t\t\t\t\t\tEnter your choice : "))
            if ((op > 2) or (op < 1)):
                raise Invalid_Choice
            break
        except:
            print(
                f"\n\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
            time.sleep(1)  # 3
            continue
    match op:
        case 1:
            while (True):
                Admin_GUI()
                print(
                    f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ASSIGN WORK{colour.end}")
                print("\n")
                file_2 = open('Work.csv', "r")
                work_ = csv.reader(file_2)
                for row_w in work_:
                    work = row_w
                file_2.close()
                S_No_w = 1
                for w in work:
                    print(f"\t\t\t\t\t\t\t{S_No_w}.{w}")
                    S_No_w += 1
                try:
                    op_w = int(input("\n\t\t\t\t\t\tChoose Work : "))
                    if ((op_w > S_No_w-1) or (op_w < 1)):
                        raise Invalid_Choice
                    break
                except:
                    print(
                        f"\n\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
                    time.sleep(2)
                    continue
            while (True):
                Admin_GUI()
                print(
                    f"\n\t\t\t\t\t\t\t\t{colour.yellow}{colour.bold}ASSIGN WORK{colour.end}")
                print("\n")
                print("\n\t\t\t\t\t\tChoose Team Leader for Work : ")
                if (len(employee) == 0):
                    print(
                        f"\n\t\t\t\t\t\t{colour.orange}Employees are on work")
                    print(
                        f"\t\t\t\t\t\t{colour.dark_gray}Preaa Enter for Main Menu...{colour.end}")
                    msvcrt.getch()
                    Admin_flag = 0
                    id = Admin_GUI()
                    return (id)
                else:
                    S_No_e = 1
                    for e in employee:
                        print(f"\t\t\t\t\t\t\t{S_No_e}.{e}")
                        S_No_e += 1
                    try:
                        op_e = int(
                            input("\n\t\t\t\t\t\tChoose Team Leader : "))
                        if ((op_e > S_No_e-1) or (op_e < 1)):
                            raise Invalid_Choice
                        break
                    except:
                        print(
                            f"\n\t\t\t\t\t\t{colour.red}{colour.bold}Invalid Choice{colour.end}")
                        time.sleep(2)
                        continue
            file1 = open('DataBase.csv', "r")
            file2 = open('modify.csv', "w", newline="")
            DataBase2 = csv.reader(file1)
            copy = csv.writer(file2)
            for row3 in DataBase2:
                if (row3[0] == employee[op_e-1]):
                    row3[7] = work[op_w-1]
                    row3[11] = "-1"
                    copy.writerow(row3)
                else:
                    copy.writerow(row3)
            file1.close()
            file2.close()
            file.close()
            os.remove('DataBase.csv')
            os.rename('modify.csv', 'DataBase.csv')
            file1 = open('DataBase.csv', "r")
            file2 = open('modify.csv', "w", newline="")
            DataBase3 = csv.reader(file1)
            copy = csv.writer(file2)
            for row3 in DataBase3:
                if (row3[6] == employee[op_e-1]):
                    row3[7] = work[op_w-1]
                    copy.writerow(row3)
                else:
                    copy.writerow(row3)
            file1.close()
            file2.close()
            os.remove('DataBase.csv')
            os.rename('modify.csv', 'DataBase.csv')
            work.pop(op_w-1)
            file3 = open('modify.csv', "w", newline="")
            copy_work = csv.writer(file3)
            copy_work.writerow(work)
            file3.close()
            os.remove('Work.csv')
            os.rename('modify.csv', 'Work.csv')
            print(f"\n\t\t\t\t\t\t{colour.orange}Work Assigned.")
            print(
                f"\t\t\t\t\t\t{colour.dark_gray}Preaa Enter to Continue...{colour.end}")
            msvcrt.getch()
            id = Assign_Work()
            return (id)
        case 2:
            Admin_flag = 0
            id = Admin_GUI()
            return (id)


flag = 0
Admin_flag = 0
Admin_GUI_flag = 0
Team_Leader_flag = 0
Team_Leader_GUI_flag = 0
Employee_GUI_flag = 0
Employee_flag = 0
Admin = "Sandeep"
file = open('DataBase.csv', "r")
DataBase = csv.reader(file)
id = GUI()
while (True):
    file = open('DataBase.csv', "r")
    DataBase = csv.reader(file)
    for row in DataBase:
        if (row[0] == id):
            if (row[6] == "630021"):
                id = Team_Leader_GUI(row)
                break
            else:
                id = Employee_GUI(row)
                break
