class condicion:
    
    def __init__(self,num2,num3):
        self.numero2= num2
        self.numero3= num3
        numero = self.numero2+self.numero3
        self.numero4=numero
        
    def condicion(self):   
        #if...elif...else...:permiten condicionar la ejecuion de uno o varios bloques
        #de sentencias al cumplimiento de una o varrias condiciones 
        if self.numero2 == self.numero3: 
          print("numero2:{} y numero3:{} son iguales".format(self.numero2,self.numero3)) 
        elif  self.numero2 < self.numero4:
           print("numero2:{} es menor numero4:{}".format(self.numero2,self.numero3))  
        else:
            print("no son iguales")
        print("fin del metodo")    
        
condi2 = condicion(9,25) 
print(condi2.numero4)   
print(condi2.condicion()) 


   
        
