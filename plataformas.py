# -*- coding: utf-8 -*-

#Consultar a la base de datos
from neo4j import GraphDatabase
uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("Hugo", "Hugo"))
    
import sys
import os
from tkinter import Tk
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
from PIL import ImageTk, Image, ImageDraw, ImageFont
from random import randint, uniform, random

raiz = Tk()

raiz.title("Plataformas")
raiz.resizable(width=False, height=False)
raiz.geometry("850x700")
raiz.config(bg="grey")

aleatorio1 = randint(1, 12)
aleatorio2 = randint(1, 12)

imagen = Image.open("C:\\Users\\Usuario\\Desktop\\Universidad\\BussinessInteligence\\Proyecto\\Imagenes\\Fondos\\"+str(aleatorio1)+".jpg")
imagen_de_fondo = ImageTk.PhotoImage(imagen)
fondo = tk.Label(raiz, image=imagen_de_fondo)
fondo.place(x=0, y=0, relwidth=1, relheight=1)


vecGen = []
final = []
libro = []
    
#Funciones
def generos():
    vector = []
    with driver.session() as session:
        for record in session.run("MATCH (g:Genero)"
                                  "RETURN g.nombre"):
                                vector.append(record["g.nombre"])
    return vector


def buscar():
    
    vectorPlataforma = []
    plataforma = [""]
      
    var2=raiz.combo2.get()
    with driver.session() as session:
        for record in session.run("MATCH (m:Pelicula)-[ES_DE]->(g:Genero{nombre:'"+str(var2)+"'})"
                                  "MATCH (m)-[ESTA_EN]->(l:Plataforma)"
                                  "RETURN l.nombre"):
            vectorPlataforma.append(record["l.nombre"])

######################################### COMBO2 #############################################                         
                                    
    var6=raiz.combo6.get()
    with driver.session() as session:
        for record in session.run("MATCH (m:Pelicula)-[ES_DE]->(g:Genero{nombre:'"+str(var6)+"'})"
                                  "MATCH (m)-[ESTA_EN]->(l:Plataforma)"
                                  "RETURN l.nombre"):
            vectorPlataforma.append(record["l.nombre"])

######################################### COMBO3 #############################################
        
    var8=raiz.combo8.get()
    with driver.session() as session:
        for record in session.run("MATCH (m:Pelicula)-[ES_DE]->(g:Genero{nombre:'"+str(var8)+"'})"
                                  "MATCH (m)-[ESTA_EN]->(l:Plataforma)"
                                  "RETURN l.nombre"):
            vectorPlataforma.append(record["l.nombre"])
                           
######################################### COMBO4 #############################################

    var10=raiz.combo10.get()
    with driver.session() as session:
        for record in session.run("MATCH (m:Pelicula)-[ES_DE]->(g:Genero{nombre:'"+str(var10)+"'})"
                                  "MATCH (m)-[ESTA_EN]->(l:Plataforma)"
                                  "RETURN l.nombre"):
            vectorPlataforma.append(record["l.nombre"])

######################################### COMBO5 #############################################

    var12=raiz.combo12.get()
    with driver.session() as session:
        for record in session.run("MATCH (m:Pelicula)-[ES_DE]->(g:Genero{nombre:'"+str(var12)+"'})"
                                  "MATCH (m)-[ESTA_EN]->(l:Plataforma)"
                                  "RETURN l.nombre"):
            vectorPlataforma.append(record["l.nombre"])

######################################### FINAL ##############################################
    
    if not vectorPlataforma:
        messagebox.showerror("Error", "Introduce algún criterio")
        nueva()

    resultado = contarElementosLista(vectorPlataforma)
    plataforma = max(resultado, key=resultado.get)         
            
    final.append(plataforma)

    raiz.label=ttk.Label(raiz)
    raiz.label.place(x=65, y=285 )
    raiz.label.config(text="Según los criterios introducidos, la plataforma que se recomienda es: " + final[0])
    raiz.label.config(font="Verdana 9 italic bold")
    
    
################################### IMAGEN PLATAFORMA #############################################

    path = 'C:\\Users\\Usuario\\Desktop\\Universidad\\BussinessInteligence\\Proyecto\\Imagenes\\Plataformas\\'+ str(final[0]) + ".jpg"
    load = Image.open(path)
    render = ImageTk.PhotoImage(load)
    img = ttk.Label(raiz, image=render)
    img.image = render
    img.place(x=115 , y=315)
        
    
##################################### INFORMACIÓN PELICULAS ###########################################
    
    def infopeli():

        info = tk.Toplevel(raiz)
    
        info.title("Películas")
        info.resizable(width=False, height=False)  
        info.geometry("850x770")
        info.config(bg="grey")
        
        titulo = []
        
        aux1 = 90
        true = 0
        
        imagenFondo = Image.open("C:\\Users\\Usuario\\Desktop\\Universidad\\BussinessInteligence\\Proyecto\\Imagenes\\Fondos\\"+str(aleatorio2)+".jpg")
        imagen_de_fondo = ImageTk.PhotoImage(imagenFondo)
        fondo = tk.Label(info, image=imagen_de_fondo)
        fondo.place(x=0, y=0, relwidth=1, relheight=1)
        
######################################### COMBO1 #############################################
        
        with driver.session() as session:
            for record in session.run("MATCH (m:Pelicula)-[:ES_DE]->(g:Genero{nombre:'"+str(var2)+"'})"
                                       "MATCH (m)-[:ESTA_EN]->(l:Plataforma{nombre:'"+str(final[0])+"'})"
                                       "RETURN m.nombre"):
                titulo.append(record["m.nombre"])

