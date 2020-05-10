#!/usr/bin/env python
# coding: utf-8

# # Simulación de Patio de Contenedores (Variante 1)

# In[1]:


import networkx as nx
import matplotlib.pyplot as plt
import random
from random import uniform, expovariate
import numpy
import datetime
from datetime import timedelta, time, date


# In[2]:


#El diccionario con la información de los barcos se encuentra a continuación
#barcos = {"codigo_barco":[día_llegada, día_partida, total_descargar, total_cargar]}

info_barcos = {
    "B-5-800":[1,6,261,618],
    "B-2-600":[1,6,296,565],
    "B-4-600":[4,9,226,426],
    "B-3-1200":[6,10,646,846],
    "B-2-1200":[11,16,699,850],
    "B-2-800":[11,14,284,701],
    "B-4-800":[15,19,400,765],
    "B-3-600":[15,20,236,517],
    "B-5-600":[15,20,215,458],
    "B-1-600":[17,21,291,562],
    "B-7-600":[20,23,290,568],
    "B-3-800":[24,28,410,796],
    "B-1-1200":[26,29,405,1045],
    "B-4-1200":[26,30,526,1193],
    "B-1-800":[26,30,335,595],
    "B-6-600":[27,32,310,566]}

barcos = []


# In[3]:


class Nodo:
    
    def __init__(self,posicion,navegable):
        self.elementos = []
        self.conexiones = []
        self.posicion = posicion
        self.navegable = navegable
        self.nodopadre = None
        self.despacho = False
        self.recepcion = False
        self.muelle = False
        self.largo = False
        self.ancho = False
        
    def agregar_conexion(self, vecino):
        self.conexiones.append(vecino)
        
    def __repr__(self):
        l = "( {} )".format(self.elementos)
        return l


# In[4]:


mapa =      [
            ["D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","_","R1","R2","R3","R4","R5","R6","R7","R8","R9","R10"],
            ["A1","A2","A3","A4","A5","A6","A7","A8","A9","A10","A11","A12","A13","A14","A15","A16","A17","A19","A20","A21","A22"],
            ["B1",[ ],"B2",[ ],"B3",[ ],"B4",[ ],"B5",[ ],"B6",[ ],"B7",[ ],"B8",[ ],"B9",[ ],"B10",[ ],"B11"],
            ["C1","C2","C3","C4","C5","C6","C7","C8","C9","C10","C11","C12","C13","C14","C15","C16","C17","C19","C20","C21","C22"],
            ["L1",[ ],"L2",[ ],"L3",[ ],"L4",[ ],"L5",[ ],"L6",[ ],"L7",[ ],"L8",[ ],"L9",[ ],"L10",[ ],"L11"],
            ["E1","E2","E3","E4","E5","E6","E7","E8","E9","E10","E11","E12","E13","E14","E15","E16","E17","E19","E20","E21","E22"],
            ["F1",[ ],"F2",[ ],"F3",[ ],"F4",[ ],"F5",[ ],"F6",[ ],"F7",[ ],"F8",[ ],"F9",[ ],"F10",[ ],"F11"],
            ["G1","G2","G3","G4","G5","G6","G7","G8","G9","G10","G11","G12","G13","G14","G15","G16","G17","G19","G20","G21","G22"],
            ["H1",[ ],"H2",[ ],"H3",[ ],"H4",[ ],"H5",[ ],"H6",[ ],"H7",[ ],"H8",[ ],"H9",[ ],"H10",[ ],"H11"],
            ["I1","I2","I3","I4","I5","I6","I7","I8","I9","I10","I11","I12","I13","I14","I15","I16","I17","I19","I20","I21","I22"],
            ["J1",[ ],"J2",[ ],"J3",[ ],"J4",[ ],"J5",[ ],"J6",[ ],"J7",[ ],"J8",[ ],"J9",[ ],"J10",[ ],"J11"],
            ["K1","K2","K3","K4","K5","K6","K7","K8","K9","K10","K11","K12","K13","K14","K15","K16","K17","K19","K20","K21","K22"],
            ["M1","M2","M3","M4","M5","M6","M7","M8","M9","M10","M11","M12","M13","M14","M15","M16","M17","M18","M19","M20","M21"]
            ]

filas_mapa=len(mapa)
columnas_mapa=len(mapa[0])

