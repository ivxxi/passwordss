#!/usr/bin/env python3.6

import random
from user import User
from credentials import Credentials

# Functions to add credentials


def create_new_credential(account_name, account_password):
    """Function to create a new account and its credentials"""
    new_credential = Credentials(account_name, account_password)
    return new_credential


def save_new_credential(credentials):
    """Function to save the newly created account and password"""
    credentials.save_credentials()


def find_credential(account_name):
    """Function that finds credentials based on account_name given"""
    return Credentials.find_by_name(account_name)


def check_existing_credentials(name):
    """Method that checks whether a particular account and its credentials exist based on searched account_name"""
    return Credentials.find_by_name(name)


def display_credentials():
    """Function which displays all saved credentials"""
    return Credentials.display_credentials()


def delete_credential(credentials):
    """
    Method that deletes credentials
    """
    return Credentials.delete_credential(credentials)


def main():

    while True:
        print("WELCOME")
        print('\n')
        print("SELECT AN OPTION:\n Enter the following: \n 'create' to create a new user account\n 'login' to login to an existing account\n 'exit' to exit\n")
        short_code = input().lower()
        print('\n')

        if short_code == 'create':
            print("enter new user account name")
            created_user_name = input()

            print("Enter a password")
            created_user_password = input()

            print("Confirm password")
            confirm_password = input()

            while confirm_password != created_user_password:
                print("Passwords do not match!")
                print("Enter a password")
                created_user_password = input()
                print("Confirm password")
                confirm_password = input()
            else:
                print(f"Account created for {created_user_name}")
                print('\n')
                print("Log in to account")
                print("Enter username")
                entered_userName = input()
                print("Enter password")
                entered_password = input()

                while entered_userName != created_user_name or entered_password != created_user_password:
                    print("invalid")
                    print("Enter username")
                    entered_userName = input()
                    print("Enter password")
                    entered_password = input()
                else:
                    print(f"login for {entered_userName} is successful ")
                    print('\n')

                    print("Select an option")
                    print('\n')

                while True:
                    print("1: View accounts \n 2: Add new account \n 3: Remove account \n4: Search account \n5: Log Out")
                    option = input()

                    if option == '2':
                        while True:
                            print("Continue to add? y/n")

                            choice = input().lower()
                            if choice == 'y':
                                print("Enter account name")
                                account_name = input()
                                print("Enter password \nTo generate random password enter 'gen' \n To create your own password enter 'own' ")
                                keyword = input().lower()
                                if keyword == 'gen':
                                    account_password = random.randint(111111, 1111111)
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')
                                elif keyword == 'own':
                                    print("Create your password")
                                    account_password = input()
                                    print(f"Account: {account_name}")
                                    print(f"Password: {account_password}")
                                    print('\n')

                                else:
                                    print("invalid")

                                save_new_credential(create_new_credential(
                                    account_name, account_password))
                            elif choice == 'n':
                                break
                            else:
                                print("invalid")
                    elif option == '1':
                        while True:
                            print("your accounts")
                            if display_credentials():

                                for credential in display_credentials():
                                    print(f"account name:{credential.account_name}")
                                    print(f"password:{credential.account_password}")

                            else:
                                print('\n')
                                print("You have no accounts")
                                print('\n')

                            print("Back to Menu? y/n")

                            back = input().lower()
                            if back == 'y':
                                break
                            elif back == 'n':
                                continue
                            else:
                                print("invalid")
                                continue

                    elif option == '5':
                        print(" confirm logout? y/n")
                        logout = input().lower()

                        if logout == 'y':
                            print("logged out")
                            break
                        elif logout == 'n':
                            continue
                    elif option == '3':
                        while True:
                            print("Search for account to delete")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"Account name: {search_credential.account_name} \n password: {search_credential.account_password}")
                                print("Delete? y/n")
                                sure = input().lower()
                                if sure == 'y':
                                    delete_credential(search_credential)
                                    print("deleted")
                                    break
                                elif sure == 'n':
                                    continue

                            else:
                                print(" Does not exist")
                                break

                    elif option == '4':
                        while True:
                            print("Continue? y/n")
                            option2 = input().lower()
                            if option2 == 'y':
                                print("Enter an account name to find credentials")

                                search_name = input()

                                if check_existing_credentials(search_name):
                                    search_credential = find_credential(search_name)
                                    print(f"Account name: {search_credential.account_name} \n password: {search_credential.account_password}")
                                else:
                                    print(" Does not exist")
                            elif option2 == 'n':
                                break
                            else:
                                print("invalid")

                    else:
                        print("invalid")
                        continue

        elif short_code == 'login':
            print("WELCOME")
            print("Enter UserName")
            default_user_name = input()

            print("Enter Your password")
            default_user_password = input()
            print('\n')

            while default_user_name != 'User' or default_user_password != '1234':
                print("invalid.\n use the following\n Username 'User' and password '1234'")
                print("Enter UserName")
                default_user_name = input()

                print("Enter Your password")
                default_user_password = input()

                print('\n')

            if default_user_name == 'User' and default_user_password == '1234':
                print("logged in")
                print('\n')
                print("Select an option")
                print('\n')

            while True:
                print("1: View accounts \n 2: Add new account \n 3: Remove account \n4: Search account \n5: Log Out")
                option = input()

                if option == '2':
                    while True:
                        print("Continue to add? y/n")

                        choice = input().lower()
                        if choice == 'y':
                            print("Enter The Account Name")
                            account_name = input()
                            print("Enter password \nTo generate random password enter 'gen' \n To create your own password enter 'own' ")
                            keyword = input().lower()
                            if keyword == 'gen':
                                account_password = random.randint(111111, 1111111)
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')
                            elif keyword == 'own':
                                print("Create your password")
                                account_password = input()
                                print(f"Account: {account_name}")
                                print(f"Password: {account_password}")
                                print('\n')

                            else:
                                print("invalid")

                            save_new_credential(create_new_credential(
                                account_name, account_password))
                        elif choice == 'n':
                            break
                        else:
                            print("invalid")
                elif option == '1':
                    while True:
                        print("your accounts:\n")
                        if display_credentials():

                            for credential in display_credentials():
                                print(f"Account name:{credential.account_name}")
                                print(f"password:{credential.account_password}\n")

                        else:
                            print('\n')
                            print("you have no account")
                            print('\n')

                        print("Back to Menu? y/n")

                        back = input().lower()
                        if back == 'y':
                            break
                        elif back == 'n':
                            continue
                        else:
                            print("invalid")

                elif option == '5':
                    print("confirm log out? y/n")
                    logout = input().lower()

                    if logout == 'y':
                        print("logged out")
                        break
                    elif logout == 'n':
                        continue

                elif option == '3':
                    while True:
                        print("Search for credential to delete")

                        search_name = input()

                        if check_existing_credentials(search_name):
                            search_credential = find_credential(search_name)
                            print(f"Account name: {search_credential.account_name} \n password: {search_credential.account_password}")
                            print("Delete? y/n")
                            sure = input().lower()
                            if sure == 'y':
                                delete_credential(search_credential)
                                print("deleted")
                                break
                            elif sure == 'n':
                                continue

                        else:
                            print("Does not exist")
                            break

                elif option == '4':
                    while True:
                        print("Continue? y/n")
                        option2 = input().lower()
                        if option2 == 'y':
                            print("Enter an account name to find credentials")

                            search_name = input()

                            if check_existing_credentials(search_name):
                                search_credential = find_credential(search_name)
                                print(f"Account name: {search_credential.account_name} \n password: {search_credential.account_password}\n")
                            else:
                                print("Does not exist")
                        elif option2 == 'n':
                            break
                        else:
                            print("invalid")
                else:
                    print("invalid")
        elif short_code == 'exit':
            break
        else:
            print("invalid")


if __name__ == '__main__':
    main()
