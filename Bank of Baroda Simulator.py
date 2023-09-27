from datetime import date

name = "Shivam"
global Full_name
global age
global mobile_number
global a_number
global check_MPINs
check_MPINs = 0000


def usernamefun():
    while True:
        username = str(input(
            "\n\t\t\t\t Enter your Username Should Be 8 character : "))  # taking input as the User name of 8 characters
        name = len(username)
        if name < 8:
            print("\n\t\t\t\t\t Enter The 8 Characters Only Try again !")
        elif len(username) > 8:
            print("\n\t\t\t\t Enter The 8 Characters Only Try again !")
        else:

            bob.append(username)
            print(" Username Added Successfully ")
            break


def addharfun():
    while True:
        addhaar = input("\n\t\t\t\t Enter your 12- Digit Addhar Number ")
        check = str(addhaar)
        if len(check) < 12:
            print("\n\t\t\t\t invalid try to change in settings : ")
        elif len(check) > 12:
            print("\n\t\t\t\t invalid try to change in settings : ")

        else:

            bob.append(addhaar)  # add to list
            print("\n\t\t\t Addhar Card Added Successfully \n\n")
            print
            break


def account_statement():
    global Full_name
    global age
    global mobile_number
    print("\n\t\t ********************* Account Holder Details **************  \n\n")
    print(
        "\n\t Branch Address : Ground Floor Laxmi Plaza , Juchandra Naigaon Station Road ,\n\t\t\t  Naigaon East , Thane Maharashtra - 401208\n")
    print("\n\t Account Number : ", a_number, "\t\t\t\t IFSC CODE :  BARBONAITH")
    print("\n\t Branch :  NAIGAON ( East )")
    if atype == "1":
        print("\n\t Account Type : Saving Account ")
    elif atype == "2":
        print("\n\t Account Type : Current Account  ")
        print("\n\t ")
    print("\n\t Account Holder : ", Full_name)
    print("\n\t Balance : ", balance)
    print("\n\t Age : ", age)
    print("\n\t Mobile Number : ", mobile_number)
    if N_op == 1:
        print("\n\t Nominee Added : Yes")
        print("\n\t Nominee Name : " + nominee_name)
    elif N_op == 2:
        print("\n\t Nominee Added : No ")
        print("\n\t Nominee Name : -     \t\t ..... ( Add Details In Setting Option )")
    print("\n\n\n\n\n\t\t\t\t     Shivam dubey ")
    print("\t\t\t\t\t शाखा प्रबंधक / Branch Manager")
    print("\n\n\n\t\t ********************* Account Holder Details **************  \n\n")
    print("\n\n\n ")


# CREATING A FUNCTION FOR faQS
def faqs():
    print("\n\t\t 1. What is the Process to Sign up /create Account in BOB ")
    print("\n\t\t Answers: The Bank of Baroda is Simple interface for A ccustomer who is lookinng to Create or signup")
    print(
        "\t\t          for new Aaccount frist Start The BOB Applicattion and Follow the Mentioned Steps Carefully :\n")
    print("\n\t\t               Step 1: Open The BOB Application -> Wait for laoding The Selection Menu ")
    print("\n\t\t               Step 2: After Opening and loading -> Enter the 1. to Create A Accounnt or signup ")
    print("\n\t\t               Step 3: After that Select The Type OF  acccount You want e.g. Saving  ")
    print(
        "\n\t\t               Step 4: Then next Bank Will provide You A 10-digit Account Nummber By Default on Screen ")
    print("\n\t\t               Step 5: Then Enter Your Full name and Usename as A Personal details ")
    print("\n\t\t               Step 6: After Filling the Personal Details -> Enter Addhar Number Correctlly ")
    print("\n\t\t               Step 7: As a last Step Create A 4-digit MPIN to Secure Your Account From Frauders ")
    print("\n\n\t\t  2. How to Deposite Money ")
    print("\n\t\t  Answers : To Deposite the Money In your Account IS Very Easy Just Enter The Amount and The MPIN")
    print("\n\t\t            Wich You Had Created  Then You Can Sucessfuly Deposite  ")
    print("\n\n\t\t  3. How I can Login IN BOB ")
    print(
        "\n\t\t  Answers : Once You Created Account Then You Can Loing Successfully By Enter the account number and MPIN ")
    print("\n\t\t            Then You Can Withdrawal and DEposite and Check Balance Sucessfully")
    print("\n\n\t\t  4. What Option are There On Main Page")
    print("\n\t\t  Answer : On The Main Window There is only 3 Options i.e ")
    print("\n\t\t               1. Create Account")
    print("\n\t\t               2. Login Account")
    print("\n\t\t               3. Quit")
    print("\n\n\t\t  5. What is The Latest Version Of BOB ?  ")
    print("\n\t\t  Answer : As of the Latest Version is 4.041 ..........")


