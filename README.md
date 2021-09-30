# Password Manager
This is a **Python** and **MySQL** password manager with the purpose of practicing MySQL database management and connection with a simple python project that allows you to run a local password manager/generator on your computer.

## Database Sctipt (Make sure to have MySQL installed)
Copy the following comands on a MySQL RDBMS (MySQL Workbench) or on a Terminal

- **Create the database**
       
      CREATE DATABASE password_manager;
      
- **Access to the database**
    
      USE password_manager;

- **Create the login table**

      CREATE TABLE login(
      id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
      name VARCHAR(100) NOT NULL,
      user VARCHAR(100),
      password VARCHAR(100) NOT NULL,
      email VARCHAR(255)
      );

## After installing
Copy the Github repository on your computer, then install the requirement on the ***requirement.txt*** file with the following command:
      
    pip install requirement.txt

Once you have the requirements installed, run the following command to run the program:
    
    python3 app.py