#SE CREAN LOS NODOS
nodos=[]
i=0 
for fila in mapa:
    nodos.append([])
   
 
    j=0
    for elemento in fila:
            
        if type(elemento)== list:
            nodo=Nodo([mapa.index(fila),j],False)
            nodo.largo = 53
            nodo.ancho = 14
            nodo.elementos.append(elemento)
            nodos[i].append(nodo)
            fila[fila.index(elemento)]=elemento

            
        elif 'M' in elemento:
            nodo=Nodo([mapa.index(fila),j],True)
            nodo.muelle=True
            nodo.elementos.append(elemento)
            nodos[i].append(nodo)
            fila[fila.index(elemento)]=elemento
            
        elif "R" in elemento:
            nodo=Nodo([mapa.index(fila),j],True)
            nodo.recepcion=True
            nodo.elementos.append(elemento)
            nodos[i].append(nodo)
            fila[fila.index(elemento)]=elemento
            
        elif elemento=="_":
            nodo=Nodo([mapa.index(fila),j],True)
            nodo.elementos.append(elemento)
            nodos[i].append(nodo)
            fila[fila.index(elemento)]=elemento
            
        elif "D" in elemento:
            nodo=Nodo([mapa.index(fila),j],True)
            nodo.despacho=True
            nodo.elementos.append(elemento)
            nodos[i].append(nodo)
            fila[fila.index(elemento)]=elemento
        
        else: 
            nodo=Nodo([mapa.index(fila),j],True)
            nodo.elementos.append(elemento)
            nodos[i].append(nodo)
            fila[fila.index(elemento)]=elemento
            
        j+=1
    i+=1        

        


# In[5]:


print(nodos)


# In[6]:


#Se crean conexiones factibles entre nodos

for lista in nodos:
    for nodo in lista:
        
        #Esquinas
        if nodo.posicion==[0,0] and nodo.navegable==True:
            if nodos[0][1].navegable==True:
                nodo.agregar_conexion(nodos[0][1])
            if nodos[1][0].navegable==True:
                nodo.agregar_conexion(nodos[1][0])

        elif nodo.posicion==[0,columnas_mapa-1] and nodo.navegable==True:
            if nodos[0][columnas_mapa-2].navegable==True:
                nodo.agregar_conexion(nodos[0][columnas_mapa-2])
            if nodos[1][columnas_mapa-1].navegable==True:
                nodo.agregar_conexion(nodos[1][columnas_mapa-1])

        elif nodo.posicion==[filas_mapa-1,0] and nodo.navegable==True:
            if nodos[filas_mapa-1][1].navegable==True:
                nodo.agregar_conexion(nodos[filas_mapa-1][1])
            if nodos[filas_mapa-2][0].navegable==True:
                nodo.agregar_conexion(nodos[filas_mapa-2][0])

        elif nodo.posicion==[filas_mapa-1,columnas_mapa-1] and nodo.navegable==True:
            if nodos[filas_mapa-1][columnas_mapa-2].navegable==True:
                nodo.agregar_conexion(nodos[filas_mapa-1][columnas_mapa-2])
            if nodos[filas_mapa-2][columnas_mapa-1].navegable==True:
                nodo.agregar_conexion(nodos[filas_mapa-2][columnas_mapa-1])


      #Vertices        
        elif nodo.posicion[0]==0 and nodo.posicion[1]!=0 and nodo.posicion[1]!=columnas_mapa-1 and nodo.navegable==True:
            if nodos[nodo.posicion[0]+1][nodo.posicion[1]].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]+1][nodo.posicion[1]])
            if nodos[nodo.posicion[0]][nodo.posicion[1]+1].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]+1])
            if nodos[nodo.posicion[0]][nodo.posicion[1]-1].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]-1])

        elif nodo.posicion[0]==filas_mapa-1 and nodo.posicion[1]!=0 and nodo.posicion[1]!=columnas_mapa-1 and nodo.navegable==True:
            if nodos[nodo.posicion[0]-1][nodo.posicion[1]].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]-1][nodo.posicion[1]])
            if nodos[nodo.posicion[0]][nodo.posicion[1]+1].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]+1])
            if nodos[nodo.posicion[0]][nodo.posicion[1]-1].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]-1])

        elif nodo.posicion[1]==0 and nodo.posicion[0]!=0 and nodo.posicion[0]!=filas_mapa-1 and nodo.navegable==True:
            if nodos[nodo.posicion[0]+1][nodo.posicion[1]].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]+1][nodo.posicion[1]])
            if nodos[nodo.posicion[0]-1][nodo.posicion[1]].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]-1][nodo.posicion[1]])
            if nodos[nodo.posicion[0]][nodo.posicion[1]+1].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]+1])

        elif nodo.posicion[1]==columnas_mapa-1 and nodo.posicion[0]!=0 and nodo.posicion[0]!=filas_mapa-1 and nodo.navegable==True:
            if nodos[nodo.posicion[0]+1][nodo.posicion[1]].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]+1][nodo.posicion[1]])
            if nodos[nodo.posicion[0]-1][nodo.posicion[1]].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]-1][nodo.posicion[1]])
            if nodos[nodo.posicion[0]][nodo.posicion[1]-1].navegable==True:
                nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]-1])


      #Al medio        
        else:
            if nodo.navegable==True and nodo.posicion[0]!=filas_mapa-1 and nodo.posicion[1]!=columnas_mapa-1 and nodo.posicion[0]!=0 and nodo.posicion[1]!=0:
                if nodos[nodo.posicion[0]+1][nodo.posicion[1]].navegable==True:
                    nodo.agregar_conexion(nodos[nodo.posicion[0]+1][nodo.posicion[1]])
                if nodos[nodo.posicion[0]-1][nodo.posicion[1]].navegable==True:
                    nodo.agregar_conexion(nodos[nodo.posicion[0]-1][nodo.posicion[1]])
                if nodos[nodo.posicion[0]][nodo.posicion[1]+1].navegable==True:
                    nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]+1])
                if nodos[nodo.posicion[0]][nodo.posicion[1]-1].navegable==True:
                    nodo.agregar_conexion(nodos[nodo.posicion[0]][nodo.posicion[1]-1])


