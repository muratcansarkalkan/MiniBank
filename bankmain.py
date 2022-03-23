# Basic banking system, I'll add more to this to expand my skills...
# Such as JSON use, MongoDB...
import banking

print("Welcome to the Bank")
print("Please enter your username and password")

attempt = 0
ui = ""
pi = ""

class Logon():
    username = "mike"
    password = "1900"
    cash = 750

    while ui != username and pi != password and attempt <= 3:
        try:
            ui = input("Please enter your username")
            pi = input("Please enter your password")
            if username == ui and password == pi:
                print("Successfully logged in...")
                choice = input("Welcome! Please select your operation")
                banking.function_dict(choice,cash)

            else:
                attempt += 1
                print("Please try again")
        except:
            pass

        if attempt >= 3:
            print("You exceeded max logon attempts")
            break

