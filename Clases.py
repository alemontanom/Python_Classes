#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 17:46:31 2021

@author: alemontano
"""

# Crear un molde de un carro con: 1) los siguientes atributos: num_serie, 
# color y kms; 2) los siguientes metodos: 

class Carro:
    # Atributos
    def __init__(self, maxP):
        self.numSerie = "000000FA"
        self.color = "Rojo"
        self.kms = 0
        self.maxP = maxP
    # Metodos
    def registrarViaje(self, kilometros):
        self.kms = self.kms + kilometros
        
    def __eq__(self, otro): #eq siempre regresa booleano 
        return self.numSerie == otro.numSerie
    
    def __lt__(self, otro): # less than
        return self.maxP < otro.maxP
    
    def __gt__(self, otro):#greater than
        return self.maxP > otro.maxP
    
    def __str__(self):#siempre regresa str
        return "Numero de serie: "+ self.numSerie + "\nMaximo pasajeros: " + str(self.maxP)
   
    def __repr__(self): #defines lo que va a imprimir, regresa str
        return self.numSerie
    
    def ajustarColor(self):
        pass 
    
from math import pi

class Cilindro:
    
    folio = 0
    
    def __init__(self, altura, radio):
        Cilindro.folio = Cilindro.folio + 1
        self.identificador = Cilindro.folio
        self.altura = altura
        self.radio = radio
        
    def __eq__(self, otro):
        return self.calcular_area() == otro.calcular_area()
    
    def __lt__(self, otro):
        return self.calcular_area() < otro.calcular_area()
    
    def __gt__(self, otro):
        return self.calcular_area() > otro.calcular_area()
    
    def __str__(self):
        return "Radio: %0.2f Altura: %0.2f" % (self.radio, self.altura)

    def __repr__(self):
        return "(r:%0.2f, a:%0.2f)" % (self.radio, self.altura)
        #return self.__str__()
    
    def calcular_area(self):
        return 2 * pi * self.radio * (self.altura + self.radio)
    
    def calcular_volumen(self):
        return pi * self.radio * self.radio * self.altura
    

from random import randint

class Dado:
    
    def __init__(self, num_lados, color):
        self.num_lados = num_lados
        self.color = color
        self.numero = 1
        
    def __str__(self):
        return str(self.numero) + " " + self.color
    
    def __repr__(self):
        return self.__str__()
    
    def lanzar(self):
        self.numero = randint(1, self.num_lados)
        return self.numero
    

dado1 = Dado(8, "rojo")
dado2 = Dado(5, "azul")

juego = [dado1, dado2]

for dado in juego:
    dado.lanzar()
    
for dado in juego:
    print(dado)
    
    
"""
carro1 = Carro(33)
print(carro1.__str__())
carro2 = Carro(45)
print(carro2.__eq__(carro1))

print(carro1.color)
print(carro1.numSerie)
print(carro2.numSerie)
carro1.numSerie = "123A"
print()
print(carro1.numSerie)
print(carro2.numSerie)
print()
print(carro1.kms)
carro1.registrarViaje(100)
carro2.registrarViaje(100)
print(carro2.kms)"""