# In[7]:



grafo_fonti = nx.Graph()
for lista in nodos:
    for nodo in lista:
        if type(nodo) != list:
            grafo_fonti.add_node(nodo)
            for vecino in nodo.conexiones:
                grafo_fonti.add_edge(nodo, vecino)


def ruta_optima(nodo_inicio, nodo_final):
    lista_nodos = list(grafo_fonti.nodes)
    for nodo_1 in lista_nodos:
        if nodo_inicio in nodo_1.elementos:
            for nodo_2 in lista_nodos:
                if nodo_final in nodo_2.elementos:
                    return nx.dijkstra_path(grafo_fonti, nodo_1, nodo_2)

print(ruta_optima('A1', 'D3'))


class TEP:
    def __init__(self, id_TEP):
        self.id_TEP = id_TEP
        self.velocidad = 0
        self.ocupado = False
        self.carga = []
        self.nodo_actual = None
        
    def moverse(self,nueva_fila,nueva_columna, ruta):
        self.recorrido.append((nueva_fila,nueva_columna))
        tiempo_moviendo = len(ruta) * self.velocidad
        
    def tomar_ct(self,ct):
        self.carga.append(ct)
        self.ocupado = True
        
    def dejar_ct (self):
        self.carga.pop[0]
        self.ocupado = False


# In[ ]:


class Container:
    def __init__(self, id_container, origen, destino, tipo):
        self.id_container = id_container
        self.origen = origen
        self.destino = destino
        self.tipo = tipo

    def mover_container(self, nodo_inicio, nodo_final):
        if self.id_container == nodo_inicio.elementos[-1]:
            nodo_inicio.elementos.remove(self.id_container)
            nodo_final.append(self.id_container)

# In[ ]:


class Barco:
    def __init__(self, id_barco, tiempo_llegada, tiempo_partida, total_descargar, total_cargar):
        self.id_container = id_barco
        self.tiempo_llegada = datetime.timedelta(days=tiempo_llegada,hours=0,minutes=0,seconds=0)
        self.tiempo_partida = datetime.timedelta(days=tiempo_partida,hours=0,minutes=0,seconds=0)
        self.total_descargar = total_descargar
        self.total_cargar = total_cargar


# In[ ]:


def simulacion():
    #Se crean los objetos
    #El patio:
    #Se crean los TEP:
    TEP1=TEP(1)
    #Los barcos:
    for info_barco in info_barcos:
        barco = Barco(info_barco,info_barcos[info_barco][0],info_barcos[info_barco][1],info_barcos[info_barco][2],info_barcos[info_barco][3])
        barcos.append(barco)
    

        
    #Parte la simulación    
    tiempo = datetime.timedelta(days=0,hours=0,minutes=0,seconds=0)
        
    while barcos!=[]:
        
        tiempo = tiempo + datetime.timedelta(days=0,hours=0,minutes=0,seconds=1)


# In[ ]:


simulacion= simulacion()


# In[ ]:





# In[ ]:





# In[ ]:


class Node:
    
    def __init__(self, value):
        self.value = value
        self.connections = []
        
    def add_vertex(self, value):
        self.connections.append(value)
        
    def __repr__(self):
        l = "Node: {} ".format(self.value)
        if len(self.connections) > 0:
            l += "-> ("+ ",".join([c.__repr__() for c in self.connections]) + ")"
        return l
    

grafo = Node(1)
last = grafo
n_5 = Node(5)
for i in range(2, 5):
    n = Node(i)
    last.add_vertex(n)
    last = n
    if i == 3:
        last.add_vertex(n_5)
    elif i == 4:
        last.add_vertex(n_5)


# In[ ]:


def dist(i,j):
    return ((i[0]-j[0])**2+(i[1]-j[1])**2)**0.5

#random.seed(3)
nodos=2  #21
N={}
A=[]
c={}

for j in range (2): #11
    for i in range(nodos):
        N[(i,j)]=(1+i,1+j) 
    
for n1 in N:
    for n2 in N:
        if n1!=n2 and (n2,n1)not in A:
            c[(n1,n2)]= dist(N[n1],N[n2])
            A.append((n1,n2))
            
G = nx.Graph()
nx.draw_networkx_nodes(G, N, N.keys(), node_size=80,node_color='red',alpha=0.8)
nx.draw_networkx_edges(G, N, A, width=1,  edge_color='black')
plt.title('Patio de Contenedores')
plt.axis('off')