# creating Function for Settings
def setting_tabss():
    global pin
    print("\n\n\t\t\t\t\t------------- Setting ------------ ")
    print("\n\t\t\t\t\t 1. Change ADDHAR Card number ")
    print("\n\t\t\t\t\t 2. FAQ'S")
    print("\n\t\t\t\t\t 3. HELP ")
    print("\n\t\t\t\t\t 4. CHANGE MPIN ")
    print("\n\t\t\t\t\t 5. View PASSBOOK ")
    print("\n\t\t\t\t\t 6. Exit ")

    choice5 = int(input("\n\t\t\t\t Enter Your Choice : "))
    if choice5 == 1:
        checkpin = int(input("\n\t\t\t\t Enter MPPIN : "))
        if checkpin == pin:
            addharfun()
        else:
            print("\n\t\t\t\tInavlid Input Try Again ")

    elif choice5 == 2:
        print("\n\n")
        faqs()
        print("\n\n")


    elif choice5 == 3:

        print("\n\t\t\t Contact Us at  ")
        print("\n\t\t\t info.bob@gmail.com")
        print("\n\t\t\t help.bob@gmail.com")
        print("\n\n\t\tToll free Number ")
        print("\n\t\t\t\t 8888-1774-1779")

    elif choice5 == 4:
        while True:
            time.sleep(1.1)
            MPIN = int(input("\n\t\t\t\t>>>> Enter a Four Digit MPIN "))
            pin = MPIN
            bob.append(pin)
            sub = str(MPIN)
            if len(sub) > 4 or len(sub) < 3:
                time.sleep(1.1)
                print("\n\n\t\t\t\t ERROR : Enter only Four digit MPIN")
            else:
                time.sleep(1.1)
                print("\n\n\t\t\t\t Your Four digit MPIN is created Sucessfully")
                break
    elif choice5 == 5:

        account_statement()

    elif choice5 == 6:
        print("\n\t\t\t\twait exiting ")


def times():
    today = date.today()
    global timenow
    timenow = "wait ..."
    # Month abbreviation, day and year
    timenow = today.strftime("%b-%d-%Y")
    print(timenow)


import random

global bob
global MPIN
MPIN = 4040
import time

