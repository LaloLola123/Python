#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("Ordenar tres números") 
    lista=[]
    lista.append(int(input("introduzca el primer número")))
    lista.append(int(input("introduzca el segundo número")))
    lista.append(int(input("introduzca el tercer número")))
    lista.sort()
    print(lista)
    
if __name__ == "__main__":
    main()