######################################### COMBO2 #############################################
        
        with driver.session() as session:
            for record in session.run("MATCH (m:Pelicula)-[:ES_DE]->(g:Genero{nombre:'"+str(var6)+"'})"
                                       "MATCH (m)-[:ESTA_EN]->(l:Plataforma{nombre:'"+str(final[0])+"'})"
                                       "RETURN m.nombre"):
                for i in range (len(titulo)):
                    if titulo[i] == record["m.nombre"]:
                        true = 1
                if true == 0:
                    titulo.append(record["m.nombre"])
                true=0

######################################### COMBO3 #############################################
                
        with driver.session() as session:
            for record in session.run("MATCH (m:Pelicula)-[:ES_DE]->(g:Genero{nombre:'"+str(var8)+"'})"
                                       "MATCH (m)-[:ESTA_EN]->(l:Plataforma{nombre:'"+str(final[0])+"'})"
                                       "RETURN m.nombre"):
                for i in range (len(titulo)):
                    if titulo[i] == record["m.nombre"]:
                        true = 1
                if true == 0:
                    titulo.append(record["m.nombre"])
                true=0

######################################### COMBO4 #############################################
                
        with driver.session() as session:
            for record in session.run("MATCH (m:Pelicula)-[:ES_DE]->(g:Genero{nombre:'"+str(var10)+"'})"
                                       "MATCH (m)-[:ESTA_EN]->(l:Plataforma{nombre:'"+str(final[0])+"'})"
                                       "RETURN m.nombre"):
                for i in range (len(titulo)):
                    if titulo[i] == record["m.nombre"]:
                        true = 1
                if true == 0:
                    titulo.append(record["m.nombre"])
                true=0

######################################### COMBO5 #############################################
        
        with driver.session() as session:
            for record in session.run("MATCH (m:Pelicula)-[:ES_DE]->(g:Genero{nombre:'"+str(var12)+"'})"
                                       "MATCH (m)-[:ESTA_EN]->(l:Plataforma{nombre:'"+str(final[0])+"'})"
                                       "RETURN m.nombre"):
                for i in range (len(titulo)):
                    if titulo[i] == record["m.nombre"]:
                        true = 1
                if true == 0:
                    titulo.append(record["m.nombre"])
                true=0

######################################### FINAL ##############################################
        
        for i in range (len(titulo)):
            
            generoPeli = []
            
            with driver.session() as session:
                for g in session.run("MATCH (m:Pelicula)-[ES_DE]-(g:Genero)"
                                     "WHERE m.nombre='"+str(titulo[i])+"'"
                                     "RETURN g.nombre"):
                        generoPeli.append(g["g.nombre"])
            
            generoPeliAux = ", ".join(generoPeli)
    
            info.label2=ttk.Label(info)
            info.label2.place(x=100, y= aux1 )
            info.label2.config(text="Película: "+titulo[i]+"      Género/s: "+str(generoPeliAux))
            info.label2.config(font="Arial 10 bold")
            aux1 = aux1 + 34
        
        info.label1=ttk.Label(info)
        info.label1.place(x=325, y=30 )
        info.label1.config(text=final[0])
        info.label1.config(font="Arial 25 bold") 
        
        info.mainloop()
    
    raiz.Button9 = ttk.Button(raiz, command=infopeli, text = "PELÍCULAS RECOMENDADAS")
    raiz.Button9.place(x=455, y=335)
    
    
################################### FUNCIONES ##############################################

def nueva():
    python = sys.executable
    os.execl(python, python, * sys.argv)
    
def contarElementosLista(lista):

    return {i:lista.count(i) for i in lista}

    
######################################## BOTONES ##########################################

raiz.Button7 = ttk.Button(raiz, command=buscar, text = "BUSCAR")
raiz.Button7.place(x=245, y=225)

raiz.Button8 = ttk.Button(raiz, command=nueva, text = "NUEVA BÚSQUEDA")
raiz.Button8.place(x=345, y=225)


###################################### COMBOBOX #############################################
vecGen = generos()

raiz.combo2 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo2.place(x=410, y=25)
raiz.combo2["values"]=vecGen

raiz.combo6 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo6.place(x=410, y=65)
raiz.combo6["values"]=vecGen

raiz.combo8 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo8.place(x=410, y=105)
raiz.combo8["values"]=vecGen

raiz.combo10 = ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo10.place(x=410, y=145)
raiz.combo10["values"]=vecGen

raiz.combo12= ttk.Combobox(raiz, state='readonly', width = 30)
raiz.combo12.place(x=410, y=185)
raiz.combo12["values"]=vecGen


###################################### LABEL #############################################
raiz.label=ttk.Label(raiz)
raiz.label.place(x=115, y=25 )
raiz.label.config(text="Género")
raiz.label.config(font="Arial 15 bold")

raiz.label=ttk.Label(raiz)
raiz.label.place(x=115, y=65 )
raiz.label.config(text="Género")
raiz.label.config(font="Arial 15 bold")

raiz.label=ttk.Label(raiz)
raiz.label.place(x=115, y=105 )
raiz.label.config(text="Género")
raiz.label.config(font="Arial 15 bold")

raiz.label=ttk.Label(raiz)
raiz.label.place(x=115, y=145 )
raiz.label.config(text="Género")
raiz.label.config(font="Arial 15 bold")

raiz.label=ttk.Label(raiz)
raiz.label.place(x=115, y=185 )
raiz.label.config(text="Género")
raiz.label.config(font="Arial 15 bold")


raiz.mainloop() 