import os
from functions import create_login, update_login, generate_password, get_login

i = True

while i == True:
    clear = lambda: os.system('clear')
    clear()
    def confirm():
        opt = input("""
Do you want to continue?

1. Yes
2. No        

Enter an option: """)

        if opt == '2':
            i = False
            print('Goodbye')
            return i
        elif opt == '1':
            i = True
            return i

    print("""
************************************************************************************
*                            WELCOME TO PASSWORD MANAGER                           *
************************************************************************************
*                                                                                  *
*   1. Check login details                                                         *
*   2. Create login                                                                *
*   3. Generate password                                                           *
*   4. Update login                                                                *
*                                                                                  *
*   0. Cancel                                                                      *
*                                                                                  *
************************************************************************************
""")

    option = input("Select an option: ")

    if(option == '1'):
        get_login()
        i = confirm()
    elif(option == '2'):
        create_login()
        i = confirm()
    elif(option == '3'):
        password = generate_password()
        print(" ")
        print("Your new password is: " + password)
        print(" ")
        i = confirm()
    elif(option == '4'):
        update_login()
        i = confirm()
    else:
        i = False
        print(" ")
        print("Goodbye!")