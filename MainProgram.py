
from bankClient import clsBankClient
from clientMenu import clsClientMenu
from EmpMenu import clsEmpMenu


while(True):
    print("are you a Client [1] or Employer [2]..")
    choice = input("enter a choice : ")
    if choice == "1":
        Number = int(input("enter client number: "))
        Password = input("enter client password :")
        if clsBankClient.CheckClientInfo(str(Number),Password):
            Client = clsBankClient(Number)
            clsClientMenu.showMenu()    
        else:
            print("Wrong info!!!")
    elif choice =="2":
        clsEmpMenu.showMenu()
    else:
        print("wrong input!!!")