random_number = random.randint(1000000000, 9999999999)
acc_random = random_number
username = "Guest-01"
countend = "Start"
time.sleep(1.1)
print("\n\n\n")
print("\t\t\t\t\t\t Welcome to ")
time.sleep(1.1)
print("\t\t\t\t\t India's International Bank    ")
time.sleep(1.1)
print("\n\t\t\t\t\t\tBank of Baroda ")
time.sleep(1.1)
print("\t\t\t\t\t\t बैंक ऑफ बड़ौदा \t\t\t\t\t")
time.sleep(1.1)
print("\n\t\t\t\t\t\t Version 4.041")
time.sleep(1.1)
print("\n\t\t\t\t\t\t wait .......")
time.sleep(1.1)
print("\n\t\t\t\t\t We are Processing ......")
time.sleep(1.1)
print("\n\t\t\t\t\t do not press any button ........")
time.sleep(1.1)
time.sleep(1.1)
print("\n\n\n")
while True:

    today = date.today()
    timenow = "wait ..."
    # Month abbreviation, day and year
    timenow = today.strftime("%b-%d-%Y")
    time.sleep(1.1)
    print("\t\t\t\t\t   बैंक ऑफ बड़ौदा \t\t\t\t\t")
    print(
        "Last Updated 02-09-2023\t\t---------------- BANK OF BARODA ----------------\t  Username \t  Date \t\t  Version")
    print(
        "  You are updated\t \t ------------ India's International Bank ---------\t  " + username + " \t{}\t   4.041".format(
            timenow))
    print("\n\t\t\t\t---------------- Welcome Back ----------------  ")
    print("\n\t\t\t\t\tBanking System Menu:")
    print("\n\t\t\t\t1. Create Account")
    print("\n\t\t\t\t2. Login  ")
    print("\n\t\t\t\t3. Exit")
    time.sleep(1)
    choice1 = input("\n\t\t\t\tEnter your choice: ")
    print("\n\n")

    if choice1 == "1":
        bob = []  # blank lis
        atype = input(
            "\n\t\t\t\t which type of account do you want to create :\n\n\n\t\t\t\t  1. Saving Account \t\t2. Current Account \n\n\t\t\t\t>>>")
        # taking the account type as input if it is then 1.saving  2.current
        bob.append(atype)

        Full_name = str(input("\n\t\t\t Enter Your Full Name : "))
        bob.append(Full_name)
        age = int(input("\n\t\t\t Enter Your Age "))
        bob.append(age)
        while True:
            mobile_number = int(input("\n\t\t\t Enter Your 10 digit Mobile Number  "))
            chck = str(mobile_number)
            if len(chck) < 10:
                print("\n\t\t\t Enter The 10 Digit Mobile Number Only ")
            elif len(chck) > 10:
                print("\n\t\t\t Enter The 10 Digit Mobile Number Only ")
            else:
                bob.append(mobile_number)
                print("\n\t\t\t mobile number Added Sucessfully ")
                break

        while True:
            username = str(input(
                "\n\t\t\t\t Enter your Username Should Be 8 character : "))  # taking input as the User name of 8 characters
            name = len(username)
            if name < 8:
                print("\n\t\t\t\t\t Enter The 8 Characters Only Try again !")
            elif len(username) > 8:
                print("\n\t\t\t\t Enter The 8 Characters Only Try again !")
            else:

                bob.append(username)
                print("\n\t\t\t\t  Username Added Successfully ")
                break

        print("\n\t\t\t Do You Want to Add Nominee Details Now \n\t\t\t 1. Yes \n\t\t\t 2. No ")
        N_op = int(input("\n\t\t\t Enter Your Choice "))
        if N_op == 1:
            nominee_name = input("\n\t\t\t Enter the Nominee Name : ")
            bob.append(nominee_name)
            print("\n\t\t\t Nominee Added Sucessfully")
        elif N_op == 2:
            print(" You Can Change The Nominee Details in Settings ")

        acc_type = atype  # taking the account type as input if it is then 1.saving  2.current
        time.sleep(1.1)
        balance = float(input("\n\t\t\t\t Enter initial balance : ₹"))
        bob.append(balance)
        time.sleep(1.1)
        # function to add addhar card
        addharfun()

        print("\n\n\t\t\t\t for Your Account Security ")
        print("\n\t\t\t\t Create a Four digit MPIN ")
        while True:
            time.sleep(1.1)
            MPIN = int(input("\n\t\t\t\t>>>> Enter a Four Digit MPIN "))
            pin = MPIN
            bob.append(pin)
            sub = str(MPIN)
            if len(sub) > 4 or len(sub) < 3:
                time.sleep(1.1)
                print("\n\n\t\t\t\t ERROR : Enter only Four digit MPIN")
            else:
                time.sleep(1.1)
                print("\n\n\t\t\t\t Your Four digit MPIN is created Sucessfully")
                break
                countend = 'created'
        time.sleep(1.5)
        print("\n\n\t\t\t\t\t             Wait .....")
        time.sleep(1.5)
        print("\n\n\t\t\t\t\t WAIT WE ARE GATHERING INFORMATION ..")
        time.sleep(1.5)
        print("\n\n\t\t\t\t  While We ar Processing Do Not Press any Key ..")
        time.sleep(1.6)
        print("\n\n\t\t\t\t\t We Are Selecting The Best Account Number For You ...")
        time.sleep(1.4)
        print("\n\n\t\t\t\t\t           All is set ........")
        time.sleep(1.4)
        a_number = acc_random
        bob.append(a_number)  # add to list
        print("\n")
        print("\n\n\t\t\t\t Your Account Number is : ", a_number)
        account_statement()
        print("\n\n\t\t\t\t Your Account Is Created Sucessfully ")
        while True:
            time.sleep(1.1)
            print("\n\n\t\t\t\t\t-------------- Welcome " + username + "---------------\t\t{} ".format(timenow))
            print("\n\n")
            print("\t\t\t\t\t\t\t   बैंक ऑफ बड़ौदा \t\t\t\t\t")
            print(
                "Your Account Number \t\t\t---------------- BANK OF BARODA ----------------\tUsername\t Date \t     Version")
            print("  ", a_number,
                  "\t\t\t\t------------- INDIA'S NO 1 BANK ---------------\t\t" + username + " \t{}    4.041".format(
                      timenow))
            print("\n\t\t\t\t\tBanking System Menu:")
            print("\n\t\t\t\t1. Deposit")
            print("\n\t\t\t\t2. Withdraw")
            print("\n\t\t\t\t3. Check Balance")
            print("\n\t\t\t\t4. Setting")
            print("\n\t\t\t\t5. Exit")
            choice2 = input("\n\t\t\t\tEnter your choice: ")
            if choice2 == "1":
                time.sleep(1.1)
                addbalance = input("\n\t\t\t\t Enter a Amount To Deposite : ₹")
                time.sleep(1.1)
                temppin = int(input("\n\t\t\t\t Enter A MPIN "))
                if temppin == pin:
                    balance = balance + float(addbalance)
                    bob.append(balance)
                    time.sleep(1.1)
                    print("\n\t\t\t\t Deposited amount ₹", addbalance)
                    print("\n\t\t\t\t current balance : ₹", balance)
                else:
                    time.sleep(1.1)
                    print("\n\t\t\t\t Invalid pin ")
            elif choice2 == "2":
                amountw = int(input("\n\t\t\t\t Enter the Amount to Withdrawal "))
                check_MPINs = int(input(" Enter The MPIN"))

                if amountw < balance and check_MPINs == pin:
                    balance = balance - amountw
                    bob.append(balance)
                    time.sleep(1.1)
                    print("\n\n \n\t\t\t\t withdrawal is Succesfull ")
                    time.sleep(1.1)
                    print("\n\t\t\t\t withdrawal Amount : ₹", amountw)
                    time.sleep(1.1)
                    print("\n\t\t\t\t current balance : ₹", balance)

                elif amountw > balance:
                    time.sleep(1.1)
                    print("\n\t\t\t\t You Account Balance is insufficient ")
                    time.sleep(1.1)
                    print("\n\t\t\t\t cannot withdrawal !! ")
                elif amountw < 0:
                    print(" \n\t\t\t\t You Account Balance is insufficient ")
                    time.sleep(1.1)
                    print("\n\t\t\t\t cannot withdrawal !! ")
                else:
                    print("\n\t\t\t\t  Invalid !! ")
            elif choice2 == "3":
                print("\n\t\t\t\t  Do You want to check Account Balance ")
                temppin = int(input(" Enter A MPIN "))
                if temppin == pin:
                    print("\n\t\t\t\t wait .......")
                    time.sleep(1.1)
                    print("\n\t\t\t\t We are Processing ......")
                    time.sleep(1.1)
                    print(" \n\t\t\t\t do not press any button ........")

                    time.sleep(1.1)
                    print("\n\t\t\t\t Your Available balance : ", balance)
                    print("\n")
                    account_statement()
                else:
                    time.sleep(1.1)
                    print("\n\t\t\t\t  Invalid MPIN .....")
            elif choice2 == "4":
                setting_tabss()





            elif choice2 == "5":
                time.sleep(1.1)
                print("\n\n\t\t\t You had Logged out  Successfully....")
                break
    elif choice1 == "2":

        time.sleep(1.1)
        account_number2 = input("\n\t\t\t\tEnter account number: ")
        time.sleep(1.1)
        check_MPIN = int(input("\n\t\t\t\t Enter your Four MPIN"))
        if check_MPIN != MPIN:
            print("\n\t\t\t\t  Frist Create Account and Then Login \n\n\n")
        elif check_MPIN == MPIN:
            time.sleep(1.1)
            print("\n\t\t\t\t You Logged in Sucessfully ")
            while True:
                time.sleep(1.1)
                print("\n\n\t\t\t\t\t-------------- Welcome " + username + "---------------\t\t{} ".format(timenow))
                print("\n\n")
                print("\t\t\t\t\t\t\t\t  बैंक ऑफ बड़ौदा \t\t\t\t\t")
                print(
                    "Your Account Number \t\t\t---------------- BANK OF BARODA ----------------\tUsername\t Date \t     Version")
                print("  ", a_number,
                      "\t\t\t\t------------- INDIA'S NO 1 BANK ---------------\t\t" + username + " \t{}    4.041".format(
                          timenow))
                print("\n\t\t\t\t\tBanking System Menu:")
                print("\n\t\t\t\t1. Deposit")
                print("\n\t\t\t\t2. Withdraw")
                print("\n\t\t\t\t3. Check Balance")
                print("\n\t\t\t\t4. Setting")
                print("\n\t\t\t\t5. Exit")
                choice2 = input("\n\t\t\t\tEnter your choice: ")
                if choice2 == "1":
                    time.sleep(1.1)
                    addbalance = input("\n\t\t\t\t Enter a Amount To Deposite : ₹")
                    time.sleep(1.1)
                    temppin = int(input("\n\t\t\t\t Enter A MPIN "))
                    if temppin == pin:
                        balance = balance + float(addbalance)
                        bob.append(balance)
                        time.sleep(1.1)
                        print("\n\t\t\t\t Deposited amount ₹", addbalance)
                        print("\n\t\t\t\t current balance : ₹", balance)
                    else:
                        time.sleep(1.1)
                        print("\n\t\t\t\t Invalid pin ")
                elif choice2 == "2":
                    amountw = int(input("\n\t\t\t\t Enter the Amount to Withdrawal "))
                    check_MPINs = int(input(" Enter The MPIN"))

                    if amountw < balance and check_MPINs == pin:
                        balance = balance - amountw
                        bob.append(balance)
                        time.sleep(1.1)
                        print("\n\n \n\t\t\t\t withdrawal is Succesfull ")
                        time.sleep(1.1)
                        print("\n\t\t\t\t withdrawal Amount : ₹", amountw)
                        time.sleep(1.1)
                        print("\n\t\t\t\t current balance : ₹", balance)

                    elif amountw > balance:
                        time.sleep(1.1)
                        print("\n\t\t\t\t You Account Balance is insufficient ")
                        time.sleep(1.1)
                        print("\n\t\t\t\t cannot withdrawal !! ")
                    elif amountw < 0:
                        print(" \n\t\t\t\t You Account Balance is insufficient ")
                        time.sleep(1.1)
                        print("\n\t\t\t\t cannot withdrawal !! ")
                    else:
                        print("\n\t\t\t\t  Invalid !! ")
                elif choice2 == "3":
                    print("\n\t\t\t\t  Do You want to check Account Balance ")
                    temppin = int(input(" Enter A MPIN "))
                    if temppin == pin:
                        print("\n\t\t\t\t wait .......")
                        time.sleep(1.1)
                        print("\n\t\t\t\t We are Processing ......")
                        time.sleep(1.1)
                        print(" \n\t\t\t\t do not press any button ........")

                        time.sleep(1.1)
                        print("\n\t\t\t\t Your Available balance : ", balance)
                        print("\n")
                        account_statement()
                    else:
                        time.sleep(1.1)
                        print("\n\t\t\t\t  Invalid MPIN .....")
                elif choice2 == "4":
                    setting_tabss()





                elif choice2 == "5":
                    time.sleep(1.1)
                    print("\n\n\t\t\t You had Logged out  Successfully....")
                    break
            else:
                print("\n\t\t\t\t No Account Exits First Create Account  ")

    elif choice1 == "3":
        print("\n\t\t\t\t  Login out ")
        break
    else:
        print("\n\t\t\t\t  Invaild input ")