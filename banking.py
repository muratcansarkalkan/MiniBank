choice = "2"

cash = 745

def function_dict(choice,cash):
    function_dict = {"1":deposit, "2":withdraw, "3":check}
    function_dict[choice](cash)
# if choice == "1":
#     deposit(cash)
# if choice == "2":
#     withdraw(cash)
# if choice == "3":
#     check(cash)

def deposit(cash):
    print("You have " + str(cash) + " annen in your account")
    cashnew = input("Please input money that you want to deposit")
    cash = cash + int(cashnew)
    print("Now, you have " + str(cash) + " USD in your account")
    return None

def withdraw(cash):
    print("You have " + str(cash) + " USD in your account")
    cashnew = input("Please input money that you want to withdraw")
    cash = cash - int(cashnew)
    print("Now, you have " + str(cash) + " USD in your account")
    return None

def check(cash):
    print("You have " + str(cash) + " USD in your account")
    return None


