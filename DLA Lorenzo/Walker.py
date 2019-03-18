#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 10:57:10 2018

@author: lorenzo
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
import imageio
import os
import time
import pickle
import copy as cp
start = time.time()
Radio = 80#Tamanio de la red
Tamanio = int(Radio*2 + 5)
cmap = colors.ListedColormap(['navy','white', 'navy'])
t = 10 #Intervalo de fotos
Total_walkers = 40000 # Total de caminantes en la red
aux_Total_Walkers = Total_walkers
from mpl_toolkits.axes_grid1 import make_axes_locatable
from matplotlib import gridspec


'''Caminante: realiza pasos en direcciones aleatorias hasta encontrar un companiero, vive en una red(matriz)'''
class Walker(object):    
    def __init__(self,tupla,r = Tamanio):
        self.x = tupla[0]
        self.y = tupla[1]
        self.r = r
    def __str__(self):
        return 'x = {}, y = {}'.format(self.x,self.y)
    def move_random(self):
        z = np.random.random()
        if z<0.25: self.x +=1
        elif z<0.5: self.x +=-1
        elif z<0.75: self.y+=1
        else: self.y +=-1
        self.x,self.y = np.mod(self.x,Tamanio),np.mod(self.y,Tamanio)# Me aseguro de que siempre se mueva dentro de la red
    
    def found_friend(self,Matrix):# se fija si hay companiero en las direcciones posibles
        if Matrix[(self.x + 1)%Tamanio][self.y] == 1 or Matrix[self.x][(self.y + 1)%Tamanio] ==1 or Matrix[self.x - 1][self.y] == 1 or Matrix[self.x][self.y - 1]==1:# or Matrix[self.x + 1][self.y - 1]==1 or Matrix[self.x-1][self.y - 1]==1 or Matrix[self.x + 1][self.y + 1]==1 or Matrix[self.x-1][self.y + 1]==1:
            return True
        else: return False
    
    def Near_edge(self,Matrix):
        if (self.x + 1 > Tamanio + 4 or self.x-1 < 1 or self.y + 1 > Tamanio + 4 or self.y-1 < 1):
            return True
        else: return False
        
    def Exit_Circle(self,Matrix):
        if (Matrix[self.x,self.y] == 2):return True
        else: return False
        
'''Esta funcion la necesito para crear walkers en los bordes de la matriz y no en cualquier lado, lo que supone que quizas se encuentre
un companiero ni bien es creado'''
def randomAtRadius(radius, Radio):
    theta = 2*np.pi*np.random.random() #generate random theta
    x=int(radius*np.cos(theta))+ Radio + 2 #use trig to transfer into X
    y=int(radius*np.sin(theta))+ Radio + 2 #find Y coordinate
    location=[x, y] #save locaction
    return location    

def DLA_Cluster(Radio,Figures = False):
    start = time.time()
    Tamanio = int(Radio*2 + 5)
    '''La matriz con la que trabajo contiene 2 en los bordes y 0 en otros lados, un caminante queda representado con 1'''
    Matrix = np.zeros((Tamanio,Tamanio),dtype = int)
    
    for i in range(Tamanio):
        for j in range(Tamanio):
            dist = (i - Radio - 2)**2 + (j - Radio - 2)**2
            if np.sqrt(dist) > Radio: Matrix[i,j]=2
    Matrix[int(Radio) + 2,int(Radio)+ 2]=1
    added = 0
    count = 0
    complete_Cluster = False
    while not complete_Cluster:
        walker = Walker(randomAtRadius(Radio,Radio))
        Exit_Circle = False
        Found_friend = False
        size_cluster = 0
        while (not Found_friend and not Exit_Circle):   
            aux = cp.copy(walker)
            aux.move_random()
            Exit_Circle_aux = aux.Exit_Circle(Matrix)
            if not Exit_Circle_aux:
                walker = cp.copy(aux)
                Exit_Circle = Exit_Circle_aux        
                if walker.found_friend(Matrix):
                    Found_friend = walker.found_friend(Matrix)
                    size_cluster = max(np.sqrt((walker.x - Radio)**2 + (walker.y - Radio)**2),size_cluster)
                    Matrix[walker.x,walker.y] = 1
                    count +=1
#            else:
#                count +=1
        intervalSavePic=range(2,400000,100)        
        if count in intervalSavePic:
            print("still working, have added ", count, " random walkers.Added",count)
            if Figures:
                plt.title("DLA Cluster", fontsize=20)
                fig = plt.figure(1)
                gs = gridspec.GridSpec(15,15)
                ax = fig.add_subplot(gs[:,:])
                im = ax.matshow(Matrix,interpolation='nearest',cmap=plt.cm.get_cmap('viridis',3), aspect='equal')
                ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
                plt.savefig("Images/cluster{}.png".format(count), dpi=200)
                plt.close()
                plt.clf()
        if size_cluster >= Radio:
            print('Listorti, total_walker = ', count)
            file = open('Matrix.pickle','wb')
            pickle.dump(Matrix,file)
            file.close()
            final = time.time()
            print('total computation time:',final - start)
            complete_Cluster = True
        if count == Total_walkers:
            complete_Cluster = True
    return count,Matrix




#    if Total_walkers == 0: y = False
#caminantes_save = [i*t for i in range(1,int(aux_Total_Walkers/t))]
#caminantes_save.sort(reverse = True)
#with imageio.get_writer('Images/movie.gif', mode='I') as writer:
#            for i in caminantes_save:
#                filename="Images/cluster"+str(i)+".png"
#                image = imageio.imread(filename)
#                writer.append_data(image)
#                os.remove(filename)
##            image = imageio.imread("Images/cluster.png")
#            writer.append_data(image)
#        
#
#        


    

