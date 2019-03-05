#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():
    print("PASO DE GRADOS CELCIUS A FARENHEIT")
    grados= float(input("Grados Celsius:"))
    paso= (grados * (9.0/5.0)) + 32
    print("El resultado es:{} " .format(paso))
if __name__ == "__main__":
   main()
