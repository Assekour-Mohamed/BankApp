from bankClient import clsBankClient

class clsClientMenu:
    def showMenu():
        print("---------------------------------")
        print("                                 ")
        print("     UPDATE PASSWORD [1]         ")
        print("     DEPOSIT AMOUNT  [2]         ")
        print("     WITHDRAW AMOUNT [3]         ")
        print("                                 ")
        print("---------------------------------")
        x = input("what is you choice : ")
        clsClientMenu.choice(x)

    def choice(opt):
        
        if opt == "1":
            newPass = input("enter new password : ")
            clsBankClient.editePassword(newPass)
            print("password updated successfully")
        elif opt == "2":
            amount = int(input("enter amount to deposit : "))
            clsBankClient.deposit(amount)
            print("amount updated successfully")
        elif opt == "3" :
            amount = int(input("enter amount to withdraw : "))
            if clsBankClient.withDraw(amount):
                print("amount updated successfully")
            else:
                print("you cant enough money")
        else :
            print("wrong input!!")

 

