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

with open('/Users/Billy/Dropbox/Alt Stable States Paper/Data/DataForFigures/April2019Exp/April2019Exp.csv', 'r') as f:
    data1 = list(reader(f))
with open('/Users/Billy/Dropbox/Alt Stable States Paper/Data/DataForFigures/CoexAltData/CoexAltData1215.csv', 'r') as f:
    data2 = list(reader(f))


Pci_initial_frac1 = ['95', '71', '7']
Pa_initial_frac2 = ['0.83', '0.5', '0.07', '0.29', '0.36']
 
fig1 = plt.figure(figsize=(7,3))
plt.grid(lw = 0.5)
plt.ylim(ymax = 1.1, ymin = -0.05)
plt.yticks(np.arange(0.0, 1.1, 0.5), fontsize=12)
plt.xlim(xmin = 0.5, xmax = 6.5)
plt.xticks(fontsize=12)

MeanEndPoints = []
SEM = []

for DF in ['1','2','3','4','5','6']:
    
    EndPoint = []
    
    for elt in ['Pci-Pa']:
        for l in Pci_initial_frac1:
            for i in data1[1::]:
                if i[0] == elt and i[7] == DF and i[8] == l and i[9] == '7':
                    if i[5] == '#DIV/0!':
                        break
                    start = (DF, float(l)/100)
                    end = (DF, i[5])
                    EndPoint.append(float(i[5]))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'grey'))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'white', alpha = 0.6))

    for elt in ['Pa-Pci 1']:
        for l in Pa_initial_frac2:
            for i in data2[1::]:
                if i[0] == elt and i[7] == DF and i[8] == l and i[9] == '6':
                    if i[6] == '':
                        break
                    s = 1-float(l)
                    start = (DF, s)
                    end = (DF, i[6])
                    EndPoint.append(float(i[6]))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'grey'))
                    plt.annotate("", xy=end, xytext=start, arrowprops=dict(width = 3, headwidth = 15, color = 'white', alpha = 0.6))

    #print(EndPoint)
    mean = np.mean(EndPoint)
    stdmean = np.std(EndPoint)/np.sqrt(len(EndPoint))
    
    MeanEndPoints.append(mean)
    SEM.append(stdmean)
    

bif = [0, 0, 0, MeanEndPoints[3], MeanEndPoints[4], 1, 1]
xbif = [0.5, 2, 3.6, 4, 5, 5.7, 6.5]

plt.errorbar([1,2,3,4,5,6], MeanEndPoints, fmt='.', lw = 3, color='k', yerr=SEM, ecolor = 'k', 
             capsize=5, capthick=3, ms = 15, zorder = 10)

plt.plot(xbif, bif, ls = '-', color = 'k', lw = 3, zorder = 10)
plt.plot(np.linspace(3.67,6.5,30), np.linspace(0,0,30), ls = 'dashed', color = 'k', lw = 3, zorder = 10)
plt.plot(np.linspace(0.5,5.63,30), np.linspace(1,1,30), ls = 'dashed', color = 'k', lw = 3, zorder = 10)
plt.xlabel('Log(Dilution Factor)', fontsize=22)
plt.ylabel('Pci Fraction', fontsize=22)

plt.tight_layout()
plt.show()
fig1.savefig("/Users/Billy/Desktop/AveragedPciPaBifurcationDiagram.png", dpi=800)