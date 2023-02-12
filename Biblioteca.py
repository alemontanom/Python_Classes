#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 16:34:51 2021

@author: alemontano
"""
class Biblioteca: 
    
    numero = 0 
    
    def __init__(self, nombre, direccion, horarios):
        Biblioteca.numero = Biblioteca.numero + 1
        self.identificador = Biblioteca.numero
        self.nombre = nombre
        self.libros = []
        self.direccion = direccion 
        self.horarios = horarios 
        self.usuarios = []
        
    def __str__(self):
        return self.nombre 
    
    def agregar_libro(self, libro):
        self.libros = self.libros + [libro]
        
    def agregar_usuario(self, usuario): #no funciona ?!
        self.usuarios = self.usuarios + [usuario]
        
    def buscar_libro(self, book): #busca por autor o titulo
        for libro in self.libros: 
            if book == libro.titulo : 
                return "Disponible"
            elif book == libro.autores:
                return "Disponible: " + libro.autores.libros  
            else:
                return "No disponible"
            
    def borrar_libros(self, libro):
        self.libros.remove(libro)
    
    def libros_usuario(self, usuario):
        return usuario.libros_rentados

class Autor: 
    
    matricula = 0 
    
    def __init__(self, nombre, fecha_nac, nacionalidad):
        Autor.matricula = Autor.matricula + 1
        self.identificador = Autor.matricula 
        self.nombre = nombre
        self.fecha_nac = fecha_nac 
        self.nacionalidad = nacionalidad
        self.libros = []
        
    def __str__(self):
        return self.nombre
    
    def anadir_libro (self, libro):
        self.libros = self.libros + [libro]
        
        
class Libro: 
    
    folio = 0 
    
    def __init__(self, titulo, autores, paginas):
        Libro.folio = Libro.folio + 1 
        self.identificador = Libro.folio 
        self.titulo = titulo 
        self.autores = autores 
        self.paginas = paginas 
        self.rentas = []
        
    def __str__(self):
        return self.titulo 
    
    def __lt__(self, otro):
        return self.paginas < otro.paginas 
    
    def registrar_renta(self, renta): 
        self.rentas = self.rentas + [renta]
        

class Usuario: 
    
    user = 0
    
    def __init__(self, nombre):
        Usuario.usser = Usuario.user + 1
        self.identificador = Usuario.user 
        self.nombre = nombre 
        self.libros_rentados = []
        
    def __str__(self):
        return self.nombre 
    
    def agregar_renta(self, libro, fecha):
        self.libros_rentados = self.libros_rentados + [[libro, fecha]]
        
        
    
    
    