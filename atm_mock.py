import random
import os
import database
import validation
from getpass import getpass

    
def init():

    print("WELCOME")
    home_page = int(input("Do you have an account with us?\n1. Register\t2. Login\n"))
    if home_page == 1:
        register()
    elif home_page == 2:
        login()
    else:
        print("Invalid entry")
        init()

def register():
    print("****REGISTER HERE****")
    first_name = input("enter your first name\n")
    last_name = input("enter last name\n")
    email = input("enter e-mail\n")
    password = input("enter password\n")
    account_number = random.randrange(1111111111, 9999999999)

    is_acc_created = database.create(account_number, first_name, last_name, email, password)

    if is_acc_created:
        print("Account Registration Successful")
        print("Account name: %s %s\nAccount number: %d" %(first_name, last_name, account_number))
        login()
    else:
        print("Oops, sorry something went wrong")
        register()

def login():
    print("********* Login ***********")

    account_number_from_user = input("What is your account number? \n")

    is_valid_account_number = validation.account_validation(account_number_from_user)

    if is_valid_account_number:

        password = getpass("What is your password \n")

        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bankOperations(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid")
        init()
        
def bankOperations(user):
    print("Hello %s %s" %(user[0], user[1]))
    selectOption = int(input("What do you want to do?\n(1) deposit (2) withdrawal (3) Transfer (4)Check Balance\n(5) Complaint (6) Logout (7) Exit \n"))
    if selectOption == 1:
        print(deposit(user))
        bankOperations(user)
    elif selectOption == 2:
        print(withdrawal(user))
        bankOperations(user)
    elif selectOption == 3:
        print(transfer(user))
        bankOperations(user)
    elif selectOption == 4:
        print(check_balance(user))
        bankOperations(user)
    elif selectOption == 5:
        print(complaints(user))
        bankOperations(user)
    elif selectOption == 6:
        logout()
    elif selectOption == 7:
        exit()
    else:
        print("Invalid entry")
        bankOperations(user)


def deposit(user):
    amount = int(input("enter amount:\n"))
    balance = int(user[4])
    balance +=amount
    print("Deposit Successful")

    #updated = database.update(user)

    return balance

def withdrawal(user):
    amount = int(input("enter amount:\n"))
    balance = int(user[4])
    if balance > amount:  
        balance -= amount
        print("Transaction Succesful")
    else:
        print("Insufficient fund")
    return balance

def transfer(user):
    amount = int(input("enter amount:\n"))
    receiver = int(input("enter recipient account:\n"))
    balance = int(user[4])
    if balance > amount:
        balance -= amount
        print("%d transfered to %s" %(amount, receiver))
    else:
        print("Insufficient fund")
    return balance

def check_balance(user):
    balance = int(user[4])
    return balance

def complaints(user):
    complaint = input("What do you want to complain about?")
    print(complaint)

def logout():
    login


init()
