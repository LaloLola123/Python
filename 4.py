#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
   numero_1 = int(input("Escriba los segundos: "))
   horas = (numero_1 / 3600)
   minutos = ((numero_1 % 3600) / 60)
   segundos = ((numero_1 % 60) / 1)
   print("Horas:" + str(horas))
   print("Minutos:" + str(minutos))
   print("Segundos:" + str(segundos))
if __name__ == "__main__":
    main()
