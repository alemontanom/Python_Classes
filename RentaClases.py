#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:43:22 2021

@author: alemontano
"""

from random import random

class RentaFija:
   
    def __init__(self, num_titulos, precio, tasa):
        self.num_titulos = num_titulos
        self.precio = precio
        self.tasa = tasa

    def __str__(self):
        return "F - " + "Titulos: " + str(self.num_titulos) + " Precio: " \
            + str(self.precio) + " Tasa: " + str(self.tasa)

    def __repr__(self):
        return "F"
   
    def __eq__(self, otro):
        return self.num_titulos*self.precio == otro.num_titulos*otro.precio
   
    def __lt__(self, otro):
        return self.num_titulos*self.precio < otro.num_titulos*otro.precio
   
    def __gt__(self, otro):
        return self.num_titulos*self.precio > otro.num_titulos*otro.precio
   
    def calcular_valor(self):
        return self.num_titulos * self.precio * (1 + self.tasa)
   
#cetes_noviembre = RentaFija(1, 100, 0.05)
#cetes_enero = RentaFija(2, 101, 0.1)
#print(cetes_noviembre, cetes_noviembre.calcular_valor())
#print(cetes_enero, cetes_enero.calcular_valor())
#print(cetes_noviembre == cetes_enero)

class RentaVariable:
   
    def __init__(self, num_titulos, precio):
        self.num_titulos = num_titulos
        self.precio = precio
       
    def __str__(self):
        return "F - " + "Titulos: " + str(self.num_titulos) + " Precio: " \
            + str(self.precio) + " Tasa: " + str(self.tasa)

    def __repr__(self):
        return "V"
   
    def __eq__(self, otro):
        return self.num_titulos*self.precio == otro.num_titulos*otro.precio
   
    def __lt__(self, otro):
        return self.num_titulos*self.precio < otro.num_titulos*otro.precio
   
    def __gt__(self, otro):
        return self.num_titulos*self.precio > otro.num_titulos*otro.precio
   
    def calcular_valor(self):
        if random() > 0.5:
            return self.num_titulos * self.precio * (1 + random()/5)
        else:
            return self.num_titulos * self.precio * (1 - random()/5)
           
acciones = RentaVariable(4, 5000)
#print(acciones.calcular_valor())
#print(acciones.calcular_valor())
#print(acciones.calcular_valor())
#print(acciones.calcular_valor())
#print(acciones.calcular_valor())
#print(acciones.calcular_valor())

class Portafolio:
   
    def __init__(self, cliente, instrumentos):
        self.cliente = cliente
        self.instrumentos = instrumentos
       
    def cuenta_tipos_de_instrumentos(self):
        fijas = 0
        variables = 0
        for instrumento in self.instrumentos:
            if isinstance(instrumento, RentaFija):
                fijas += 1
            elif isinstance(instrumento, RentaVariable):
                variables += 1
        return fijas, variables
   
    def calcular_valor(self):
        total = 0.00
        for instrumento in self.instrumentos:
            total += instrumento.calcular_valor()
        return total
   
    def cargar(self, nombre_archivo):
        with open(nombre_archivo, "r") as archivo:
            for instrumento in archivo.readlines():
                instrumento = instrumento.strip.split(",")
                print(instrumento)
                if len(instrumento) == 2:
                    self.instrumentos.append(RentaVariable(int(instrumento[0]),
                                                           float(instrumento[1])))
                else:
                    self.instrumentos.append(RentaFija(int(instrumento[0]),
                                                       float(instrumento[1]),
                                                       float(instrumento[2])))
   
instrumentos = [RentaFija(2, 100, 0.05), RentaVariable(2, 55000),
                RentaFija(3, 110, 0.01)]
   
portafolio = Portafolio("Octavio Gutierrez", instrumentos)
print(portafolio.cuenta_tipos_de_instrumentos())
print(portafolio.calcular_valor())