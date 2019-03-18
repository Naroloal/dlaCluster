#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 07:36:44 2019

@author: lorenzo
"""
'''Una vez corrido WAlker.py grafico'''
import matplotlib.pyplot as plt
import pickle
import numpy as np
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable

#file = open('Matrix.pickle','rb')
##Matrix = pickle.load(file)
#file.close()
#'''iniciar i manualamente para el guardado de figuras'''
#i = i+1
#fig = plt.figure(1)
#gs = gridspec.GridSpec(15,15)
#ax = fig.add_subplot(gs[:,:])
#im = ax.matshow(Matrix,interpolation='nearest',cmap=plt.cm.get_cmap('viridis',3), aspect='equal')
#divider = make_axes_locatable(ax)
#cax = divider.append_axes("right", size="5%", pad=0.05)
#bar =plt.colorbar(im, cax=cax)
#bar.set_ticks(np.arange(0,2.1,1))
#bar.ax.tick_params(labelsize = 24)
#ax.tick_params(axis = 'both', which = 'major', labelsize = 24)
#plt.savefig('fig{}.png'.format(i))

fig = plt.subplot()
plt.scatter(np.arange(10,80,5),[0.05,0.5,1.39,4.11,7.19,12,17,31,47,62,84,103,149], color='blue', edgecolors='blue', s=30)
plt.scatter(np.arange(10,80,5),[0.1,0.5,1.54,3.24,6.1,11.62,18,47,42,61,78,105,135,185], color='tomato', edgecolors='tomato', s=30)
plt.title("Tiempo de Computo",fontsize=20)
plt.xlabel("Radio",fontsize=15)
plt.ylabel("Tiempo",fontsize=15)
plt.grid(True)
fig.spines["top"].set_visible(False)  
fig.spines["right"].set_visible(False)  
fig.set_xticks(fontsize = 30)
fig.set_yticks(fontsize = 30)
plt.show()