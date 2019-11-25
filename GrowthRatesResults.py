#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 16:48:12 2019

@author: Billy
"""

""" Carrying capcity plot for supplement """

from matplotlib import pyplot as plt
#import numpy as np
from matplotlib import rcParams
rcParams.update({'figure.autolayout': True})

    
    
###Report K in millions of cells per microLiter
##Numbers from spreadsheet in folder
K_Pp = 0.777632207088
K_Pp_SEM = .00763103969692

K_Ea = 0.734990891248
K_Ea_SEM = .0488032495061

K_Pv = 0.484734044243
K_Pv_SEM = .00485874933763

fig1 = plt.figure(figsize=(11,13))

plt.errorbar([1], [K_Pv], fmt='.', lw = 3, color='seagreen', yerr=[K_Pv_SEM], ecolor = 'seagreen', 
                 capsize=5, capthick=3, ms = 20, zorder = 10, )
plt.errorbar([2], [K_Pp], fmt='.', lw = 3, color='purple', yerr=[K_Pp_SEM], ecolor = 'purple', 
                 capsize=5, capthick=3, ms = 20, zorder = 10)
plt.errorbar([3], [K_Ea], fmt='.', lw = 3, color='orange', yerr=[K_Ea_SEM], ecolor = 'orange', 
                 capsize=5, capthick=3, ms = 20, zorder = 10)
#plt.xlabel('Species', fontsize=30)
plt.ylabel('Growth Rate\n'+r'[hour$^{-1}$]', fontsize=30)
plt.xticks([1,2,3], ['Pv','Pp','Ea'], fontsize=30)
plt.yticks([0.50, 0.60, 0.70, 0.80], fontsize=22)
plt.grid(lw = 2.0)
plt.ylim(ymax = 0.85, ymin = 0.45)
#plt.title(title, fontsize=22)
plt.show()
plt.tight_layout()
fig1.savefig('/Users/Billy/Desktop/GrowthRates.png', dpi=800) 