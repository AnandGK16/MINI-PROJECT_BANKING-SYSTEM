"""Project : Banking System
Dear Students,
We have covered core python, now it's time to test your coding and logical skills, also to know how confident you are with the syntax, i'm giving you a small project:
Write a python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also.
You should make a video presentation explaining the code and output and upload it to your github account. Also add that github link to your assessment sheet provided in the quality framework
PS:  Explanation should be in English
Submission Date :10-12-2023
"""



from random import randint

# User data dictionary containing account details
user_data = {
    "anand1234": {"password": "Anand@2000", "balance": 5000, "phone": 9876543210},
    "athira2345": {"password": "Athira@1999", "balance": 4000, "phone": 87654332109},
    "manu3456": {"password": "Manu@2000", "balance": 6000, "phone": 7654321098},
    "john4567": {"password": "John@1998", "balance": 3000, "phone": 6543210987}
}

# Function to display the main menu
def display_menu():
    print("Welcome to the XYZ BANK\n\nPlease select an option")
    print("1. Check Balance")
    print("2. Cash Deposit")
    print("3. Cash Withdraw")
    print("4. Change Password")
    print("5. Exit\n")

# Function to check account balance
def balance_check():
    print("\nYou selected Check Balance")
    print("Your account balance is", user_data[user_id]["balance"])

# Function to handle cash deposit
def cash_deposit():
    print("\nYou selected Cash Deposit")
    deposit_amount = float(input("\nEnter the amount: "))
    user_data[user_id]["balance"] += deposit_amount
    current_balance = user_data[user_id]["balance"]
    print(f"\nRs.{deposit_amount} is credited to your account\nThe current account balance is Rs.{current_balance}")

# Function to handle cash withdrawal
def cash_withdraw():
    print("\nYou selected Cash Withdraw")
    withdraw_amount = float(input("\nEnter the amount: "))

    if withdraw_amount > user_data[user_id]["balance"]:
        print("Insufficient Balance.")
    else:
        user_data[user_id]["balance"] -= withdraw_amount
        current_balance = user_data[user_id]["balance"]
        print(f"\nRs.{withdraw_amount} is debited from your account\nThe current account balance is Rs.{current_balance}")

# Function to change the password
def change_pass():
    pass1 = input("Enter your new password: ")
    pass2 = input("Re-enter your new password: ")

    if pass1 == pass2:
        user_data[user_id]["password"] = pass1
        print("Password changed successfully")
    else:
        print("The passwords entered do not match. Please try again")

# Function to handle the forgot password scenario
def forgot():
    response = input("\nForgot password? Type YES/NO: ")

    if response.upper() == "YES":
        phone_number = user_data[user_id]["phone"]
        print(f"An OTP has been sent to your registered phone number: {phone_number}")

        # Generate a random 6-digit OTP and multiply it by 5 for security reasons
        otp = randint(100000, 999999)
        print("Please Ignore ", otp * 5)

        try:
            otp_response = int(input("\nEnter the OTP: "))

            if otp_response == otp:
                display_menu()
                selection()
            else:
                print("Incorrect OTP. Returning to login.")
        except ValueError:
            print("Invalid input. Please enter a valid integer OTP.")
            print("Returning to login.")

# Function to handle the user's menu selection
def selection():
    menu_choice = int(input("Enter your option: "))

    if menu_choice == 1:
        balance_check()
    elif menu_choice == 2:
        cash_deposit()
    elif menu_choice == 3:
        cash_withdraw()
    elif menu_choice == 4:
        change_pass()
    elif menu_choice == 5:
        print("\nThank you for using XYZ BANK. Goodbye!")
    else:
        print("Invalid option")

# Account login
user_id = input("Enter your username: ")
password = input("Enter your password: ")

if user_id in user_data and user_data[user_id]["password"] == password:
    print("\nLogin successful\n")
    display_menu()
    selection()
else:
    print("Incorrect username or password")
    forgot()






