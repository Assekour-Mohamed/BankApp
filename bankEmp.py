import random
import bankData
from bankClient import clsBankClient
class clsBankEmp:
 
    def addClient():

        clientNumber = str(len(bankData.dicAccount_Balance) + 1)
        
        bankData.dicAccount_Balance[clientNumber] = "0"
        
        bankData.dicClient_Password[clientNumber] = "1234@"

        accountNumber = str(clientNumber * 100 + random.randint(0,100))
        bankData.dicClient_AccountNumber[clientNumber] = accountNumber
    
    def DeleteClient(clientNumber):
        if clsBankClient.isClientFound(clientNumber) :
            del bankData.dicAccount_Balance[clientNumber]
            del bankData.dicClient_AccountNumber[clientNumber]
            del bankData.dicClient_Password[clientNumber]
            return True
        else:
            return False
    def showClients():
        print("Clients NUMBERS/BALANCES")
        print(bankData.dicAccount_Balance)

        print("Clients NUMBERS/ACCOUNT NUMBERS")
        print(bankData.dicClient_AccountNumber)

        print("Clients NUMBERS/PASSWORDS")
        print(bankData.dicClient_Password)

    




    
        

 