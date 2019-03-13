#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__

def main():
   print("Es un año bisiesto")
   fecha=int(input("Escriba un año:"))

   if fecha % 400 == 0:
       print("Es bisiesto porque es múltiplo de 400")
   elif fecha %100 == 0: 
       print("No es bisiesto porque es múltiplo de 100")
   elif fecha % 4 ==0:
       print("Es bisiesto porque es múltiplo de 4")
   else:
       print("No es bisiesto")

if __name__ == "__main__":
    main()
