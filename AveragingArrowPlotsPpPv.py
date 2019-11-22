#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:42:27 2019

@author: Billy
"""

""" Supplemental figures: Pci-Pv averaging bifurcation diagrams """

from csv import reader
from matplotlib import pyplot as plt
import numpy as np

with open('/Users/Billy/Dropbox/Alt Stable States Paper/Data/DataForFigures/Coex_Bis_2_21/Coex_Bis_2_21_D7.csv', 'r') as f:
    data1 = list(reader(f))
with open('/Users/Billy/Dropbox/Alt Stable States Paper/Data/DataForFigures/Alt1DF4/Alt1DF4.csv', 'r') as f:
    data2 = list(reader(f))


Pp_initial_frac1 = ['0.87', '0.75', '0.59', '0.27', '0.08']
Pp_initial_frac2 = ['94', '59.5', '14.9']
 
fig1 = plt.figure(figsize=(7,3))
plt.grid(lw = 0.5)
plt.ylim(ymax = 1.1, ymin = -0.05)
plt.yticks(np.arange(0.0, 1.1, 0.5), fontsize=12)
plt.xlim(xmin = 0.5, xmax = 5.5)
plt.xticks(fontsize=12)

MeanEndPoints = []
SEM = []

for DF in ['1','2','3','4','5']:
#    
#    EndPoint = []
    
    for elt in ['Pp-Pv 1']:
        for l in Pp_initial_frac1:
            for i in data1[1::]:
                if i[0] == elt and i[7] == DF and i[8] == l and i[9] == '7':
                    #print('check')
                    start = (DF, float(l))
                    end = (DF, i[5])
#                    EndPoint.append(float(i[5]))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'grey'))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'white', alpha = 0.6))

    for elt in ['Pp-Pv 1', 'Pp-Pv 2']:
        for l in Pp_initial_frac2:
            for i in data2[1::]:
                if i[0] == elt and i[7] == DF and i[8] == l and i[9] == '7':
                    start = (DF, float(l)/100)
                    end = (DF, i[5])
#                    EndPoint.append(float(i[5]))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'grey'))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'white', alpha = 0.6))

    #print(EndPoint)
    #mean = np.mean(EndPoint)
    #stdmean = np.std(EndPoint)/np.sqrt(len(EndPoint))
    #
    #MeanEndPoints.append(mean)
    #SEM.append(stdmean)
    

bif = [1, 1, 0, 0, 0]
xbif = [0.5, 1.8, 3.15, 5, 5.5]

#MeanEndPoints = [0,0,0,1,0,1,1]
#plt.errorbar([1,2,3,3,4,4,5], MeanEndPoints, fmt='.', lw = 3, color='k', yerr=[0,0,0,0,0,0,0], ecolor = 'k', 
#             capsize=5, capthick=3, ms = 15, zorder = 10)

plt.plot(xbif, bif, ls = 'dashed', color = 'k', lw = 3, zorder = 10)
plt.plot(np.linspace(0.5,3.25,30), np.linspace(0,0,30), ls = '-', color = 'k', lw = 3, zorder = 10)
plt.plot(np.linspace(1.75,5.5,30), np.linspace(1,1,30), ls = '-', color = 'k', lw = 3, zorder = 10)
plt.xlabel('Log(Dilution Factor)', fontsize=22)
plt.ylabel('Pp Fraction', fontsize=22)

plt.tight_layout()
plt.show()
fig1.savefig("/Users/Billy/Desktop/AveragedPpPvBifurcationDiagram.png", dpi=800)