from bankEmp import clsBankEmp
class clsEmpMenu:
    def showMenu():
        print("---------------------------------")
        print("                                 ")
        print("     ADD CLIENT     [1]          ")
        print("     DELETE CLIENT  [2]          ")
        print("     SHOW CLIENTS   [3]          ")
        print("                                 ")
        print("---------------------------------")
        x = input("what is you choice : ")
        clsEmpMenu.choice(x)

    def choice(opt):
        if opt == "1":
            clsBankEmp.addClient()
            print("adding client successfully")
        elif opt == "2":
            clientToDel = input("enter client number to delete : ")

            if clsBankEmp.DeleteClient(clientToDel):
                print("deleted client successfully")
            else:
                print("client nmuber was not found")
        elif opt=="3":
            clsBankEmp.showClients()
        else :
            print("wrong input!!")
        
