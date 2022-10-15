#Banco Atm

class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber = cardnumber
        self.pin = pin
        self.saldo = 50000
        
        self.user = {
            'cardnumber':self.cardnumber,
            'pin':self.pin,
            'saldo':self.saldo 
        
        }       
    def print_user(self):
        print(self)
        
    def check_balance(self):
        user = self.user
        print("seu saldo é: ")
        print(user["saldo"])
    
    def saque(self,valor):
        if self.user["saldo"]>valor:
            saldo2 = self.user['saldo']
            print("saque realizado com sucesso")
            print(f'saldo restante: {saldo2-valor}')
        else:
            print("saldo insuficiente")     
            

pin_number = int(input("Informe seu PIN: "))
card_number = int(input("Informe o numero do cartão: "))
     
new_user = Atm(card_number, pin_number)
opcao = int(input("digite 1 para ver o saldo ou 2 para sacar: "))
if opcao == 1:
    new_user.check_balance()
elif opcao == 2:
    valor = int(input("quanto você deseja sacar?"))
    new_user.saque(valor)
else:
    print("opção invalida")    
           
    

#new_user.print_user()
 
  