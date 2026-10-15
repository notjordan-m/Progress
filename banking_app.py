user_name = input("Enter Your Username:")
user_password = input("Enter your Password: ")
balance = 1000

if user_name == "jonzz" and user_password == "1234":
    print("Login Successful")
    logged_in = True
    if logged_in : True
    choice = int(input("Choose an option from the menu:\n 1. Send money\n 2. Request Money\n 3. Check Balance\n 4. Exit\nYour Choice: "))
    if choice ==1:
        contact = input("Choose A Contact to send money to: ")
        if contact in ["Bob", "Andy", "John"]:
            amount = int(input("Enter the amount to send:"))
            if amount <= balance:
                balance -= amount
                print(f"You Sent ${amount} to {contact} Your new balance is ${balance}")
    if choice ==2: 
        contact = input("Choose A Contact to request money from: ")
        if contact in ["Bob", "Andy", "John"]:
            amount = int(input("Enter the amount to request:"))
            print(f"You requested ${amount} from {contact}")
    if choice ==3:
        print(f"Your balance is ${balance}")
    if choice ==4:
        print("See you next time!")

else:
    print("Login Failed. Please check your username and password.")
