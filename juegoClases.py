#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 16:41:46 2021

@author: alemontano
"""

from random import randint

class Juego:

    def __init__(self, num_jugadores, num_dados, num_lados):
        self.num_jugadores = num_jugadores
        self.num_dados = num_dados
        self.num_lados = num_lados
        self.jugadores = []
   
    def __str__(self):
        pass
   
    def crea_jugadores_asigna_dados(self):
        jugador_id = 1
        COLORES = ["ROJO", "AZUL", "ROSA"]
        #Ciclo para crear cada uno de los jugadores
        for jugador in range(self.num_jugadores):
           
            dados = []
            #Ciclo para crear los dados de cada jugador
            for dado in range(self.num_dados):
                dados.append(Dado(self.num_lados, COLORES[randint(0, 2)]))
            self.jugadores.append(Jugador("Jugador"+str(jugador_id), dados))
            jugador_id += 1
   
    def jugar(self):
        for jugador in self.jugadores:
            jugador.participa()
            print(jugador.nombre)
            for dado in jugador.dados:
                print("\t", dado)
            print("\n")

class Jugador:
   
    def __init__(self, nombre, dados):
        self.nombre = nombre
        self.dados = dados
        self.puntos = 0
       
    def __str__(self):
        resultado = self.nombre + "\n"
        resultado += "\tPuntos: " + str(self.puntos) + "\n"
        for dado in self.dados:
            resultado += "\t\t" + dado.__str__() + "\n"
        return resultado
   
    def __eq__(self, otro):
        return self.puntos == otro.puntos
   
    def __lt__(self, otro):
        return self.puntos < otro.puntos
   
    def __gt__(self, otro):
        return self.puntos > otro.puntos
   
    def participa(self):
        self.puntos = 0
        PUNTOS_EXTRA_POR_PAR = 3
        PUNTOS_EXTRA_POR_TODOS_IGUALES = 100
       
        for dado in self.dados:
            dado.lanzar()
            self.puntos += dado.numero
            if dado.numero % 2 == 0:
                self.puntos += PUNTOS_EXTRA_POR_PAR
       
        iguales = True
        base = self.dados[0].numero
        contador = 1
        while (contador < len(self.dados)) and iguales:
            if self.dados[contador].numero != base:
                iguales == False
            contador += 1
        if iguales:
            self.puntos += PUNTOS_EXTRA_POR_TODOS_IGUALES
        return self.puntos

# Reglas de la puntuacion
# Jugador lanza sus lados
# 1) Sumar el resultado (numero) de cada lado
# 2) Por cada numero par se suman 3 puntos
# 3) Si todos los numeros son iguales, se aumentan 100 puntos

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

juego = Juego(3, 2, 8)
juego.crea_jugadores_asigna_dados()
juego.jugar()