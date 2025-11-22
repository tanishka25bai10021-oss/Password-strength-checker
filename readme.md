#  Project Title
Password Strength Checker

# Overview of the Project
This project is a simple Python-based password strength checker tool.
It evaluates whether a password follows essential security rules including minimum length, use of uppercase and lowercase letters, digits, and special characters.
The program gives a clear pass/fail report for each requirement and an overall strength result (Strong/Weak).

# Features
✔ Checks minimum password length
✔ Detects uppercase letters
✔ Detects lowercase letters
✔ Validates presence of at least one number
✔ Verifies presence of special characters
✔ Provides user-friendly strength report
✔ Helps users improve weak passwords

# Technologies / Tools Used
Python 3.x
IDE/Text Editor (VS Code, PyCharm, etc.)

# Steps to Install & Run the Project
1. Install Python 3 on your system
2. Download or clone the project repository
3. Open the Python file in a code editor or terminal
4.Run the program using the specific code
5.  Enter a password when prompted
6. View the strength report in the console
   
# Instructions for Testing
Try different types of passwords:
Password Example
Expected Output
abc
Weak → fails length + no uppercase + no digit + no special
Abc123
Weak → fails length + no special
Abc@1234
Strong
HELLO@123
Weak → no lowercase
