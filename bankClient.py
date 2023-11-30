import bankData

class clsBankClient:

    def isClientFound(clientNum):
        for k in bankData.dicClient_Password.keys():
            if k == clientNum :
                return True
        
        return False
    def CheckClientInfo(clientNum, password):
        for k,v in bankData.dicClient_Password.items():
            if k == clientNum and v == password:
                return True
        
        return False
    
    def __init__(self,clientNumber):
        bankData.currentClientNumber = clientNumber
    
    def editePassword(NewPassword):
            bankData.dicClient_Password[str(bankData.currentClientNumber)] = NewPassword
    
    def deposit(Amount):
        oldAmount = int(bankData.dicAccount_Balance[str(bankData.currentClientNumber)]) 
        bankData.dicAccount_Balance[str(bankData.currentClientNumber)] =str( oldAmount + Amount)

    def withDraw(Amount):
        oldAmount = int(bankData.dicAccount_Balance[str(bankData.currentClientNumber)] )
        if Amount < oldAmount:
            bankData.dicAccount_Balance[str(bankData.currentClientNumber)] = str(oldAmount + Amount)
            return True
        else :
            return False
     