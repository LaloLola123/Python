#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
 
def main():
   a = float(input("Escriba primer coeficiente: "))
   
       
   b = float(input("Escriba segundo coeficiente: "))
   if a == 0:
       if b == 0:
           print("Indeterminación")
       elif b > 0:
           print("Solución es Maś Infinito")
       elif b < 0:
           print("Solución es Menos Infinito")
   else:    
       x = ((-b)/(a))
       print(x)
   
if __name__ == "__main__":
    main()

