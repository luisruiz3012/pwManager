import os
from getpass import getpass
from password_generator import generate_password
import mysql.connector as mysql

clear = lambda: os.system('clear')
clear()

db = mysql.connect(
        host = 'localhost',
        user = getpass('Enter your user: '),
        passwd = getpass('Enter the main password: '),
        database = 'password_manager'
    )

cur = db.cursor()

def get_login():
    name = input("Enter the name of the website or app that you want to check: ").lower()
    query = "SELECT * FROM login WHERE name= '" + name + "'"
    cur.execute(query)
    data = cur.fetchall()
    print(""" 

YOUR LOGIN DETAILS

""")
    print("Website: " + data[0][1])
    print("Username: " + data[0][2])
    print("Password: " + data[0][3])
    print("Email: " + data[0][4])
    print(" ")

def create_login():
    name = input("Enter the website or app name: ").lower()
    user = input("Enter a username(press enter if none): ")
    password = generate_password()

    email = input("Enter an email address: ")
    info = (name, user, password, email)

    query = 'INSERT INTO login(name, user, password, email) VALUES(%s, %s, %s, %s)'
    cur.execute(query, info)
    db.commit()

    print(" ")
    print("Login created successfully!")
    print(" ")
    
def update_login():
    selection = input("""
What do you wanto to update?

1. Email
2. Username
3. Password

Enter an option: """)
    
    if(selection == '1'):
        name = input("Enter the website name where the email will be updated: ")
        email = input("Enter the new email for this website: ")

        info = (email, name)

        query = 'UPDATE login SET email=%s WHERE name=%s'
        cur.execute(query, info)
        db.commit()

        print(" ")
        print("Details updated successfully!")
        print(" ")

    elif(selection == '2'):
        name = input("Enter the website name where the email will be updated: ")
        user = input("Enter the new username for this website: ")

        info = (user, name)

        query = 'UPDATE login SET user=%s WHERE name=%s'
        cur.execute(query, info)
        db.commit()

        print(" ")
        print("Details updated successfully!")
        print(" ")

    elif(selection == '3'):
        name = input("Enter the website name where the email will be updated: ")
        password = input("Enter the new password for this website: ")

        info = (password, name)

        query = 'UPDATE login SET password=%s WHERE name=%s'
        cur.execute(query, info)
        db.commit()

        print(" ")
        print("Details updated successfully!")
        print(" ")